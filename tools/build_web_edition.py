"""Generate a full linked web edition for the whole physics course.

Transforms every lesson's self-contained ``Student_Exploration.html`` into a
web-edition lesson page wrapped in the Kinematics site shell (site.css/site.js):
co-branded header + nav, hero, sticky TOC with scroll-spy, prev/next pager, and a
"Download teacher guide" link. Also generates a landing page per unit (lesson
grid) and a course index linking all units. Copies _assets, teacher guides, and
unit plans.

Output: Publisher_Ready_Curriculum/Physics_Web/  (one browsable site, all units)

Usage:
    python tools/build_web_edition.py
"""
from __future__ import annotations
import re
import shutil
from html import escape
from pathlib import Path

from bs4 import BeautifulSoup, Tag

ROOT = Path(__file__).resolve().parent.parent
REFACTOR = ROOT / "Publisher_Ready_Curriculum" / "01_Physics_East_Meadow_Refactor"
ASSET_SRC = ROOT / "Publisher_Ready_Curriculum" / "01_Physics_East_Meadow_Web" / "_assets"
OUT = ROOT / "Publisher_Ready_Curriculum" / "Physics_Web"

UNIT_NAMES = {
    "00_Math_in_Science": "Math in Science",
    "01_Kinematics": "Kinematics",
    "02_Forces": "Forces",
    "03_Momentum_Impulse": "Momentum & Impulse",
    "04_Energy": "Work, Energy & Power",
    "05_Thermodynamics": "Thermal Energy & Conservation",
    "06_Electrostatics": "Electrostatics",
    "07_Current_Electricity": "Current Electricity",
    "08_Waves": "Waves & Sound",
    "09_Modern_Physics": "Modern Physics",
}

# data-section (Student_Exploration) -> (web section id, extra class)
SECTION_MAP = {
    "phenomenon": ("phenomenon", ""),
    "driving-question": ("driving", "driver"),
    "notice-wonder": ("notice", "notice-wonder"),
    "initial-model": ("initial", ""),
    "interactive": ("investigate", ""),
    "make-it-make-sense": ("mims", ""),
    "vocab": ("vocab", "vocab"),
    "revise-model": ("revise", ""),
    "return-to-phenomenon": ("return", ""),
    "exit-ticket": ("exit", "exit"),
    "explore-further": ("explore", ""),
}
TOC = [
    ("phenomenon", "Phenomenon"), ("driving", "Driving question"),
    ("notice", "Notice &amp; wonder"), ("initial", "Initial model"),
    ("investigate", "Investigate"), ("mims", "Make it make sense"),
    ("vocab", "Vocabulary"), ("revise", "Revise"),
    ("return", "Return to phenomenon"), ("exit", "Exit ticket"),
    ("explore", "Explore further"),
]

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
    'family=Architects+Daughter&family=Lora:ital,wght@0,400;0,600;1,400&'
    'family=JetBrains+Mono:wght@500&display=swap">'
)
SVG_DEFS = (
    '<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">\n'
    '  <defs><filter id="ink-wobble" x="-2%" y="-2%" width="104%" height="104%">\n'
    '    <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" seed="3" result="noise"/>\n'
    '    <feDisplacementMap in="SourceGraphic" in2="noise" scale="1.5"/>\n'
    '  </filter></defs>\n</svg>'
)
CONTROLS_CSS = """
/* ----- interactive control primitives (carried from the lesson pages) ----- */
.controls { display: flex; flex-direction: column; gap: .55rem; margin: 1rem 0; }
.controls label { display: flex; justify-content: space-between; align-items: center; gap: 1rem; font-size: .92rem; }
.controls input[type="range"] { flex: 1; accent-color: var(--red-pen); }
.noscript-storyboard { display: block; }
"""


