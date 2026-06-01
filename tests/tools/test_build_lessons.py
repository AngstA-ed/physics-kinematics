"""End-to-end build test on a fixture lesson."""
from pathlib import Path
import shutil
import pytest
from tools.build_lessons import build_lesson_folder
from tools.scaffold_lesson import scaffold_lesson


@pytest.fixture
def working_lesson(tmp_path: Path, fixtures_dir: Path) -> Path:
    src = fixtures_dir / "valid_lesson"
    dst = tmp_path / "01_Sample"
    shutil.copytree(src, dst)
    return dst


def test_build_produces_all_expected_artifacts(working_lesson: Path, schema_path: Path):
    build_lesson_folder(
        working_lesson,
        schema_path=schema_path,
        reference_doc=None,
        css_root=working_lesson.parent,
    )
    expected = [
        "Student_Exploration.html",
        "Student_Exploration.onenote.html",
        "Teacher_Guide.md",
        "Teacher_Guide.docx",
        "Teacher_Guide.onenote.html",
        "Answer_Key.md",
        "Answer_Key.docx",
        "Answer_Key.onenote.html",
    ]
    for name in expected:
        assert (working_lesson / name).exists(), f"missing {name}"


def test_docx_only_lesson_builds_docx_and_no_html(tmp_path: Path, schema_path: Path):
    """A scaffolded DOCX-only lesson builds 4 DOCX files and emits no HTML."""
    lesson = tmp_path / "01_Sample"
    scaffold_lesson(
        out_dir=lesson,
        unit_name="Forces",
        lesson_number="01",
        lesson_title="Sample",
        strategy_chips=[],
        docx_only=True,
    )
    # Scaffold writes markdown sources only — no HTML student page.
    assert not (lesson / "Student_Exploration.html").exists()
    build_lesson_folder(
        lesson, schema_path=schema_path, reference_doc=None, css_root=lesson.parent,
    )
    for name in ["Teacher_Guide.docx", "Answer_Key.docx",
                 "Student_Worksheet.docx", "Student_Notes.docx"]:
        assert (lesson / name).exists(), f"missing {name}"
    assert not list(lesson.glob("*.onenote.html")), "DOCX-only must emit no HTML"


def test_build_fails_when_validator_rejects_lesson(working_lesson: Path, schema_path: Path):
    # Break the lesson by emptying the teacher guide
    (working_lesson / "Teacher_Guide.md").write_text("# broken\n", encoding="utf-8")
    with pytest.raises(Exception):
        build_lesson_folder(
            working_lesson, schema_path=schema_path,
            reference_doc=None, css_root=working_lesson.parent,
        )
