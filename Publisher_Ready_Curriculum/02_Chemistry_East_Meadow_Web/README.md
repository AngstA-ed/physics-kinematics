# Chemistry — Web Edition

A browser-first, lab-notebook-styled version of the full chemistry curriculum
(14 units, 79 lessons), generated from the markdown sources in
[`../02_Chemistry_East_Meadow_Refactor/`](../02_Chemistry_East_Meadow_Refactor/).
Sibling of [`../01_Physics_East_Meadow_Web/`](../01_Physics_East_Meadow_Web/) —
same design system, same delivery target (SharePoint Permissive, GitHub Pages,
or any static host).

## Generated, not hand-authored

Unlike the physics web edition (hand-authored interactive pages for one unit),
this whole site is **generated** by `tools/build_web.py`. Each lesson page maps
the lesson's `Student_Worksheet.md` sections onto the lab-notebook template,
pulls vocabulary / strategy chips / "explore further" links from
`Teacher_Guide.md`, embeds the lesson figures, and links a downloadable
`Teacher_Guide.docx`. A handful of flagship lessons additionally get a custom
interactive widget (registered in `tools/build_web.py`).

## Build

```
source .venv/bin/activate
python tools/build_lessons.py --root Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor   # ensure DOCX are current
python tools/build_web.py                                  # whole course
python tools/build_web.py --units 04_Gas_Laws              # one unit (index left as-is)
```

Output: `index.html` (course hub) · `units/<unit>.html` (per-unit lesson grid) ·
`lessons/<UU>-<LL>-<slug>.html` (79 lesson pages) · `teacher_guides/*.docx`
(downloads) · `lessons/fig/<UU>_<LL>/*.png` (copied figures).

## Preview locally

```
python3 -m http.server 8099 --directory Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Web
# open http://localhost:8099/
```

## Visual identity

Reuses the physics **lab-notebook** design system in `_assets/site.css` — cream
graph paper, Architects Daughter handwriting headlines, Lora body, JetBrains
Mono readouts, hand-drawn outline buttons and chips, stamped section numbers.
The per-page hero stamp (e.g. "UNIT 04") is set by a `--hero-stamp` CSS variable
the generator writes into each page; the rest of the design lives in the shared
`:root` token block.