def slugify(title: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return re.sub(r"-+", "-", s)


def chip_label(text: str) -> str:
    return text if text.upper() == "BTC" else text.title()


def inner(tag: Tag) -> str:
    return tag.decode_contents()


def parse_lesson(html_path: Path) -> dict:
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "lxml")
    shell = soup.select_one(".lesson-shell") or soup.body
    h1 = shell.select_one("header.brand-header h1")
    h1_text = h1.get_text(" ", strip=True) if h1 else html_path.parent.name
    m = re.search(r"Lesson\s+\d+:\s*(.+)$", h1_text)
    title = m.group(1).strip() if m else h1_text

    chips = []
    for c in shell.select(".strategy-chip"):
        cls = next((k for k in c.get("class", []) if k != "strategy-chip"), "")
        chips.append((chip_label(c.get_text(strip=True)), cls))

    body, summary, lede = [], "", ""
    for child in shell.children:
        if not isinstance(child, Tag):
            continue
        if child.name in ("header", "footer"):
            continue
        if child.name == "aside" and "turn-and-talk" in child.get("class", []):
            body.append(f'<aside class="tt">{inner(child)}</aside>')
            continue
        if child.name == "section":
            ds = child.get("data-section", "")
            if ds == "phenomenon":
                p = child.find("p")
                summary = p.get_text(" ", strip=True) if p else ""
            if ds == "driving-question":
                lede = child.get_text(" ", strip=True).replace("Driving Question", "").strip()
            sid, extra = SECTION_MAP.get(ds, (ds or "sec", ""))
            cls = ("section " + extra).strip()
            body.append(f'<section id="{sid}" class="{cls}">{inner(child)}</section>')
    if len(summary) > 165:
        summary = summary[:162].rsplit(" ", 1)[0] + "…"
    return {"title": title, "chips": chips, "body": "\n".join(body),
            "summary": summary, "lede": lede or summary}


# ---------- HTML templates ----------

def _head(title: str, depth: int) -> str:
    up = "../" * depth
    return (f'<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{escape(title)}</title>\n{FONTS}\n'
            f'<link rel="stylesheet" href="{up}_assets/site.css">\n</head>\n<body>\n'
            f'{SVG_DEFS}\n<div class="progress-bar"></div>')


def _header(depth: int, label: str, nav: list[tuple[str, str, bool]]) -> str:
    up = "../" * depth
    items = "\n".join(
        f'      <a href="{href}"{" class=\"active\"" if active else ""}>{escape(txt)}</a>'
        for txt, href, active in nav)
    return (f'\n<header class="site-header">\n  <div class="site-header-inner">\n'
            f'    <a class="brand-lockup" href="{up}index.html">\n      <span class="logos">\n'
            f'        <img src="{up}_assets/brand/em_logo.svg" alt="East Meadow Schools">\n'
            f'        <span class="x">×</span>\n'
            f'        <img src="{up}_assets/brand/vs_logo.svg" alt="Valley Stream Central HSD">\n'
            f'      </span>\n      <span class="label">{escape(label)}</span>\n    </a>\n'
            f'    <nav>\n{items}\n    </nav>\n  </div>\n</header>')


FOOTER = ('\n<footer class="site-footer">\n  <div class="site-footer-inner">\n'
          '    <span class="tagline">Learning, Achieving, Succeeding!</span>\n'
          '    <span>East Meadow Schools × Valley Stream Central High School District · 2026</span>\n'
          '  </div>\n</footer>')


def _chips_html(chips: list[tuple[str, str]]) -> str:
    return "".join(f'<span class="chip {cls}">{escape(t)}</span>' for t, cls in chips)


def lesson_page(unit_name: str, num: str, lesson: dict, *, teacher_docx: str | None,
                prev: tuple[str, str, str], nxt: tuple[str, str, str], total: int) -> str:
    head = _head(f"{lesson['title']} · {unit_name} · Lesson {num}", depth=2)
    header = _header(2, f"Physics · {unit_name}", [
        ("Course", "../../index.html", False), ("Unit", "../index.html", False)])
    td = (f'\n    <a href="../teacher_guides/{teacher_docx}" class="teacher-download" download>'
          f'Download teacher guide (DOCX)</a>' if teacher_docx else "")
    hero = (f'\n<section class="hero">\n  <div class="hero-inner">\n'
            f'    <div class="eyebrow">Lesson {num} · Unit: {escape(unit_name)}</div>\n'
            f'    <h1>{escape(lesson["title"])}</h1>\n'
            f'    <p class="lede">{escape(lesson["lede"])}</p>\n'
            f'    <div class="chips">{_chips_html(lesson["chips"])}</div>{td}\n'
            f'  </div>\n</section>')
    toc = "\n".join(f'        <li><a href="#{sid}">{label}</a></li>' for sid, label in TOC)
    pager = (f'\n      <nav class="pager">\n'
             f'        <a class="prev" href="{prev[0]}"><span class="label">{prev[1]}</span>'
             f'<span class="target">{escape(prev[2])}</span></a>\n'
             f'        <a class="next" href="{nxt[0]}"><span class="label">{nxt[1]}</span>'
             f'<span class="target">{escape(nxt[2])}</span></a>\n      </nav>')
    main = (f'\n<main>\n  <div class="shell with-toc">\n    <div>\n{lesson["body"]}\n{pager}\n    </div>\n'
            f'    <aside class="toc">\n      <h4>On this page</h4>\n      <ol>\n{toc}\n      </ol>\n    </aside>\n  </div>\n</main>')
    foot = ('\n<footer class="site-footer">\n  <div class="site-footer-inner">\n'
            '    <span class="tagline">Learning, Achieving, Succeeding!</span>\n'
            f'    <span>Lesson {num} of {total} · Unit: {escape(unit_name)}</span>\n  </div>\n</footer>')
    return (head + header + hero + main + foot +
            '\n<script type="module" src="../../_assets/site.js"></script>\n</body>\n</html>\n')


