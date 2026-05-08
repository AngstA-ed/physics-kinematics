"""Thin subprocess wrapper around Pandoc for our two output formats."""
from __future__ import annotations
import subprocess
from pathlib import Path


def md_to_docx(src: Path, out: Path, reference_doc: Path | None) -> None:
    cmd = ["pandoc", str(src), "-o", str(out)]
    if reference_doc and reference_doc.is_file():
        cmd += [f"--reference-doc={reference_doc}"]
    subprocess.run(cmd, check=True)


def md_to_onenote_html(src: Path, out: Path) -> None:
    cmd = [
        "pandoc",
        str(src),
        "-o",
        str(out),
        "--standalone",
        "--embed-resources",   # Pandoc 3.x replacement for --self-contained
        "--no-highlight",
    ]
    subprocess.run(cmd, check=True)
