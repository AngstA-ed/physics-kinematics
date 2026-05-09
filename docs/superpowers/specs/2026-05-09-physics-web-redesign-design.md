# Physics Web Edition — Lab Notebook Redesign Spec

**Date:** 2026-05-09
**Author:** Curriculum lead (Adam Stanco) with Claude
**Status:** Approved for planning
**Scope:** All 12 pages of the web edition (`Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/`) — 9 lessons + index + unit_plan + assessment.
**Source decisions:**
- Aesthetic direction: **Lab notebook** (chosen over chalkboard, editorial, retro-arcade)
- Approach: **Lab-notebook-as-chrome** (notebook frame, cleanly readable serif body)
- Handwriting font: **Architects Daughter** (chosen over Caveat, Patrick Hand, typewriter)
- Audience: **Both equally** — student-warm and adult-credible
- Animation budget: **Medium** — noticeable but not showy
- Dark mode: **Light only**

---

## 1. Goals and Non-Goals

### Goals

1. Replace the current modern-SaaS visual identity with a **lab-notebook** identity that reads as educational, science-y, and fun without sacrificing credibility for adult adopters.
2. Apply the new identity uniformly across **all 12 pages** of the web edition in a single migration.
3. Preserve every existing schema invariant (required headings, vocab cap, MC-emphasis rules, all 30 tests passing) — the redesign is visual only.
4. Honor the medium animation budget — first-load choreography on lesson interactives is the most ambitious moment; everything else is subtle hover and scroll-in motion.
5. Keep page weight under the existing 500 KB-per-page budget; net per-page increase ~90 KB from font payload.
6. `prefers-reduced-motion: reduce` disables all decorative animation while keeping essential interactive feedback.
7. Single-file rollback — reverting `_assets/site.css` returns the site to its current modern-SaaS look.

### Non-Goals (explicit YAGNI)

