"""Convert rich interactive HTML lesson pages into OneNote-paste-friendly static HTML.

Removes JS, inlines CSS, replaces iframes with paste-time instructions, and replaces
interactive widgets (data-interactive="true") with their sibling <noscript> content.
Image base64 inlining is handled here too when image paths are local.
"""
from __future__ import annotations
import base64
import mimetypes
import re
from pathlib import Path
from bs4 import BeautifulSoup, Tag


def _embed_css(soup: BeautifulSoup, css_root: Path) -> None:
    """Replace <link rel=stylesheet> with inlined <style>, where possible."""
    for link in list(soup.find_all("link", rel="stylesheet")):
        href = link.get("href", "")
        css_path = (css_root / href).resolve() if href else None
        if css_path and css_path.is_file():
            style = soup.new_tag("style")
            style.string = css_path.read_text(encoding="utf-8")
            link.replace_with(style)
        else:
            link.decompose()


def _strip_scripts(soup: BeautifulSoup) -> None:
    for s in list(soup.find_all("script")):
        s.decompose()


def _replace_iframes(soup: BeautifulSoup) -> None:
    for iframe in list(soup.find_all("iframe")):
        src = iframe.get("src", "")
        # Convert YouTube embed URL to watch URL when possible
        watch = re.sub(r"youtube\.com/embed/([^?&]+)", r"youtube.com/watch?v=\1", src)
        wrapper = soup.new_tag("div", **{"class": "video-paste-instruction"})
        instr = soup.new_tag("p")
        instr.string = (
            "Video — in OneNote: Insert → Online Video, then paste this URL:"
        )
        link = soup.new_tag("a", href=watch)
        link.string = watch
        wrapper.append(instr)
        wrapper.append(link)
        iframe.replace_with(wrapper)


def _replace_interactive_widgets(soup: BeautifulSoup) -> None:
    for widget in list(soup.select('[data-interactive="true"]')):
        section = widget.find_parent("section") or widget.parent
        noscript = section.find("noscript") if section else None
        if noscript is None:
            # Should have been caught by validator; leave a placeholder.
            placeholder = soup.new_tag("div", **{"class": "missing-storyboard"})
            placeholder.string = "[Static fallback missing — see interactive version]"
            widget.replace_with(placeholder)
            continue
        # Move noscript children into widget's place; drop the noscript wrapper
        new_div = soup.new_tag("div", **{"class": "noscript-storyboard"})
        for child in list(noscript.children):
            new_div.append(child)
        widget.replace_with(new_div)
        noscript.decompose()


def _inline_images(soup: BeautifulSoup, html_dir: Path | None) -> None:
    if html_dir is None:
        return
    for img in list(soup.find_all("img")):
        src = img.get("src", "")
        if not src or src.startswith(("data:", "http:", "https:")):
            continue
        candidate = (html_dir / src).resolve()
        if candidate.is_file():
            mime, _ = mimetypes.guess_type(candidate)
            if mime is None:
                continue
            data = base64.b64encode(candidate.read_bytes()).decode("ascii")
            img["src"] = f"data:{mime};base64,{data}"


def staticify(html: str, *, css_root: Path, html_dir: Path | None = None) -> str:
    """Return a OneNote-paste-friendly static version of the given HTML.

    Parameters
    ----------
    html : str
        Source interactive HTML.
    css_root : Path
        Directory used to resolve relative <link rel="stylesheet"> hrefs.
    html_dir : Path | None
        Directory used to resolve relative <img src> for base64 inlining.
    """
    soup = BeautifulSoup(html, "lxml")
    _embed_css(soup, css_root)
    _strip_scripts(soup)
    _replace_iframes(soup)
    _replace_interactive_widgets(soup)
    _inline_images(soup, html_dir)
    return str(soup)
