"""Walk the unit tree and build all lesson artifacts.

Usage:
    python tools/build_lessons.py                              # build everything
    python tools/build_lessons.py 01_Kinematics                # one unit
    python tools/build_lessons.py 01_Kinematics/01_Vectors     # one lesson
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

# When run as `python tools/build_lessons.py`, ensure the project root is on
# sys.path so the absolute `tools.*` imports resolve.
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from tools.pandoc_runner import md_to_docx, md_to_onenote_html
from tools.static_ifier import staticify
from tools.validators import (
    validate_teacher_guide, validate_answer_key, validate_student_html,
    validate_student_worksheet, validate_student_notes,
    validate_onenote_html, validate_unit_plan, validate_assessment,
    ValidationError,
)

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REFACTOR = ROOT / "Publisher_Ready_Curriculum" / "01_Physics_East_Meadow_Refactor"
DEFAULT_REFERENCE = DEFAULT_REFACTOR / "_assets" / "brand" / "reference.docx"


def build_lesson_folder(
    folder: Path, *, schema_path: Path, reference_doc: Path | None, css_root: Path,
) -> list[str]:
    """Build one lesson folder. Returns list of relative output paths.

    Two modes, auto-detected per folder:

    * **Legacy / interactive** — folder has `Student_Exploration.html`. Builds
      Teacher Guide + Answer Key DOCX/onenote plus the static-ified student page
      (the Kinematics pilot).
    * **DOCX-only** — no HTML page. Builds Teacher Guide + Student Worksheet +
      Student Notes + Answer Key to DOCX. This is the format for all units
      authored after the pilot.
    """
    written: list[str] = []

    student_html = folder / "Student_Exploration.html"
    teacher_md = folder / "Teacher_Guide.md"
    answer_md = folder / "Answer_Key.md"
    worksheet_md = folder / "Student_Worksheet.md"
    notes_md = folder / "Student_Notes.md"

    # 1. Validate required sources
    if not teacher_md.exists():
        raise ValidationError(f"{folder.name}: Teacher_Guide.md missing")
    if not answer_md.exists():
        raise ValidationError(f"{folder.name}: Answer_Key.md missing")
    validate_teacher_guide(teacher_md, schema_path)
    validate_answer_key(answer_md, schema_path)

    docx_only = not student_html.exists()
    md_sources = [teacher_md, answer_md]

    if docx_only:
        if not worksheet_md.exists():
            raise ValidationError(f"{folder.name}: Student_Worksheet.md missing")
        if not notes_md.exists():
            raise ValidationError(f"{folder.name}: Student_Notes.md missing")
        validate_student_worksheet(worksheet_md, schema_path)
        validate_student_notes(notes_md, schema_path)
        md_sources += [worksheet_md, notes_md]
    else:
        validate_student_html(student_html, schema_path)

    # 2. Build DOCX from every markdown source. DOCX-only lessons emit no HTML
    #    (per the build-out spec); legacy lessons also emit the OneNote HTML.
    for md in md_sources:
        docx = md.with_suffix(".docx")
        md_to_docx(md, docx, reference_doc)
        written.append(str(docx))
        if not docx_only:
            onhtml = md.with_suffix(".onenote.html")
            md_to_onenote_html(md, onhtml)
            validate_onenote_html(onhtml, schema_path)
            written.append(str(onhtml))

    # 3. Legacy only: static-ify the interactive HTML student page
    if not docx_only:
        onenote_html = folder / "Student_Exploration.onenote.html"
        static_text = staticify(
            student_html.read_text(encoding="utf-8"),
            css_root=css_root,
            html_dir=folder,
        )
        onenote_html.write_text(static_text, encoding="utf-8")
        validate_onenote_html(onenote_html, schema_path)
        written.append(str(onenote_html))

    return written


def build_unit_plan(folder: Path, *, schema_path: Path, reference_doc: Path | None,
                    docx_only: bool = False) -> list[str]:
    written: list[str] = []
    md = folder / "Unit_Plan.md"
    if not md.exists():
        return written
    validate_unit_plan(md, schema_path)
    docx = md.with_suffix(".docx")
    md_to_docx(md, docx, reference_doc)
    written.append(str(docx))
    if not docx_only:
        onhtml = md.with_suffix(".onenote.html")
        md_to_onenote_html(md, onhtml)
        validate_onenote_html(onhtml, schema_path)
        written.append(str(onhtml))
    return written


def build_assessments(
    folder: Path, *, schema_path: Path, reference_doc: Path | None,
) -> list[str]:
    written: list[str] = []
    for md in folder.glob("*.md"):
        validate_assessment(md, schema_path)
        docx = md.with_suffix(".docx")
        onhtml = md.with_suffix(".onenote.html")
        md_to_docx(md, docx, reference_doc)
        md_to_onenote_html(md, onhtml)
        written += [str(docx), str(onhtml)]
    return written


def _is_lesson_folder(folder: Path) -> bool:
    """A folder is a lesson if it has a Teacher Guide (either format)."""
    return (folder / "Teacher_Guide.md").exists()


def _iter_lesson_folders(unit: Path):
    for child in sorted(unit.iterdir()):
        if child.is_dir() and _is_lesson_folder(child):
            yield child


def _unit_is_docx_only(unit: Path) -> bool:
    """A unit is DOCX-only when none of its lessons has an interactive HTML
    student page (so the unit plan should emit no OneNote HTML either)."""
    return not any((lesson / "Student_Exploration.html").exists()
                   for lesson in _iter_lesson_folders(unit))


def build_target(target: Path, *, schema_path: Path, reference_doc: Path | None) -> dict:
    css_root = DEFAULT_REFACTOR / "_assets"
    report = {"built": [], "failed": []}
    if _is_lesson_folder(target):
        try:
            report["built"] += build_lesson_folder(
                target, schema_path=schema_path,
                reference_doc=reference_doc, css_root=css_root,
            )
        except Exception as e:
            report["failed"].append((str(target), str(e)))
        return report

    # Otherwise treat as unit
    if (target / "Unit_Plan.md").exists():
        try:
            report["built"] += build_unit_plan(
                target, schema_path=schema_path, reference_doc=reference_doc,
                docx_only=_unit_is_docx_only(target),
            )
        except Exception as e:
            report["failed"].append((str(target), str(e)))
    if (target / "Assessments").is_dir():
        try:
            report["built"] += build_assessments(
                target / "Assessments",
                schema_path=schema_path,
                reference_doc=reference_doc,
            )
        except Exception as e:
            report["failed"].append((str(target / "Assessments"), str(e)))
    for lesson in _iter_lesson_folders(target):
        try:
            report["built"] += build_lesson_folder(
                lesson, schema_path=schema_path,
                reference_doc=reference_doc, css_root=css_root,
            )
        except Exception as e:
            report["failed"].append((str(lesson), str(e)))
    return report


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("target", nargs="?", default="", help="Unit or lesson folder (relative to refactor root)")
    p.add_argument("--schema", default=str(ROOT / "tools" / "lesson_schema.yaml"))
    p.add_argument("--reference", default=str(DEFAULT_REFERENCE))
    args = p.parse_args()

    schema_path = Path(args.schema)
    reference = Path(args.reference) if Path(args.reference).is_file() else None

    if args.target:
        target = (DEFAULT_REFACTOR / args.target).resolve()
    else:
        target = DEFAULT_REFACTOR.resolve()

    if _is_lesson_folder(target):
        report = build_target(target, schema_path=schema_path, reference_doc=reference)
    elif target == DEFAULT_REFACTOR.resolve():
        report = {"built": [], "failed": []}
        for unit in sorted(target.iterdir()):
            if unit.is_dir() and unit.name.startswith(("0", "1")) and unit.name != "_assets":
                sub = build_target(unit, schema_path=schema_path, reference_doc=reference)
                report["built"] += sub["built"]
                report["failed"] += sub["failed"]
    else:
        report = build_target(target, schema_path=schema_path, reference_doc=reference)

    # Write build_report.md (spec §7.2 step 5)
    report_md = ROOT / "build_report.md"
    lines: list[str] = ["# Build report", ""]
    lines.append(f"Target: `{target.relative_to(ROOT) if target.is_relative_to(ROOT) else target}`")
    lines.append(f"Built: {len(report['built'])} artifacts")
    lines.append(f"Failed: {len(report['failed'])}")
    lines.append("")
    if report["built"]:
        lines.append("## Built")
        lines += [f"- `{p}`" for p in report["built"]]
        lines.append("")
    if report["failed"]:
        lines.append("## Failed")
        for path, err in report["failed"]:
            lines.append(f"- `{path}`: {err}")
        lines.append("")
    report_md.write_text("\n".join(lines), encoding="utf-8")

    print(f"Built {len(report['built'])} artifacts. Report: {report_md.relative_to(ROOT)}")
    if report["failed"]:
        print(f"FAILED: {len(report['failed'])}", file=sys.stderr)
        for path, err in report["failed"]:
            print(f"  {path}: {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
