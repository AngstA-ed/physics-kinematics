"""Combine all lesson documents into one sequential Word file.

Walks the East Meadow refactor units in curriculum order and concatenates, for
each lesson, its documents in a fixed sequence (Teacher Guide → Student Worksheet
→ Student Notes → Answer Key), with a page break between documents. A unit's Unit
Plan, if present, leads that unit.

Two engines:

* ``pandoc`` (default) — concatenates the Markdown SOURCES and renders ONE clean
  DOCX through pandoc + the brand reference doc. This is the same toolchain that
  builds the individual lesson DOCX, so the result renders in every previewer
  (macOS Quick Look, SharePoint/OneDrive web preview, Word). Recommended.
* ``docxcompose`` — binary-merges the already-built DOCX. Valid for desktop Word
  but does not render in some lightweight/web previewers; kept for completeness.

Usage:
    python tools/combine_docx.py                      # whole physics curriculum
    python tools/combine_docx.py --units 02_Forces 04_Energy
    python tools/combine_docx.py --docs Teacher_Guide Student_Worksheet Student_Notes
    python tools/combine_docx.py --engine docxcompose
    python tools/combine_docx.py -o /path/Combined.docx
"""
from __future__ import annotations
import argparse
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFACTOR = ROOT / "Publisher_Ready_Curriculum" / "01_Physics_East_Meadow_Refactor"
REFERENCE = REFACTOR / "_assets" / "brand" / "reference.docx"

# Per-lesson document order (basenames, no extension).
DEFAULT_DOC_ORDER = ["Teacher_Guide", "Student_Worksheet", "Student_Notes", "Answer_Key"]

# A hard page break in pandoc's docx output.
PAGE_BREAK = '\n\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n'

# Rewrite relative figure links to absolute so a single concatenated Markdown
# file resolves every lesson's own images.
_FIG_RE = re.compile(r'\]\(\.?/?figures/')

# Demote ATX headings by one level (H1→H2 … H5→H6) so per-document titles nest
# under a unit-level H1 — giving the TOC a clean "Unit → document" hierarchy.
_HEAD_RE = re.compile(r'^(#{1,5})(\s)', re.MULTILINE)

DOC_TITLE = "East Meadow × Valley Stream — Physics Curriculum"

# Friendly unit display names (folder → heading).
UNIT_NAMES = {
    "00_Math_in_Science": "Unit 0 · Math in Science",
    "01_Kinematics": "Unit 1 · Kinematics",
    "02_Forces": "Unit 2 · Forces",
    "03_Momentum_Impulse": "Unit 3 · Momentum & Impulse",
    "04_Energy": "Unit 4 · Work, Energy & Power",
    "05_Thermodynamics": "Unit 5 · Thermal Energy & Conservation",
    "06_Electrostatics": "Unit 6 · Electrostatics",
    "07_Current_Electricity": "Unit 7 · Current Electricity",
    "08_Waves": "Unit 8 · Waves & Sound",
    "09_Modern_Physics": "Unit 9 · Modern Physics",
}


def _unit_dirs(root: Path, only: list[str] | None) -> list[Path]:
    units = [d for d in sorted(root.iterdir())
             if d.is_dir() and d.name[:2].isdigit()]
    if only:
        wanted = set(only)
        units = [u for u in units if u.name in wanted]
    return units


def _lesson_dirs(unit: Path) -> list[Path]:
    return [d for d in sorted(unit.iterdir())
            if d.is_dir() and d.name[:2].isdigit()]


def collect(root: Path, only_units: list[str] | None, doc_order: list[str],
            ext: str) -> list[Path]:
    """Ordered list of files to combine (ext = '.md' or '.docx')."""
    paths: list[Path] = []
    for unit in _unit_dirs(root, only_units):
        unit_plan = unit / f"Unit_Plan{ext}"
        if unit_plan.is_file():
            paths.append(unit_plan)
        for lesson in _lesson_dirs(unit):
            for name in doc_order:
                p = lesson / f"{name}{ext}"
                if p.is_file():
                    paths.append(p)
    return paths


def _prep(md_path: Path) -> str:
    """Load a lesson Markdown source: absolutize figure links, demote headings."""
    text = md_path.read_text(encoding="utf-8")
    absfig = str(md_path.parent.resolve())
    text = _FIG_RE.sub(f']({absfig}/figures/', text)
    return _HEAD_RE.sub(r'#\1\2', text)  # H1→H2 … so doc titles nest under unit H1


