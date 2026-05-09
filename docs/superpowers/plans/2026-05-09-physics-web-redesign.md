# Physics Web Edition — Lab Notebook Redesign Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the current modern-SaaS visual identity of the Physics web edition with a "lab notebook" identity — cream paper, fountain-pen ink, hand-drawn arrows, taped-on cards, hand-drawn outline buttons — across all 12 pages of `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/`.

**Architecture:** Pure CSS + SVG. No new JS dependencies. Three Google Fonts (Architects Daughter / Lora / JetBrains Mono) replace Inter. Two new SVG asset files (`notebook.svg` for filters and doodles, `icons.svg` for inline icon sprites). The existing class names in HTML stay primary so the migration is "rewrite the rules, not the markup." Single-file rollback via `git checkout HEAD~1 -- _assets/site.css` if the result is wrong.

**Tech Stack:** CSS3 (custom properties, `border-image`, `linear-gradient` paper textures, SVG `feTurbulence` filters). Vanilla JS for animation triggers. Google Fonts via CDN. No build step.

**Spec:** `docs/superpowers/specs/2026-05-09-physics-web-redesign-design.md`

---

## File Structure

```
Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/
├── _assets/
│   ├── site.css            # REWRITE — new tokens, components, animations (~600 lines, similar to current ~660)
│   ├── site.js             # MODIFY — add IntersectionObserver scroll-in handler (+ ~30 lines)
│   ├── notebook.svg        # CREATE — SVG filter library + 6 doodle symbols
│   ├── icons.svg           # CREATE — inline icon sprite (beaker, scissors, ↗, etc.)
│   └── brand/
│       ├── em_logo.svg     # UNCHANGED — kept as fallback
│       ├── vs_logo.svg     # UNCHANGED — kept as fallback
│       ├── em_stamp.svg    # CREATE — purple rubber-stamp version
│       └── vs_stamp.svg    # CREATE — blue rubber-stamp version
├── index.html              # MODIFY — font link, masthead markup, class swaps (~15 line diff)
├── unit_plan.html          # MODIFY — same pattern (~10 line diff)
├── assessment.html         # MODIFY — same pattern (~10 line diff)
└── lessons/                # MODIFY — same pattern in each (~10 line diff per file)
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

**Files NOT touched:** any markdown source under `01_Physics_East_Meadow_Refactor/`, all `tools/*.py`, all `tests/*.py`, `lesson_schema.yaml`, `.github/workflows/*`, the SVG/JS internals of any lesson interactive widget.

---

## Migration order (rationale)

1. **Phase A — Asset infrastructure.** SVG filters and font links must exist before CSS rules reference them. Without this, intermediate commits would render with missing filter URLs and fallback fonts. Phase A produces zero visible change but unlocks everything downstream.

2. **Phase B — site.css rewrite.** Done in 13 small commits, each replacing one logical section of the stylesheet. Each commit is internally consistent (a valid CSS file) and produces an *increasingly notebook-y* page in the browser. The migration is visually progressive — at any point, you can stop, reload, and see the redesign so far.

3. **Phase C — HTML markup updates.** A handful of new classes and inline SVG references are added to all 12 pages. These changes are forward-compatible with the *old* CSS, so doing Phase B before Phase C is safe.

4. **Phase D — JS animation additions.** Animation triggers in `site.js` reference DOM nodes that exist after Phase C. Last code phase.

5. **Phase E — README + verification.** Document the new font dependencies, run validators, manual QA on all 12 pages, push.

The final result, end-to-end, is one PR with ~22 commits.

---

# Phase A: Asset infrastructure

## Task A1: Create SVG filter and doodle library

**Files:**
- Create: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/notebook.svg`

Per spec §2.6, this file holds:
- `<filter id="ink-wobble">` for hand-drawn imperfection
- `<filter id="paper-grain">` for paper texture
- Six `<symbol>` doodles for inter-section dividers (arrow, star, check, arrow-bend, spiral, bullet)
- One `<symbol>` for scissors (Exit Ticket section)
- One `<symbol>` for beaker (lab-interactive heading)
- Ten `<symbol>`s for stamped-circle digits 0–9 (TOC)

- [ ] **Step 1: Write `_assets/notebook.svg` with all filters and symbols**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" style="position:absolute;width:0;height:0" aria-hidden="true">
  <!-- Ink-wobble filter: gives borders/strokes a slight hand-drawn imperfection -->
  <filter id="ink-wobble" x="-2%" y="-2%" width="104%" height="104%">
    <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" seed="3" result="noise"/>
    <feDisplacementMap in="SourceGraphic" in2="noise" scale="1.5"/>
  </filter>

  <!-- Paper-grain: subtle texture over large paper backgrounds -->
  <filter id="paper-grain" x="0%" y="0%" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="1.4" numOctaves="2" stitchTiles="stitch" seed="1"/>
    <feColorMatrix values="0 0 0 0 0.85
                            0 0 0 0 0.78
                            0 0 0 0 0.55
                            0 0 0 0.04 0"/>
  </filter>

  <!-- Doodles: inter-section dividers, ~28x16 each -->
  <symbol id="doodle-arrow" viewBox="0 0 32 16">
    <path d="M2,8 Q8,4 14,8 T26,8 M22,4 L28,8 L22,12" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </symbol>
  <symbol id="doodle-star" viewBox="0 0 24 16">
    <path d="M12,2 L13.8,7 L19,7 L14.6,10 L16.2,15 L12,12 L7.8,15 L9.4,10 L5,7 L10.2,7 Z" stroke="currentColor" stroke-width="1.4" fill="none" stroke-linejoin="round"/>
  </symbol>
  <symbol id="doodle-check" viewBox="0 0 24 16">
    <path d="M3,9 L9,14 L21,3" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </symbol>
  <symbol id="doodle-arrow-bend" viewBox="0 0 32 16">
    <path d="M3,4 Q14,4 18,8 Q22,12 28,12 M24,9 L28,12 L25,15" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </symbol>
  <symbol id="doodle-spiral" viewBox="0 0 24 16">
    <path d="M16,8 Q16,4 12,4 Q6,4 6,9 Q6,13 12,13 Q19,13 19,7 Q19,2 11,2" stroke="currentColor" stroke-width="1.4" fill="none" stroke-linecap="round"/>
  </symbol>
  <symbol id="doodle-bullet" viewBox="0 0 24 16">
    <circle cx="12" cy="8" r="3" stroke="currentColor" stroke-width="1.6" fill="none"/>
    <circle cx="12" cy="8" r="1" fill="currentColor"/>
  </symbol>

  <!-- Section icons -->
  <symbol id="icon-scissors" viewBox="0 0 20 20">
    <circle cx="5" cy="14" r="3" stroke="currentColor" stroke-width="1.4" fill="none"/>
    <circle cx="15" cy="14" r="3" stroke="currentColor" stroke-width="1.4" fill="none"/>
    <path d="M7,12 L18,3 M13,12 L2,3" stroke="currentColor" stroke-width="1.4" fill="none" stroke-linecap="round"/>
  </symbol>
  <symbol id="icon-beaker" viewBox="0 0 20 20">
    <path d="M7,3 L7,8 L3,16 Q3,18 5,18 L15,18 Q17,18 17,16 L13,8 L13,3 Z" stroke="currentColor" stroke-width="1.4" fill="none" stroke-linejoin="round"/>
    <line x1="6" y1="3" x2="14" y2="3" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
    <path d="M5,13 Q8,12 11,13 T15,14" stroke="currentColor" stroke-width="1" fill="none"/>
  </symbol>

  <!-- Stamped-circle digits 0-9 for TOC -->
  <symbol id="digit-0" viewBox="0 0 22 22"><circle cx="11" cy="11" r="9" stroke="currentColor" stroke-width="1.6" fill="none"/><text x="11" y="15" text-anchor="middle" font-family="Architects Daughter, cursive" font-size="11" fill="currentColor">0</text></symbol>
  <symbol id="digit-1" viewBox="0 0 22 22"><circle cx="11" cy="11" r="9" stroke="currentColor" stroke-width="1.6" fill="none"/><text x="11" y="15" text-anchor="middle" font-family="Architects Daughter, cursive" font-size="11" fill="currentColor">1</text></symbol>
  <symbol id="digit-2" viewBox="0 0 22 22"><circle cx="11" cy="11" r="9" stroke="currentColor" stroke-width="1.6" fill="none"/><text x="11" y="15" text-anchor="middle" font-family="Architects Daughter, cursive" font-size="11" fill="currentColor">2</text></symbol>
  <symbol id="digit-3" viewBox="0 0 22 22"><circle cx="11" cy="11" r="9" stroke="currentColor" stroke-width="1.6" fill="none"/><text x="11" y="15" text-anchor="middle" font-family="Architects Daughter, cursive" font-size="11" fill="currentColor">3</text></symbol>
  <symbol id="digit-4" viewBox="0 0 22 22"><circle cx="11" cy="11" r="9" stroke="currentColor" stroke-width="1.6" fill="none"/><text x="11" y="15" text-anchor="middle" font-family="Architects Daughter, cursive" font-size="11" fill="currentColor">4</text></symbol>
  <symbol id="digit-5" viewBox="0 0 22 22"><circle cx="11" cy="11" r="9" stroke="currentColor" stroke-width="1.6" fill="none"/><text x="11" y="15" text-anchor="middle" font-family="Architects Daughter, cursive" font-size="11" fill="currentColor">5</text></symbol>
  <symbol id="digit-6" viewBox="0 0 22 22"><circle cx="11" cy="11" r="9" stroke="currentColor" stroke-width="1.6" fill="none"/><text x="11" y="15" text-anchor="middle" font-family="Architects Daughter, cursive" font-size="11" fill="currentColor">6</text></symbol>
  <symbol id="digit-7" viewBox="0 0 22 22"><circle cx="11" cy="11" r="9" stroke="currentColor" stroke-width="1.6" fill="none"/><text x="11" y="15" text-anchor="middle" font-family="Architects Daughter, cursive" font-size="11" fill="currentColor">7</text></symbol>
  <symbol id="digit-8" viewBox="0 0 22 22"><circle cx="11" cy="11" r="9" stroke="currentColor" stroke-width="1.6" fill="none"/><text x="11" y="15" text-anchor="middle" font-family="Architects Daughter, cursive" font-size="11" fill="currentColor">8</text></symbol>
  <symbol id="digit-9" viewBox="0 0 22 22"><circle cx="11" cy="11" r="9" stroke="currentColor" stroke-width="1.6" fill="none"/><text x="11" y="15" text-anchor="middle" font-family="Architects Daughter, cursive" font-size="11" fill="currentColor">9</text></symbol>
</svg>
```

- [ ] **Step 2: Verify the file is valid XML/SVG**

Run: `python3 -c "import xml.etree.ElementTree as ET; ET.parse('Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/notebook.svg')" && echo "valid"`
Expected: `valid`

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/notebook.svg
git commit -m "feat(web): add notebook.svg — ink-wobble + paper-grain filters, doodles, stamped digits"
```

## Task A2: Create rubber-stamp brand SVGs

**Files:**
- Create: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/brand/em_stamp.svg`
- Create: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/brand/vs_stamp.svg`

Per spec §3.3, brand wordmarks render as rubber-stamp SVGs. The existing `em_logo.svg` / `vs_logo.svg` are kept as fallback (used by the OneNote-friendly track).

- [ ] **Step 1: Write `_assets/brand/em_stamp.svg`**

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 130 36" role="img" aria-label="East Meadow Schools">
  <g filter="url(#ink-wobble)">
    <rect x="3" y="3" width="124" height="30" stroke="#5a2466" stroke-width="2" fill="none" rx="2"/>
    <text x="65" y="24" text-anchor="middle" font-family="Architects Daughter, cursive" font-size="14" fill="#5a2466" letter-spacing="0.04em">EAST MEADOW</text>
  </g>
</svg>
```

- [ ] **Step 2: Write `_assets/brand/vs_stamp.svg`**

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 36" role="img" aria-label="Valley Stream Central HSD">
  <g filter="url(#ink-wobble)">
    <rect x="3" y="3" width="194" height="30" stroke="#2a4d8f" stroke-width="2" fill="none" rx="2"/>
    <text x="100" y="24" text-anchor="middle" font-family="Architects Daughter, cursive" font-size="14" fill="#2a4d8f" letter-spacing="0.04em">VALLEY STREAM CENTRAL</text>
  </g>
</svg>
```

- [ ] **Step 3: Verify both files are valid**

Run: `python3 -c "import xml.etree.ElementTree as ET; ET.parse('Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/brand/em_stamp.svg'); ET.parse('Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/brand/vs_stamp.svg'); print('valid')"`
Expected: `valid`

- [ ] **Step 4: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/brand/em_stamp.svg \
        Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/brand/vs_stamp.svg
git commit -m "feat(web): add rubber-stamp brand SVGs (East Meadow + Valley Stream)"
```

## Task A3: Run validators to confirm baseline before CSS changes

**Files:** none

- [ ] **Step 1: Run web-edition validator**

Run: `source .venv/bin/activate && python tools/validate_web.py`
Expected: `OK — checked 12 HTML files; no answer-revealing emphasis in any MC option.`

- [ ] **Step 2: Run full pytest suite**

Run: `source .venv/bin/activate && python -m pytest tests/tools/ -q`
Expected: `30 passed`

- [ ] **Step 3: No commit (baseline check only)**

---

# Phase B: site.css rewrite (in 13 atomic chunks)

Each task in this phase replaces a logical section of `_assets/site.css`. After each commit, the page is internally consistent — open `index.html` or any lesson in the browser and the rebuilt portion will look new while still-untouched portions look as before. This is intentional: the migration is visually progressive.

For brevity in this plan, the entire current contents of each section being replaced is *not* re-printed; the pattern is "find the section labeled `/* ----- X ----- */` in the current file and replace it with the new code shown below." The implementer should use `Edit` with `old_string` + `new_string` matching at the section comment markers.

## Task B1: Rewrite `:root` token block

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css`

