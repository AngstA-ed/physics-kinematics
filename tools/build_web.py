"""Generate the Chemistry web edition (lab-notebook static site) from the
existing refactor markdown — mirroring 01_Physics_East_Meadow_Web.

For every lesson it maps the Student_Worksheet.md sections onto the physics
lesson-page template, pulls vocabulary / strategy chips / explore links from the
Teacher_Guide.md, copies figures + the built Teacher_Guide.docx, and writes a
styled HTML page. Also writes an index hub and one page per unit.

Usage:
    python tools/build_web.py                 # whole course
    python tools/build_web.py --units 02_Physical_Behavior_of_Matter
"""
from __future__ import annotations
import argparse, html, re, shutil, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFACTOR = ROOT / "Publisher_Ready_Curriculum" / "02_Chemistry_East_Meadow_Refactor"
WEB = ROOT / "Publisher_Ready_Curriculum" / "02_Chemistry_East_Meadow_Web"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Architects+Daughter&family=Lora:ital,wght@0,400;0,600;1,400&'
         'family=JetBrains+Mono:wght@500&display=swap">')
INK_SVG = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">\n'
           '  <defs><filter id="ink-wobble" x="-2%" y="-2%" width="104%" height="104%">'
           '<feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" seed="3" result="noise"/>'
           '<feDisplacementMap in="SourceGraphic" in2="noise" scale="1.5"/></filter></defs></svg>')
FOOTER = ('<footer class="site-footer"><div class="site-footer-inner">'
          '<span class="tagline">Learning, Achieving, Succeeding!</span>'
          '<span>{sub}</span></div></footer>')

# Worksheet H2 heading -> (section id, extra class, toc label)
SECTION_MAP = {
    "phenomenon": ("phenomenon", "", "Phenomenon"),
    "notice & wonder": ("notice", "notice-wonder", "Notice &amp; wonder"),
    "notice and wonder": ("notice", "notice-wonder", "Notice &amp; wonder"),
    "initial model": ("initial", "", "Initial model"),
    "investigation": ("investigate", "", "Investigate"),
    "make it make sense": ("mims", "", "Make it make sense"),
    "revise your model": ("revise", "", "Revise"),
    "exit ticket": ("exit", "exit", "Exit ticket"),
}
SECTION_ORDER = ["phenomenon", "driving", "notice", "initial", "investigate",
                 "mims", "vocab", "revise", "exit", "explore"]
TOC_LABELS = {"phenomenon": "Phenomenon", "driving": "Driving question",
              "notice": "Notice &amp; wonder", "initial": "Initial model",
              "investigate": "Investigate", "mims": "Make it make sense",
              "vocab": "Vocabulary", "revise": "Revise", "exit": "Exit ticket",
              "explore": "Explore further"}


def md_to_html(md: str) -> str:
    """Markdown fragment -> HTML via pandoc."""
    if not md.strip():
        return ""
    r = subprocess.run(["pandoc", "-f", "markdown", "-t", "html", "--wrap=none"],
                       input=md, capture_output=True, text=True)
    return r.stdout.strip()


def slug(lesson_dir: str) -> str:
    return re.sub(r"^\d+_", "", lesson_dir).replace("_", "-").lower()


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.is_file() else ""


def split_sections(md: str) -> dict[str, str]:
    """Split markdown into {lowercased H2 heading: body markdown}."""
    out, cur, buf = {}, None, []
    for line in md.splitlines():
        m = re.match(r"^##\s+(.*)", line)
        if m:
            if cur is not None:
                out[cur] = "\n".join(buf).strip()
            cur = m.group(1).strip().lower()
            buf = []
        elif cur is not None:
            buf.append(line)
    if cur is not None:
        out[cur] = "\n".join(buf).strip()
    return out


def parse_vocab(tg: str) -> list[tuple[str, str]]:
    sec = split_sections(tg).get("key vocabulary (max 3)", "")
    terms = []
    for line in sec.splitlines():
        m = re.match(r"-\s*\*\*(.+?)\*\*\s*[—-]\s*(.+)", line.strip())
        if m:
            terms.append((m.group(1).strip(), m.group(2).strip()))
    return terms[:3]


