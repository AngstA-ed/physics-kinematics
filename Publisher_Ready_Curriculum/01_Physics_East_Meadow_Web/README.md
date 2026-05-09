# Physics — Kinematics · Web Edition

A modern, browser-first version of the Kinematics pilot unit, built without OneNote constraints. Every lesson is a self-contained HTML page with rich, drag-and-slide interactivity, intended for direct browser delivery (SharePoint Permissive document library, GitHub Pages, or any static host).

This is the **sibling** of [`../01_Physics_East_Meadow_Refactor/`](../01_Physics_East_Meadow_Refactor/), which is the OneNote-paste-friendly track. Same source pedagogy; different delivery target.

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