The current file starts with a large `:root { ... }` block defining colors, fonts, spacing, etc. Replace the entire `:root` block with the new tokens.

- [ ] **Step 1: Open the current file and locate the `:root` block**

Run: `head -80 Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css`
The block starts at line 8 with `:root {` and ends ~line 60 with the closing `}`.

- [ ] **Step 2: Use Edit to replace the `:root` block**

Find the existing block (starts with `:root {` and ends with the matching `}`). Replace with:

```css
:root {
  /* ===== Lab notebook redesign — paper & ink palette ===== */
  --paper: #fbf6e8;
  --paper-edge: #f1eada;
  --paper-tape: #e8dfc6;
  --grid: rgba(166, 124, 82, 0.18);
  --rule: rgba(42, 77, 143, 0.15);

  --ink: #2b2418;
  --ink-soft: #574a36;
  --ink-faint: #8a7a5a;

  --em-purple: #5a2466;
  --vs-blue: #2a4d8f;
  --red-pen: #c14626;
  --highlighter: #fdd35e;
  --mint: #3d8a5e;
  --peach: #e89668;

  /* Compatibility aliases — old token names continue to work */
  --em-purple-soft: #7c3a8a;
  --em-orange: var(--peach);
  --vs-blue-soft: #4d6fa8;
  --on-brand: var(--paper);
  --surface-0: var(--paper);
  --surface-1: var(--paper);
  --surface-2: var(--paper-edge);
  --surface-3: var(--paper-edge);
  --border: rgba(43, 36, 24, 0.18);
  --border-strong: rgba(43, 36, 24, 0.35);
  --ink-subtle: var(--ink-faint);

  /* Strategy chip palette aliases */
  --strat-hochman: var(--red-pen);
  --strat-active: var(--vs-blue);
  --strat-btc: var(--mint);
  --strat-circle: var(--peach);

  /* Gradient legacy compat — flatten to paper for hero/banner contexts */
  --grad-co-brand: linear-gradient(135deg, var(--paper) 0%, var(--paper-edge) 100%);
  --grad-co-brand-soft: var(--paper);
  --grad-orange: linear-gradient(135deg, var(--peach), #f1b298);

  /* Type */
  --font-body: "Lora", Georgia, "Iowan Old Style", serif;
  --font-display: "Architects Daughter", "Comic Sans MS", cursive;
  --font-mono: "JetBrains Mono", ui-monospace, "SF Mono", "Monaco", monospace;

  /* Type scale */
  --fs-hero: clamp(2.25rem, 5vw, 3.5rem);
  --fs-h1: clamp(1.75rem, 3vw, 2.25rem);
  --fs-h2: 1.5rem;
  --fs-h3: 1.125rem;
  --fs-body: 1rem;
  --fs-small: 0.875rem;
  --fs-tiny: 0.75rem;

  /* Spacing (8px baseline, unchanged) */
  --s-1: 4px;
  --s-2: 8px;
  --s-3: 16px;
  --s-4: 24px;
  --s-5: 32px;
  --s-6: 48px;
  --s-7: 72px;
  --s-8: 96px;

  /* Radius — squared off for notebook */
  --r-xs: 2px;
  --r-sm: 4px;
  --r-md: 4px;
  --r-lg: 6px;
  --r-pill: 9999px;

  /* Shadows — softer, paper-y */
  --shadow-1: 0 1px 0 rgba(43, 36, 24, 0.06);
  --shadow-2: 0 2px 4px rgba(43, 36, 24, 0.08);
  --shadow-3: 0 6px 14px rgba(43, 36, 24, 0.10);
  --shadow-glow: 0 0 0 3px rgba(193, 70, 38, 0.18);

  /* Layout */
  --content-width: 1120px;
  --reading-width: 76ch;
}
```

- [ ] **Step 3: Smoke-test by opening the local site**

Run: `open Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/index.html`
Expected: Body now uses Lora (serif) instead of Inter; colors shift toward cream paper and fountain-pen ink; the rest of the layout still works.

- [ ] **Step 4: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css
git commit -m "feat(web/css): replace :root tokens with paper-and-ink palette"
```

## Task B2: Rewrite base styles + reset

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css`

Replace the section labeled `/* ----- Reset / base ----- */` (and continuing through the `select`/`textarea` rules — about 80 lines) with new base styles aligned to the notebook aesthetic.

