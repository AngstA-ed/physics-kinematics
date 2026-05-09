# Physics — Kinematics · Web Edition

A modern, browser-first version of the Kinematics pilot unit, built without OneNote constraints. Every lesson is a self-contained HTML page with rich, drag-and-slide interactivity, intended for direct browser delivery (SharePoint Permissive document library, GitHub Pages, or any static host).

This is the **sibling** of [`../01_Physics_East_Meadow_Refactor/`](../01_Physics_East_Meadow_Refactor/), which is the OneNote-paste-friendly track. Same source pedagogy; different delivery target.

## Teacher guide downloads

Each lesson hero has a **Download teacher guide (DOCX)** button. The downloads ship with the site at `teacher_guides/<lesson-slug>-teacher-guide.docx`.

The DOCX content is generated from the markdown sources in the OneNote-friendly track (`../01_Physics_East_Meadow_Refactor/01_Kinematics/<lesson>/Teacher_Guide.md`) via Pandoc + the co-branded reference template. After a teacher-guide markdown change, regenerate and re-copy:

```
source .venv/bin/activate
python tools/build_lessons.py 01_Kinematics       # rebuilds DOCX from MD
# Then re-copy into the web edition:
for L in 01_Vectors:01-vectors 02_Distance_and_Displacement:02-distance-displacement \
         03_Average_Speed_and_Velocity:03-velocity 04_Acceleration:04-acceleration \
         05_Motion_Graphs:05-motion-graphs 06_Freefall:06-freefall \
         07_Vertical_Projectiles:07-vertical-projectiles \
         08_Horizontal_Projectile_Motion:08-horizontal-projectile-motion \
         09_Projectiles_at_an_Angle:09-projectiles-at-an-angle; do
  src_dir="${L%%:*}"; dest_name="${L##*:}"
  cp "../01_Physics_East_Meadow_Refactor/01_Kinematics/${src_dir}/Teacher_Guide.docx" \
     "teacher_guides/${dest_name}-teacher-guide.docx"
done
```

The teacher guides follow the **5E phenomenon-based lesson model** documented in PPTX slide 32 (the joint training deck). Each guide has minute-by-minute facilitation script, sample teacher language, and anticipated student responses inside each phase (Engage / Explore / Explain / Elaborate / Evaluate).

## Visual identity

The web edition uses a **lab-notebook** identity — cream paper, fountain-pen ink, hand-drawn arrows, taped-on cards, hand-drawn outline buttons. The design system lives in `_assets/site.css`; brand tokens in the `:root` block at the top.

### Fonts (Google Fonts)

- **Architects Daughter** — block-print handwriting for headlines, callouts, and stamps
- **Lora** — readable serif for body text and lesson copy
- **JetBrains Mono** — tabular numbers in lab-readout panels

The fonts are loaded from `fonts.googleapis.com`. For air-gapped classrooms or districts that block third-party CDNs, vendor the three fonts locally:

1. Download `woff2` files for each font from `https://google-webfonts-helper.herokuapp.com/`.
2. Place them in `_assets/fonts/` (create the folder).
3. In each HTML page, replace the Google Fonts `<link>` with a local `_assets/fonts.css` that has `@font-face` declarations pointing at the local woff2 files.

### Rolling back to the previous SaaS design

Run `git checkout HEAD~1 -- Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css` from the project root. The HTML markup is forward-compatible with both stylesheets, so reverting the single CSS file restores the previous look. To also restore the previous typography, re-add the original Inter `<link>` tag in each HTML page.

## Sharing the demo

Paste this link into an email or Slack message to take someone on a self-paced tour:

```
https://angsta-ed.github.io/physics-kinematics/?tour=1
```

The recipient lands on the unit homepage and immediately starts a 9-step guided walkthrough — through the landing, the Vectors playground, the three-graph Acceleration simulator, the Projectiles target-shooting game, the Unit Plan, and the Regents-style assessment. Each step has a short copy-deck-style explanation and a "Skip tour" escape hatch. Tour state lives in sessionStorage, so back/forward and tab refresh resume cleanly. There is also a "Take the 2-minute tour" button on the landing-page hero for anyone who arrives without the query param.

## What's different from the OneNote-friendly track

| Aspect | OneNote-friendly track | Web edition (this folder) |
|---|---|---|
| Layout primitives | Tables for paste fidelity | Modern flexbox + CSS grid |
| Typography | Inter, conservative weights | Inter, bold display weights, large hero type |
| Interactives | Sliders + animations + `<noscript>` storyboard required | Drag-and-drop, multi-vector, live three-graph linkages, target-shooting games — no static fallback constraint |
| Branding | Co-branded header lockup | Co-branded gradient hero + sticky header lockup + brand-tinted accent system |
| Navigation | Folder structure | Top-level index, prev/next pager, sticky table-of-contents per page, scroll-spy |
| Reading aids | Linear scroll | Reading progress bar, anchored sections |
| External fonts | None (system stack) | `rsms.me/inter` for the Inter family |
| External JS / CDNs | None | None — still self-contained except font CSS |
| Teacher materials | DOCX sources | Linked from the OneNote-friendly track |