def unit_index(unit_name: str, lessons: list[dict], *, unit_plan: str | None) -> str:
    head = _head(f"{unit_name} · Physics · East Meadow × Valley Stream", depth=1)
    header = _header(1, f"Physics · {unit_name}", [
        ("Course", "../index.html", False), ("Unit", "index.html", True)])
    n = len(lessons)
    dl = (f'<a class="teacher-download" href="{unit_plan}" download>Download unit plan (DOCX)</a>'
          if unit_plan else "")
    hero = (f'\n<section class="hero">\n  <div class="hero-inner">\n'
            f'    <div class="eyebrow">Unit · {escape(unit_name)} · {n} lessons</div>\n'
            f'    <h1>{escape(unit_name)}</h1>\n'
            f'    <p class="lede">{n} phenomenon-based lessons. Each opens with a real phenomenon, '
            f'gives students hands-on tools to investigate it, and ends with a transfer task. '
            f'Click any lesson to launch its interactive student page.</p>\n'
            f'    <div class="chips"><span class="chip">NYSSLS</span>'
            f'<span class="chip">SEL · every lesson</span>'
            f'<span class="chip">Differentiation · every lesson</span></div>\n    {dl}\n'
            f'  </div>\n</section>')
    cards = []
    for li in lessons:
        cards.append(
            f'          <li><a class="lesson-card" href="lessons/{li["slug"]}.html">\n'
            f'            <div class="number">Lesson {li["num"]}</div>\n'
            f'            <div class="title">{escape(li["title"])}</div>\n'
            f'            <div class="summary">{escape(li["summary"])}</div>\n'
            f'            <div class="footer"><span>{escape(", ".join(t for t, _ in li["chips"]))}</span></div>\n'
            f'          </a></li>')
    grid = "\n".join(cards)
    main = (f'\n<main>\n  <div class="shell">\n    <div>\n      <section class="section">\n'
            f'        <h2><span class="num">{n} lessons</span> Unit at a glance</h2>\n'
            f'        <ol class="lesson-grid">\n{grid}\n        </ol>\n      </section>\n    </div>\n  </div>\n</main>')
    return (head + header + hero + main + FOOTER +
            '\n<script type="module" src="../_assets/site.js"></script>\n</body>\n</html>\n')


