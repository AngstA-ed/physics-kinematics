"""Test that pandoc_runner produces docx and onenote.html from a markdown source."""
from pathlib import Path
from tools.pandoc_runner import md_to_docx, md_to_onenote_html


def test_md_to_docx_creates_file(tmp_path: Path):
    md = tmp_path / "x.md"
    md.write_text("# Hello\n\nBody.\n", encoding="utf-8")
    out = tmp_path / "x.docx"
    md_to_docx(md, out, reference_doc=None)
    assert out.exists()
    assert out.stat().st_size > 0


def test_md_to_onenote_html_self_contained(tmp_path: Path):
    md = tmp_path / "x.md"
    md.write_text("# Hello\n\nBody.\n", encoding="utf-8")
    out = tmp_path / "x.onenote.html"
    md_to_onenote_html(md, out)
    text = out.read_text(encoding="utf-8")
    assert "<h1" in text
    assert "Body" in text
    assert "<script" not in text
    assert "<iframe" not in text