def parse_chips(tg: str) -> tuple[list[str], str]:
    chips, nyssls = [], ""
    for line in tg.splitlines():
        m = re.search(r"Strategy chips?:\s*(.+)", line)
        if m and not chips:
            chips = [c.strip() for c in re.split(r"[·,/]", m.group(1)) if c.strip()][:3]
        m2 = re.search(r"\bHS-[A-Z]+\d-\d+\b", line)
        if m2 and not nyssls:
            nyssls = m2.group(0)
    return chips, nyssls


def parse_explore(tg: str) -> str:
    """Curated Resources 'Javalab / Labs' bullets -> resource-list HTML."""
    secs = split_sections(tg)
    # the curated resources sub-headings are ### so they fall under the H2 body
    body = ""
    for k, v in secs.items():
        if "curated resources" in k:
            body = v
            break
    items = []
    block = re.split(r"###\s+Javalab\s*/\s*Labs", body)
    if len(block) > 1:
        seg = re.split(r"\n###\s+", block[1])[0]
        for line in seg.splitlines():
            lm = re.match(r"-\s*(.+)", line.strip())
            if not lm:
                continue
            txt = lm.group(1)
            link = re.search(r"<(https?://[^>]+)>|\((https?://[^)]+)\)|(https?://\S+)", txt)
            url = next((g for g in (link.groups() if link else []) if g), None)
            label = re.sub(r"<https?://[^>]+>|\(https?://[^)]+\)|https?://\S+", "", txt).strip(" :—-")
            label = re.sub(r"\*\*(.+?)\*\*", r"\1", label)
            if url:
                dom = re.sub(r"^https?://(www\.)?", "", url).split("/")[0]
                items.append(f'<li><a href="{html.escape(url)}" target="_blank" rel="noopener">'
                             f'{html.escape(label) or dom}<span class="source">{html.escape(dom)}</span></a></li>')
            elif label:
                items.append(f'<li><span>{html.escape(label)}</span></li>')
    return "\n".join(items)


def header_html(depth: int, label: str) -> str:
    up = "../" * depth
    return f'''<header class="site-header"><div class="site-header-inner">
  <a class="brand-lockup" href="{up}index.html"><span class="logos">
    <img src="{up}_assets/brand/em_logo.svg" alt="East Meadow Schools"><span class="x">×</span>
    <img src="{up}_assets/brand/vs_logo.svg" alt="Valley Stream Central HSD"></span>
    <span class="label">Chemistry</span></a>
  <nav><a href="{up}index.html">All Units</a><span class="label">· {label}</span></nav>
</div></header>'''


def stamp_css(text: str) -> str:
    svg = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 90 36'>"
           "<rect x='3' y='3' width='84' height='30' stroke='black' stroke-width='2.5' fill='none'/>"
           "<text x='45' y='22' text-anchor='middle' font-family='Architects Daughter' "
           f"font-size='12' fill='black'>{text}</text></svg>")
    return f'<style>.hero{{--hero-stamp:url("{svg}")}}</style>'


def page_shell(title: str, css_depth: int, header: str, hero: str, body: str,
               footer_sub: str, stamp: str = "NYSSLS") -> str:
    up = "../" * css_depth
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
  {FONTS}
  <link rel="stylesheet" href="{up}_assets/site.css">
  {stamp_css(stamp)}