## Hosting

Three good options. Pick whichever your district allows.

### 1. SharePoint document library (Permissive mode)

Drop `01_Physics_East_Meadow_Web/` into a SharePoint document library that has **Browser File Handling** set to **Permissive**. Students click `index.html` from the library and get the full interactive experience. Confirm the setting with district IT before committing.

### 2. GitHub Pages

```
git checkout gh-pages
git rm -rf .
cp -R Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/* .
git add -A
git commit -m "Publish Kinematics web edition"
git push origin gh-pages
```

The site is then live at `https://<your-org>.github.io/<repo>/`.

### 3. Local file:// for in-class use

Open `index.html` directly from disk. Everything works without a server. The only network call is to `rsms.me/inter` for the Inter font; if the classroom is offline, the system fallback (San Francisco / Helvetica Neue) renders fine.

## Folder structure

```
01_Physics_East_Meadow_Web/
├── README.md                          # this file
├── index.html                         # unit landing page (lesson grid)
├── unit_plan.html                     # pacing, strategy rotation, vocabulary scope
├── assessment.html                    # Regents-style cluster (15 MC + 1 CR)
├── _assets/
│   ├── site.css                       # design system (~300 lines)
│   ├── site.js                        # progress bar, TOC scroll-spy, helpers
│   └── brand/
│       ├── em_logo.svg                # placeholder East Meadow wordmark
│       └── vs_logo.svg                # placeholder Valley Stream Central wordmark
└── lessons/
    ├── 01-vectors.html
    ├── 02-distance-displacement.html
    ├── 03-velocity.html
    ├── 04-acceleration.html
    ├── 05-motion-graphs.html
    ├── 06-freefall.html
    ├── 07-vertical-projectiles.html
    ├── 08-horizontal-projectile-motion.html
    └── 09-projectiles-at-an-angle.html
```

## Interactive highlights per lesson

| Lesson | What students do |
|---|---|
| 01 Vectors | Click "+ Add vector" to drop arrows on a grid. Drag tips to set magnitude/direction. Up to 6 vectors chained head-to-tail; live magnitude/direction/path readouts. Toggle component view. |
| 02 Distance and Displacement | Step-by-step path builder (E/W/N/S buttons). Toggle "show distance" and "show displacement" independently. Round-trip exposes zero-displacement walks. |
| 03 Average Speed and Velocity | Pick a scenario (straight, reversal, overshoot). Two cars race side-by-side; live readouts compare distance, average speed, and average velocity. |
| 04 Acceleration | a-slider from −4 to +4 m/s², plus initial velocity. Three linked graphs (x-t, v-t, a-t) draw simultaneously as the dot moves on the position track. |
| 05 Motion Graphs | Pick a scenario (constant v, constant a, reversal, speed-up-then-slow-down). All three graphs (x-t, v-t, a-t) draw alongside the moving dot. |
| 06 Freefall | Drop a rock and a feather side by side. Toggle air resistance: with it off, both land together. With it on, the feather quickly hits a low terminal velocity. |
| 07 Vertical Projectiles | Slider for v₀. Press Throw. Ball goes up, peaks (v=0), comes back down. v-t graph draws as a single straight line through zero. Peak time highlighted. |
| 08 Horizontal Projectile Motion | Cliff sandbox: vary table height and horizontal launch speed. A rolled marble and a dropped marble fall together — verify their fall times match every time. |
| 09 Projectiles at an Angle | **Target-shooting game.** Slide v₀ and θ. Press Launch. Aim at a target box. Toggle "Show optimal angle" to overlay the 45° trajectory at the same v₀. Optional moving-target mode. |

## Authoring notes

- All lessons share the same shell template (header + hero + TOC + sections + pager + footer).
- Lesson interactive code lives inline in each `.html` file (small enough to keep co-located).
- Brand tokens live in `_assets/site.css` `:root` — change the gradient or palette in one place.
- Pure ES module imports for `_assets/site.js`; no build step.

## Open questions / known limitations

- **Logos are placeholders.** Replace `_assets/brand/em_logo.svg` and `vs_logo.svg` with the official wordmarks when available.
- **Inter font is loaded from `rsms.me/inter`.** For air-gapped classrooms, vendor the font locally and update the `@import` URL.
- **Touch targets** on the vector playground (drag-handle circles) work but are sized for desktop; for an iPad-first deployment, increase the handle radius from 8 to 12.
- **No teacher materials in this folder.** Teacher Guides, Answer Keys, and the printable Unit Plan DOCX live in the OneNote-friendly track at [`../01_Physics_East_Meadow_Refactor/01_Kinematics/`](../01_Physics_East_Meadow_Refactor/01_Kinematics/). Both tracks share the same scope and sequence.

## Compatibility

Tested with: Safari 17+, Chrome 120+, Firefox 122+, Edge 120+. Mobile Safari (iPad) renders correctly; desktop pointer events for the drag-handle interactives are implemented as `pointerdown/move/up`, which work on touch.

JavaScript-disabled experience: lessons render with full content but the interactive widgets are blank. The teacher-friendly track has explicit `<noscript>` storyboard fallbacks; this web track does not — by design.
