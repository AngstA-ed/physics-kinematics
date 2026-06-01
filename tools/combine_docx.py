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


def combine_pandoc(md_paths: list[Path], out: Path, reference: Path | None) -> None:
    """Concatenate Markdown sources → one clean DOCX via pandoc."""
    parts: list[str] = []
    for i, p in enumerate(md_paths):
        text = p.read_text(encoding="utf-8")
        absfig = str(p.parent.resolve())
        text = _FIG_RE.sub(f']({absfig}/figures/', text)
        if i:
            parts.append(PAGE_BREAK)
        parts.append(text)
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_name(out.stem + ".__combined__.md")
    tmp.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    try:
        cmd = ["pandoc", str(tmp), "-o", str(out),
               f"--resource-path={REFACTOR}"]
        if reference and reference.is_file():
            cmd.append(f"--reference-doc={reference}")
        subprocess.run(cmd, check=True)
    finally:
        tmp.unlink(missing_ok=True)


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

    ext = ".md" if args.engine == "pandoc" else ".docx"
    paths = collect(root, args.units, doc_order, ext)
    if not paths:
        raise SystemExit("No source files found to combine.")
    print(f"Combining {len(paths)} documents via {args.engine} → "
          f"{out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    if args.engine == "pandoc":
        combine_pandoc(paths, out, reference)
    else:
        combine_docxcompose(paths, out)
    print(f"Wrote {out} ({out.stat().st_size / 1024 / 1024:.1f} MB)")


if __name__ == "__main__":
    main()