</head><body>
{INK_SVG}
<div class="progress-bar"></div>
{header}
{hero}
<main>{body}</main>
{FOOTER.format(sub=html.escape(footer_sub))}
<script type="module" src="{up}_assets/site.js"></script>
</body></html>'''


def lesson_page(unit, lesson_dir, idx, total, prev_link, next_link) -> str:
    ldir = REFACTOR / unit["dir"] / lesson_dir
    tg = read(ldir / "Teacher_Guide.md")
    ws = read(ldir / "Student_Worksheet.md")
    title = re.sub(r"\s*[—-]\s*Student Worksheet.*$", "",
                   (ws.splitlines() or ["Lesson"])[0].lstrip("# ")).strip() or slug(lesson_dir)
    secs = split_sections(ws)
    chips, nyssls = parse_chips(tg)
    vocab = parse_vocab(tg)
    fig_rel = f"fig/{unit['num']}_{lesson_dir.split('_')[0]}"

    def fix_imgs(h):
        return h.replace('src="figures/', f'src="{fig_rel}/').replace("src='figures/", f"src='{fig_rel}/")

    # driving question split out of phenomenon
    phen = secs.get("phenomenon", "")
    driving = ""
    dm = re.search(r"\*\*Driving question:?\*\*\s*(.+)", phen)
    if dm:
        driving = dm.group(1).strip()
        phen = re.sub(r"\*\*Driving question:?\*\*.*", "", phen).strip()
    lede = re.sub(r"<[^>]+>", "", md_to_html(phen)).strip().split("\n")[0][:240]

    blocks = []
    num = 1

    def sec(sid, cls, label, inner):
        nonlocal num
        cl = ("section " + cls).strip()
        blocks.append(f'<section id="{sid}" class="{cl}">'
                      f'<h2><span class="num">{num:02d}</span> {label}</h2>{inner}</section>')
        num += 1

    if phen:
        sec("phenomenon", "", "Phenomenon", fix_imgs(md_to_html(phen)))
    if driving:
        sec("driving", "driver", "Driving question",
            f'<p style="font-size:1.25rem;font-weight:600;">{html.escape(driving)}</p>')
    if "notice & wonder" in secs or "notice and wonder" in secs:
        body = md_to_html(secs.get("notice & wonder") or secs.get("notice and wonder"))
        sec("notice", "notice-wonder", "Notice &amp; wonder",
            fix_imgs(body) + '<textarea rows="5" placeholder="What I notice / What I wonder…"></textarea>')
    if "initial model" in secs:
        sec("initial", "", "Initial model", fix_imgs(md_to_html(secs["initial model"])))
    if "investigation" in secs:
        sec("investigate", "", "Investigate", fix_imgs(md_to_html(secs["investigation"])))
    if "make it make sense" in secs:
        sec("mims", "", "Make it make sense", fix_imgs(md_to_html(secs["make it make sense"])))
    if vocab:
        dl = "".join(f"<dt>{html.escape(t)}</dt><dd>{html.escape(d)}</dd>" for t, d in vocab)
        extra = ""
        if "vocabulary in action" in secs:
            extra = fix_imgs(md_to_html(secs["vocabulary in action"]))
        sec("vocab", "vocab", "Key vocabulary", f"<dl>{dl}</dl>{extra}")
    if "revise your model" in secs:
        sec("revise", "", "Revise your model", fix_imgs(md_to_html(secs["revise your model"])))
    if "exit ticket" in secs:
        sec("exit", "exit", "Exit ticket", fix_imgs(md_to_html(secs["exit ticket"])))
    explore = parse_explore(tg)
    if explore:
        sec("explore", "", "Explore further", f'<ul class="resource-list">{explore}</ul>')

    chip_html = "".join(f'<span class="chip">{html.escape(c)}</span>' for c in chips)
    if nyssls:
        chip_html += f'<span class="chip">{html.escape(nyssls)}</span>'
    tg_dl = f'../teacher_guides/{unit["num"]}-{lesson_dir.split("_")[0]}-{slug(lesson_dir)}-teacher-guide.docx'
    hero = f'''<section class="hero"><div class="hero-inner">
  <div class="eyebrow">Lesson {lesson_dir.split('_')[0]} · Unit {unit['num']}: {html.escape(unit['name'])}</div>
  <h1>{html.escape(title)}</h1>
  <p class="lede">{html.escape(lede)}</p>
  <div class="chips">{chip_html}</div>
  <a href="{tg_dl}" class="teacher-download" download>Download teacher guide (DOCX)</a>
</div></section>'''

    # TOC
    present = []
    for b in blocks:
        m = re.search(r'id="([a-z]+)"', b)
        if m:
            present.append(m.group(1))
    toc = "".join(f'<li><a href="#{sid}">{TOC_LABELS.get(sid, sid)}</a></li>' for sid in present)
    pager = f'''<nav class="pager">
  <a class="prev" href="{prev_link[0]}"><span class="label">← {prev_link[1]}</span><span class="target">{prev_link[2]}</span></a>
  <a class="next" href="{next_link[0]}"><span class="label">{next_link[1]} →</span><span class="target">{next_link[2]}</span></a>
