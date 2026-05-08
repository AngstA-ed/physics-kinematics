"""Test scaffold_lesson creates a new lesson folder with required files."""
from pathlib import Path
from tools.scaffold_lesson import scaffold_lesson


def test_scaffold_creates_three_files(tmp_path: Path):
    out = tmp_path / "01_Vectors"
    scaffold_lesson(
        out_dir=out,
        unit_name="Kinematics",
        lesson_number="01",
        lesson_title="Vectors",
        strategy_chips=["RESTORATIVE CIRCLE", "ACTIVE LEARNING"],
    )
    assert (out / "Student_Exploration.html").is_file()
    assert (out / "Teacher_Guide.md").is_file()
    assert (out / "Answer_Key.md").is_file()


def test_scaffold_substitutes_placeholders(tmp_path: Path):
    out = tmp_path / "01_Vectors"
    scaffold_lesson(
        out_dir=out,
        unit_name="Kinematics",
        lesson_number="01",
        lesson_title="Vectors",
        strategy_chips=["HOCHMAN"],
    )
    text = (out / "Teacher_Guide.md").read_text(encoding="utf-8")
    assert "{{LESSON_TITLE}}" not in text
    assert "Vectors" in text
    assert "Kinematics" in text
    assert "HOCHMAN" in text


def test_scaffold_html_has_required_data_sections(tmp_path: Path):
    out = tmp_path / "01_Vectors"
    scaffold_lesson(
        out_dir=out,
        unit_name="Kinematics",
        lesson_number="01",
        lesson_title="Vectors",
        strategy_chips=[],
    )
    html = (out / "Student_Exploration.html").read_text(encoding="utf-8")
    for section in ["phenomenon", "interactive", "vocab", "exit-ticket", "explore-further"]:
        assert f'data-section="{section}"' in html
