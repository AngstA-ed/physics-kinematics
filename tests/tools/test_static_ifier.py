"""Tests for tools.static_ifier — interactive HTML → OneNote-paste HTML."""
from pathlib import Path
from tools.static_ifier import staticify


def _process(fixtures_dir: Path) -> str:
    src = fixtures_dir / "sample_interactive.html"
    css_root = fixtures_dir.parent.parent.parent / "Publisher_Ready_Curriculum" / "01_Physics_East_Meadow_Refactor" / "_assets"
    return staticify(src.read_text(encoding="utf-8"), css_root=css_root)


def test_strips_script_tags(fixtures_dir: Path):
    out = _process(fixtures_dir)
    assert "<script" not in out


def test_strips_external_stylesheet_links(fixtures_dir: Path):
    out = _process(fixtures_dir)
    assert '<link rel="stylesheet"' not in out


def test_inlines_local_style_blocks(fixtures_dir: Path):
    out = _process(fixtures_dir)
    assert ".local { color: red; }" in out


def test_replaces_iframe_with_link_and_instruction(fixtures_dir: Path):
    out = _process(fixtures_dir)
    assert "<iframe" not in out
    assert "youtube.com/embed/abc123" in out or "youtube.com/watch?v=abc123" in out
    assert "Insert" in out and "Online Video" in out


def test_replaces_interactive_with_noscript_content(fixtures_dir: Path):
    out = _process(fixtures_dir)
    assert "Storyboard frame 1" in out
    assert "data-interactive" not in out


def test_keeps_brand_header(fixtures_dir: Path):
    out = _process(fixtures_dir)
    assert 'class="brand-header"' in out