- [ ] **Step 1: Use Edit to replace the base-styles block**

Locate the existing comment `/* ----- Reset / base ----- */` and replace from there through the end of the textarea rules with:

```css
/* ----- Reset / base ----- */
*, *::before, *::after { box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
  margin: 0;
  font-family: var(--font-body);
  font-size: var(--fs-body);
  line-height: 1.6;
  color: var(--ink);
  background: var(--paper);
  background-image:
    linear-gradient(rgba(166, 124, 82, 0.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(166, 124, 82, 0.06) 1px, transparent 1px);
  background-size: 22px 22px;
  background-attachment: fixed;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

img, svg { display: block; max-width: 100%; }

a {
  color: var(--vs-blue);
  text-decoration: none;
  border-bottom: 1px solid rgba(42, 77, 143, 0.3);
  transition: border-color 0.15s ease, color 0.15s ease;
}

a:hover { border-bottom-color: var(--vs-blue); color: var(--em-purple); }

h1, h2, h3, h4 {
  font-family: var(--font-display);
  color: var(--ink);
  line-height: 1.15;
  margin: 0 0 var(--s-3);
  letter-spacing: 0;
}

h1 { font-size: var(--fs-h1); font-weight: 400; }
h2 { font-size: var(--fs-h2); font-weight: 400; }
h3 { font-size: var(--fs-h3); font-weight: 400; }

p { margin: 0 0 var(--s-3); max-width: var(--reading-width); }

ol, ul { margin: 0 0 var(--s-3); padding-left: 1.4em; }
li { margin-bottom: var(--s-2); }

button {
  font-family: var(--font-display);
  font-size: var(--fs-small);
  font-weight: 400;
  padding: var(--s-2) var(--s-4);
  border-radius: var(--r-sm);
  border: 2px solid var(--ink);
  background: var(--paper);
  color: var(--ink);
  cursor: pointer;
  position: relative;
  transition: transform 0.12s ease, background-color 0.2s ease;
  letter-spacing: 0.02em;
}

button:hover {
  background-image: repeating-linear-gradient(
    45deg,
    transparent,
    transparent 4px,
    rgba(43, 36, 24, 0.08) 4px,
    rgba(43, 36, 24, 0.08) 5px
  );
}

button:active { transform: scale(0.98); }

button:focus-visible {
  outline: 2px solid var(--red-pen);
  outline-offset: 3px;
}

button.primary {
  border-color: var(--em-purple);
  color: var(--em-purple);
}

button.primary:hover {
  background-image: repeating-linear-gradient(
    45deg,
    transparent,
    transparent 4px,
    rgba(90, 36, 102, 0.10) 4px,
    rgba(90, 36, 102, 0.10) 5px
  );
}

button.accent {
  border-color: var(--vs-blue);
  color: var(--vs-blue);
}

button.accent:hover {
  background-image: repeating-linear-gradient(
    45deg,
    transparent,
    transparent 4px,
    rgba(42, 77, 143, 0.10) 4px,
    rgba(42, 77, 143, 0.10) 5px
  );
}

input[type="range"] {
  appearance: none;
  -webkit-appearance: none;
  height: 3px;
  background: var(--ink);
  border-radius: var(--r-pill);
  outline: none;
}

input[type="range"]::-webkit-slider-thumb {
  appearance: none;
  -webkit-appearance: none;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: var(--em-purple);
  cursor: pointer;
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.3);
}

input[type="range"]::-moz-range-thumb {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: var(--em-purple);
  cursor: pointer;
  border: 0;
}

select {
  font-family: var(--font-body);
  font-size: var(--fs-small);
  padding: var(--s-2) var(--s-3);
  border-radius: var(--r-sm);
  border: 2px solid var(--ink);
  background: var(--paper);
  cursor: pointer;
}

textarea {
  width: 100%;
  font-family: var(--font-body);
  font-size: var(--fs-body);
  padding: var(--s-3);
  border-radius: var(--r-sm);
  border: 2px solid var(--ink);
  background: var(--paper);
  background-image: linear-gradient(var(--rule) 1px, transparent 1px);
  background-size: 100% 28px;
  line-height: 28px;
  resize: vertical;
}

textarea:focus { outline: none; border-color: var(--red-pen); box-shadow: var(--shadow-glow); }
```

- [ ] **Step 2: Reload the local site**

Run: `open Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/index.html` (or just refresh the open tab)
Expected: Body text in Lora; headings in Architects Daughter; buttons have hand-drawn outline + cross-hatch on hover; textareas have ruled-paper lines.

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css
git commit -m "feat(web/css): rewrite base typography and form controls (notebook style)"
```

## Task B3: Rewrite reading-progress bar

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css`

- [ ] **Step 1: Locate the existing `.progress-bar` rule and replace**

Find the rule starting `.progress-bar {` and replace through its final `}`:

```css
/* ----- Reading progress bar (fountain-pen line) ----- */
.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  background: var(--vs-blue);
  width: 0%;
  z-index: 100;
  transition: width 0.05s linear;
}

.progress-bar::after {
  content: "";
  position: absolute;
  right: -3px;
  top: -1.5px;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--vs-blue);
  opacity: 0.7;
  animation: inkBleed 1.5s ease-in-out infinite;
}

@keyframes inkBleed {
  0%, 100% { opacity: 0.7; }
  50% { opacity: 0.85; }
}
```

- [ ] **Step 2: Smoke-test**

Refresh the browser and scroll. Expected: thin blue line at the top widens with scroll progress; small "ink-bleed" dot at the leading edge softly pulses.

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css
git commit -m "feat(web/css): progress bar as fountain-pen line with ink-bleed dot"
```

## Task B4: Rewrite site-header (paper masthead with index-card tabs)

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css`

- [ ] **Step 1: Replace the `/* ----- Site shell ----- */` section**

Locate the comment `/* ----- Site shell ----- */` and replace through the end of the `.site-header nav` rules (~80 lines) with:

```css
/* ----- Site header (paper masthead) ----- */
.site-header {
  background: var(--paper);
  background-image: linear-gradient(rgba(166, 124, 82, 0.06) 1px, transparent 1px);
  background-size: 100% 28px;
  border-bottom: 1px solid var(--ink);
  position: relative;
}

.site-header::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: -1px;
  height: 1px;
  background: var(--ink);
  filter: url(#ink-wobble);
}

.site-header-inner {
  max-width: var(--content-width);
  margin: 0 auto;
  padding: var(--s-3) var(--s-4) 0;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: var(--s-4);
}

.brand-lockup {
  display: flex;
  align-items: center;
  gap: var(--s-3);
  color: var(--ink);
  text-decoration: none;
  border: 0;
  padding-bottom: var(--s-3);
}

.brand-lockup:hover { border: 0; }

.brand-lockup .logos {
  display: flex;
  align-items: center;
  gap: var(--s-3);
  background: transparent;
  padding: 0;
  border-radius: 0;
  backdrop-filter: none;
}

.brand-lockup .logos img { height: 24px; width: auto; transform: rotate(-1.5deg); }
.brand-lockup .logos .x { opacity: 0.5; font-weight: 400; font-family: var(--font-display); color: var(--ink-faint); font-size: 1.1rem; }

.brand-lockup .label {
  font-size: var(--fs-tiny);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 400;
  color: var(--ink-soft);
  font-family: var(--font-display);
}

.site-header nav {
  display: flex;
  gap: 4px;
  align-items: flex-end;
}

.site-header nav a {
  color: var(--ink-soft);
  font-size: var(--fs-small);
  padding: var(--s-2) var(--s-3) calc(var(--s-2) + 4px);
  border-radius: var(--r-sm) var(--r-sm) 0 0;
  border: 1px solid var(--ink);
  border-bottom: 0;
  background: var(--paper-edge);
  font-weight: 400;
  font-family: var(--font-display);
  transition: transform 0.12s ease;
  margin-bottom: -1px;
  position: relative;
}

.site-header nav a:hover {
  background: var(--paper);
  transform: translateY(-1px);
  border-bottom: 0;
}

.site-header nav a.active {
  background: var(--paper);
  color: var(--ink);
  z-index: 1;
}
```

- [ ] **Step 2: Smoke-test**

Refresh. Expected: header is now cream paper with subtle ruled lines; nav links look like tabbed index cards sticking up from the masthead; active tab dips lower.

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css
git commit -m "feat(web/css): site header as paper masthead with index-card tabs"
```

## Task B5: Rewrite hero (notebook cover-page)

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css`

- [ ] **Step 1: Replace the `/* ----- Hero ----- */` section**

Locate `/* ----- Hero (lesson + index) ----- */` and replace through the chips rules (~70 lines) with:

```css
/* ----- Hero (notebook cover-page) ----- */
.hero {
  background: var(--paper);
  background-image:
    linear-gradient(var(--grid) 1px, transparent 1px),
    linear-gradient(90deg, var(--grid) 1px, transparent 1px);
  background-size: 22px 22px;
  color: var(--ink);
  padding: var(--s-7) var(--s-4) var(--s-7);
  position: relative;
  overflow: visible;
  border-bottom: 2px dashed var(--ink-faint);
}

.hero::before {
  content: "";
  position: absolute;
  top: var(--s-4);
  right: var(--s-4);
  width: 90px;
  height: 36px;
  background: var(--em-purple);
  -webkit-mask: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 90 36'><rect x='3' y='3' width='84' height='30' stroke='black' stroke-width='2.5' fill='none'/><text x='45' y='22' text-anchor='middle' font-family='Architects Daughter' font-size='12' fill='black'>UNIT 01</text></svg>") no-repeat center / contain;
  mask: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 90 36'><rect x='3' y='3' width='84' height='30' stroke='black' stroke-width='2.5' fill='none'/><text x='45' y='22' text-anchor='middle' font-family='Architects Daughter' font-size='12' fill='black'>UNIT 01</text></svg>") no-repeat center / contain;
  transform: rotate(-6deg);
  opacity: 0.85;
}

.hero-inner {
  max-width: var(--content-width);
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

.hero .eyebrow {
  font-size: var(--fs-small);
  text-transform: uppercase;
  letter-spacing: 0.10em;
  font-weight: 400;
  margin-bottom: var(--s-3);
  color: var(--ink-soft);
  font-family: var(--font-display);
}

.hero h1 {
  font-size: var(--fs-hero);
  font-weight: 400;
  font-family: var(--font-display);
  letter-spacing: 0;
  line-height: 1.1;
  color: var(--ink);
  max-width: 24ch;
  margin-bottom: var(--s-4);
}

.hero .lede {
  font-family: var(--font-body);
  font-size: 1.125rem;
  max-width: 52ch;
  color: var(--ink-soft);
  margin-bottom: var(--s-4);
}

.chips { display: flex; gap: var(--s-2); flex-wrap: wrap; }

.chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 12px;
  border-radius: var(--r-sm);
  font-size: var(--fs-tiny);
  font-weight: 400;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  background: var(--paper-tape);
  color: var(--ink);
  font-family: var(--font-display);
  border: 1px solid rgba(43, 36, 24, 0.2);
  transform: rotate(var(--chip-rot, -1deg));
  position: relative;
  transition: transform 0.12s ease, background-color 0.15s ease;
}

.chip:nth-child(2n) { --chip-rot: 1.5deg; }
.chip:nth-child(3n) { --chip-rot: -0.5deg; }
.chip:nth-child(4n) { --chip-rot: 1deg; }

.chip:hover { transform: rotate(0deg) translateY(-1px); }

.chip::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--ink-faint);
}

.chip.hochman::before { background: var(--red-pen); }
.chip.active::before { background: var(--vs-blue); }
.chip.btc::before { background: var(--mint); }
.chip.circle::before { background: var(--peach); }
```

- [ ] **Step 2: Smoke-test**

Refresh `index.html` and any lesson. Expected: hero is now graph paper with brown ink text; large headline in Architects Daughter; chips look like taped-on tape rectangles with random rotation that straighten on hover. Note: the unit-stamp top-right will appear but isn't yet wired to per-page text — the static "UNIT 01" placeholder is fine for this commit.

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css
git commit -m "feat(web/css): hero as notebook cover-page with stamp + tape chips"
```

## Task B6: Rewrite section cards + dividers

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css`

- [ ] **Step 1: Replace the `.section` rules**

Locate `/* ----- Sections ----- */` and replace through the end of the section variant rules (driver/notice-wonder/exit) with:

```css
/* ----- Section cards (notebook pages) ----- */
.section {
  background: var(--paper);
  border: 2px dashed var(--ink-faint);
  border-radius: var(--r-md);
  padding: var(--s-5) var(--s-5);
  box-shadow: none;
  position: relative;
}

.section + .section { margin-top: var(--s-4); }

.section + .section::before {
  content: "";
  position: absolute;
  top: calc(var(--s-2) * -1 - 6px);
  left: 50%;
  transform: translateX(-50%);
  width: 32px;
  height: 16px;
  background: var(--paper);
  background-image: var(--divider-doodle, none);
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  color: var(--ink-faint);
}

/* Cycle through 6 doodle variants by section index using nth-of-type */
main .section:nth-of-type(6n+1) { --divider-doodle: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 16'><path d='M2,8 Q8,4 14,8 T26,8 M22,4 L28,8 L22,12' stroke='%238a7a5a' stroke-width='1.6' fill='none' stroke-linecap='round' stroke-linejoin='round'/></svg>"); }
main .section:nth-of-type(6n+2) { --divider-doodle: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 16'><path d='M12,2 L13.8,7 L19,7 L14.6,10 L16.2,15 L12,12 L7.8,15 L9.4,10 L5,7 L10.2,7 Z' stroke='%238a7a5a' stroke-width='1.4' fill='none' stroke-linejoin='round'/></svg>"); }
main .section:nth-of-type(6n+3) { --divider-doodle: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 16'><path d='M3,9 L9,14 L21,3' stroke='%238a7a5a' stroke-width='1.8' fill='none' stroke-linecap='round' stroke-linejoin='round'/></svg>"); }
main .section:nth-of-type(6n+4) { --divider-doodle: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 16'><path d='M3,4 Q14,4 18,8 Q22,12 28,12 M24,9 L28,12 L25,15' stroke='%238a7a5a' stroke-width='1.6' fill='none' stroke-linecap='round' stroke-linejoin='round'/></svg>"); }
main .section:nth-of-type(6n+5) { --divider-doodle: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 16'><path d='M16,8 Q16,4 12,4 Q6,4 6,9 Q6,13 12,13 Q19,13 19,7 Q19,2 11,2' stroke='%238a7a5a' stroke-width='1.4' fill='none' stroke-linecap='round'/></svg>"); }
main .section:nth-of-type(6n) { --divider-doodle: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 16'><circle cx='12' cy='8' r='3' stroke='%238a7a5a' stroke-width='1.6' fill='none'/><circle cx='12' cy='8' r='1' fill='%238a7a5a'/></svg>"); }

.section h2 {
  display: flex;
  align-items: baseline;
  gap: var(--s-3);
  margin-top: 0;
  margin-bottom: var(--s-3);
  font-family: var(--font-body);
  font-size: var(--fs-h2);
  font-weight: 600;
  color: var(--ink);
  position: relative;
}

.section h2::after {
  content: "";
  display: block;
  position: absolute;
  bottom: -3px;
  left: 0;
  width: 60%;
  height: 3px;
  background: var(--red-pen);
  filter: url(#ink-wobble);
  opacity: 0.65;
  border-radius: 2px;
}

.section h2 .num {
  font-size: var(--fs-tiny);
  font-weight: 400;
  color: var(--em-purple);
  font-family: var(--font-display);
  background: transparent;
  border: 1.5px solid var(--em-purple);
  padding: 2px 8px;
  border-radius: var(--r-sm);
  letter-spacing: 0.06em;
  transform: rotate(-2deg);
  flex-shrink: 0;
}

/* Special section variants */
.section.driver {
  background: var(--paper);
  color: var(--ink);
  border-color: var(--em-purple);
  border-style: dashed;
  border-width: 2px;
  position: relative;
}

.section.driver h2, .section.driver p { color: var(--ink); }

.section.driver p:first-of-type {
  background: linear-gradient(180deg, transparent 50%, var(--highlighter) 50%, var(--highlighter) 92%, transparent 92%);
  display: inline;
  padding: 0 4px;
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
}

.section.driver .num {
  border-color: var(--em-purple);
  color: var(--em-purple);
}

.section.notice-wonder {
  background: var(--paper);
  background-image: linear-gradient(var(--rule) 1px, transparent 1px);
  background-size: 100% 28px;
  background-position: 0 var(--s-5);
}

.section.exit {
  border-style: dashed;
  border-color: var(--em-purple);
  border-width: 2.5px;
  position: relative;
}

.section.exit::before {
  content: "✂";
  position: absolute;
  top: -10px;
  left: 24px;
  background: var(--paper);
  padding: 0 6px;
  color: var(--em-purple);
  font-size: 1rem;
}
```

- [ ] **Step 2: Smoke-test on a lesson page**

Run: `open Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/01-vectors.html`
Expected: Each section is a cream card with dashed brown border. Doodles appear at section dividers. Section number badges are purple-bordered with a slight rotation. The Driving Question text is highlighted yellow. Exit Ticket has a "✂" mark at the top-left.

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css
git commit -m "feat(web/css): section cards as notebook pages with doodle dividers"
```

## Task B7: Rewrite turn-and-talk callouts + vocabulary box

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css`

- [ ] **Step 1: Replace the `.tt` and `.vocab` rules**

Locate `/* ----- Turn and Talk callouts ----- */` and `/* ----- Vocabulary box ----- */` (back to back), and replace both blocks with:

```css
/* ----- Turn and Talk callouts (margin notes) ----- */
.tt {
  margin: var(--s-4) 0;
  padding: var(--s-3) var(--s-4) var(--s-3) calc(var(--s-4) + 8px);
  background: var(--paper);
  border-left: 4px solid var(--vs-blue);
  background-image: linear-gradient(var(--rule) 1px, transparent 1px);
  background-size: 100% 28px;
  background-position: 0 0;
  font-family: var(--font-body);
  font-size: 1rem;
  color: var(--ink);
  position: relative;
}

.tt::before {
  content: "Turn and Talk →";
  display: inline-block;
  font-family: var(--font-display);
  font-size: var(--fs-tiny);
  font-weight: 400;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--vs-blue);
  margin-right: var(--s-2);
}

/* ----- Vocabulary box (taped-on index card) ----- */
.vocab {
  background: var(--paper-edge);
  border: 1.5px solid var(--ink-faint);
  border-radius: var(--r-sm);
  padding: var(--s-4) var(--s-5) var(--s-4);
  position: relative;
  transform: rotate(-0.5deg);
  margin-top: var(--s-5);
}

/* Two paper-tape rectangles at top corners */
.vocab::before,
.vocab::after {
  content: "";
  position: absolute;
  top: -10px;
  width: 56px;
  height: 18px;
  background: var(--paper-tape);
  border: 1px solid rgba(43, 36, 24, 0.15);
  opacity: 0.85;
}

.vocab::before { left: 24px; transform: rotate(-4deg); }
.vocab::after { right: 24px; transform: rotate(3deg); }

.vocab h2 {
  color: var(--em-purple);
  font-family: var(--font-display);
  font-size: var(--fs-h2);
  font-weight: 400;
}

.vocab dl { margin: 0; }

.vocab dt {
  font-family: var(--font-body);
  font-weight: 600;
  color: var(--em-purple);
  margin-top: var(--s-3);
  font-size: 1.05rem;
}

.vocab dd {
  margin: 4px 0 0;
  padding-left: 0;
  color: var(--ink-soft);
  font-family: var(--font-body);
  line-height: 1.55;
}
```

- [ ] **Step 2: Smoke-test**

Refresh a lesson page. Expected: Turn-and-Talk callouts now look like ruled-paper margin notes with the title in handwriting. Vocabulary box rotates -0.5° and has two paper-tape rectangles at the top corners.

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css
git commit -m "feat(web/css): turn-and-talk margin notes + taped vocab card"
```

## Task B8: Rewrite lab interactives chrome (frame + readouts)

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css`

- [ ] **Step 1: Replace the `.lab` and `.lab-readouts` rules**

Locate `/* ----- Interactive containers ----- */` and replace through the end of the `.lab-readouts .readout-card .val` rules with:

```css
/* ----- Lab interactives (notebook lab-bench) ----- */
.lab {
  background: var(--paper);
  background-image:
    linear-gradient(var(--grid) 1px, transparent 1px),
    linear-gradient(90deg, var(--grid) 1px, transparent 1px);
  background-size: 22px 22px;
  border: 2px solid var(--ink);
  border-radius: var(--r-md);
  padding: var(--s-4);
  margin: var(--s-4) 0;
  position: relative;
}

.lab::before {
  content: "EXPERIMENT";
  position: absolute;
  top: -12px;
  left: 18px;
  background: var(--paper);
  padding: 0 8px;
  font-family: var(--font-display);
  font-size: var(--fs-tiny);
  letter-spacing: 0.12em;
  color: var(--em-purple);
}

.lab-canvas {
  background: var(--paper);
  border-radius: var(--r-sm);
  padding: var(--s-3);
  margin-bottom: var(--s-3);
  display: flex;
  justify-content: center;
  border: 1px dashed var(--ink-faint);
}

.lab-controls {
  display: flex;
  flex-direction: column;
  gap: var(--s-3);
}

.lab-controls .row {
  display: flex;
  flex-wrap: wrap;
  gap: var(--s-3);
  align-items: center;
}

.lab-controls label {
  display: flex;
  flex-direction: column;
  gap: 4px;
  flex: 1;
  min-width: 200px;
  font-size: var(--fs-small);
  font-family: var(--font-body);
  font-weight: 400;
  color: var(--ink);
}

.lab-controls .label-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

/* ----- Lab readouts (data-log table) ----- */
.lab-readouts {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 0;
  background: var(--paper);
  padding: 0;
  border-radius: var(--r-sm);
  border: 1.5px solid var(--ink);
  overflow: hidden;
}

.readout-card {
  display: flex;
  flex-direction: column;
  gap: 2px;
  padding: var(--s-3);
  border-right: 1px dashed var(--ink-faint);
  border-bottom: 1px dashed var(--ink-faint);
}

.readout-card:last-child { border-right: 0; }

.readout-card .key {
  font-size: var(--fs-tiny);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--ink-faint);
  font-weight: 400;
  font-family: var(--font-display);
}

.readout-card .val {
  font-family: var(--font-mono);
  font-size: 1.25rem;
  font-weight: 500;
  color: var(--em-purple);
  font-variant-numeric: tabular-nums;
}

.readout-card .val.accent { color: var(--vs-blue); }

.button-bar {
  display: flex;
  gap: var(--s-2);
  flex-wrap: wrap;
}
```

- [ ] **Step 2: Smoke-test**

Refresh `lessons/01-vectors.html`. Expected: vector playground now sits inside a 2px solid ink-bordered box with graph-paper background; "EXPERIMENT" label tabs out from the top-left; readouts render as a tabular data-log with monospace numbers.

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css
git commit -m "feat(web/css): lab interactives as notebook lab-bench with data-log readouts"
```

## Task B9: Rewrite TOC (paper bookmark with stamped digits)

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css`

- [ ] **Step 1: Replace the `.toc` rules**

Locate `/* ----- Sticky TOC ----- */` and replace through the end of the `.toc a.active` rules with:

```css
/* ----- Sticky TOC (paper bookmark) ----- */
.toc {
  position: sticky;
  top: var(--s-4);
  font-size: var(--fs-small);
  background: var(--paper-edge);
  border: 1px solid var(--ink-faint);
  border-right: 0;
  padding: var(--s-3);
  border-radius: var(--r-sm) 0 0 var(--r-sm);
  margin-right: -1px;
  position: relative;
}

.toc::after {
  content: "";
  position: absolute;
  right: -12px;
  top: 0;
  bottom: 0;
  width: 12px;
  background: var(--paper-edge);
  clip-path: polygon(0 0, 100% 8%, 60% 16%, 100% 24%, 70% 32%, 100% 40%, 60% 48%, 100% 56%, 70% 64%, 100% 72%, 60% 80%, 100% 88%, 0 100%);
  border-top: 1px solid var(--ink-faint);
  border-bottom: 1px solid var(--ink-faint);
  border-right: 1px solid var(--ink-faint);
}

.toc h4 {
  font-size: var(--fs-tiny);
  text-transform: uppercase;
  letter-spacing: 0.10em;
  color: var(--ink-soft);
  margin: 0 0 var(--s-2);
  font-weight: 400;
  font-family: var(--font-display);
}

.toc ol { list-style: none; padding: 0; margin: 0; counter-reset: toc; }
.toc li { margin: 0; counter-increment: toc; }

.toc a {
  display: flex;
  align-items: center;
  gap: var(--s-2);
  padding: 6px 0;
  color: var(--ink-soft);
  border: 0;
  font-weight: 400;
  font-family: var(--font-body);
}

.toc a::before {
  content: counter(toc, decimal-leading-zero);
  font-size: var(--fs-tiny);
  font-variant-numeric: tabular-nums;
  font-family: var(--font-display);
  color: var(--ink);
  background: var(--paper);
  border: 1.5px solid var(--ink);
  width: 26px;
  height: 26px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  transition: background-color 0.2s ease, color 0.2s ease, border-color 0.2s ease;
}

.toc a:hover { color: var(--em-purple); border: 0; }

.toc a.active { color: var(--em-purple); font-weight: 600; }
.toc a.active::before { background: var(--red-pen); color: var(--paper); border-color: var(--red-pen); }
```

- [ ] **Step 2: Smoke-test**

Refresh any lesson, scroll. Expected: the right-side TOC has a torn paper-edge look, numbers in circular "stamped" badges, active section's badge fills with red ink.

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css
git commit -m "feat(web/css): TOC as paper bookmark with stamped-digit badges"
```

## Task B10: Rewrite lesson grid (index page) + pager

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css`

- [ ] **Step 1: Replace `.lesson-grid` and `.pager` rules**

Locate `/* ----- Lesson card grid (index page) ----- */` and `/* ----- Pager (lesson nav at bottom) ----- */` and replace both blocks with:

```css
/* ----- Lesson card grid (index page, notebook page thumbnails) ----- */
.lesson-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: var(--s-3);
  list-style: none;
  padding: 0;
}

.lesson-card {
  display: flex;
  flex-direction: column;
  gap: var(--s-2);
  background: var(--paper);
  background-image: linear-gradient(var(--grid) 1px, transparent 1px);
  background-size: 100% 22px;
  border: 1.5px solid var(--ink-faint);
  border-radius: var(--r-sm);
  padding: var(--s-4);
  text-decoration: none;
  color: inherit;
  transition: transform 0.15s ease, border-color 0.15s ease;
  position: relative;
  overflow: hidden;
}

.lesson-card::before { display: none; }

.lesson-card:hover {
  border-color: var(--ink);
  transform: translateY(-2px);
  background-color: var(--paper);
}

.lesson-card:hover::after {
  content: "↗";
  position: absolute;
  bottom: var(--s-3);
  right: var(--s-3);
  color: var(--red-pen);
  font-family: var(--font-display);
  font-size: 1.4rem;
  opacity: 0;
  animation: fadeInUp 0.2s ease forwards;
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

.lesson-card .number {
  font-size: var(--fs-tiny);
  font-weight: 400;
  color: var(--em-purple);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-family: var(--font-display);
  border: 1.5px solid var(--em-purple);
  padding: 2px 6px;
  align-self: flex-start;
  border-radius: var(--r-sm);
  transform: rotate(-2deg);
}

.lesson-card .title {
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.3;
}

.lesson-card .summary {
  font-size: var(--fs-small);
  color: var(--ink-soft);
  font-family: var(--font-body);
  flex: 1;
}

.lesson-card .footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: var(--fs-tiny);
  color: var(--ink-faint);
  font-family: var(--font-display);
  letter-spacing: 0.06em;
  padding-top: var(--s-2);
  border-top: 1px dashed var(--ink-faint);
}

/* ----- Pager (lesson nav) ----- */
.pager {
  display: flex;
  justify-content: space-between;
  gap: var(--s-3);
  margin-top: var(--s-6);
  padding-top: var(--s-4);
  border-top: 2px dashed var(--ink-faint);
}

.pager a {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 2px;
  padding: var(--s-3);
  border: 1.5px solid var(--ink-faint);
  border-radius: var(--r-sm);
  text-decoration: none;
  color: inherit;
  transition: transform 0.12s ease, border-color 0.15s ease;
  font-family: var(--font-body);
}

.pager a:hover {
  border-color: var(--ink);
  transform: translateY(-1px);
  background: var(--paper-edge);
}

.pager a.next { text-align: right; }

.pager .label {
  font-size: var(--fs-tiny);
  color: var(--ink-faint);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 400;
  font-family: var(--font-display);
}

.pager .target {
  font-size: var(--fs-body);
  font-weight: 600;
  color: var(--em-purple);
  font-family: var(--font-body);
}
```

- [ ] **Step 2: Smoke-test**

Refresh `index.html` and any lesson page. Expected: lesson cards on the index look like graph-paper thumbnails with a stamped lesson-number badge and an arrow doodle that fades in on hover. Pager (prev/next at lesson bottom) styled the same way.

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css
git commit -m "feat(web/css): lesson grid + pager as notebook page thumbnails"
```

## Task B11: Rewrite footer + tour panel + tour CTA + resource list

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css`

- [ ] **Step 1: Replace `.site-footer`, `.tour-cta`, `.tour-highlight`, `#tour-panel`, `.resource-list`, `details.misc` blocks**

Locate `/* ----- Footer ----- */` and replace from there through the end of the `details.misc[open] summary` rule with:

```css
/* ----- Footer (paper edge) ----- */
.site-footer {
  margin-top: var(--s-8);
  padding: var(--s-5) var(--s-4);
  background: transparent;
  color: var(--ink-faint);
  font-size: var(--fs-small);
  border-top: 1.5px dashed var(--ink-faint);
}

.site-footer-inner {
  max-width: var(--content-width);
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: var(--s-3);
  flex-wrap: wrap;
}

.tagline {
  font-style: italic;
  font-weight: 500;
  font-family: var(--font-display);
  transform: rotate(0.5deg);
  display: inline-block;
  color: var(--ink-soft);
  font-size: 1rem;
}

/* ----- Resource list (Explore Further) ----- */
.resource-list {
  list-style: none;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--s-2);
}

.resource-list li { margin: 0; }

.resource-list a {
  display: block;
  padding: var(--s-3);
  border: 1.5px solid var(--ink-faint);
  border-radius: var(--r-sm);
  text-decoration: none;
  color: inherit;
  font-weight: 600;
  font-family: var(--font-body);
  border-bottom-width: 1.5px;
  transition: transform 0.12s ease, border-color 0.15s ease, background-color 0.15s ease;
}

.resource-list a:hover {
  background: var(--paper-edge);
  border-color: var(--ink);
  transform: translateY(-1px);
}

.resource-list .source {
  display: block;
  font-size: var(--fs-tiny);
  color: var(--ink-faint);
  font-family: var(--font-display);
  letter-spacing: 0.04em;
  margin-top: 2px;
  font-weight: 400;
}

/* ----- Misconceptions / details ----- */
details.misc {
  border: 1.5px dashed var(--ink-faint);
  border-radius: var(--r-sm);
  padding: var(--s-2) var(--s-3);
  margin: var(--s-2) 0;
  background: var(--paper-edge);
}

details.misc summary {
  cursor: pointer;
  font-weight: 600;
  color: var(--red-pen);
  font-family: var(--font-display);
}

details.misc[open] summary { margin-bottom: var(--s-2); }

/* ----- Tour CTA on hero ----- */
.tour-cta {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 18px;
  margin-top: var(--s-3);
  background: var(--paper);
  color: var(--em-purple);
  border: 2px solid var(--em-purple);
  border-radius: var(--r-sm);
  font-size: var(--fs-small);
  font-weight: 400;
  letter-spacing: 0.04em;
  cursor: pointer;
  text-decoration: none;
  font-family: var(--font-display);
  border-bottom: 2px solid var(--em-purple);
  backdrop-filter: none;
  -webkit-backdrop-filter: none;
  transition: transform 0.12s ease, background-color 0.15s ease;
}

.tour-cta:hover {
  background: var(--paper-edge);
  border-bottom: 2px solid var(--em-purple);
  transform: translateY(-1px);
}

.tour-cta::before {
  content: "▶";
  font-size: 0.75em;
}

/* ----- Tour panel + highlight ----- */
.tour-highlight {
  position: relative;
  z-index: 99;
  outline: 3px solid var(--red-pen);
  outline-offset: 6px;
  border-radius: var(--r-sm);
  animation: tourPulse 1.6s ease-in-out infinite;
}

@keyframes tourPulse {
  0%, 100% { outline-color: var(--red-pen); box-shadow: 0 0 0 0 rgba(193, 70, 38, 0.4); }
  50% { outline-color: rgba(193, 70, 38, 0.6); box-shadow: 0 0 0 8px rgba(193, 70, 38, 0); }
}

#tour-panel {
  position: fixed;
  bottom: var(--s-4);
  right: var(--s-4);
  max-width: 380px;
  background: var(--paper);
  border: 1.5px solid var(--ink);
  border-radius: var(--r-sm);
  box-shadow: var(--shadow-3);
  padding: var(--s-4);
  z-index: 200;
  font-family: var(--font-body);
  font-size: var(--fs-small);
  transform: rotate(-1deg);
  animation: tourPanelIn 0.25s ease-out;
}

#tour-panel::before,
#tour-panel::after {
  content: "";
  position: absolute;
  top: -10px;
  width: 56px;
  height: 18px;
  background: var(--paper-tape);
  border: 1px solid rgba(43, 36, 24, 0.15);
  opacity: 0.85;
}

#tour-panel::before { left: 16px; transform: rotate(-4deg); }
#tour-panel::after { right: 16px; transform: rotate(3deg); }

@keyframes tourPanelIn {
  from { opacity: 0; transform: translateY(8px) rotate(-1deg); }
  to { opacity: 1; transform: translateY(0) rotate(-1deg); }
}

#tour-panel .tour-step-info {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: var(--fs-tiny);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--ink-faint);
  font-weight: 400;
  font-family: var(--font-display);
  margin-bottom: var(--s-2);
}

#tour-panel .dot-row {
  display: inline-flex;
  gap: 4px;
}

#tour-panel .dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--ink-faint);
}

#tour-panel .dot.active {
  background: var(--em-purple);
  width: 18px;
  border-radius: var(--r-pill);
}

#tour-panel h4 {
  margin: 0 0 var(--s-2);
  color: var(--em-purple);
  font-size: 1.05rem;
  font-family: var(--font-display);
  font-weight: 400;
}

#tour-panel p {
  margin: 0;
  font-size: var(--fs-small);
  color: var(--ink-soft);
  font-family: var(--font-body);
  line-height: 1.55;
}

#tour-panel .tour-controls {
  display: flex;
  gap: var(--s-2);
  margin-top: var(--s-3);
  align-items: center;
}

#tour-panel .tour-skip {
  margin-right: auto;
  background: transparent;
  border: 0;
  color: var(--ink-faint);
  padding: var(--s-2) 0;
  font-weight: 400;
  font-family: var(--font-body);
  text-decoration: underline;
}

#tour-panel .tour-skip:hover {
  background: transparent;
  color: var(--ink-soft);
}

#tour-panel button:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  #tour-panel {
    left: var(--s-2);
    right: var(--s-2);
    bottom: var(--s-2);
    max-width: none;
    transform: rotate(0deg);
  }
  #tour-panel::before, #tour-panel::after { display: none; }
}
```

- [ ] **Step 2: Smoke-test**

Visit `index.html?tour=1` to launch the tour. Expected: tour panel renders as a slightly rotated paper note with two paper-tape rectangles at the top corners, handwriting heading, and serif body. Tour CTA button on the hero is now a hand-drawn outline button.

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css
git commit -m "feat(web/css): footer, tour panel, tour CTA, resource list as notebook elements"
```

## Task B12: Add print stylesheet override

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css`