</nav>'''
    body = (f'<div class="shell with-toc"><div>{"".join(blocks)}{pager}</div>'
            f'<aside class="toc"><h4>On this page</h4><ol>{toc}</ol></aside></div>')
    header = header_html(1, html.escape(unit["name"]))
    return page_shell(f"{title} · {unit['name']} · Chemistry", 1, header, hero, body,
                      f"Lesson {lesson_dir.split('_')[0]} of {total} · Unit {unit['num']}: {unit['name']}",
                      stamp=f"UNIT {unit['num']}")


def unit_page(unit, lessons) -> str:
    cards = []
    for i, (ld, title, chips, nyssls) in enumerate(lessons, 1):
        href = f"../lessons/{unit['num']}-{ld.split('_')[0]}-{slug(ld)}.html"
        foot = f'<span>{html.escape(nyssls)}</span><span>{html.escape(" · ".join(chips))}</span>'
        cards.append(f'''<li><a class="lesson-card" href="{href}">
      <div class="number">Lesson {ld.split('_')[0]}</div><div class="title">{html.escape(title)}</div>
      <div class="footer">{foot}</div></a></li>''')
    hero = f'''<section class="hero"><div class="hero-inner">
  <div class="eyebrow">Unit {unit['num']} · {len(lessons)} lessons</div>
  <h1>{html.escape(unit['name'])}</h1>
  <a href="../teacher_guides/Unit_{unit['num']}_Plan.docx" class="teacher-download" download>Download unit plan (DOCX)</a>
</div></section>'''
    body = (f'<div class="shell"><div><section class="section">'
            f'<h2><span class="num">{len(lessons)} lessons</span> Unit at a glance</h2>'
            f'<ol class="lesson-grid">{"".join(cards)}</ol></section></div></div>')
    header = header_html(1, html.escape(unit["name"]))
    return page_shell(f"{unit['name']} · Chemistry", 1, header, hero, body,
                      f"Unit {unit['num']}: {unit['name']}", stamp=f"UNIT {unit['num']}")


def index_page(units) -> str:
    cards = []
    for u in units:
        href = f"units/{u['dir']}.html"
        cards.append(f'''<li><a class="lesson-card" href="{href}">
      <div class="number">Unit {u['num']}</div><div class="title">{html.escape(u['name'])}</div>
      <div class="summary">{u['nlessons']} lessons</div>
      <div class="footer"><span>{html.escape(u['nyssls'])}</span><span></span></div></a></li>''')
    hero = '''<section class="hero"><div class="hero-inner">
  <div class="eyebrow">Regents Chemistry · East Meadow × Valley Stream · 14 units</div>
  <h1>Phenomenon-based chemistry — built for the new NYSSLS Regents.</h1>
  <p class="lede">Every lesson opens with a real phenomenon, gives students something to investigate,
  introduces three vocabulary terms in the second half, and ends with a transfer task. Click any unit to begin.</p>
  <div class="chips"><span class="chip">NYSSLS</span><span class="chip">5E phenomenon-based</span>
  <span class="chip">SEL · every lesson</span><span class="chip">Differentiation · every lesson</span></div>
