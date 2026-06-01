# Physics — Full Web Edition (all units)

A single browsable, linked website for the whole Regents Physics course
(East Meadow × Valley Stream Central HSD). Generated from the lesson sources in
`../01_Physics_East_Meadow_Refactor/` — do **not** hand-edit the pages here;
edit the sources and regenerate.

## Structure

```
index.html                     ← course landing (10 unit cards)
_assets/                        site.css · site.js · brand/ · notebook.svg
<NN_Unit>/index.html            unit landing (lesson grid + unit-plan download)
<NN_Unit>/lessons/<slug>.html   interactive lesson pages (site shell + interactive + TOC + prev/next)
<NN_Unit>/teacher_guides/*.docx teacher guides (download links from each lesson hero)
<NN_Unit>/Unit_Plan.docx        unit plan (download link from the unit page)
```

Each lesson page wraps the lesson's interactive Student Exploration content in the
site shell: co-branded header + nav, hero with strategy chips and a "Download
teacher guide" link, sticky table of contents with scroll-spy, a reading-progress
bar, and prev/next pager. Images (logos + figures) are embedded as data URIs, so
pages are self-contained.

## Coverage

10 units · 58 lesson pages (Math in Science, Kinematics, Forces, Momentum &
Impulse, Work/Energy/Power, Thermal Energy, Electrostatics, Current Electricity,
Waves & Sound, Modern Physics).

## Regenerate

```bash
source .venv/bin/activate
python tools/build_web_edition.py        # rebuilds this whole site
python tools/validate_web.py             # (optional) answer-leak check
```

The generator copies `_assets` from the original Kinematics web edition
(`../01_Physics_East_Meadow_Web/_assets/`) and appends the interactive control
styles. The original Kinematics hand-built web edition is left untouched.

## Deploy

Drop this folder into a SharePoint document library (Browser File Handling =
Permissive) or publish to GitHub Pages. All links are relative, so it works from
any base path. The handwriting/serif fonts load from Google Fonts when online and
fall back to system fonts offline; all other styling and images are self-contained.