- Refactoring the lesson interactives (vector playground, projectile launcher, etc.). The SVG/JS inside `<div data-interactive="true">` blocks stays untouched; only the surrounding chrome changes.
- Redesigning the OneNote-friendly track at `01_Physics_East_Meadow_Refactor/`. Different audience, different track, separate identity.
- Dark-mode / blueprint alt theme.
- Custom hand-drawn raster illustrations (cost-benefit doesn't pay off; SVG and CSS get us 90% of the look).
- Per-lesson visual themes (e.g., "Vectors gets one identity, Projectiles gets another"). Single unified system.
- Brand-stamp PNG creation. SVG renders are sufficient for the placeholder logos.
- Audio — no soundtrack, no click sounds, no synth tones.
- Easter-egg interactions beyond the planned hover/load animations.
- Schema validators for design rules. Manual visual QA is the right tool.

---

## 2. Design Tokens

### 2.1 Paper & ink palette

Replace the current SaaS-bright palette with desaturated, paper-and-ink versions. Both district brand colors stay recognizable but read as inks rather than UI buttons.

| Token | Value | Role |
|---|---|---|
| `--paper` | `#fbf6e8` | Cream notebook page (warm, not pure white) |
| `--paper-edge` | `#f1eada` | Subtly darker page edge / margin tint |
| `--paper-tape` | `#e8dfc6` | Masking-tape rectangles on taped index cards |
| `--grid` | `rgba(166, 124, 82, 0.18)` | Sepia graph lines on backgrounds |
| `--rule` | `rgba(42, 77, 143, 0.15)` | Faint blue ruled-line tint |
| `--ink` | `#2b2418` | Body text — fountain-pen brown-black |
| `--ink-soft` | `#574a36` | Secondary text |
| `--ink-faint` | `#8a7a5a` | Captions, margin notes |
| `--em-purple` | `#5a2466` | EM-stamp purple (deeper than the previous `#662e80` so it reads as ink, not a Tailwind preset) |
| `--vs-blue` | `#2a4d8f` | Fountain-pen blue (replaces electric `#2ea3f2`) |
| `--red-pen` | `#c14626` | Corrections, "stamps," HOCHMAN strategy chip |
| `--highlighter` | `#fdd35e` | Yellow highlighter behind key terms (Driving Question banner) |
| `--mint` | `#3d8a5e` | BTC chip, ✓ "correct" annotations |
| `--peach` | `#e89668` | EM accent, RESTORATIVE CIRCLE chip (replaces previous `#f37366`) |

The two original brand identifiers (`--em-purple`, `--vs-blue`) are **renamed semantically only**. All existing CSS references to `--em-purple` and `--vs-blue` continue to work.

### 2.2 Typography

| Use | Font | Weight | Source |
|---|---|---|---|
| Hand-drawn headlines, captions, "stamp" badges | **Architects Daughter** | 400 | Google Fonts |
| Body — paragraphs, lesson copy, navigation | **Lora** | 400 / 600 / italic | Google Fonts |
| Tabular numbers, code-like readouts in interactives | **JetBrains Mono** | 500 | Google Fonts |

Single Google Fonts `<link>` per page imports all three:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Architects+Daughter&family=Lora:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@500&display=swap">
```

Inter is dropped. Total transferred font weight ~95 KB gzipped. Display strategy `swap` — Lora falls back to Georgia / system serif during load.

For air-gapped classrooms, the README documents how to vendor the three fonts into `_assets/fonts/` and swap the `<link>` for a local `@font-face` declaration.

### 2.3 Type scale

```css
--fs-hero: clamp(2.25rem, 5vw, 3.5rem);  /* unchanged */
--fs-h1: clamp(1.75rem, 3vw, 2.25rem);
--fs-h2: 1.5rem;
--fs-h3: 1.125rem;
--fs-body: 1rem;
--fs-small: 0.875rem;
--fs-tiny: 0.75rem;
```

Architects Daughter renders ~92% of the size of Lora at the same `font-size`. Hero handwriting elements get an extra +5% nudge to match the visual size of Lora at the same role.

### 2.4 Paper textures (CSS-only)

Two backgrounds applied selectively across the site:

1. **Graph paper** — for hero, lab-interactive containers, sketch-heavy sections. Two `linear-gradient` lines repeating at 22 px:
   ```css
   background-image:
     linear-gradient(var(--grid) 1px, transparent 1px),
     linear-gradient(90deg, var(--grid) 1px, transparent 1px);
   background-size: 22px 22px;
   ```
2. **Ruled paper** — for body sections (Phenomenon, Driving Question, Notice & Wonder, etc.). Single horizontal-line gradient at 28 px line-height (matches Lora's line-height):
   ```css
   background-image: linear-gradient(var(--rule) 1px, transparent 1px);
   background-size: 100% 28px;
   ```
   Type sits on the line.

No raster images for textures.

### 2.5 Spacing & radius

Current spacing scale (`--s-1` through `--s-8`, 8 px baseline) carries over. Two changes:

- **Card radius reduced** from `12 px` to `4 px`. Notebooks have square corners; rounded SaaS cards conflict with the metaphor.
- **Paper-edge "torn" effect** on section dividers — replace solid borders with a 2 px irregular dashed border using `border-image` (see §2.6).

### 2.6 SVG filter library — `_assets/notebook.svg`

A single inline SVG file referenced once per page (or imported as a sprite). Defines:

- `<filter id="ink-wobble">` — `feTurbulence` (baseFrequency 0.05) + `feDisplacementMap` (scale 1.5). Applied to a few hero/display elements where ink imperfection sells the metaphor (rubber-stamp badges, hand-drawn arrows on the hero).
- `<filter id="paper-grain">` — very subtle `feTurbulence` + `feColorMatrix` mixed at low opacity. Applied to large paper backgrounds (hero, lab containers).
- `<symbol id="doodle-arrow">`, `<symbol id="doodle-star">`, `<symbol id="doodle-check">`, `<symbol id="doodle-arrow-bend">`, `<symbol id="doodle-spiral">`, `<symbol id="doodle-bullet">` — six small doodle SVG symbols for inter-section dividers. Each is ~30×20 px, hand-drawn-feel paths.

Filter degrades to a no-op (visible content stays readable) when unsupported.

---

## 3. Component reimagining

The same DOM nodes get new visual treatments. Existing class names stay primary so reverting just `site.css` returns the previous look.

### 3.1 Reading-progress bar (top of every page)

- Current: solid 3 px gradient line.
- New: 3 px line in `--vs-blue` with a small ellipse at the leading edge (faux ink-bleed dot, 6 px diameter, 0.7 opacity). Subtle 2 % opacity oscillation on the dot during scroll, removable per §4.

### 3.2 Site header / masthead

- Current: full-width gradient header with a pill-shaped logo lockup and SaaS-style nav links.
- New: `--paper` background, 1 px hand-drawn rule across the bottom, brand wordmarks rendered as **rubber-stamp SVGs** (slight rotation, faint imperfect ink coverage via the `ink-wobble` filter), the "×" between district names becomes a hand-drawn cross icon. Nav links render as **tabbed index cards** sticking up from the masthead. Active tab dips lower (selected state); hover lifts a tab 1 px.

### 3.3 Hero

- Current: full-width gradient banner with white headline and chip badges.
- New: **notebook cover-page** layout. Graph-paper background visible. Unit/lesson title rendered in Architects Daughter at hero size. **Hand-drawn arrows** in `--red-pen` point at one or two key terms in the headline (e.g., an arrow with the caption "← what we're studying"). A **purple "EM" rubber-stamp** SVG sits in the upper right at -8° rotation. **Strategy chips** rendered as torn paper-tape badges (irregular `border-image` edges, ±2° rotation per chip, semi-transparent paper-tape background).

The "Take the 2-minute tour" CTA button gets the same hand-drawn outline treatment as primary buttons (§3.10).

### 3.4 Section cards

- Current: white cards, 12 px rounded corners, soft shadow. Numbered pill badge per section.
- New: cream (`--paper`) cards, **4 px** corners, **2 px irregular dashed border** (via `border-image`), no drop shadow. The numbered badge becomes a **purple rubber-stamp SVG** that reads `01 · 02 · 03 …` with a hand-drawn box around it. The h2 title stays in Lora bold serif (readability), with a small **hand-drawn underline in red ink** rendered as an inline SVG sitting beneath it.
- **Inter-section dividers** — replace clean gaps with a 2 px dashed horizontal line containing a tiny doodle in the middle. The doodle cycles through the six variants in `notebook.svg` (`#doodle-arrow`, `#doodle-star`, `#doodle-check`, etc.). Selection is deterministic by section index so reloads show the same doodle in the same place.

### 3.5 Special section variants

| Section | Treatment |
|---|---|
| **Notice & Wonder** | Margin-notes block with ruled-paper background, label text rendered as if in the page margin (slight indent). The textarea stays a `<textarea>` (real form control) but visually styled with ruled lines behind. |
| **Driving Question** | Yellow-highlighter banner: `--highlighter` rendered behind the question text via inline SVG with an irregular ending (highlighter stops mid-stroke, end edge has natural pen-pressure variation). |
| **Vocabulary box** | Taped-on index card: rotated -1°, two small `--paper-tape` rectangles at the top corners, term/definition pairs in the index-card grid pattern. |
| **Make-It-Make-Sense** | Stays as `<ol>`, but each `<li>` gets a hand-drawn **circled number** in red ink to the left, items spaced like notebook lines. Sentence-frame `<details>` reveals as if peeling back a flap. |
| **Exit Ticket** | Dashed coupon/perforation box. Heading prefixed with a tiny scissors doodle (`#doodle-scissors`). Background `--paper-edge` so it reads as a tear-off section. |
| **Lab interactives** | The interactive itself is unchanged; only the frame. Heading reads "EXPERIMENT N" in Architects Daughter with a small hand-drawn beaker icon next to it. The readouts panel becomes a **data-log table** styled like a notebook observations table — column headers in Architects Daughter, values in JetBrains Mono. |

### 3.6 Sticky table of contents

- Current: left-bordered narrow column of `01·` numbered links.
- New: a card with a torn right edge (looks like a paper bookmark). Section numbers become **stamped circles** rendered as inline SVGs (one `<symbol>` per digit 0–9 in `notebook.svg`, each ~22×22 px hand-drawn). Stacking digits for two-digit section numbers is in scope; rendering via Unicode characters (⓪ ① ② …) is not — those are hard to style consistently across browsers and don't match the hand-drawn aesthetic. Active section's number circle fills with `--red-pen` ink.

### 3.7 Index page lesson grid

- Current: card grid with subtle hover lift.
- New: cards become **notebook page thumbnails** — each card has a small graph-paper inset preview, the lesson number rendered as a purple rubber-stamp top-left, lesson title in Lora bold serif, summary in italic Lora. Hover behavior preserved (lift 2 px), with the addition of a small **↗ arrow doodle** fading in at the bottom-right corner ("click here").

### 3.8 Strategy chips

- Current: pill shapes with colored dot indicators.
- New: torn paper-tape rectangles, `±2°` rotation, semi-transparent paper-tape background, label in Architects Daughter all-caps. Color variants via `.chip.hochman`, `.chip.active`, `.chip.btc`, `.chip.circle` map to the new palette tokens.

### 3.9 Pager (prev/next at bottom of lesson pages)

- Current: bordered cards.
- New: hand-drawn boxes with arrow doodles. Hover: arrow doodle grows by 2–3 px with a slight bounce.

### 3.10 Buttons & form controls

- **Primary buttons** ("Add vector", "Throw", "Launch", "Drop"): 2 px hand-drawn outline (slight stroke-wobble via `ink-wobble` filter), `--paper` background, label text in Architects Daughter. Hover: hand-drawn hatch pattern (4 diagonal pen strokes) draws in across the button background in 200 ms. Click: button briefly scales 0.98 and back ("stamp" effect). Focus: 2 px solid `--red-pen` outline at `outline-offset: 3px` (uses default browser focus styling — no hand-drawn focus indicator, since hand-drawn focus rings are hard to perceive for keyboard users).
- **Sliders** (range inputs): track becomes a hand-drawn line, thumb becomes a `--em-purple` ink dot.
- **Toggles / checkboxes**: hand-drawn checkbox shape with a wobbly red-ink ✓ when active.
- **Selects (`<select>`)**: paper background, hand-drawn outline.

### 3.11 Footer

- Current: thin gray strip with tagline.
- New: **bottom-of-page paper edge** — faint horizontal rule, tagline ("Learning, Achieving, Succeeding!") in Architects Daughter, slightly slanted right (transform: rotate(0.5deg)), as if signed.

### 3.12 Tour panel (the demo guided tour)

- Current: floating panel with progress dots, skip/back/next.
- New: same panel, but styled as a **paper sticky-note** (slight rotation, paper-tape rectangles at top corners, Architects Daughter for the step heading). Progress dots become small circled numbers. The "Skip tour" link becomes hand-drawn underlined text.

---

## 4. Animation choreography

Medium budget. All animations are CSS-only or use the existing `IntersectionObserver`. No new JavaScript dependencies.

### 4.1 Page-level

- **Page load** — body fades in 200 ms. Hero handwriting *draws in* via SVG `stroke-dasharray` animation (600 ms total, ease-out), hand-drawn arrows trace last.
- **Scroll-in for sections** — each `.section` fades + translates up 8 px when entering viewport. Triggered by IntersectionObserver. One-shot per section per page load. 250 ms duration.
- **Doodle reveals** — inter-section dashed dividers and their mid-line doodles fade in 100 ms after the section above settles.
- **Reading-progress bar** — leading-edge ink-bleed dot has a 2 % opacity oscillation, 1.5 s cycle. Removable via the same `prefers-reduced-motion` query.

### 4.2 Hover micro-interactions

| Element | Animation |
|---|---|
| Lesson cards (index grid) | Lift 2 px, ↗ arrow doodle fades in bottom-right, border darkens. ~150 ms. |
| Buttons | Hand-drawn hatch pattern draws in across background in 200 ms. Click briefly scales 0.98 and back. |
| Strategy-chip tape badges | Lift 1 px, rotate back to 0° ("tape smooths out"). 120 ms. |
| TOC links | Active section's stamped-circle number fills with red ink, 300 ms ease. |
| Pager prev/next | Arrow doodle grows by 2–3 px with slight bounce. |

### 4.3 Lab-interactive first-reveal choreography

When a student first opens a page with an interactive widget:

1. SVG canvas stays static for ~150 ms.
2. **Axes draw themselves** via `stroke-dasharray` reveal — 400 ms.
3. **Labels fade in** — 200 ms.
4. **Controls slide up** from below — 200 ms.
5. Total first-time choreography: ~750 ms.

After the first reveal, all student-driven changes (slider drags, button clicks, projectile animations, dot motion, etc.) stay exactly as today — instant feedback, no animation between states.

### 4.4 Accessibility — `prefers-reduced-motion: reduce`

Disables every animation in §§4.1–4.3 *except* essential interactive feedback (button-press scale, slider thumb tracking). Page-load drawing, scroll-in fades, hover hatch, stamp click — all gated behind the media query and become instant-snap-into-place when the OS pref is on.

Focus rings stay default — no hand-drawn focus styles, which tend to be hard to perceive.

### 4.5 What's deliberately NOT animated

- No parallax (hero or anywhere).
- No particle backgrounds, sparkles, floating icons.
- No scroll-jacking — wheel/touchpad scroll stays browser-native.
- No infinite loops beyond the optional 1.5 s ink-bleed pulse on the progress bar.
- No animation on data readouts during user interaction — instant tabular updates only.

---

## 5. Implementation strategy

### 5.1 Files changed

| File | Change |
|---|---|
| `_assets/site.css` | **Rewrite** (~600 lines, similar to current ~660). New tokens, new components, new animations. Existing class names stay primary so the diff is "rewrite the rules, not the markup." |
| `_assets/site.js` | **Add** ~30 lines — IntersectionObserver scroll-in handler, hand-drawn animation triggers. Existing tour, scroll-spy, progress-bar helpers untouched. |
| `_assets/notebook.svg` (new) | SVG filter library — `ink-wobble`, `paper-grain`, six doodle symbols. ~80 lines. |
| `_assets/icons.svg` (new) | Sprite of inline icon doodles (beaker, scissors, ↗ etc.). ~20 small symbols. |
| `_assets/brand/em_stamp.svg`, `vs_stamp.svg` | **Replace** the placeholder text-as-svg files with rubber-stamp SVG renders (slight rotation, ink-imperfect outline). |
| `index.html`, `unit_plan.html`, `assessment.html` | **Light touch** — add `<link>` for new fonts, add SVG-filter include, swap a few class names (`hero` → `hero notebook-cover`, etc.), adjust masthead markup for index-card tabs. ~10–15 lines diff per file. |
| `lessons/01-vectors.html` … `lessons/09-projectiles-at-an-angle.html` | **Light touch** — same pattern as above. Lesson body content (interactives, vocab, exit ticket prose) is unchanged. ~10 lines diff per file. |

### 5.2 Files NOT changed

- All lesson markdown sources (`Teacher_Guide.md`, `Answer_Key.md`, `Unit_Plan.md`) in the OneNote-friendly track.
- The OneNote-friendly track folder entirely (`01_Physics_East_Meadow_Refactor/`).
- All Python tooling (`tools/build_lessons.py`, `tools/validators.py`, `tools/validate_web.py`).
- Schema (`tools/lesson_schema.yaml`).
- All tests (`tests/tools/*.py`).
- GitHub Actions workflow (`.github/workflows/deploy-pages.yml`).
- Any of the rich SVG/JS lesson interactives (vector playground, projectile launcher, two-cars race, etc.). Their *frames* change; their *internals* don't.

### 5.3 Migration

Single PR, all 12 pages at once. Reasoning: tokens are global; partial rollout would cause mid-migration visual conflict.

### 5.4 Rollback

```bash
git checkout HEAD~1 -- Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css
```

Reverts CSS only; HTML class additions are forward-compatible with both stylesheets so this single-file revert restores the previous look.

### 5.5 Performance targets

- Per-page weight: stays under **500 KB** (current ~95 KB; net +~90 KB from font payload).
- First Contentful Paint on 4G classroom WiFi: under **1.2 s**.
- Lighthouse Performance score: **≥ 90** (current is 96 — accept up to a 6-point drop from the new fonts).
- All animations run at **60 fps** on a 2018 iPad (the lowest-spec target device).

### 5.6 Validators

Existing validators all stay green. Specifically:

- 30 pytest tests pass.
- `python tools/validate_web.py` passes (no new emphasis tags inside MC options).
- No new validation rules introduced for the redesign itself.

---

## 6. Risk register

| Risk | Likelihood | Mitigation |
|---|---|---|
| Architects Daughter is hard for ELL students or those with reading difficulties | Low–Medium | Used only for headlines, captions, and chip labels — never body text. ELL students continue to read normal serif paragraphs. `prefers-reduced-motion` query is wired. If accessibility feedback comes in, introduce a "plain text" preference toggle in a follow-up. |
| District print policy — handwriting font might not print clearly on some printers | Low | Print stylesheet overrides hero/headline fonts to Lora bold for print. Notebook chrome (graph paper, dashed borders) prints understated. |
| Adults dismiss the look as "for kids" before reading content | Medium | "Both audiences" target was explicitly chosen for this. Mitigations: keep Lora body throughout, keep brand identifiers (district names, NYSSLS standard codes) in clean serif/uppercase, keep the assessment page especially restrained. The notebook metaphor leans on Darwin/Curie/Feynman associations — credibly serious science. |
| SVG filter rendering varies across browsers (especially older Safari) | Low | Filters used only on a few hero elements; all content readable without them. Filter degrades to no-effect, not broken layout. |
| Font load FOUT (flash of unstyled text) | Low | `display=swap` shows fallback (Georgia / system serif) until Lora loads. Architects Daughter falls back to a generic cursive while loading. Both swaps are visually similar enough that users shouldn't notice. |
| Google Fonts CDN blocked at the school district | Low–Medium | README documents how to vendor the three fonts into `_assets/fonts/` and swap the `<link>` for a local `@font-face` declaration. Same pattern as the previous Inter swap-out documented in the existing README. |
| OneNote-paste version of the same content stops looking right | N/A | OneNote-friendly track is a separate folder, untouched. Both continue to exist as siblings. |
| Visual regression (something breaks on a page nobody looked at) | Medium | Manual visual QA pass on all 12 pages is part of the implementation plan's final phase. Each page diff is reviewed before merge. |

---

## 7. Open questions

None blocking. The following are trackable but don't gate implementation:

1. **Real district logo SVGs** — placeholder rubber-stamp SVGs use district-name typography. When official logo files become available, they replace the rubber-stamp wordmarks (`em_stamp.svg`, `vs_stamp.svg`) with one drop-in.
2. **East Meadow tagline** — VSCHSD's "Learning, Achieving, Succeeding!" is in the footer; East Meadow's equivalent is unconfirmed, so the footer pairs the VSCHSD tagline with the EM district name only.
3. **Custom illustration commission** — if the curriculum wants per-lesson hand-drawn diagrams (rock-vs-feather race, projectile arcs annotated, etc.) authored as raster SVG assets later, the design system has slots for them in the §3.5 lab-interactive frame. Out of scope for this redesign.

---

## 8. Deliverables

End of implementation:

1. **`_assets/site.css`** rewritten with the new design system.
2. **`_assets/site.js`** with ~30 added lines for scroll-in animation triggers.
3. **`_assets/notebook.svg`**, **`_assets/icons.svg`**, **`_assets/brand/em_stamp.svg`**, **`_assets/brand/vs_stamp.svg`** added.
4. All 12 HTML pages migrated to the new identity (each ~10–15 lines diff).
5. **Updated README** in `01_Physics_East_Meadow_Web/README.md` documenting the new font dependencies and how to vendor them for offline classrooms.
6. All 30 pytest tests still passing.
7. `python tools/validate_web.py` still passing.
8. Manual visual QA notes in the PR description, per page.
9. CI deploy succeeds; live site at `https://angsta-ed.github.io/physics-kinematics/` reflects the new look.

After merge, the redesign is live and reverting requires only `git checkout HEAD~1 -- Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css`.