</div></section>'''
    body = (f'<div class="shell"><div><section class="section">'
            f'<h2><span class="num">14 units</span> The course</h2>'
            f'<ol class="lesson-grid">{"".join(cards)}</ol></section></div></div>')
    header = ('<header class="site-header"><div class="site-header-inner">'
              '<a class="brand-lockup" href="index.html"><span class="logos">'
              '<img src="_assets/brand/em_logo.svg" alt="East Meadow Schools"><span class="x">×</span>'
              '<img src="_assets/brand/vs_logo.svg" alt="Valley Stream Central HSD"></span>'
              '<span class="label">Chemistry</span></a>'
              '<nav><a href="index.html" class="active">All Units</a></nav></div></header>')
    return page_shell("Chemistry · East Meadow × Valley Stream", 0, header, hero, body,
                      "East Meadow Schools × Valley Stream Central High School District · 2026")


def discover_units(only):
    units = []
    for d in sorted(REFACTOR.iterdir()):
        if not d.is_dir() or not d.name[:2].isdigit():
            continue
        if only and d.name not in only:
            continue
        num = d.name.split("_")[0]
        name = re.sub(r"^\d+_", "", d.name).replace("_", " ")
        lessons = [x.name for x in sorted(d.iterdir()) if x.is_dir() and x.name[:2].isdigit()]
        units.append({"dir": d.name, "num": num, "name": name, "lessons": lessons})
    return units


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--units", nargs="*", default=None)
    args = ap.parse_args()
    units = discover_units(set(args.units) if args.units else None)
    (WEB / "lessons").mkdir(parents=True, exist_ok=True)
    (WEB / "units").mkdir(parents=True, exist_ok=True)
    (WEB / "teacher_guides").mkdir(parents=True, exist_ok=True)

    index_units = []
    npages = 0
    for u in units:
        lesson_meta = []
        for ld in u["lessons"]:
            tg = read(REFACTOR / u["dir"] / ld / "Teacher_Guide.md")
            ws = read(REFACTOR / u["dir"] / ld / "Student_Worksheet.md")
            title = re.sub(r"\s*[—-]\s*Student Worksheet.*$", "",
                           (ws.splitlines() or ["Lesson"])[0].lstrip("# ")).strip()
            chips, nyssls = parse_chips(tg)
            lesson_meta.append((ld, title or slug(ld), chips, nyssls))
        # lesson pages
        total = len(u["lessons"])
        for i, ld in enumerate(u["lessons"]):
            prev = ("../index.html", "Unit index", u["name"]) if i == 0 else \
                (f"{u['num']}-{u['lessons'][i-1].split('_')[0]}-{slug(u['lessons'][i-1])}.html",
                 "Previous", lesson_meta[i-1][1])
            nxt = (f"../units/{u['dir']}.html", "Unit page", u["name"]) if i == total-1 else \
                (f"{u['num']}-{u['lessons'][i+1].split('_')[0]}-{slug(u['lessons'][i+1])}.html",
                 "Next lesson", lesson_meta[i+1][1])
            page = lesson_page(u, ld, i, total, prev, nxt)
            (WEB / "lessons" / f"{u['num']}-{ld.split('_')[0]}-{slug(ld)}.html").write_text(page, encoding="utf-8")
            npages += 1
            # copy figures
            figsrc = REFACTOR / u["dir"] / ld / "figures"
            if figsrc.is_dir():
                figdst = WEB / "lessons" / "fig" / f"{u['num']}_{ld.split('_')[0]}"
                figdst.mkdir(parents=True, exist_ok=True)
                for png in figsrc.glob("*.png"):
                    shutil.copy2(png, figdst / png.name)
            # copy teacher guide docx
            tgd = REFACTOR / u["dir"] / ld / "Teacher_Guide.docx"
            if tgd.is_file():
                shutil.copy2(tgd, WEB / "teacher_guides" /
                             f"{u['num']}-{ld.split('_')[0]}-{slug(ld)}-teacher-guide.docx")
        # unit page + unit plan docx
        (WEB / "units" / f"{u['dir']}.html").write_text(unit_page(u, lesson_meta), encoding="utf-8")
        upd = REFACTOR / u["dir"] / "Unit_Plan.docx"
        if upd.is_file():
            shutil.copy2(upd, WEB / "teacher_guides" / f"Unit_{u['num']}_Plan.docx")
        _, unyssls = parse_chips(read(REFACTOR / u["dir"] / u["lessons"][0] / "Teacher_Guide.md")) if u["lessons"] else ("", "")
        index_units.append({**u, "nlessons": total, "nyssls": unyssls})

    if not args.units:  # only rewrite index on a full build
        (WEB / "index.html").write_text(index_page(index_units), encoding="utf-8")
    print(f"Wrote {npages} lesson pages + {len(units)} unit pages"
          + ("" if args.units else " + index") + f" to {WEB.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