def build_markdown(root: Path, only_units: list[str] | None,
                   doc_order: list[str]) -> tuple[str, int]:
    """Build the combined Markdown with a unit-heading hierarchy. Returns
    (markdown, document_count)."""
    blocks: list[str] = []
    ndocs = 0
    for unit in _unit_dirs(root, only_units):
        name = UNIT_NAMES.get(unit.name) or \
            re.sub(r'^\d+[_-]?', '', unit.name).replace('_', ' ')
        blocks.append(PAGE_BREAK)          # each unit starts on a fresh page
        blocks.append(f"# {name}\n")        # unit-level H1 (TOC level 1)
        files: list[Path] = []
        if (unit / "Unit_Plan.md").is_file():
            files.append(unit / "Unit_Plan.md")
        for lesson in _lesson_dirs(unit):
            files += [lesson / f"{n}.md" for n in doc_order
                      if (lesson / f"{n}.md").is_file()]
        for di, p in enumerate(files):
            if di:                          # page break between docs, not before the first
                blocks.append(PAGE_BREAK)
            blocks.append(_prep(p))         # doc title becomes H2 (TOC level 2)
            ndocs += 1
    return "\n\n".join(blocks) + "\n", ndocs


def combine_pandoc(root: Path, only_units: list[str] | None,
                   doc_order: list[str], out: Path, reference: Path | None) -> int:
    """Concatenate Markdown sources → one clean DOCX (with TOC) via pandoc.
    Returns the number of documents combined."""
    markdown, ndocs = build_markdown(root, only_units, doc_order)
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_name(out.stem + ".__combined__.md")
    tmp.write_text(markdown, encoding="utf-8")
    try:
        cmd = ["pandoc", str(tmp), "-o", str(out),
               "--toc", "--toc-depth=2",
               "--metadata", f"title={DOC_TITLE}",
               f"--resource-path={REFACTOR}"]
        if reference and reference.is_file():
            cmd.append(f"--reference-doc={reference}")
        subprocess.run(cmd, check=True)
    finally:
        tmp.unlink(missing_ok=True)
    return ndocs


def combine_docxcompose(docx_paths: list[Path], out: Path) -> None:
    """Binary-merge built DOCX via docxcompose (desktop-Word only)."""
    from docx import Document
    from docxcompose.composer import Composer
    master = Document(str(docx_paths[0]))
    composer = Composer(master)
    for p in docx_paths[1:]:
        master.add_page_break()
        composer.append(Document(str(p)))
    out.parent.mkdir(parents=True, exist_ok=True)
    composer.save(str(out))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(REFACTOR))
    ap.add_argument("--units", nargs="*", default=None,
                    help="Restrict to these unit folder names (default: all)")
    ap.add_argument("--docs", nargs="*", default=None,
                    help="Per-lesson doc basenames in order (default: Teacher_Guide Student_Worksheet Student_Notes Answer_Key)")
    ap.add_argument("--engine", choices=["pandoc", "docxcompose"], default="pandoc")
    ap.add_argument("-o", "--out", default=None)
    args = ap.parse_args()

    root = Path(args.root).resolve()
    doc_order = [d[:-5] if d.endswith(".docx") else d.removesuffix(".md")
                 for d in (args.docs or DEFAULT_DOC_ORDER)]
    out = Path(args.out).resolve() if args.out else \
        root / "Physics_Curriculum_Combined.docx"
    reference = REFERENCE if REFERENCE.is_file() else None

    rel = out.relative_to(ROOT) if out.is_relative_to(ROOT) else out
    if args.engine == "pandoc":
        ndocs = combine_pandoc(root, args.units, doc_order, out, reference)
        print(f"Combined {ndocs} documents (with TOC) via pandoc → {rel}")
    else:
        paths = collect(root, args.units, doc_order, ".docx")
        if not paths:
            raise SystemExit("No source files found to combine.")
        print(f"Combining {len(paths)} documents via docxcompose → {rel}")
        combine_docxcompose(paths, out)
    print(f"Wrote {out} ({out.stat().st_size / 1024 / 1024:.1f} MB)")


if __name__ == "__main__":
    main()
