"""Make every Student_Exploration.html fully self-contained so it renders
standalone (file://, OneNote paste, SharePoint, email, moved/downloaded copies)
with no external dependencies:

* inline _assets/lesson.css as a <style> block, and
* embed every local image (brand logos + figures) as a base64 data URI.

Re-run whenever lesson.css or a figure changes. Idempotent: refreshes an existing
inlined <style> block or replaces the external <link>; images already embedded as
data: URIs are left alone.

Usage:
    python tools/inline_lesson_css.py
"""
from __future__ import annotations
import base64
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFACTOR = ROOT / "Publisher_Ready_Curriculum" / "01_Physics_East_Meadow_Refactor"
CSS = REFACTOR / "_assets" / "lesson.css"

MARK = "data-inlined=\"lesson.css\""
LINK_RE = re.compile(r'[ \t]*<link[^>]*lesson\.css[^>]*>\s*', re.IGNORECASE)
STYLE_RE = re.compile(r'[ \t]*<style data-inlined="lesson\.css">.*?</style>\s*',
                      re.IGNORECASE | re.DOTALL)
# Only image-file src values appear with these extensions in these pages.
IMG_SRC_RE = re.compile(r'src="([^"]+\.(?:svg|png|jpe?g|gif))"', re.IGNORECASE)
_MIME = {".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg",
         ".jpeg": "image/jpeg", ".gif": "image/gif"}


def _inline_images(text: str, html_dir: Path) -> str:
    def repl(m: re.Match) -> str:
        src = m.group(1)
        if src.startswith(("data:", "http:", "https:")):
            return m.group(0)
        target = (html_dir / src).resolve()
        if not target.is_file():
            return m.group(0)
        mime = _MIME.get(target.suffix.lower())
        if not mime:
            return m.group(0)
        b64 = base64.b64encode(target.read_bytes()).decode("ascii")
        return f'src="data:{mime};base64,{b64}"'
    return IMG_SRC_RE.sub(repl, text)


def inline_one(html_path: Path, css: str) -> bool:
    text = html_path.read_text(encoding="utf-8")
    block = f'<style {MARK}>\n{css}\n</style>\n'
    if STYLE_RE.search(text):                       # refresh existing inline block
        new = STYLE_RE.sub(block, text, count=1)
    elif LINK_RE.search(text):                      # replace the external <link>
        new = LINK_RE.sub(block, text, count=1)
    else:
        new = text
    new = _inline_images(new, html_path.parent)
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
    print(f"Self-contained {changed}/{len(pages)} Student_Exploration.html pages "
          f"(inlined CSS + embedded images)")


if __name__ == "__main__":
    main()
