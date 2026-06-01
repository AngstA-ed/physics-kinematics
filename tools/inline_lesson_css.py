"""Inline _assets/lesson.css into every Student_Exploration.html as a <style>
block, so the pages render standalone (file://, OneNote paste, SharePoint,
email) with no dependency on an external stylesheet.

Re-run this whenever lesson.css changes. Idempotent: replaces an existing
inlined block or the external <link>.

Usage:
    python tools/inline_lesson_css.py
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFACTOR = ROOT / "Publisher_Ready_Curriculum" / "01_Physics_East_Meadow_Refactor"
CSS = REFACTOR / "_assets" / "lesson.css"

MARK = "data-inlined=\"lesson.css\""
LINK_RE = re.compile(r'[ \t]*<link[^>]*lesson\.css[^>]*>\s*', re.IGNORECASE)
STYLE_RE = re.compile(r'[ \t]*<style data-inlined="lesson\.css">.*?</style>\s*',
                      re.IGNORECASE | re.DOTALL)


def inline_one(html_path: Path, css: str) -> bool:
    text = html_path.read_text(encoding="utf-8")
    block = f'<style {MARK}>\n{css}\n</style>\n'
    if STYLE_RE.search(text):                       # refresh existing inline block
        new = STYLE_RE.sub(block, text, count=1)
    elif LINK_RE.search(text):                      # replace the external <link>
        new = LINK_RE.sub(block, text, count=1)
    else:
        return False
    if new != text:
        html_path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    css = CSS.read_text(encoding="utf-8")
    pages = sorted(REFACTOR.glob("*/*/Student_Exploration.html"))
    changed = 0
    for p in pages:
        if inline_one(p, css):
            changed += 1
    print(f"Inlined lesson.css into {changed}/{len(pages)} Student_Exploration.html pages")


if __name__ == "__main__":
    main()