def course_index(units: list[dict]) -> str:
    head = _head("Physics · East Meadow × Valley Stream Central HSD", depth=0)
    header = _header(0, "Physics", [("Course", "index.html", True)])
    total = sum(u["n"] for u in units)
    hero = (f'\n<section class="hero">\n  <div class="hero-inner">\n'
            f'    <div class="eyebrow">Regents Physics · {len(units)} units · {total} lessons</div>\n'
            f'    <h1>Physics — the whole course, phenomenon by phenomenon.</h1>\n'
            f'    <p class="lede">NYSSLS-aligned, phenomenon-based lessons for the joint East Meadow / '
            f'Valley Stream Central pilot. Every lesson is an interactive student page; teacher guides, '
            f'worksheets, notes, and answer keys ship alongside.</p>\n'
            f'    <div class="chips"><span class="chip">NYSSLS HS-PS</span>'
            f'<span class="chip">5E phenomenon-based</span><span class="chip">SEL + Differentiation</span></div>\n'
            f'  </div>\n</section>')

    # "Jump to unit" chip nav
    jump = "".join(
        f'<a class="chip" href="#unit-{u["folder"]}">Unit {u["unit_no"]} · {escape(u["name"])}</a>'
        for u in units)
    overview = (f'      <section class="section">\n'
                f'        <h2><span class="num">{len(units)} units</span> Jump to a unit</h2>\n'
                f'        <div class="chips">{jump}</div>\n      </section>')

    # One section per unit, listing its lessons as cards
    unit_sections = []
    for u in units:
        cards = []
        for li in u["lessons"]:
            chips_txt = ", ".join(t for t, _ in li["chips"])
            cards.append(
                f'          <li><a class="lesson-card" href="{u["folder"]}/lessons/{li["slug"]}.html">\n'
                f'            <div class="number">Lesson {li["num"]}</div>\n'
                f'            <div class="title">{escape(li["title"])}</div>\n'
                f'            <div class="summary">{escape(li["summary"])}</div>\n'
                f'            <div class="footer"><span>{escape(chips_txt)}</span></div>\n'
                f'          </a></li>')
        grid = "\n".join(cards)
        unit_sections.append(
            f'      <section class="section" id="unit-{u["folder"]}">\n'
            f'        <h2><span class="num">Unit {u["unit_no"]}</span> '
            f'<a href="{u["folder"]}/index.html">{escape(u["name"])}</a> '
            f'<span class="num">· {u["n"]} lessons</span></h2>\n'
            f'        <ol class="lesson-grid">\n{grid}\n        </ol>\n      </section>')

    main = ('\n<main>\n  <div class="shell">\n    <div>\n'
            + overview + "\n" + "\n".join(unit_sections)
            + '\n    </div>\n  </div>\n</main>')
    return (head + header + hero + main + FOOTER +
            '\n<script type="module" src="_assets/site.js"></script>\n</body>\n</html>\n')


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(ASSET_SRC, OUT / "_assets")
    # append interactive control styles to the copied site.css
    css = OUT / "_assets" / "site.css"
    css.write_text(css.read_text(encoding="utf-8") + CONTROLS_CSS, encoding="utf-8")

    units_meta = []
    for unit_dir in sorted(REFACTOR.iterdir()):
        if not unit_dir.is_dir() or not unit_dir.name[:2].isdigit():
            continue
        unit_name = UNIT_NAMES.get(unit_dir.name,
                                   re.sub(r"^\d+_", "", unit_dir.name).replace("_", " "))
        lesson_dirs = [d for d in sorted(unit_dir.iterdir())
                       if d.is_dir() and d.name[:2].isdigit()
                       and (d / "Student_Exploration.html").is_file()]
        if not lesson_dirs:
            continue
        out_unit = OUT / unit_dir.name
        (out_unit / "lessons").mkdir(parents=True, exist_ok=True)
        (out_unit / "teacher_guides").mkdir(parents=True, exist_ok=True)

        parsed = []
        for d in lesson_dirs:
            num = d.name[:2]
            data = parse_lesson(d / "Student_Exploration.html")
            data["num"] = num
            data["slug"] = f"{num}-{slugify(data['title'])}"
            # copy teacher guide
            tg = d / "Teacher_Guide.docx"
            tg_name = None
            if tg.is_file():
                tg_name = f"{data['slug']}-teacher-guide.docx"
                shutil.copy2(tg, out_unit / "teacher_guides" / tg_name)
            data["tg"] = tg_name
            parsed.append(data)

        # unit plan
        up = unit_dir / "Unit_Plan.docx"
        up_name = None
        if up.is_file():
            up_name = "Unit_Plan.docx"
            shutil.copy2(up, out_unit / up_name)

        total = len(parsed)
        for i, data in enumerate(parsed):
            if i == 0:
                prev = ("../index.html", "← Unit index", unit_name)
            else:
                p = parsed[i - 1]
                prev = (f"{p['slug']}.html", "← Previous lesson", p["title"])
            if i == total - 1:
                nxt = ("../index.html", "Back to unit →", unit_name)
            else:
                nx = parsed[i + 1]
                nxt = (f"{nx['slug']}.html", "Next lesson →", nx["title"])
            page = lesson_page(unit_name, data["num"], data, teacher_docx=data["tg"],
                               prev=prev, nxt=nxt, total=total)
            (out_unit / "lessons" / f"{data['slug']}.html").write_text(page, encoding="utf-8")

        (out_unit / "index.html").write_text(
            unit_index(unit_name, parsed, unit_plan=up_name), encoding="utf-8")
        units_meta.append({
            "folder": unit_dir.name, "name": unit_name,
            "unit_no": unit_dir.name[:2].lstrip("0") or "0", "n": total,
            "lessons": [{"num": d["num"], "title": d["title"], "slug": d["slug"],
                         "summary": d["summary"], "chips": d["chips"]} for d in parsed],
        })

    (OUT / "index.html").write_text(course_index(units_meta), encoding="utf-8")
    n_lessons = sum(u["n"] for u in units_meta)
    print(f"Built web edition: {len(units_meta)} units, {n_lessons} lesson pages → "
          f"{OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
