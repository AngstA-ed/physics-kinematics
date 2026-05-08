"""Tests for tools.validators — lesson structure validation."""
from pathlib import Path
import pytest
from tools.validators import (
    validate_teacher_guide,
    validate_answer_key,
    validate_student_html,
    validate_onenote_html,
    ValidationError,
)


def test_teacher_guide_passes_with_all_required_headings(tmp_path: Path, schema_path: Path):
    headings = [
        "Cover", "Curated Resources (from East Meadow Scope & Sequence)",
        "CCC Focus", "NYSSLS Observation Checklist Crosswalk",
        "Opening Connection", "At-a-Glance", "Lesson Objectives", "Agenda",
        "Discussion Prompts", "Common Misconceptions",
        "Access & Differentiation", "Strategy Spotlight",
        "Exit Ticket + Closing Reflection", "Companion Materials",
    ]
    sub_headings = "\n\n".join([
        "### NYSSLS Standards\nHS-PS2-1.",
        "### Phenomenon\nA phenomenon link.",
        "### Javalab / Labs\n- Lab A",
        "### Assessments\n- Assessment A",
    ])
    body_parts = []
    for h in headings:
        body_parts.append(f"## {h}\n")
        if h == "Curated Resources (from East Meadow Scope & Sequence)":
            body_parts.append(sub_headings + "\n")
    body_parts.append("\n## Key Vocabulary (max 3)\n- term1\n- term2\n")
    file = tmp_path / "Teacher_Guide.md"
    file.write_text("\n".join(body_parts), encoding="utf-8")

    validate_teacher_guide(file, schema_path)


def test_teacher_guide_fails_when_section_missing(tmp_path: Path, schema_path: Path):
    file = tmp_path / "Teacher_Guide.md"
    file.write_text("## Cover\n## Agenda\n", encoding="utf-8")
    with pytest.raises(ValidationError, match="missing required heading"):
        validate_teacher_guide(file, schema_path)


def test_teacher_guide_fails_when_curated_subheading_missing(tmp_path: Path, schema_path: Path):
    body = []
    for h in [
        "Cover", "Curated Resources (from East Meadow Scope & Sequence)",
        "CCC Focus", "NYSSLS Observation Checklist Crosswalk",
        "Opening Connection", "At-a-Glance", "Lesson Objectives", "Agenda",
        "Discussion Prompts", "Common Misconceptions",
        "Access & Differentiation", "Strategy Spotlight",
        "Exit Ticket + Closing Reflection", "Companion Materials",
    ]:
        body.append(f"## {h}\n")
        if h.startswith("Curated"):
            # Only NYSSLS, missing the others
            body.append("### NYSSLS Standards\nHS-PS2-1.\n")
    file = tmp_path / "Teacher_Guide.md"
    file.write_text("\n".join(body), encoding="utf-8")
    with pytest.raises(ValidationError, match="Curated Resources missing sub-heading"):
        validate_teacher_guide(file, schema_path)


def test_teacher_guide_fails_when_vocab_exceeds_three(tmp_path: Path, schema_path: Path):
    headings = [
        "Cover", "Curated Resources (from East Meadow Scope & Sequence)",
        "CCC Focus", "NYSSLS Observation Checklist Crosswalk",
        "Opening Connection", "At-a-Glance", "Lesson Objectives", "Agenda",
        "Discussion Prompts", "Common Misconceptions",
        "Access & Differentiation", "Strategy Spotlight",
        "Exit Ticket + Closing Reflection", "Companion Materials",
    ]
    sub = "\n".join([
        "### NYSSLS Standards\nHS-PS2-1.",
        "### Phenomenon\nLink",
        "### Javalab / Labs\n- A",
        "### Assessments\n- A",
    ])
    body = []
    for h in headings:
        body.append(f"## {h}\n")
        if h.startswith("Curated"):
            body.append(sub + "\n")
    body.append("\n## Key Vocabulary (max 3)\n- a\n- b\n- c\n- d\n")
    file = tmp_path / "Teacher_Guide.md"
    file.write_text("\n".join(body), encoding="utf-8")
    with pytest.raises(ValidationError, match="vocab exceeds"):
        validate_teacher_guide(file, schema_path)


def test_student_html_fails_when_interactive_missing_noscript(tmp_path: Path, schema_path: Path):
    html = """<html><body>
    <header class="brand-header"></header>
    <section data-section="phenomenon"></section>
    <section data-section="driving-question"></section>
    <section data-section="notice-wonder"></section>
    <section data-section="initial-model"></section>
    <section data-section="interactive">
      <div data-interactive="true"><svg></svg><script>console.log("x");</script></div>
    </section>
    <section data-section="make-it-make-sense"></section>
    <section data-section="vocab"></section>
    <section data-section="revise-model"></section>
    <section data-section="return-to-phenomenon"></section>
    <section data-section="exit-ticket"></section>
    <section data-section="explore-further"></section>
    </body></html>"""
    file = tmp_path / "Student_Exploration.html"
    file.write_text(html, encoding="utf-8")
    with pytest.raises(ValidationError, match="interactive widget missing.*noscript"):
        validate_student_html(file, schema_path)


def test_onenote_html_fails_when_script_present(tmp_path: Path, schema_path: Path):
    html = "<html><body><script>alert('x')</script></body></html>"
    file = tmp_path / "X.onenote.html"
    file.write_text(html, encoding="utf-8")
    with pytest.raises(ValidationError, match="forbidden tag"):
        validate_onenote_html(file, schema_path)


def test_onenote_html_passes_when_clean(tmp_path: Path, schema_path: Path):
    html = "<html><body><h1>Hi</h1><p>Plain content.</p></body></html>"
    file = tmp_path / "X.onenote.html"
    file.write_text(html, encoding="utf-8")
    validate_onenote_html(file, schema_path)


def test_answer_key_fails_when_section_missing(tmp_path: Path, schema_path: Path):
    file = tmp_path / "Answer_Key.md"
    file.write_text("## Cover\n", encoding="utf-8")
    with pytest.raises(ValidationError, match="missing required heading"):
        validate_answer_key(file, schema_path)