- [ ] **Step 1: Replace the existing `@media print` block at end of file**

Locate `/* Print */` near the end of the file and replace through the end with:

```css
/* Print — degrade to plain document */
@media print {
  .site-header, .site-footer, .toc, .pager, .progress-bar, #tour-panel, .tour-cta { display: none; }
  .tour-highlight { outline: 0; animation: none; }

  body {
    background: white;
    color: black;
    font-family: Georgia, serif;
  }

  body::before, body::after { display: none; }

  h1, h2, h3, h4 {
    font-family: Georgia, serif;
    font-weight: 700;
    color: black;
  }

  .section, .lab, .vocab {
    box-shadow: none;
    border: 1px solid #999;
    background: white;
    background-image: none;
    break-inside: avoid;
    transform: none;
  }

  .section + .section::before { display: none; }
  .section h2::after { display: none; }
  .vocab::before, .vocab::after { display: none; }
  .lab::before {
    border: 1px solid #999;
    background: white;
    color: black;
  }
  .lab-canvas { background: white; border: 1px solid #ccc; }

  .hero {
    background: white;
    background-image: none;
    color: black;
    padding: var(--s-3);
    border-bottom: 2px solid black;
  }
  .hero::before { display: none; }
  .hero h1, .hero .eyebrow, .hero .lede { color: black; font-family: Georgia, serif; }

  .chip {
    transform: none;
    background: white;
    border: 1px solid #999;
    color: black;
  }

  .tt {
    background: white;
    background-image: none;
    border: 1px solid #999;
    border-left: 3px solid black;
  }

  .lesson-card { background: white; background-image: none; border: 1px solid #999; }
  .lesson-card .number { transform: none; }
}
```

- [ ] **Step 2: Smoke-test print preview**

In your browser, open any lesson, then File → Print Preview (Cmd+P, then Cancel without printing). Expected: the print version drops paper-tape rotations, paper textures, and decorative dividers; uses Georgia serif throughout; renders in clean black-on-white with `1px solid #999` borders.

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css
git commit -m "feat(web/css): print stylesheet — clean black-on-white serif fallback"
```

## Task B13: Add scroll-in animation keyframes (CSS side)

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css`

- [ ] **Step 1: Append the animation block at the very end of the file**

Use Edit, finding `}` (the last `}` of the print block) and appending after it:

```css

/* ===========================================================
 * Animations (medium budget)
 * Hooked up by IntersectionObserver in site.js. The body class
 * "anim-ready" is added once site.js wires the observer; if JS
 * is disabled or not yet loaded, sections stay visible (no FOUC).
 * =========================================================== */

@keyframes sectionFadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes drawIn {
  from { stroke-dashoffset: var(--draw-length, 200); }
  to { stroke-dashoffset: 0; }
}

@keyframes labReveal {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes hatchIn {
  from { background-size: 0 100%; }
  to { background-size: 100% 100%; }
}

body.anim-ready .section { opacity: 0; transform: translateY(8px); }
body.anim-ready .section.in-view {
  animation: sectionFadeIn 250ms ease-out forwards;
}

body.anim-ready .lab { opacity: 0; }
body.anim-ready .lab.in-view {
  animation: labReveal 400ms ease-out 150ms forwards;
}

body.anim-ready .lab.in-view .lab-controls {
  animation: labReveal 400ms ease-out 350ms forwards;
}

@media (prefers-reduced-motion: reduce) {
  body.anim-ready .section,
  body.anim-ready .lab,
  body.anim-ready .lab .lab-controls {
    opacity: 1;
    transform: none;
    animation: none;
  }
  .progress-bar::after { animation: none; }
  .tour-highlight { animation: none; }
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

- [ ] **Step 2: Smoke-test (no visible change yet — JS wires this up in Phase D)**

Refresh the page. Expected: nothing animates yet (JS hasn't been updated), but the page still renders normally because `body.anim-ready` isn't set without JS.

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css
git commit -m "feat(web/css): add scroll-in keyframes + prefers-reduced-motion gating"
```

---

# Phase C: HTML page updates (font links + SVG include + class swaps)

## Task C1: Update index.html, unit_plan.html, assessment.html

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/index.html`
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/unit_plan.html`
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/assessment.html`

- [ ] **Step 1: Update font link in `index.html`**

Use Edit on `index.html` to replace:

```html
  <link rel="preconnect" href="https://rsms.me/">
  <link rel="stylesheet" href="https://rsms.me/inter/inter.css">
  <link rel="stylesheet" href="_assets/site.css">
```

with:

```html
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Architects+Daughter&family=Lora:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@500&display=swap">
  <link rel="stylesheet" href="_assets/site.css">
```

- [ ] **Step 2: Add SVG include + sprite reference to `index.html`**

In `index.html`, find `<body>` and add immediately after it:

```html
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <use href="_assets/notebook.svg#ink-wobble"/>
</svg>
```

Wait — that's not the right pattern for filter inclusion. Instead, find `<body>` and add immediately after:

```html
<div hidden aria-hidden="true">
  <object data="_assets/notebook.svg" type="image/svg+xml" tabindex="-1" style="position:absolute;width:0;height:0"></object>
