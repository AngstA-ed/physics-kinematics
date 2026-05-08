"""Validate lesson source files against lesson_schema.yaml."""
from __future__ import annotations
from pathlib import Path
import re
import yaml


class ValidationError(Exception):
    """Raised when a lesson source file fails schema validation."""


def _load_schema(schema_path: Path) -> dict:
    with open(schema_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _heading_levels(text: str) -> list[tuple[int, str]]:
    """Return [(level, text), ...] for ATX headings (e.g. ##, ###)."""
    out = []
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if m:
            out.append((len(m.group(1)), m.group(2)))
    return out


def _level_two_headings(text: str) -> list[str]:
    return [h for lvl, h in _heading_levels(text) if lvl == 2]


def _level_three_headings_after(text: str, h2: str) -> list[str]:
    """Return ### headings that fall under the given ## section, before the next ##."""
    out: list[str] = []
    in_section = False
    for level, heading in _heading_levels(text):
        if level == 2:
            if heading == h2:
                in_section = True
            elif in_section:
                break
        elif level == 3 and in_section:
            out.append(heading)
    return out


def _vocab_count(text: str) -> int:
    """Count bullet items under '## Key Vocabulary'."""
    in_vocab = False
    count = 0
    for line in text.splitlines():
        if re.match(r"^##\s+Key Vocabulary", line):
            in_vocab = True
            continue
        if in_vocab and re.match(r"^##\s+", line):
            break
        if in_vocab and re.match(r"^[-*]\s+\S", line):
            count += 1
    return count


def validate_teacher_guide(path: Path, schema_path: Path) -> None:
    schema = _load_schema(schema_path)
    text = path.read_text(encoding="utf-8")
    h2s = _level_two_headings(text)

    for required in schema["teacher_guide_required_headings"]:
        if required not in h2s:
            raise ValidationError(
                f"{path.name}: missing required heading '## {required}'"
            )

    curated_h2 = "Curated Resources (from East Meadow Scope & Sequence)"
    sub = _level_three_headings_after(text, curated_h2)
    for required_sub in schema["curated_resources_required_subheadings"]:
        if required_sub not in sub:
            raise ValidationError(
                f"{path.name}: Curated Resources missing sub-heading '### {required_sub}'"
            )

    vocab = _vocab_count(text)
    if vocab > schema["vocab_max"]:
        raise ValidationError(
            f"{path.name}: vocab exceeds {schema['vocab_max']} (found {vocab})"
        )


def validate_answer_key(path: Path, schema_path: Path) -> None:
    schema = _load_schema(schema_path)
    text = path.read_text(encoding="utf-8")
    h2s = _level_two_headings(text)
    for required in schema["answer_key_required_headings"]:
        if required not in h2s:
            raise ValidationError(
                f"{path.name}: missing required heading '## {required}'"
            )


def validate_unit_plan(path: Path, schema_path: Path) -> None:
    schema = _load_schema(schema_path)
    text = path.read_text(encoding="utf-8")
    h2s = _level_two_headings(text)
    for required in schema["unit_plan_required_headings"]:
        if required not in h2s:
            raise ValidationError(
                f"{path.name}: missing required heading '## {required}'"
            )


def validate_student_html(path: Path, schema_path: Path) -> None:
    """Validate the rich interactive HTML page."""
    from bs4 import BeautifulSoup
    schema = _load_schema(schema_path)
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")

    if not soup.select_one("header.brand-header"):
        raise ValidationError(f"{path.name}: missing co-branded header (.brand-header)")

    sections = {s.get("data-section") for s in soup.select("[data-section]")}
    for required in schema["student_html_required_data_sections"]:
        if required not in sections:
            raise ValidationError(
                f"{path.name}: missing data-section='{required}'"
            )

    for widget in soup.select('[data-interactive="true"]'):
        # The noscript fallback may be a sibling or descendant of the same
        # parent section.
        section = widget.find_parent("section") or widget.parent
        if section is None or not section.find("noscript"):
            raise ValidationError(
                f"{path.name}: interactive widget missing sibling <noscript> storyboard"
            )


def validate_onenote_html(path: Path, schema_path: Path) -> None:
    schema = _load_schema(schema_path)
    text = path.read_text(encoding="utf-8")
    for forbidden in schema["forbidden_in_onenote_html"]:
        if forbidden in text:
            raise ValidationError(
                f"{path.name}: forbidden tag '{forbidden}' present in OneNote HTML"
            )
