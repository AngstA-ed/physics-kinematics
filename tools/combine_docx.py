"""Combine all lesson DOCX into one sequential Word document.

Walks the East Meadow refactor units in curriculum order and appends, for each
lesson, its documents in a fixed sequence (Teacher Guide → Student Worksheet →
Student Notes → Answer Key), with a page break between documents. A unit's Unit
Plan, if present, leads that unit. Styles and embedded figures are preserved via
docxcompose.

Usage:
    python tools/combine_docx.py                      # whole physics curriculum
    python tools/combine_docx.py --units 02_Forces 04_Energy
    python tools/combine_docx.py --docs Teacher_Guide Student_Worksheet
    python tools/combine_docx.py -o /path/Combined.docx
"""
from __future__ import annotations
import argparse
from pathlib import Path

from docx import Document
from docxcompose.composer import Composer

ROOT = Path(__file__).resolve().parent.parent
REFACTOR = ROOT / "Publisher_Ready_Curriculum" / "01_Physics_East_Meadow_Refactor"

# Per-lesson document order.
DEFAULT_DOC_ORDER = [
    "Teacher_Guide.docx",
    "Student_Worksheet.docx",
    "Student_Notes.docx",
    "Answer_Key.docx",
]


def _unit_dirs(root: Path, only: list[str] | None) -> list[Path]:
    units = [d for d in sorted(root.iterdir())
             if d.is_dir() and d.name[:2].isdigit()]
    if only:
        wanted = set(only)
        units = [u for u in units if u.name in wanted]
    return units


def collect_docx(root: Path, only_units: list[str] | None,
                 doc_order: list[str]) -> list[Path]:
    """Return the ordered list of DOCX paths to combine."""
    paths: list[Path] = []
    for unit in _unit_dirs(root, only_units):
        unit_plan = unit / "Unit_Plan.docx"
        if unit_plan.is_file():
            paths.append(unit_plan)
        lessons = [d for d in sorted(unit.iterdir())
                   if d.is_dir() and d.name[:2].isdigit()]
        for lesson in lessons:
            for name in doc_order:
                p = lesson / name
                if p.is_file():
                    paths.append(p)
    return paths


def combine(paths: list[Path], out: Path) -> None:
    if not paths:
        raise SystemExit("No DOCX files found to combine.")
    master = Document(str(paths[0]))
    composer = Composer(master)
    for p in paths[1:]:
        master.add_page_break()
        composer.append(Document(str(p)))
    out.parent.mkdir(parents=True, exist_ok=True)
    composer.save(str(out))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(REFACTOR),
                    help="Curriculum root (default: physics East Meadow refactor)")
    ap.add_argument("--units", nargs="*", default=None,
                    help="Restrict to these unit folder names (default: all)")
    ap.add_argument("--docs", nargs="*", default=None,
                    help="Doc filenames per lesson, in order (default: TG, Worksheet, Notes, Answer Key)")
    ap.add_argument("-o", "--out", default=None,
                    help="Output .docx path")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    doc_order = [d if d.endswith(".docx") else f"{d}.docx" for d in args.docs] \
        if args.docs else DEFAULT_DOC_ORDER
    out = Path(args.out).resolve() if args.out else \
        root / "Physics_Curriculum_Combined.docx"

    paths = collect_docx(root, args.units, doc_order)
    print(f"Combining {len(paths)} documents → {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    combine(paths, out)
    size_mb = out.stat().st_size / (1024 * 1024)
    print(f"Wrote {out} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
