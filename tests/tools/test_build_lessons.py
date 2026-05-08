"""End-to-end build test on a fixture lesson."""
from pathlib import Path
import shutil
import pytest
from tools.build_lessons import build_lesson_folder


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


def test_build_fails_when_validator_rejects_lesson(working_lesson: Path, schema_path: Path):
    # Break the lesson by emptying the teacher guide
    (working_lesson / "Teacher_Guide.md").write_text("# broken\n", encoding="utf-8")
    with pytest.raises(Exception):
        build_lesson_folder(
            working_lesson, schema_path=schema_path,
            reference_doc=None, css_root=working_lesson.parent,
        )