</div>
```

Actually, the cleanest pattern is to inline-include the SVG defs at the top of the body. Use Edit to find `<body>` in `index.html` and replace it with:

```html
<body>
<!-- SVG defs (filters, doodles) — inlined so url(#ink-wobble) works in CSS -->
<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><use href="_assets/notebook.svg#ink-wobble"/></svg>
```

Hmm, this won't work either because `<use>` referencing a filter doesn't actually instantiate the filter for CSS `url(#ink-wobble)`. The filter must be in the same document.

Correct pattern: read `_assets/notebook.svg` content (without the outer `<svg>` wrapper) and inline it. But that's verbose to repeat across 12 files. Use a simpler approach: the SVG defs file is fetched and its content is loaded via a small `<script>` block that injects the SVG into the body.

Actually the simplest robust pattern: put the SVG defs inline at the top of `<body>` in each HTML file. Verbose but reliable. The defs are small (~3KB).

Use Edit to replace `<body>` with:

```html
<body>
<!-- SVG defs — must be inline for filter url() references in CSS -->
<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <defs>
    <filter id="ink-wobble" x="-2%" y="-2%" width="104%" height="104%">
      <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" seed="3" result="noise"/>
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="1.5"/>
    </filter>
  </defs>
</svg>
```

This inlines just the `ink-wobble` filter (the only one CSS references via `url(#ink-wobble)`). The doodle and stamped-digit symbols in `notebook.svg` are referenced as `url(...)` in CSS using inline `data:image/svg+xml` URIs (already done in Task B6), so they don't need external symbol resolution.

- [ ] **Step 3: Apply identical updates to `unit_plan.html` and `assessment.html`**

Repeat steps 1–2 for `unit_plan.html` and `assessment.html`.

- [ ] **Step 4: Smoke-test all three pages**

```bash
open Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/index.html
open Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/unit_plan.html
open Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/assessment.html
```

Expected: all three load with Lora body, Architects Daughter headings, and the section-h2 red ink underlines have the wobbly hand-drawn imperfection from `ink-wobble`.

- [ ] **Step 5: Run web validator**

Run: `source .venv/bin/activate && python tools/validate_web.py`
Expected: `OK — checked 12 HTML files; no answer-revealing emphasis in any MC option.`

- [ ] **Step 6: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/index.html \
        Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/unit_plan.html \
        Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/assessment.html
git commit -m "feat(web/html): swap Inter for Google fonts + inline ink-wobble filter (top-level pages)"
```

## Task C2: Update lesson 01–05 HTML pages

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/01-vectors.html`
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/02-distance-displacement.html`
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/03-velocity.html`
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/04-acceleration.html`
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/05-motion-graphs.html`

- [ ] **Step 1: Replace the Inter font link with Google Fonts in each of the five files**

For each lesson file 01-vectors, 02-distance-displacement, 03-velocity, 04-acceleration, 05-motion-graphs, replace the `<head>` font link block. Find:

```html
  <link rel="stylesheet" href="https://rsms.me/inter/inter.css">
  <link rel="stylesheet" href="../_assets/site.css">
```

Replace with:

```html
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Architects+Daughter&family=Lora:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@500&display=swap">
  <link rel="stylesheet" href="../_assets/site.css">
```

- [ ] **Step 2: Add the inline SVG defs after `<body>` in each of the five files**

In each lesson file, find the line `<body>` and replace with:

```html
<body>
<!-- SVG defs — must be inline for filter url() references in CSS -->
<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <defs>
    <filter id="ink-wobble" x="-2%" y="-2%" width="104%" height="104%">
      <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" seed="3" result="noise"/>
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="1.5"/>
    </filter>
  </defs>
</svg>
```

- [ ] **Step 3: Smoke-test 01–05**

```bash
for f in 01-vectors 02-distance-displacement 03-velocity 04-acceleration 05-motion-graphs; do
  open "Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/${f}.html"
done
```

Expected: all five lessons render with the new fonts and notebook chrome.

- [ ] **Step 4: Run validator**

Run: `source .venv/bin/activate && python tools/validate_web.py`
Expected: `OK — checked 12 HTML files; …`

- [ ] **Step 5: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/01-vectors.html \
        Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/02-distance-displacement.html \
        Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/03-velocity.html \
        Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/04-acceleration.html \
        Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/05-motion-graphs.html
git commit -m "feat(web/html): font + filter updates for lessons 01-05"
```

## Task C3: Update lesson 06–09 HTML pages

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/06-freefall.html`
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/07-vertical-projectiles.html`
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/08-horizontal-projectile-motion.html`
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/09-projectiles-at-an-angle.html`

- [ ] **Step 1: Replace the Inter font link with Google Fonts in each of the four files**

For each lesson file 06-freefall, 07-vertical-projectiles, 08-horizontal-projectile-motion, 09-projectiles-at-an-angle, find:

```html
  <link rel="stylesheet" href="https://rsms.me/inter/inter.css">
  <link rel="stylesheet" href="../_assets/site.css">
```

Replace with:

```html
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Architects+Daughter&family=Lora:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@500&display=swap">
  <link rel="stylesheet" href="../_assets/site.css">
```

- [ ] **Step 2: Add the inline SVG defs after `<body>` in each of the four files**

In each of the four lesson files, find the line `<body>` and replace with:

```html
<body>
<!-- SVG defs — must be inline for filter url() references in CSS -->
<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <defs>
    <filter id="ink-wobble" x="-2%" y="-2%" width="104%" height="104%">
      <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" seed="3" result="noise"/>
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="1.5"/>
    </filter>
  </defs>
</svg>
```

- [ ] **Step 3: Smoke-test**

```bash
for f in 06-freefall 07-vertical-projectiles 08-horizontal-projectile-motion 09-projectiles-at-an-angle; do
  open "Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/${f}.html"
done
```

Expected: all four lessons render with the new fonts and notebook chrome.

- [ ] **Step 4: Run validator**

Run: `source .venv/bin/activate && python tools/validate_web.py`
Expected: `OK — checked 12 HTML files; …`

- [ ] **Step 5: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/06-freefall.html \
        Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/07-vertical-projectiles.html \
        Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/08-horizontal-projectile-motion.html \
        Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/09-projectiles-at-an-angle.html
git commit -m "feat(web/html): font + filter updates for lessons 06-09"
```

---

# Phase D: site.js — animation triggers

## Task D1: Add IntersectionObserver scroll-in handler

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.js`

- [ ] **Step 1: Append the new code at end of file (after the existing `const G = 9.8;` export)**

Find the end of the file (after the last existing function like `revealHint` or the existing tour logic). Append a new IIFE block right before the existing tour code, OR more simply, add to the bottom of the file:

Use Edit to find the line `export const G = 9.8;` and replace it with:

```javascript
export const G = 9.8;

// ===========================================================
// Scroll-in animation triggers (lab-notebook redesign)
// Adds .in-view to .section and .lab elements when they enter
// the viewport. CSS keyframes (in site.css) animate them.
// Also flips body.anim-ready so the initial-hidden styles apply.
// Respects prefers-reduced-motion via the CSS gate.
// ===========================================================
(function () {
  // Don't apply scroll-in animations if user prefers reduced motion;
  // the CSS @media query will keep things visible regardless, but we
  // also skip the observer to save event work.
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Mark the body as animation-ready *after* the page has had a chance
  // to paint, so the initial-hidden state doesn't FOUC.
  requestAnimationFrame(() => {
    document.body.classList.add("anim-ready");
  });

  if (reduce) {
    // Add .in-view to everything immediately so nothing stays hidden.
    document.querySelectorAll(".section, .lab").forEach(el => el.classList.add("in-view"));
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("in-view");
        observer.unobserve(entry.target);
      }
    });
  }, { rootMargin: "0px 0px -10% 0px", threshold: 0.05 });

  document.querySelectorAll(".section, .lab").forEach(el => observer.observe(el));
})();
```

- [ ] **Step 2: Smoke-test**

Refresh `lessons/01-vectors.html`. Expected: as you scroll, sections fade and translate up 8px on entry. Refresh and scroll again — the animation only fires once per section per page load.

- [ ] **Step 3: Verify reduced-motion mode**

In macOS: System Settings → Accessibility → Display → "Reduce motion" ON. Refresh the page. Expected: sections appear in place, no fade. (Toggle off after testing.)

- [ ] **Step 4: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.js
git commit -m "feat(web/js): IntersectionObserver scroll-in for sections + lab containers"
```

---

# Phase E: README + final verification

## Task E1: Update web edition README

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/README.md`

- [ ] **Step 1: Add a "Visual identity" section near the top of the README**

Use the Edit tool on `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/README.md`. Find the line `## Sharing the demo` and replace with the following content (which keeps `## Sharing the demo` at the bottom and adds a new section above it):

`old_string`:

    ## Sharing the demo

`new_string` (use 4-backtick fences in the README content where bash is shown so they nest correctly inside markdown):

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

- [ ] **Step 2: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/README.md
git commit -m "docs(web): document the lab-notebook redesign and rollback path"
```

## Task E2: Run all validators + tests

**Files:** none

- [ ] **Step 1: Run pytest suite**

Run: `source .venv/bin/activate && python -m pytest tests/tools/ -q`
Expected: `30 passed`

- [ ] **Step 2: Run web validator**

Run: `source .venv/bin/activate && python tools/validate_web.py`
Expected: `OK — checked 12 HTML files; no answer-revealing emphasis in any MC option.`

- [ ] **Step 3: No commit (verification only)**

## Task E3: Manual visual QA — top-level pages

**Files:** none (visual review only)

- [ ] **Step 1: Open each top-level page and inspect**

```bash
open Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/index.html
open Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/unit_plan.html
open Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/assessment.html
```

For each page, verify:
- Body uses Lora serif typography
- Headings use Architects Daughter (block-print)
- Header masthead is cream paper with index-card tabs
- Hero is graph-paper background with handwritten title
- Sections are notebook pages with dashed borders and doodle dividers
- Specific to `index.html`: lesson cards show the ↗ arrow doodle on hover
- Specific to `unit_plan.html`: the pacing table renders cleanly
- Specific to `assessment.html`: the stimulus SVG and MC options render correctly; no `<strong>` accidentally introduced into MC options

- [ ] **Step 2: Run web validator one more time**

Run: `source .venv/bin/activate && python tools/validate_web.py`
Expected: `OK — checked 12 HTML files; …`

- [ ] **Step 3: No commit (verification only)**

## Task E4: Manual visual QA — all 9 lessons

**Files:** none (visual review only)

- [ ] **Step 1: Open every lesson and click through one full lesson interaction**

```bash
for f in 01-vectors 02-distance-displacement 03-velocity 04-acceleration 05-motion-graphs 06-freefall 07-vertical-projectiles 08-horizontal-projectile-motion 09-projectiles-at-an-angle; do
  open "Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/${f}.html"
done
```

For each lesson, verify:
- Hero, sections, vocab, exit-ticket, explore-further, pager all render with notebook style
- Lab interactive container has the "EXPERIMENT" tab label and graph-paper background
- Interactive widget (vector playground / projectile launcher / etc.) still functions — drag, slide, click all work as before
- TOC on the right is the paper-bookmark style with stamped-digit numbers
- No console errors

- [ ] **Step 2: Test the tour**

Run: `open "Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/index.html?tour=1"`
Click through all 9 tour steps. Expected: tour panel renders as a slightly-rotated paper note with paper-tape corners; advances correctly across pages.

- [ ] **Step 3: Print-preview at least one lesson**

In Chrome: Cmd+P on any lesson, view the preview, then Cancel. Expected: clean black-on-white serif rendering; no graph-paper, no rotations, readable layout.

- [ ] **Step 4: No commit (verification only)**

## Task E5: Push and verify CI

**Files:** none

- [ ] **Step 1: Push the branch**

Run: `git push origin physics-east-meadow-refactor`
Expected: push succeeds, CI workflow auto-triggers.

- [ ] **Step 2: Watch the deploy**

Run: `gh run watch $(gh run list --workflow=deploy-pages.yml --limit 1 --json databaseId --jq '.[0].databaseId')`
Expected: build job + deploy job both succeed in ~30s; "Validate web assessments (no answer reveals)" step prints `OK — checked 12 HTML files; …`.

- [ ] **Step 3: Verify the live site is updated**

Run: `open https://angsta-ed.github.io/physics-kinematics/`
Expected: live site reflects the new lab-notebook design.

- [ ] **Step 4: Smoke-test live tour**

Run: `open "https://angsta-ed.github.io/physics-kinematics/?tour=1"`
Expected: tour starts; runs through all 9 steps; live URL is shareable for async demos.

- [ ] **Step 5: No commit needed; the deploy is the final state.**

---

## Done criteria

- All 22 tasks above are checked off.
- `python tools/validate_web.py` exits 0.
- `python -m pytest tests/tools/` exits 0 (30 passed).
- All 12 pages render with the lab-notebook identity in the browser.
- Print preview produces a clean serif document.
- Tour works end-to-end (`?tour=1` link valid).
- Live GitHub Pages deploy reflects the redesign.
- The OneNote-friendly track at `01_Physics_East_Meadow_Refactor/` is unchanged (verify with `git diff main -- Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor`; expected: empty output).
