# Physics East Meadow Refactor — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Pilot a refactored Physics curriculum (Kinematics unit, 9 lessons) that mirrors the NEW East Meadow Scope and Sequence, ships in two flavors per student artifact (rich interactive HTML + OneNote-paste static HTML) with co-branded VSCHSD × East Meadow DOCX teacher materials, and is reproducible via Python tooling.

**Architecture:** Markdown sources for all DOCX artifacts (Pandoc + reference DOCX template); hand-authored interactive HTML for student exploration pages with mandatory `<noscript>` SVG storyboard fallbacks; a Python `static_ifier` pass converts interactive HTML to OneNote-paste-friendly static HTML. Build orchestrated by `tools/build_lessons.py`. Tools are TDD'd against fixture lessons; pilot validates the pattern end-to-end with the Vectors lesson before scaling to the remaining eight.

**Tech Stack:** Python 3.14 (already in `.venv`), Pandoc (Homebrew install in Phase A), `python-docx` (already in `.venv`), BeautifulSoup4 (for static-ifier HTML transformations), PyYAML (for `lesson_schema.yaml`), pytest (for tooling tests). Plain HTML/CSS/JS + inline SVG for student pages; KaTeX (vendored) for math rendering.

**Spec:** `docs/superpowers/specs/2026-05-08-physics-east-meadow-refactor-design.md`

---

## File Structure

```
Publisher_Ready_Curriculum/
  _archive/
    01_Physics_East_Meadow_Refactor_2026-05-08/      # archived old partial work
  01_Physics_East_Meadow_Refactor/
    README.md                                         # unit index + hosting workflow
    Scope_and_Sequence.md                             # copy of source MD
    OneNote_Import_Guide.md                           # one-page paste workflow
    _assets/
      brand/
        em_logo.svg                                   # placeholder
        em_logo.png                                   # placeholder
        vs_logo.svg                                   # placeholder
        vs_logo.png                                   # placeholder
        brand.css                                     # CSS custom properties
        reference.docx                                # Pandoc reference template
      lesson.css
      lesson.js
      icons.svg
      katex/                                          # vendored KaTeX
    00_Math_in_Science/README.md                      # stub
    01_Kinematics/
      Unit_Plan.md / .docx / .onenote.html
      Assessments/
        Kinematics_Regents_Style_Set.md / .docx / .onenote.html
      Visuals/
        Visual_Prompts.md
      01_Vectors/                                     # PILOT LESSON
        Student_Exploration.html
        Student_Exploration.onenote.html
        Teacher_Guide.md / .docx / .onenote.html
        Answer_Key.md / .docx / .onenote.html
      02_Distance_and_Displacement/ ... 09_Projectiles_at_an_Angle/
    02_Forces/README.md ... 09_Modern_Physics/README.md  # stubs
tools/
  __init__.py
  lesson_schema.yaml
  scaffold_lesson.py
  build_lessons.py
  publish_pages.py
  static_ifier.py
  validators.py
  pandoc_runner.py
  templates/
    student_exploration.html.tmpl
    teacher_guide.md.tmpl
    answer_key.md.tmpl
    unit_plan.md.tmpl
    lesson_readme.md.tmpl
  lesson_qa_checklist.md
tests/tools/
  __init__.py
  conftest.py
  test_validators.py
  test_static_ifier.py
  test_scaffold_lesson.py
  test_build_lessons.py
  fixtures/
    valid_lesson/                                     # complete passing lesson
    invalid_no_noscript/
    invalid_too_many_vocab/
    invalid_missing_section/
    sample_interactive.html
    sample_interactive_expected_onenote.html
docs/superpowers/plans/2026-05-08-physics-east-meadow-refactor-plan.md  # this file
```

---

## Lesson Authoring Reference (used by Phases C and D)

**The lesson backbone is fixed (spec §5.1).** Every Student_Exploration.html and every Teacher_Guide.md follows this 10-step arc; every Teacher_Guide includes the 14-section structure (spec §6.4); every Answer_Key follows §6.5.

**Three concrete authoring deliverables per lesson:**
1. `Student_Exploration.html` — must include sections 1–16 from spec §6.2, including a `<div data-interactive="true">` containing the live JS interactive AND a `<noscript>` sibling block containing a 3–5 frame storyboard SVG showing key states.
2. `Teacher_Guide.md` — must include all 14 headings from spec §6.4 in order. Curated Resources block (heading 2) pulls verbatim from the corresponding row in `Scope_and_Sequence.md`.
3. `Answer_Key.md` — one entry per "Make it Make Sense" prompt and exit-ticket item, each with expected answer + 1-2 sentence rubric + NYSSLS tag.

**The `tools/scaffold_lesson.py` script generates skeletons of all three with required headings already in place** — the engineer fills in content, not structure.

---

# Phase A: Setup and Tooling

This phase produces the build/scaffold/publish tools, TDD-style. By the end of Phase A, `python tools/build_lessons.py tests/tools/fixtures/valid_lesson` should green-build a sample lesson with no real curriculum content yet.

## Task A1: Install Pandoc

**Files:** none (system dependency)

- [ ] **Step 1: Install Pandoc via Homebrew**

Run: `brew install pandoc`
Expected: Installation completes without error.

- [ ] **Step 2: Verify Pandoc version**

Run: `pandoc --version | head -1`
Expected: Prints `pandoc 3.x.x` or higher.

- [ ] **Step 3: No commit (system dependency only)**

## Task A2: Add Python dependencies

**Files:**
- Modify: `requirements.txt` (create if missing)
- Modify: `.venv` (via pip install)

- [ ] **Step 1: Create or update requirements.txt**

Write `requirements.txt`:

```
python-docx>=1.1.0
beautifulsoup4>=4.12.0
PyYAML>=6.0
pytest>=8.0
lxml>=5.0
```

- [ ] **Step 2: Install dependencies into venv**

Run: `source .venv/bin/activate && pip install -r requirements.txt`
Expected: All five packages install without error.

- [ ] **Step 3: Commit**

```bash
git add requirements.txt
git commit -m "chore: add tooling dependencies for Physics refactor"
```

## Task A3: Archive existing partial refactor

**Files:**
- Move: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/` → `Publisher_Ready_Curriculum/_archive/01_Physics_East_Meadow_Refactor_2026-05-08/`

- [ ] **Step 1: Create archive directory**

Run: `mkdir -p Publisher_Ready_Curriculum/_archive`
Expected: directory exists.

- [ ] **Step 2: Move existing partial refactor**

Run: `git mv Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor Publisher_Ready_Curriculum/_archive/01_Physics_East_Meadow_Refactor_2026-05-08`
Expected: `git status` shows the rename as a single move.

- [ ] **Step 3: Commit**

```bash
git commit -m "chore: archive partial Physics East Meadow refactor before pilot rebuild"
```

## Task A4: Create new pilot folder skeleton

**Files:**
- Create: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/` (and 10 unit subfolders)

- [ ] **Step 1: Create unit folders**

Run:
```bash
cd Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor && mkdir -p \
  _assets/brand _assets/katex \
  00_Math_in_Science 01_Kinematics 02_Forces 03_Momentum_Impulse \
  04_Energy 05_Thermodynamics 06_Electrostatics 07_Current_Electricity \
  08_Waves 09_Modern_Physics
```
Expected: 10 unit folders + `_assets/` exist.

- [ ] **Step 2: Create stub README in each non-pilot unit**

For each non-pilot unit (00, 02–09), write `README.md` containing:

```markdown
# Unit stub

This unit will be authored after the Kinematics pilot is accepted. The folder structure mirrors `01_Kinematics/`.

See `../README.md` and `../Scope_and_Sequence.md` for the unit scope.
```

- [ ] **Step 3: Create Kinematics unit subfolders**

Run:
```bash
cd Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics && mkdir -p \
  Assessments Visuals \
  01_Vectors 02_Distance_and_Displacement 03_Average_Speed_and_Velocity \
  04_Acceleration 05_Motion_Graphs 06_Freefall \
  07_Vertical_Projectiles 08_Horizontal_Projectile_Motion 09_Projectiles_at_an_Angle
```
Expected: 9 lesson folders + Assessments + Visuals exist.

- [ ] **Step 4: Copy source MD into refactor folder**

Run:
```bash
cp "Physics/NEW East Meadow Physics Scope and Sequence.md" \
   Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/Scope_and_Sequence.md
```
Expected: `Scope_and_Sequence.md` is present.

- [ ] **Step 5: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor
git commit -m "feat: scaffold Physics refactor folder skeleton with stub units"
```

## Task A5: Brand tokens — `brand.css`

**Files:**
- Create: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/_assets/brand/brand.css`

- [ ] **Step 1: Write brand.css**

Write the file with exactly:

```css
/*
 * VSCHSD × East Meadow co-branding tokens.
 * Source: public CSS inspection of vschsd.org and emufsd.us, 2026-05-08.
 * Update here only — referenced by every HTML lesson page.
 */
:root {
  --em-purple: #662e80;
  --em-orange: #f37366;
  --vs-blue: #2ea3f2;
  --ink: #1a1a1a;
  --paper: #ffffff;
  --rule: #e6e6e6;
  --tint-curated: #f5f2fb;     /* light purple background for Curated Resources box */

  --font-body: Inter, "Open Sans", system-ui, -apple-system, sans-serif;
  --font-display: Inter, system-ui, sans-serif;

  --radius: 6px;
  --max-content-width: 72ch;
}

body {
  font-family: var(--font-body);
  color: var(--ink);
  background: var(--paper);
  line-height: 1.5;
  margin: 0;
}

h1, h2, h3 {
  font-family: var(--font-display);
  color: var(--em-purple);
  font-weight: 700;
}

a { color: var(--vs-blue); }

.curated-resources {
  background: var(--tint-curated);
  border-left: 4px solid var(--em-purple);
  padding: 1rem 1.25rem;
  border-radius: var(--radius);
  margin: 1.5rem 0;
}

.brand-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  border-bottom: 1px solid var(--rule);
  padding: 0.75rem 0;
}

.brand-header img { height: 40px; width: auto; }

.brand-header .divider {
  width: 1px;
  height: 32px;
  background: var(--rule);
}

.brand-header .district-name {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--ink);
}

.strategy-chip {
  display: inline-block;
  padding: 2px 8px;
  border-radius: 999px;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-right: 4px;
  background: var(--vs-blue);
  color: white;
  font-weight: 600;
}

.strategy-chip.hochman      { background: var(--em-purple); }
.strategy-chip.active       { background: var(--vs-blue); }
.strategy-chip.btc          { background: #2a7f4f; }
.strategy-chip.circle       { background: var(--em-orange); }

.warning {
  border-left: 4px solid var(--em-orange);
  background: #fff4f1;
  padding: 0.5rem 0.75rem;
  border-radius: var(--radius);
}

@media print {
  .interactive, .controls, button { display: none !important; }
  .noscript-storyboard { display: block !important; }
}
```

- [ ] **Step 2: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/_assets/brand/brand.css
git commit -m "feat: add VSCHSD x East Meadow co-branding tokens"
```

## Task A6: Placeholder logos

**Files:**
- Create: `_assets/brand/em_logo.svg`, `vs_logo.svg`

- [ ] **Step 1: Write em_logo.svg placeholder**

Write `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/_assets/brand/em_logo.svg`:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 40" role="img" aria-label="East Meadow Schools placeholder logo">
  <rect width="160" height="40" rx="6" fill="#662e80"/>
  <text x="80" y="25" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-weight="700" font-size="14">East Meadow</text>
</svg>
```

- [ ] **Step 2: Write vs_logo.svg placeholder**

Write `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/_assets/brand/vs_logo.svg`:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 40" role="img" aria-label="Valley Stream Central HSD placeholder logo">
  <rect width="200" height="40" rx="6" fill="#2ea3f2"/>
  <text x="100" y="25" text-anchor="middle" fill="white" font-family="Inter, sans-serif" font-weight="700" font-size="14">Valley Stream Central</text>
</svg>
```

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/_assets/brand/em_logo.svg \
        Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/_assets/brand/vs_logo.svg
git commit -m "feat: add placeholder VSCHSD and East Meadow logos"
```

## Task A7: Pandoc reference DOCX

**Files:**
- Create: `tools/make_reference_docx.py`
- Create (output): `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/_assets/brand/reference.docx`

- [ ] **Step 1: Write `tools/make_reference_docx.py`**

```python
"""Generate Pandoc reference DOCX with co-branded styles.

Run once whenever brand tokens change:
    source .venv/bin/activate && python tools/make_reference_docx.py
"""
from pathlib import Path
from docx import Document
from docx.shared import Pt, RGBColor, Inches

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "Publisher_Ready_Curriculum" / "01_Physics_East_Meadow_Refactor" / "_assets" / "brand" / "reference.docx"

EM_PURPLE = RGBColor(0x66, 0x2E, 0x80)
VS_BLUE = RGBColor(0x2E, 0xA3, 0xF2)
INK = RGBColor(0x1A, 0x1A, 0x1A)


def main() -> None:
    doc = Document()

    # Body / Normal
    normal = doc.styles["Normal"]
    normal.font.name = "Inter"
    normal.font.size = Pt(11)
    normal.font.color.rgb = INK

    # Headings
    for level, size in [(1, 22), (2, 16), (3, 13)]:
        style = doc.styles[f"Heading {level}"]
        style.font.name = "Inter"
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.color.rgb = EM_PURPLE

    # Hyperlink color via Body Text approximation: most teachers won't see it,
    # but Pandoc respects the Hyperlink character style if present.
    if "Hyperlink" in [s.name for s in doc.styles]:
        doc.styles["Hyperlink"].font.color.rgb = VS_BLUE

    # Page margins
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)

    # Insert a styled paragraph so Pandoc has a sample of every style applied
    doc.add_heading("Co-branded reference", level=1)
    doc.add_heading("Subheading", level=2)
    doc.add_paragraph("Body text sample.").style = normal

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(OUT)
    print(f"Wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run the script**

Run: `source .venv/bin/activate && python tools/make_reference_docx.py`
Expected: prints `Wrote Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/_assets/brand/reference.docx`.

- [ ] **Step 3: Verify the DOCX opens in Word/Preview without errors**

Run: `open Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/_assets/brand/reference.docx`
Expected: Opens in Word/Preview showing the styled headings.

- [ ] **Step 4: Commit**

```bash
git add tools/make_reference_docx.py \
        Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/_assets/brand/reference.docx
git commit -m "feat: generate Pandoc reference DOCX with co-branded styles"
```

## Task A8: Shared lesson assets — `lesson.css`

**Files:**
- Create: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/_assets/lesson.css`

- [ ] **Step 1: Write lesson.css**

```css
/* Lesson-page layout primitives. Imports brand.css. */
@import url("./brand/brand.css");

.lesson-shell {
  max-width: var(--max-content-width);
  margin: 2rem auto;
  padding: 0 1rem;
}

.lesson-section {
  margin: 2.5rem 0;
}

.notice-wonder, .initial-model, .revise-model {
  border: 2px dashed var(--rule);
  border-radius: var(--radius);
  padding: 1rem;
  background: #fafafa;
}

.turn-and-talk {
  border-left: 4px solid var(--vs-blue);
  background: #f0f9ff;
  padding: 0.75rem 1rem;
  border-radius: var(--radius);
  margin: 1.25rem 0;
}

.turn-and-talk::before {
  content: "Turn and Talk · ";
  font-weight: 700;
  color: var(--vs-blue);
}

.exit-ticket {
  border: 2px solid var(--em-purple);
  border-radius: var(--radius);
  padding: 1rem;
  margin: 1.5rem 0;
}

.vocab-box {
  background: #fff8f0;
  border-radius: var(--radius);
  padding: 0.75rem 1rem;
}

.controls {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin: 1rem 0;
}

.controls label {
  font-size: 0.875rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

.controls input[type="range"] { flex: 1; }

.readout {
  font-variant-numeric: tabular-nums;
  font-weight: 600;
  color: var(--em-purple);
}

.noscript-storyboard {
  display: none;
}

.noscript .noscript-storyboard,
noscript .noscript-storyboard {
  display: block;
}
```

- [ ] **Step 2: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/_assets/lesson.css
git commit -m "feat: add shared lesson page layout CSS"
```

## Task A9: Shared lesson JS — `lesson.js`

**Files:**
- Create: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/_assets/lesson.js`

- [ ] **Step 1: Write lesson.js**

```javascript
/* Lesson interactive helpers. Lessons may inline additional logic. */

/**
 * Bind a slider input to a target element's text content via a formatter.
 * @param {string} sliderId
 * @param {string} readoutId
 * @param {(value: number) => string} formatter
 * @returns {HTMLInputElement | null}
 */
export function bindSlider(sliderId, readoutId, formatter) {
  const slider = document.getElementById(sliderId);
  const readout = document.getElementById(readoutId);
  if (!slider || !readout) return null;
  const update = () => { readout.textContent = formatter(parseFloat(slider.value)); };
  slider.addEventListener("input", update);
  update();
  return slider;
}

/** Helper for SVG element creation with attributes. */
export function svgEl(tag, attrs = {}) {
  const el = document.createElementNS("http://www.w3.org/2000/svg", tag);
  for (const [k, v] of Object.entries(attrs)) el.setAttribute(k, String(v));
  return el;
}

/** Reveal a hidden hint element. */
export function revealHint(hintId) {
  const el = document.getElementById(hintId);
  if (el) el.hidden = false;
}
```

- [ ] **Step 2: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/_assets/lesson.js
git commit -m "feat: add shared lesson JS helpers"
```

## Task A10: Lesson schema — `lesson_schema.yaml`

**Files:**
- Create: `tools/lesson_schema.yaml`

- [ ] **Step 1: Write the schema**

```yaml
# Single source of truth for lesson structure rules.
# Both tools/scaffold_lesson.py and tools/validators.py read this.

teacher_guide_required_headings:
  - "Cover"
  - "Curated Resources (from East Meadow Scope & Sequence)"
  - "CCC Focus"
  - "NYSSLS Observation Checklist Crosswalk"
  - "Opening Connection"
  - "At-a-Glance"
  - "Lesson Objectives"
  - "Agenda"
  - "Discussion Prompts"
  - "Common Misconceptions"
  - "Access & Differentiation"
  - "Strategy Spotlight"
  - "Exit Ticket + Closing Reflection"
  - "Companion Materials"

curated_resources_required_subheadings:
  - "NYSSLS Standards"
  - "Phenomenon"
  - "Javalab / Labs"
  - "Assessments"

answer_key_required_headings:
  - "Cover"
  - "Make-It-Make-Sense Answers"
  - "Exit Ticket Answer"
  - "Closing Reflection (rubric)"

unit_plan_required_headings:
  - "Cover"
  - "Unit Scope (from East Meadow Scope & Sequence)"
  - "Pacing Calendar"
  - "Strategy Rotation"
  - "NYSSLS Coverage Matrix"
  - "Vocabulary Scope"

student_html_required_data_sections:
  - "phenomenon"
  - "driving-question"
  - "notice-wonder"
  - "initial-model"
  - "interactive"
  - "make-it-make-sense"
  - "vocab"
  - "revise-model"
  - "return-to-phenomenon"
  - "exit-ticket"
  - "explore-further"

vocab_max: 3

forbidden_in_onenote_html:
  - "<script"
  - "<iframe"
  - "<link rel=\"stylesheet\""

strategy_chip_values:
  - "HOCHMAN"
  - "ACTIVE LEARNING"
  - "BTC"
  - "RESTORATIVE CIRCLE"
```

- [ ] **Step 2: Commit**

```bash
git add tools/lesson_schema.yaml
git commit -m "feat: define lesson schema as single source of truth"
```

## Task A11: Validators — failing tests first

**Files:**
- Create: `tests/tools/__init__.py` (empty)
- Create: `tests/tools/conftest.py`
- Create: `tests/tools/test_validators.py`

- [ ] **Step 1: Write conftest.py**

```python
"""Shared pytest fixtures for tools tests."""
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = Path(__file__).resolve().parent / "fixtures"


@pytest.fixture
def fixtures_dir() -> Path:
    return FIXTURES


@pytest.fixture
def schema_path() -> Path:
    return ROOT / "tools" / "lesson_schema.yaml"
```

- [ ] **Step 2: Write the failing tests**

Write `tests/tools/test_validators.py`:

```python
"""Tests for tools.validators — lesson structure validation."""
from pathlib import Path
import pytest
from tools.validators import (
    validate_teacher_guide,
    validate_answer_key,
    validate_student_html,
    validate_onenote_html,
    ValidationError,
)


def test_teacher_guide_passes_with_all_required_headings(tmp_path: Path, schema_path: Path):
    headings = [
        "Cover", "Curated Resources (from East Meadow Scope & Sequence)",
        "CCC Focus", "NYSSLS Observation Checklist Crosswalk",
        "Opening Connection", "At-a-Glance", "Lesson Objectives", "Agenda",
        "Discussion Prompts", "Common Misconceptions",
        "Access & Differentiation", "Strategy Spotlight",
        "Exit Ticket + Closing Reflection", "Companion Materials",
    ]
    sub_headings = "\n\n".join([
        "### NYSSLS Standards\nHS-PS2-1.",
        "### Phenomenon\nA phenomenon link.",
        "### Javalab / Labs\n- Lab A",
        "### Assessments\n- Assessment A",
    ])
    body_parts = []
    for h in headings:
        body_parts.append(f"## {h}\n")
        if h == "Curated Resources (from East Meadow Scope & Sequence)":
            body_parts.append(sub_headings + "\n")
    body_parts.append("\n## Key Vocabulary (max 3)\n- term1\n- term2\n")
    file = tmp_path / "Teacher_Guide.md"
    file.write_text("\n".join(body_parts), encoding="utf-8")

    validate_teacher_guide(file, schema_path)


def test_teacher_guide_fails_when_section_missing(tmp_path: Path, schema_path: Path):
    file = tmp_path / "Teacher_Guide.md"
    file.write_text("## Cover\n## Agenda\n", encoding="utf-8")
    with pytest.raises(ValidationError, match="missing required heading"):
        validate_teacher_guide(file, schema_path)


def test_teacher_guide_fails_when_curated_subheading_missing(tmp_path: Path, schema_path: Path):
    body = []
    for h in [
        "Cover", "Curated Resources (from East Meadow Scope & Sequence)",
        "CCC Focus", "NYSSLS Observation Checklist Crosswalk",
        "Opening Connection", "At-a-Glance", "Lesson Objectives", "Agenda",
        "Discussion Prompts", "Common Misconceptions",
        "Access & Differentiation", "Strategy Spotlight",
        "Exit Ticket + Closing Reflection", "Companion Materials",
    ]:
        body.append(f"## {h}\n")
        if h.startswith("Curated"):
            # Only NYSSLS, missing the others
            body.append("### NYSSLS Standards\nHS-PS2-1.\n")
    file = tmp_path / "Teacher_Guide.md"
    file.write_text("\n".join(body), encoding="utf-8")
    with pytest.raises(ValidationError, match="Curated Resources missing sub-heading"):
        validate_teacher_guide(file, schema_path)


def test_teacher_guide_fails_when_vocab_exceeds_three(tmp_path: Path, schema_path: Path):
    headings = [
        "Cover", "Curated Resources (from East Meadow Scope & Sequence)",
        "CCC Focus", "NYSSLS Observation Checklist Crosswalk",
        "Opening Connection", "At-a-Glance", "Lesson Objectives", "Agenda",
        "Discussion Prompts", "Common Misconceptions",
        "Access & Differentiation", "Strategy Spotlight",
        "Exit Ticket + Closing Reflection", "Companion Materials",
    ]
    sub = "\n".join([
        "### NYSSLS Standards\nHS-PS2-1.",
        "### Phenomenon\nLink",
        "### Javalab / Labs\n- A",
        "### Assessments\n- A",
    ])
    body = []
    for h in headings:
        body.append(f"## {h}\n")
        if h.startswith("Curated"):
            body.append(sub + "\n")
    body.append("\n## Key Vocabulary (max 3)\n- a\n- b\n- c\n- d\n")
    file = tmp_path / "Teacher_Guide.md"
    file.write_text("\n".join(body), encoding="utf-8")
    with pytest.raises(ValidationError, match="vocab exceeds"):
        validate_teacher_guide(file, schema_path)


def test_student_html_fails_when_interactive_missing_noscript(tmp_path: Path, schema_path: Path):
    html = """<html><body>
    <header class="brand-header"></header>
    <section data-section="phenomenon"></section>
    <section data-section="driving-question"></section>
    <section data-section="notice-wonder"></section>
    <section data-section="initial-model"></section>
    <section data-section="interactive">
      <div data-interactive="true"><svg></svg><script>console.log("x");</script></div>
    </section>
    <section data-section="make-it-make-sense"></section>
    <section data-section="vocab"></section>
    <section data-section="revise-model"></section>
    <section data-section="return-to-phenomenon"></section>
    <section data-section="exit-ticket"></section>
    <section data-section="explore-further"></section>
    </body></html>"""
    file = tmp_path / "Student_Exploration.html"
    file.write_text(html, encoding="utf-8")
    with pytest.raises(ValidationError, match="interactive widget missing.*noscript"):
        validate_student_html(file, schema_path)


def test_onenote_html_fails_when_script_present(tmp_path: Path, schema_path: Path):
    html = "<html><body><script>alert('x')</script></body></html>"
    file = tmp_path / "X.onenote.html"
    file.write_text(html, encoding="utf-8")
    with pytest.raises(ValidationError, match="forbidden tag"):
        validate_onenote_html(file, schema_path)


def test_onenote_html_passes_when_clean(tmp_path: Path, schema_path: Path):
    html = "<html><body><h1>Hi</h1><p>Plain content.</p></body></html>"
    file = tmp_path / "X.onenote.html"
    file.write_text(html, encoding="utf-8")
    validate_onenote_html(file, schema_path)


def test_answer_key_fails_when_section_missing(tmp_path: Path, schema_path: Path):
    file = tmp_path / "Answer_Key.md"
    file.write_text("## Cover\n", encoding="utf-8")
    with pytest.raises(ValidationError, match="missing required heading"):
        validate_answer_key(file, schema_path)
```

- [ ] **Step 3: Run tests — expect ImportError**

Run: `source .venv/bin/activate && python -m pytest tests/tools/test_validators.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'tools.validators'` (or similar — module not yet defined).

## Task A12: Validators — implementation

**Files:**
- Create: `tools/__init__.py` (empty)
- Create: `tools/validators.py`

- [ ] **Step 1: Create empty `tools/__init__.py`**

Run: `touch tools/__init__.py`

- [ ] **Step 2: Implement `tools/validators.py`**

```python
"""Validate lesson source files against lesson_schema.yaml."""
from __future__ import annotations
from pathlib import Path
import re
import yaml


class ValidationError(Exception):
    """Raised when a lesson source file fails schema validation."""


def _load_schema(schema_path: Path) -> dict:
    with open(schema_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _heading_levels(text: str) -> list[tuple[int, str]]:
    """Return [(level, text), ...] for ATX headings (e.g. ##, ###)."""
    out = []
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if m:
            out.append((len(m.group(1)), m.group(2)))
    return out


def _level_two_headings(text: str) -> list[str]:
    return [h for lvl, h in _heading_levels(text) if lvl == 2]


def _level_three_headings_after(text: str, h2: str) -> list[str]:
    """Return ### headings that fall under the given ## section, before the next ##."""
    out: list[str] = []
    in_section = False
    for level, heading in _heading_levels(text):
        if level == 2:
            if heading == h2:
                in_section = True
            elif in_section:
                break
        elif level == 3 and in_section:
            out.append(heading)
    return out


def _vocab_count(text: str) -> int:
    """Count bullet items under '## Key Vocabulary'."""
    in_vocab = False
    count = 0
    for line in text.splitlines():
        if re.match(r"^##\s+Key Vocabulary", line):
            in_vocab = True
            continue
        if in_vocab and re.match(r"^##\s+", line):
            break
        if in_vocab and re.match(r"^[-*]\s+\S", line):
            count += 1
    return count


def validate_teacher_guide(path: Path, schema_path: Path) -> None:
    schema = _load_schema(schema_path)
    text = path.read_text(encoding="utf-8")
    h2s = _level_two_headings(text)

    for required in schema["teacher_guide_required_headings"]:
        if required not in h2s:
            raise ValidationError(
                f"{path.name}: missing required heading '## {required}'"
            )

    curated_h2 = "Curated Resources (from East Meadow Scope & Sequence)"
    sub = _level_three_headings_after(text, curated_h2)
    for required_sub in schema["curated_resources_required_subheadings"]:
        if required_sub not in sub:
            raise ValidationError(
                f"{path.name}: Curated Resources missing sub-heading '### {required_sub}'"
            )

    vocab = _vocab_count(text)
    if vocab > schema["vocab_max"]:
        raise ValidationError(
            f"{path.name}: vocab exceeds {schema['vocab_max']} (found {vocab})"
        )


def validate_answer_key(path: Path, schema_path: Path) -> None:
    schema = _load_schema(schema_path)
    text = path.read_text(encoding="utf-8")
    h2s = _level_two_headings(text)
    for required in schema["answer_key_required_headings"]:
        if required not in h2s:
            raise ValidationError(
                f"{path.name}: missing required heading '## {required}'"
            )


def validate_unit_plan(path: Path, schema_path: Path) -> None:
    schema = _load_schema(schema_path)
    text = path.read_text(encoding="utf-8")
    h2s = _level_two_headings(text)
    for required in schema["unit_plan_required_headings"]:
        if required not in h2s:
            raise ValidationError(
                f"{path.name}: missing required heading '## {required}'"
            )


def validate_student_html(path: Path, schema_path: Path) -> None:
    """Validate the rich interactive HTML page."""
    from bs4 import BeautifulSoup
    schema = _load_schema(schema_path)
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")

    if not soup.select_one("header.brand-header"):
        raise ValidationError(f"{path.name}: missing co-branded header (.brand-header)")

    sections = {s.get("data-section") for s in soup.select("[data-section]")}
    for required in schema["student_html_required_data_sections"]:
        if required not in sections:
            raise ValidationError(
                f"{path.name}: missing data-section='{required}'"
            )

    for widget in soup.select('[data-interactive="true"]'):
        # The noscript fallback may be a sibling or descendant of the same
        # parent section.
        section = widget.find_parent("section") or widget.parent
        if section is None or not section.find("noscript"):
            raise ValidationError(
                f"{path.name}: interactive widget missing sibling <noscript> storyboard"
            )


def validate_onenote_html(path: Path, schema_path: Path) -> None:
    schema = _load_schema(schema_path)
    text = path.read_text(encoding="utf-8")
    for forbidden in schema["forbidden_in_onenote_html"]:
        if forbidden in text:
            raise ValidationError(
                f"{path.name}: forbidden tag '{forbidden}' present in OneNote HTML"
            )
```

- [ ] **Step 3: Run tests — expect all pass**

Run: `source .venv/bin/activate && python -m pytest tests/tools/test_validators.py -v`
Expected: All 8 tests pass.

- [ ] **Step 4: Commit**

```bash
git add tools/__init__.py tools/validators.py tests/tools/__init__.py tests/tools/conftest.py tests/tools/test_validators.py
git commit -m "feat(tools): add lesson schema validators with TDD"
```

## Task A13: Static-ifier — failing tests first

**Files:**
- Create: `tests/tools/test_static_ifier.py`
- Create: `tests/tools/fixtures/sample_interactive.html`

- [ ] **Step 1: Write fixture HTML**

Write `tests/tools/fixtures/sample_interactive.html`:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Sample Interactive</title>
  <link rel="stylesheet" href="../_assets/lesson.css">
  <style>.local { color: red; }</style>
</head>
<body>
  <header class="brand-header"><div>Header</div></header>
  <main>
    <section data-section="phenomenon">
      <iframe src="https://www.youtube.com/embed/abc123" title="Phenomenon video"></iframe>
    </section>
    <section data-section="interactive">
      <div data-interactive="true">
        <svg width="100" height="100"><circle cx="50" cy="50" r="20" fill="blue"/></svg>
        <script>console.log("alive");</script>
      </div>
      <noscript class="noscript-storyboard">
        <p>Storyboard frame 1: ...</p>
      </noscript>
    </section>
  </main>
  <script type="module" src="../_assets/lesson.js"></script>
</body>
</html>
```

- [ ] **Step 2: Write the failing tests**

Write `tests/tools/test_static_ifier.py`:

```python
"""Tests for tools.static_ifier — interactive HTML → OneNote-paste HTML."""
from pathlib import Path
from tools.static_ifier import staticify


def _process(fixtures_dir: Path) -> str:
    src = fixtures_dir / "sample_interactive.html"
    css_root = fixtures_dir.parent.parent.parent / "Publisher_Ready_Curriculum" / "01_Physics_East_Meadow_Refactor" / "_assets"
    return staticify(src.read_text(encoding="utf-8"), css_root=css_root)


def test_strips_script_tags(fixtures_dir: Path):
    out = _process(fixtures_dir)
    assert "<script" not in out


def test_strips_external_stylesheet_links(fixtures_dir: Path):
    out = _process(fixtures_dir)
    assert '<link rel="stylesheet"' not in out


def test_inlines_local_style_blocks(fixtures_dir: Path):
    out = _process(fixtures_dir)
    assert ".local { color: red; }" in out


def test_replaces_iframe_with_link_and_instruction(fixtures_dir: Path):
    out = _process(fixtures_dir)
    assert "<iframe" not in out
    assert "youtube.com/embed/abc123" in out or "youtube.com/watch?v=abc123" in out
    assert "Insert" in out and "Online Video" in out


def test_replaces_interactive_with_noscript_content(fixtures_dir: Path):
    out = _process(fixtures_dir)
    assert "Storyboard frame 1" in out
    assert "data-interactive" not in out


def test_keeps_brand_header(fixtures_dir: Path):
    out = _process(fixtures_dir)
    assert 'class="brand-header"' in out
```

- [ ] **Step 3: Run tests — expect ImportError**

Run: `source .venv/bin/activate && python -m pytest tests/tools/test_static_ifier.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'tools.static_ifier'`.

## Task A14: Static-ifier — implementation

**Files:**
- Create: `tools/static_ifier.py`

- [ ] **Step 1: Implement static_ifier.py**

```python
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
```

- [ ] **Step 2: Run tests — expect all pass**

Run: `source .venv/bin/activate && python -m pytest tests/tools/test_static_ifier.py -v`
Expected: All 6 tests pass.

- [ ] **Step 3: Commit**

```bash
git add tools/static_ifier.py tests/tools/fixtures/sample_interactive.html tests/tools/test_static_ifier.py
git commit -m "feat(tools): add interactive→OneNote static-ifier with TDD"
```

## Task A15: Pandoc runner — failing test first

**Files:**
- Create: `tests/tools/test_pandoc_runner.py`

- [ ] **Step 1: Write the test**

```python
"""Test that pandoc_runner produces docx and onenote.html from a markdown source."""
from pathlib import Path
from tools.pandoc_runner import md_to_docx, md_to_onenote_html


def test_md_to_docx_creates_file(tmp_path: Path):
    md = tmp_path / "x.md"
    md.write_text("# Hello\n\nBody.\n", encoding="utf-8")
    out = tmp_path / "x.docx"
    md_to_docx(md, out, reference_doc=None)
    assert out.exists()
    assert out.stat().st_size > 0


def test_md_to_onenote_html_self_contained(tmp_path: Path):
    md = tmp_path / "x.md"
    md.write_text("# Hello\n\nBody.\n", encoding="utf-8")
    out = tmp_path / "x.onenote.html"
    md_to_onenote_html(md, out)
    text = out.read_text(encoding="utf-8")
    assert "<h1" in text
    assert "Body" in text
    assert "<script" not in text
    assert "<iframe" not in text
```

- [ ] **Step 2: Run — expect ImportError**

Run: `source .venv/bin/activate && python -m pytest tests/tools/test_pandoc_runner.py -v`
Expected: FAIL with module not found.

## Task A16: Pandoc runner — implementation

**Files:**
- Create: `tools/pandoc_runner.py`

- [ ] **Step 1: Implement pandoc_runner.py**

```python
"""Thin subprocess wrapper around Pandoc for our two output formats."""
from __future__ import annotations
import subprocess
from pathlib import Path


def md_to_docx(src: Path, out: Path, reference_doc: Path | None) -> None:
    cmd = ["pandoc", str(src), "-o", str(out)]
    if reference_doc and reference_doc.is_file():
        cmd += [f"--reference-doc={reference_doc}"]
    subprocess.run(cmd, check=True)


def md_to_onenote_html(src: Path, out: Path) -> None:
    cmd = [
        "pandoc",
        str(src),
        "-o",
        str(out),
        "--standalone",
        "--embed-resources",   # Pandoc 3.x replacement for --self-contained
        "--no-highlight",
    ]
    subprocess.run(cmd, check=True)
```

- [ ] **Step 2: Run tests**

Run: `source .venv/bin/activate && python -m pytest tests/tools/test_pandoc_runner.py -v`
Expected: Both tests pass (requires Pandoc installed from Task A1).

- [ ] **Step 3: Commit**

```bash
git add tools/pandoc_runner.py tests/tools/test_pandoc_runner.py
git commit -m "feat(tools): wrap pandoc for docx and onenote.html outputs"
```

## Task A17: Templates for scaffolding

**Files:**
- Create: `tools/templates/student_exploration.html.tmpl`
- Create: `tools/templates/teacher_guide.md.tmpl`
- Create: `tools/templates/answer_key.md.tmpl`
- Create: `tools/templates/unit_plan.md.tmpl`

- [ ] **Step 1: Write `tools/templates/student_exploration.html.tmpl`**

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{{LESSON_TITLE}} — Unit: {{UNIT_NAME}}</title>
  <link rel="stylesheet" href="../../_assets/lesson.css">
</head>
<body>
<div class="lesson-shell">

<header class="brand-header">
  <img src="../../_assets/brand/em_logo.svg" alt="East Meadow Schools">
  <div class="divider"></div>
  <img src="../../_assets/brand/vs_logo.svg" alt="Valley Stream Central HSD">
  <div>
    <div class="district-name">East Meadow Schools × Valley Stream Central HSD</div>
    <h1>Unit: {{UNIT_NAME}} — Lesson {{LESSON_NUMBER}}: {{LESSON_TITLE}}</h1>
    <div>{{STRATEGY_CHIPS}}</div>
  </div>
</header>

<section class="lesson-section" data-section="phenomenon">
  <h2>Phenomenon</h2>
  <p>{{PHENOMENON_DESCRIPTION}}</p>
</section>

<section class="lesson-section" data-section="driving-question">
  <h2>Driving Question</h2>
  <p><strong>{{DRIVING_QUESTION}}</strong></p>
</section>

<section class="lesson-section notice-wonder" data-section="notice-wonder">
  <h2>Notice &amp; Wonder</h2>
  <p>List two things you notice and two things you wonder.</p>
  <textarea rows="6" placeholder="What I notice / What I wonder…"></textarea>
</section>

<aside class="turn-and-talk">{{TURN_AND_TALK_1}}</aside>

<section class="lesson-section initial-model" data-section="initial-model">
  <h2>Initial Model</h2>
  <p>Sketch your first explanation of the phenomenon.</p>
</section>

<section class="lesson-section" data-section="interactive">
  <h2>Investigate</h2>
  <div data-interactive="true">
    <!-- Author the live SVG/JS interactive here. -->
    {{INTERACTIVE_PLACEHOLDER}}
  </div>
  <noscript class="noscript-storyboard">
    <!-- Author 3-5 storyboard frames here. -->
    {{STORYBOARD_PLACEHOLDER}}
  </noscript>
</section>

<aside class="turn-and-talk">{{TURN_AND_TALK_2}}</aside>

<section class="lesson-section" data-section="make-it-make-sense">
  <h2>Make It Make Sense</h2>
  <ol>
    <li>{{MIMS_Q1}}</li>
    <li>{{MIMS_Q2}}</li>
    <li>{{MIMS_Q3}}</li>
  </ol>
</section>

<section class="lesson-section vocab-box" data-section="vocab">
  <h2>Key Vocabulary (max 3)</h2>
  <ul>
    <li>{{VOCAB_1}}</li>
    <li>{{VOCAB_2}}</li>
    <li>{{VOCAB_3}}</li>
  </ul>
</section>

<section class="lesson-section revise-model" data-section="revise-model">
  <h2>Revise Your Model</h2>
  <p>Based on what we just learned, update your initial model.</p>
</section>

<section class="lesson-section" data-section="return-to-phenomenon">
  <h2>Return to the Phenomenon</h2>
  <p>{{RETURN_PROMPT}}</p>
</section>

<section class="lesson-section exit-ticket" data-section="exit-ticket">
  <h2>Exit Ticket + Closing Reflection</h2>
  <ol>
    <li>{{EXIT_Q}}</li>
    <li><em>Reflection:</em> What is one thing that surprised you today? Who helped you make sense of something?</li>
  </ol>
</section>

<section class="lesson-section" data-section="explore-further">
  <h2>Explore Further</h2>
  <ul>
    {{CURATED_LINKS}}
  </ul>
</section>

<footer>
  <p style="font-size:.8rem;color:#666;">Learning, Achieving, Succeeding! · {{LESSON_ID}}</p>
</footer>

</div>
</body>
</html>
```

- [ ] **Step 2: Write `tools/templates/teacher_guide.md.tmpl`**

```markdown
# {{LESSON_TITLE}} — Teacher Guide

## Cover

**Unit: {{UNIT_NAME}} — Lesson {{LESSON_NUMBER}}: {{LESSON_TITLE}}**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: {{STRATEGY_CHIPS}}

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

{{NYSSLS_VERBATIM}}

### Phenomenon

{{PHENOMENON_VERBATIM}}

### Javalab / Labs

{{LABS_VERBATIM}}

### Assessments

{{ASSESSMENTS_VERBATIM}}

## CCC Focus

{{CCC_FOCUS}}

## NYSSLS Observation Checklist Crosswalk

| # | Item | Where it shows up in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phenomenon section |
| 2 | Turn and Talk (2–3×) | Two callouts at notice-wonder and post-investigation |
| 3 | Students develop questions/models/procedures | Initial Model + Revise Your Model blocks |
| 4 | CCC defined and used | CCC Focus (above); restated in agenda step 2 |
| 5 | ENL — ≤3 vocab, second half | Key Vocabulary section, post-investigation |
| 6 | Revisit phenomenon with evidence | Return to the Phenomenon section |
| 7 | ENL/SPED supports | Access & Differentiation section |
| 8 | Assessment check | Exit Ticket + Closing Reflection |

## Opening Connection

Pick one (SEL):
- 1-question check-in (e.g., "On a scale of 1–5, how's your week going?")
- "Name something you noticed since last class"
- Quick gratitude / effort acknowledgment

## At-a-Glance

- **Duration:** 42 minutes (1 period)
- **Materials:** {{MATERIALS}}
- **Safety:** {{SAFETY}}
- **Prior knowledge:** {{PRIOR_KNOWLEDGE}}

## Lesson Objectives

{{OBJECTIVES}}

## Agenda

| Time | Block | Notes |
|---|---|---|
{{AGENDA_ROWS}}

## Discussion Prompts

{{DISCUSSION_PROMPTS}}

## Common Misconceptions

{{MISCONCEPTIONS}}

## Access & Differentiation

- **ELL/ENL supports:** {{ELL_SUPPORTS}}
- **IEP/SPED supports:** {{SPED_SUPPORTS}}
- **Extensions:** {{EXTENSIONS}}

## Strategy Spotlight

{{STRATEGY_SPOTLIGHT}}

## Exit Ticket + Closing Reflection

{{EXIT_TICKET}}

## Companion Materials

- `Student_Exploration.html` (rich interactive)
- `Student_Exploration.onenote.html` (OneNote-paste static)
- `Answer_Key.docx`

## Key Vocabulary (max 3)

- {{VOCAB_1}}
- {{VOCAB_2}}
- {{VOCAB_3}}
```

- [ ] **Step 3: Write `tools/templates/answer_key.md.tmpl`**

```markdown
# {{LESSON_TITLE}} — Answer Key

## Cover

Unit: {{UNIT_NAME}} — Lesson {{LESSON_NUMBER}}: {{LESSON_TITLE}}
East Meadow Schools × Valley Stream Central HSD

## Make-It-Make-Sense Answers

{{MIMS_ANSWERS}}

## Exit Ticket Answer

{{EXIT_TICKET_ANSWER}}

## Closing Reflection (rubric)

Closing reflection is formative, not graded. Award full credit for any honest response. Look for:
- Surprise / interest signal in answer 1
- Naming a peer or self-acknowledgment in answer 2
```

- [ ] **Step 4: Write `tools/templates/unit_plan.md.tmpl`**

```markdown
# Unit: {{UNIT_NAME}} — Unit Plan

## Cover

East Meadow Schools × Valley Stream Central High School District
Unit: {{UNIT_NAME}}

## Unit Scope (from East Meadow Scope & Sequence)

The verbatim unit table from `Scope_and_Sequence.md`:

{{UNIT_TABLE_VERBATIM}}

## Pacing Calendar

{{PACING_CALENDAR}}

## Strategy Rotation

| Lesson | Strategy chips |
|---|---|
{{STRATEGY_ROTATION_ROWS}}

## NYSSLS Coverage Matrix

{{NYSSLS_MATRIX}}

## Vocabulary Scope

3 terms per lesson. Aggregated for the unit:

{{VOCAB_AGGREGATE}}
```

- [ ] **Step 5: Commit**

```bash
git add tools/templates/
git commit -m "feat(tools): add lesson scaffolding templates"
```

## Task A18: Scaffold script — failing test

**Files:**
- Create: `tests/tools/test_scaffold_lesson.py`

- [ ] **Step 1: Write the test**

```python
"""Test scaffold_lesson creates a new lesson folder with required files."""
from pathlib import Path
from tools.scaffold_lesson import scaffold_lesson


def test_scaffold_creates_three_files(tmp_path: Path):
    out = tmp_path / "01_Vectors"
    scaffold_lesson(
        out_dir=out,
        unit_name="Kinematics",
        lesson_number="01",
        lesson_title="Vectors",
        strategy_chips=["RESTORATIVE CIRCLE", "ACTIVE LEARNING"],
    )
    assert (out / "Student_Exploration.html").is_file()
    assert (out / "Teacher_Guide.md").is_file()
    assert (out / "Answer_Key.md").is_file()


def test_scaffold_substitutes_placeholders(tmp_path: Path):
    out = tmp_path / "01_Vectors"
    scaffold_lesson(
        out_dir=out,
        unit_name="Kinematics",
        lesson_number="01",
        lesson_title="Vectors",
        strategy_chips=["HOCHMAN"],
    )
    text = (out / "Teacher_Guide.md").read_text(encoding="utf-8")
    assert "{{LESSON_TITLE}}" not in text
    assert "Vectors" in text
    assert "Kinematics" in text
    assert "HOCHMAN" in text


def test_scaffold_html_has_required_data_sections(tmp_path: Path):
    out = tmp_path / "01_Vectors"
    scaffold_lesson(
        out_dir=out,
        unit_name="Kinematics",
        lesson_number="01",
        lesson_title="Vectors",
        strategy_chips=[],
    )
    html = (out / "Student_Exploration.html").read_text(encoding="utf-8")
    for section in ["phenomenon", "interactive", "vocab", "exit-ticket", "explore-further"]:
        assert f'data-section="{section}"' in html
```

- [ ] **Step 2: Run — expect ImportError**

Run: `source .venv/bin/activate && python -m pytest tests/tools/test_scaffold_lesson.py -v`
Expected: FAIL with module not found.

## Task A19: Scaffold script — implementation

**Files:**
- Create: `tools/scaffold_lesson.py`

- [ ] **Step 1: Write scaffold_lesson.py**

```python
"""Scaffold a new lesson folder from templates.

Usage:
    python tools/scaffold_lesson.py 01_Kinematics 03 "Average Speed and Velocity" \
        --strategies "Hochman:sentence-expansion"
"""
from __future__ import annotations
import argparse
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = Path(__file__).resolve().parent / "templates"


def _render_chips(chips: Sequence[str]) -> str:
    if not chips:
        return ""
    out = []
    for chip in chips:
        kind = chip.split(":", 1)[0].lower().replace(" ", "-")
        cls = {
            "hochman": "hochman",
            "active-learning": "active",
            "btc": "btc",
            "restorative-circle": "circle",
        }.get(kind, "")
        out.append(f'<span class="strategy-chip {cls}">{chip.upper()}</span>')
    return " ".join(out)


def _render(template_text: str, mapping: dict[str, str]) -> str:
    out = template_text
    for k, v in mapping.items():
        out = out.replace(f"{{{{{k}}}}}", v)
    return out


def scaffold_lesson(
    *,
    out_dir: Path,
    unit_name: str,
    lesson_number: str,
    lesson_title: str,
    strategy_chips: Sequence[str],
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    chip_html = _render_chips(strategy_chips)
    chip_md = ", ".join(c.upper() for c in strategy_chips) if strategy_chips else "(none)"

    common = {
        "UNIT_NAME": unit_name,
        "LESSON_NUMBER": lesson_number,
        "LESSON_TITLE": lesson_title,
        "STRATEGY_CHIPS": chip_html,
        "LESSON_ID": f"{unit_name.lower()}-{lesson_number}",
        "PHENOMENON_DESCRIPTION": "[Author the phenomenon framing here.]",
        "DRIVING_QUESTION": "[Author the driving question here.]",
        "TURN_AND_TALK_1": "[Author Turn and Talk #1 prompt here.]",
        "TURN_AND_TALK_2": "[Author Turn and Talk #2 prompt here.]",
        "INTERACTIVE_PLACEHOLDER": "<!-- Author the live SVG/JS interactive here. -->",
        "STORYBOARD_PLACEHOLDER": "<p>Storyboard frame 1: [describe]</p><p>Storyboard frame 2: [describe]</p><p>Storyboard frame 3: [describe]</p>",
        "MIMS_Q1": "[Question 1]",
        "MIMS_Q2": "[Question 2]",
        "MIMS_Q3": "[Question 3]",
        "VOCAB_1": "[term 1]",
        "VOCAB_2": "[term 2]",
        "VOCAB_3": "[term 3]",
        "RETURN_PROMPT": "[Re-pose the original phenomenon. Ask students to use evidence from today.]",
        "EXIT_Q": "[Exit ticket question]",
        "CURATED_LINKS": "<li>[Link from MD row]</li>",
    }
    teacher_extra = {
        **common,
        "STRATEGY_CHIPS": chip_md,
        "NYSSLS_VERBATIM": "[Paste verbatim from Scope_and_Sequence.md, including the bold performance expectation and (parenthesized CCC).]",
        "PHENOMENON_VERBATIM": "[Paste the teacher-curated phenomenon and link from the MD row.]",
        "LABS_VERBATIM": "[Paste the teacher-curated lab links from the MD row, in MD order.]",
        "ASSESSMENTS_VERBATIM": "[Paste the teacher-curated assessment links from the MD row, in MD order.]",
        "CCC_FOCUS": "[One-line CCC focus.]",
        "MATERIALS": "[Materials list.]",
        "SAFETY": "[Safety notes or 'None'.]",
        "PRIOR_KNOWLEDGE": "[Prior knowledge bullets.]",
        "OBJECTIVES": "[I can… statements.]",
        "AGENDA_ROWS": "| 0–3 | Opening Connection (SEL) | … |\n| 3–7 | Phenomenon hook | … |\n| 7–12 | Notice & Wonder + Turn and Talk #1 | … |",
        "DISCUSSION_PROMPTS": "- [Prompt 1]\n- [Prompt 2]",
        "MISCONCEPTIONS": "- [Misconception → correction]",
        "ELL_SUPPORTS": "[Sentence frames, word-choice boxes, bilingual glossary.]",
        "SPED_SUPPORTS": "[Chunked tasks, graphic organizer.]",
        "EXTENSIONS": "[Extension prompt.]",
        "STRATEGY_SPOTLIGHT": "(none)" if not strategy_chips else "[Describe the specific Hochman/Active/BTC/Circle move and how to facilitate it.]",
        "EXIT_TICKET": "[Exit ticket prompt; new transfer phenomenon optional.]",
    }
    answer_extra = {
        **common,
        "MIMS_ANSWERS": "1. [Answer 1] · *Rubric:* … · NYSSLS: HS-PS2-1\n2. [Answer 2] · *Rubric:* … · NYSSLS: HS-PS2-1\n3. [Answer 3] · *Rubric:* … · NYSSLS: HS-PS2-1",
        "EXIT_TICKET_ANSWER": "[Expected answer + tolerance/rubric + NYSSLS tag.]",
    }

    (out_dir / "Student_Exploration.html").write_text(
        _render((TEMPLATES / "student_exploration.html.tmpl").read_text(encoding="utf-8"), common),
        encoding="utf-8",
    )
    (out_dir / "Teacher_Guide.md").write_text(
        _render((TEMPLATES / "teacher_guide.md.tmpl").read_text(encoding="utf-8"), teacher_extra),
        encoding="utf-8",
    )
    (out_dir / "Answer_Key.md").write_text(
        _render((TEMPLATES / "answer_key.md.tmpl").read_text(encoding="utf-8"), answer_extra),
        encoding="utf-8",
    )


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("unit_dir", help="Unit folder, e.g. 01_Kinematics")
    p.add_argument("lesson_number", help="Two-digit lesson number, e.g. 03")
    p.add_argument("lesson_title", help='Lesson title, e.g. "Average Speed and Velocity"')
    p.add_argument("--strategies", default="", help="Comma-separated strategy chips")
    args = p.parse_args()

    chips = [c.strip() for c in args.strategies.split(",") if c.strip()]
    unit_path = ROOT / "Publisher_Ready_Curriculum" / "01_Physics_East_Meadow_Refactor" / args.unit_dir
    slug = args.lesson_title.replace(" ", "_").replace("/", "_")
    lesson_dir = unit_path / f"{args.lesson_number}_{slug}"
    unit_name = args.unit_dir.split("_", 1)[1].replace("_", " ")
    scaffold_lesson(
        out_dir=lesson_dir,
        unit_name=unit_name,
        lesson_number=args.lesson_number,
        lesson_title=args.lesson_title,
        strategy_chips=chips,
    )
    print(f"Scaffolded {lesson_dir.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run tests — expect pass**

Run: `source .venv/bin/activate && python -m pytest tests/tools/test_scaffold_lesson.py -v`
Expected: All 3 tests pass.

- [ ] **Step 3: Commit**

```bash
git add tools/scaffold_lesson.py tests/tools/test_scaffold_lesson.py
git commit -m "feat(tools): add scaffold_lesson with TDD"
```

## Task A20: Build orchestrator — failing test

**Files:**
- Create: `tests/tools/test_build_lessons.py`
- Create: `tests/tools/fixtures/valid_lesson/` (a passing fixture lesson)

- [ ] **Step 1: Create the valid_lesson fixture**

Run scaffold to create a fixture (then commit it):

```bash
source .venv/bin/activate && python -c "
from pathlib import Path
from tools.scaffold_lesson import scaffold_lesson
out = Path('tests/tools/fixtures/valid_lesson')
scaffold_lesson(
    out_dir=out, unit_name='Demo', lesson_number='01',
    lesson_title='Sample', strategy_chips=[]
)
"
```

Expected: directory `tests/tools/fixtures/valid_lesson/` now contains `Student_Exploration.html`, `Teacher_Guide.md`, `Answer_Key.md`.

- [ ] **Step 2: Verify the fixture validates as-is**

The scaffolded files include all required headings, sub-headings, and the interactive+noscript pair, so they should pass without modification. Confirm:

```bash
source .venv/bin/activate && python -c "
from pathlib import Path
from tools.validators import validate_teacher_guide, validate_answer_key, validate_student_html
base = Path('tests/tools/fixtures/valid_lesson')
schema = Path('tools/lesson_schema.yaml')
validate_teacher_guide(base / 'Teacher_Guide.md', schema)
validate_answer_key(base / 'Answer_Key.md', schema)
validate_student_html(base / 'Student_Exploration.html', schema)
print('OK')
"
```
Expected: prints `OK`. If any validator raises, fix the template (Task A17) — do not hand-edit the fixture, or it will drift from the scaffold output.

- [ ] **Step 3: Write the build test**

Write `tests/tools/test_build_lessons.py`:

```python
"""End-to-end build test on a fixture lesson."""
from pathlib import Path
import shutil
import pytest
from tools.build_lessons import build_lesson_folder


@pytest.fixture
def working_lesson(tmp_path: Path, fixtures_dir: Path) -> Path:
    src = fixtures_dir / "valid_lesson"
    dst = tmp_path / "01_Sample"
    shutil.copytree(src, dst)
    return dst


def test_build_produces_all_expected_artifacts(working_lesson: Path, schema_path: Path):
    build_lesson_folder(
        working_lesson,
        schema_path=schema_path,
        reference_doc=None,
        css_root=working_lesson.parent,
    )
    expected = [
        "Student_Exploration.html",
        "Student_Exploration.onenote.html",
        "Teacher_Guide.md",
        "Teacher_Guide.docx",
        "Teacher_Guide.onenote.html",
        "Answer_Key.md",
        "Answer_Key.docx",
        "Answer_Key.onenote.html",
    ]
    for name in expected:
        assert (working_lesson / name).exists(), f"missing {name}"


def test_build_fails_when_validator_rejects_lesson(working_lesson: Path, schema_path: Path):
    # Break the lesson by emptying the teacher guide
    (working_lesson / "Teacher_Guide.md").write_text("# broken\n", encoding="utf-8")
    with pytest.raises(Exception):
        build_lesson_folder(
            working_lesson, schema_path=schema_path,
            reference_doc=None, css_root=working_lesson.parent,
        )
```

- [ ] **Step 4: Run — expect ImportError**

Run: `source .venv/bin/activate && python -m pytest tests/tools/test_build_lessons.py -v`
Expected: FAIL with module not found.

## Task A21: Build orchestrator — implementation

**Files:**
- Create: `tools/build_lessons.py`

- [ ] **Step 1: Write build_lessons.py**

```python
"""Walk the unit tree and build all lesson artifacts.

Usage:
    python tools/build_lessons.py                              # build everything
    python tools/build_lessons.py 01_Kinematics                # one unit
    python tools/build_lessons.py 01_Kinematics/01_Vectors     # one lesson
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path
from tools.pandoc_runner import md_to_docx, md_to_onenote_html
from tools.static_ifier import staticify
from tools.validators import (
    validate_teacher_guide, validate_answer_key, validate_student_html,
    validate_onenote_html, validate_unit_plan, ValidationError,
)

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REFACTOR = ROOT / "Publisher_Ready_Curriculum" / "01_Physics_East_Meadow_Refactor"
DEFAULT_REFERENCE = DEFAULT_REFACTOR / "_assets" / "brand" / "reference.docx"


def build_lesson_folder(
    folder: Path, *, schema_path: Path, reference_doc: Path | None, css_root: Path,
) -> list[str]:
    """Build one lesson folder. Returns list of relative output paths."""
    written: list[str] = []

    # 1. Validate sources
    student_html = folder / "Student_Exploration.html"
    teacher_md = folder / "Teacher_Guide.md"
    answer_md = folder / "Answer_Key.md"
    if not student_html.exists():
        raise ValidationError(f"{folder.name}: Student_Exploration.html missing")
    if not teacher_md.exists():
        raise ValidationError(f"{folder.name}: Teacher_Guide.md missing")
    if not answer_md.exists():
        raise ValidationError(f"{folder.name}: Answer_Key.md missing")
    validate_student_html(student_html, schema_path)
    validate_teacher_guide(teacher_md, schema_path)
    validate_answer_key(answer_md, schema_path)

    # 2. Build DOCX + onenote HTML from markdown sources
    for md in [teacher_md, answer_md]:
        docx = md.with_suffix(".docx")
        onhtml = md.with_suffix(".onenote.html")
        md_to_docx(md, docx, reference_doc)
        md_to_onenote_html(md, onhtml)
        validate_onenote_html(onhtml, schema_path)
        written += [str(docx.relative_to(ROOT)), str(onhtml.relative_to(ROOT))]

    # 3. Static-ify the interactive HTML
    onenote_html = folder / "Student_Exploration.onenote.html"
    static_text = staticify(
        student_html.read_text(encoding="utf-8"),
        css_root=css_root,
        html_dir=folder,
    )
    onenote_html.write_text(static_text, encoding="utf-8")
    validate_onenote_html(onenote_html, schema_path)
    written.append(str(onenote_html.relative_to(ROOT)))

    return written


def build_unit_plan(folder: Path, *, schema_path: Path, reference_doc: Path | None) -> list[str]:
    written: list[str] = []
    md = folder / "Unit_Plan.md"
    if not md.exists():
        return written
    validate_unit_plan(md, schema_path)
    docx = md.with_suffix(".docx")
    onhtml = md.with_suffix(".onenote.html")
    md_to_docx(md, docx, reference_doc)
    md_to_onenote_html(md, onhtml)
    validate_onenote_html(onhtml, schema_path)
    written += [str(docx.relative_to(ROOT)), str(onhtml.relative_to(ROOT))]
    return written


def build_assessments(folder: Path, *, reference_doc: Path | None) -> list[str]:
    written: list[str] = []
    for md in folder.glob("*.md"):
        docx = md.with_suffix(".docx")
        onhtml = md.with_suffix(".onenote.html")
        md_to_docx(md, docx, reference_doc)
        md_to_onenote_html(md, onhtml)
        written += [str(docx.relative_to(ROOT)), str(onhtml.relative_to(ROOT))]
    return written


def _iter_lesson_folders(unit: Path):
    for child in sorted(unit.iterdir()):
        if child.is_dir() and (child / "Student_Exploration.html").exists():
            yield child


def build_target(target: Path, *, schema_path: Path, reference_doc: Path | None) -> dict:
    css_root = DEFAULT_REFACTOR / "_assets"
    report = {"built": [], "failed": []}
    if (target / "Student_Exploration.html").exists():
        try:
            report["built"] += build_lesson_folder(
                target, schema_path=schema_path,
                reference_doc=reference_doc, css_root=css_root,
            )
        except Exception as e:
            report["failed"].append((str(target), str(e)))
        return report

    # Otherwise treat as unit
    if (target / "Unit_Plan.md").exists():
        try:
            report["built"] += build_unit_plan(
                target, schema_path=schema_path, reference_doc=reference_doc,
            )
        except Exception as e:
            report["failed"].append((str(target), str(e)))
    if (target / "Assessments").is_dir():
        try:
            report["built"] += build_assessments(
                target / "Assessments", reference_doc=reference_doc,
            )
        except Exception as e:
            report["failed"].append((str(target / "Assessments"), str(e)))
    for lesson in _iter_lesson_folders(target):
        try:
            report["built"] += build_lesson_folder(
                lesson, schema_path=schema_path,
                reference_doc=reference_doc, css_root=css_root,
            )
        except Exception as e:
            report["failed"].append((str(lesson), str(e)))
    return report


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("target", nargs="?", default="", help="Unit or lesson folder (relative to refactor root)")
    p.add_argument("--schema", default=str(ROOT / "tools" / "lesson_schema.yaml"))
    p.add_argument("--reference", default=str(DEFAULT_REFERENCE))
    args = p.parse_args()

    schema_path = Path(args.schema)
    reference = Path(args.reference) if Path(args.reference).is_file() else None

    if args.target:
        target = (DEFAULT_REFACTOR / args.target).resolve()
    else:
        target = DEFAULT_REFACTOR.resolve()

    if (target / "Student_Exploration.html").exists():
        report = build_target(target, schema_path=schema_path, reference_doc=reference)
    elif target == DEFAULT_REFACTOR.resolve():
        report = {"built": [], "failed": []}
        for unit in sorted(target.iterdir()):
            if unit.is_dir() and unit.name.startswith(("0", "1")) and unit.name != "_assets":
                sub = build_target(unit, schema_path=schema_path, reference_doc=reference)
                report["built"] += sub["built"]
                report["failed"] += sub["failed"]
    else:
        report = build_target(target, schema_path=schema_path, reference_doc=reference)

    # Write build_report.md (spec §7.2 step 5)
    report_md = ROOT / "build_report.md"
    lines: list[str] = ["# Build report", ""]
    lines.append(f"Target: `{target.relative_to(ROOT) if target.is_relative_to(ROOT) else target}`")
    lines.append(f"Built: {len(report['built'])} artifacts")
    lines.append(f"Failed: {len(report['failed'])}")
    lines.append("")
    if report["built"]:
        lines.append("## Built")
        lines += [f"- `{p}`" for p in report["built"]]
        lines.append("")
    if report["failed"]:
        lines.append("## Failed")
        for path, err in report["failed"]:
            lines.append(f"- `{path}`: {err}")
        lines.append("")
    report_md.write_text("\n".join(lines), encoding="utf-8")

    print(f"Built {len(report['built'])} artifacts. Report: {report_md.relative_to(ROOT)}")
    if report["failed"]:
        print(f"FAILED: {len(report['failed'])}", file=sys.stderr)
        for path, err in report["failed"]:
            print(f"  {path}: {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Run tests**

Run: `source .venv/bin/activate && python -m pytest tests/tools/test_build_lessons.py -v`
Expected: Both tests pass.

- [ ] **Step 3: Commit**

```bash
git add tools/build_lessons.py tests/tools/test_build_lessons.py tests/tools/fixtures/valid_lesson/
git commit -m "feat(tools): orchestrate full lesson build with validation"
```

## Task A22: Publish-pages helper

**Files:**
- Create: `tools/publish_pages.py`

- [ ] **Step 1: Write publish_pages.py**

```python
"""Copy interactive Student_Exploration.html files to the gh-pages branch.

Run only if SharePoint Permissive mode is unavailable and HTML must be hosted on
GitHub Pages. The script writes a self-contained `gh_pages_out/` directory that
the user manually copies onto a `gh-pages` branch.
"""
from __future__ import annotations
import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFACTOR = ROOT / "Publisher_Ready_Curriculum" / "01_Physics_East_Meadow_Refactor"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--out", default=str(ROOT / "gh_pages_out"))
    args = p.parse_args()
    out = Path(args.out)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    # Copy _assets
    shutil.copytree(REFACTOR / "_assets", out / "_assets")

    # Copy each lesson's Student_Exploration.html into a mirroring path
    for unit in sorted(REFACTOR.iterdir()):
        if not unit.is_dir() or unit.name.startswith("_"):
            continue
        for lesson in sorted(unit.iterdir()):
            if not lesson.is_dir():
                continue
            html = lesson / "Student_Exploration.html"
            if not html.is_file():
                continue
            target = out / unit.name / lesson.name / "Student_Exploration.html"
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(html, target)

    print(f"Published interactives to {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: Smoke-test the script**

Run: `source .venv/bin/activate && python tools/publish_pages.py`
Expected: prints `Published interactives to gh_pages_out`. (Output dir is empty for now since no real lessons yet — that's fine.)

- [ ] **Step 3: Commit**

```bash
git add tools/publish_pages.py
echo "gh_pages_out/" >> .gitignore
git add .gitignore
git commit -m "feat(tools): add publish_pages.py for GitHub Pages fallback"
```

## Task A23: QA checklist doc

**Files:**
- Create: `tools/lesson_qa_checklist.md`

- [ ] **Step 1: Write the checklist**

```markdown
# Manual QA checklist (per lesson, pilot only)

Run after `python tools/build_lessons.py 01_Kinematics/NN_Topic` succeeds.

1. Open `Student_Exploration.html` via `file://` URL in Chrome — verify it renders
   and interacts correctly with no server.
2. Print preview — verify the print stylesheet hides interactive controls and
   shows the static fallback.
3. Disable JavaScript (DevTools → Settings → Disable JavaScript) — verify the
   storyboard fallback and curated MD links remain usable.
4. Open `Student_Exploration.onenote.html` in a browser — verify no JS warnings,
   no broken images, no external requests in the Network tab.
5. Select All → Copy → Paste into a OneNote page (test on web, desktop, and
   iPad clients) — verify layout, images, and links survive the paste.
6. Open `Teacher_Guide.docx` in Word — verify cover lockup, fonts, and tinted
   Curated Resources box render correctly.
7. Re-run `python tools/build_lessons.py 01_Kinematics/NN_Topic` and confirm
   zero hard-fails.
```

- [ ] **Step 2: Commit**

```bash
git add tools/lesson_qa_checklist.md
git commit -m "docs: add per-lesson manual QA checklist"
```

---

# Phase B: Pilot Unit Foundation

## Task B1: Author Kinematics Unit_Plan source

**Files:**
- Create: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/Unit_Plan.md`

- [ ] **Step 1: Author the Unit_Plan.md**

Write the file. Use this skeleton — fill content from `Scope_and_Sequence.md` lines 19–32 (the Kinematics unit table) and from spec §5.6 (strategy rotation):

```markdown
# Unit: Kinematics — Unit Plan

## Cover

East Meadow Schools × Valley Stream Central High School District
Unit: Kinematics
9 lessons · ~2 weeks at 42-minute periods (one double period per week)

## Unit Scope (from East Meadow Scope & Sequence)

The verbatim Kinematics table from `Scope_and_Sequence.md`:

| Topic | NYSSLS | Phenomenon | Javalab/labs | Assessments |
|---|---|---|---|---|
| Vectors | HS-PS2-1 | Physics Classroom Vector Animations | PhET Vector Addition; Physics Classroom Vector Addition Interactive; Vector Golf | An Introduction to Free Body Diagrams (Better Lesson) |
| Distance/Displacement |   |   | Vector Walk (Physics Classroom) |   |
| Average Speed/Velocity |   |   |   |   |
| Acceleration | HS-PS2-1 | Physics Classroom: Acceleration | OPhysics: Uniform Acceleration in 1D; Speeding up/Slowing Down | Newton's Second Law in 1-D Motion (Better Lesson) |
| Motion graphs | HS-PS2-1 |   | PhET Moving Man; Physics Classroom: Graph that Motion |   |
| Freefall |   | Jumping from Space! | Java Lab: Freefall |   |
| Thrown upwards / Vertical Projectiles |   | (image) | OPhysics Projectile Motion; PhET Projectile Motion |   |
| Horizontal Projectile Motion |   | MythBusters Bullet Fired/Dropped; Shoot-n-Drop | PhET Projectile Motion; Java Lab: Horizontal |   |
| Projectiles at an Angle |   | Jamaal Murray hail mary | PhET Projectile Motion; Projectile Lab worksheet |   |

## Pacing Calendar

| Week | Day | Lesson | Notes |
|---|---|---|---|
| 1 | M | 01 Vectors | Restorative Circle (unit opener) |
| 1 | T | 02 Distance and Displacement |   |
| 1 | W (double) | 03 Average Speed and Velocity | Hochman: sentence expansion |
| 1 | Th | 04 Acceleration | BTC: random groups + VNPS |
| 1 | F | 05 Motion Graphs | Active Learning: gallery walk |
| 2 | M | 06 Freefall | Hochman: because/but/so |
| 2 | T | 07 Vertical Projectiles |   |
| 2 | W (double) | 08 Horizontal Projectile Motion | BTC + Hochman: paragraph topic sentence |
| 2 | Th | 09 Projectiles at an Angle | Active Learning: project-based design |
| 2 | F | Unit assessment | Regents-style cluster |

## Strategy Rotation

| Lesson | Strategy chips |
|---|---|
| 01 Vectors | RESTORATIVE CIRCLE · ACTIVE LEARNING |
| 02 Distance/Displacement | (none) |
| 03 Average Speed and Velocity | HOCHMAN |
| 04 Acceleration | BTC |
| 05 Motion Graphs | ACTIVE LEARNING |
| 06 Freefall | HOCHMAN |
| 07 Vertical Projectiles | (none) |
| 08 Horizontal Projectiles | BTC · HOCHMAN |
| 09 Projectiles at an Angle | ACTIVE LEARNING |

Total: HOCHMAN 3 · ACTIVE LEARNING 3 · BTC 2 · RESTORATIVE CIRCLE 1.

## NYSSLS Coverage Matrix

| Lesson | HS-PS2-1 | HS-PS2-2 | Notes |
|---|---|---|---|
| 01–05 | ✓ |   | Net force / acceleration thread starts here |
| 06–09 | ✓ |   | Freefall and projectile motion as constant a = -g case |
| (Forces unit) | ✓ | ✓ | Conservation of momentum lives in next unit |

## Vocabulary Scope

3 terms per lesson, introduced in the second half:

- 01 Vectors: vector, magnitude, direction
- 02 Distance/Displacement: distance, displacement, scalar
- 03 Velocity: speed, velocity, average rate
- 04 Acceleration: acceleration, deceleration, slope
- 05 Motion Graphs: position-time, velocity-time, area-under-curve
- 06 Freefall: freefall, gravity (g), terminal velocity
- 07 Vertical Projectiles: peak, time-of-flight, symmetry
- 08 Horizontal Projectiles: horizontal velocity, vertical velocity, range
- 09 Angled Projectiles: launch angle, range equation, optimal angle
```

- [ ] **Step 2: Build the unit plan**

Run: `source .venv/bin/activate && python tools/build_lessons.py 01_Kinematics`
Expected: prints `Built 2 artifacts.` and produces `Unit_Plan.docx` and `Unit_Plan.onenote.html`.

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/Unit_Plan.md \
        Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/Unit_Plan.docx \
        Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/Unit_Plan.onenote.html
git commit -m "feat(kinematics): author unit plan with verbatim MD scope"
```

## Task B2: Author Kinematics Regents-style assessment set

**Files:**
- Create: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/Assessments/Kinematics_Regents_Style_Set.md`

- [ ] **Step 1: Author the assessment markdown**

Write a Regents-style cluster:

```markdown
# Kinematics — Regents-Style Question Set

East Meadow Schools × Valley Stream Central High School District
Unit: Kinematics — assessment cluster aligned to HS-PS2-1.

## Stimulus

A student records the motion of a remote-control car on a long, straight track. The car starts at rest, accelerates uniformly for 3.0 seconds, then continues at constant velocity for 4.0 seconds, then decelerates uniformly to rest in 2.0 seconds. The student plots a velocity-time graph from her data.

[Insert velocity-time graph: starts at v = 0, rises linearly to v = 6 m/s at t = 3 s, holds at 6 m/s until t = 7 s, falls linearly to 0 at t = 9 s.]

## Multiple choice (15 questions)

1. During the first phase (0–3 s), the car's acceleration is closest to:
   - (A) 0 m/s²
   - (B) 1.0 m/s²
   - (C) 2.0 m/s²
   - (D) 6.0 m/s²

2. (… 14 more multiple-choice items, mixing direct readings of the graph,
   net-force application via F = ma assuming a 0.5 kg car, and graphical
   reasoning about position-time vs velocity-time. Each item names HS-PS2-1
   in the answer key.)

## Constructed response (1 cluster)

Use the velocity-time graph above to answer all parts.

(a) Calculate the total distance traveled by the car. Show your work.

(b) Sketch the corresponding position-time graph for the same 9-second
window. Label the slope of each segment.

(c) The student claims that "the car has zero acceleration during the
constant-velocity phase but the net force on the car is not zero because
the wheels are still pushing." Support or refute this claim using
Newton's second law. Use evidence from the graph in your reasoning.
```

- [ ] **Step 2: Build the assessment**

Run: `source .venv/bin/activate && python tools/build_lessons.py 01_Kinematics`
Expected: builds Assessments DOCX + OneNote HTML.

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/Assessments/
git commit -m "feat(kinematics): author Regents-style assessment cluster"
```

---

# Phase C: Pilot Lesson — Vectors (end-to-end validation)

This phase produces ONE complete lesson to validate the pattern before scaling.

## Task C1: Scaffold the Vectors lesson

**Files:**
- Move/recreate: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/01_Vectors/`

- [ ] **Step 1: Remove the empty placeholder folder if present**

Run: `rm -rf Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/01_Vectors`

- [ ] **Step 2: Run scaffold**

Run:
```bash
source .venv/bin/activate && python tools/scaffold_lesson.py 01_Kinematics 01 "Vectors" \
    --strategies "RESTORATIVE CIRCLE,ACTIVE LEARNING"
```
Expected: prints `Scaffolded Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/01_Vectors`.

- [ ] **Step 3: Verify three files present**

Run: `ls Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/01_Vectors`
Expected: `Answer_Key.md  Student_Exploration.html  Teacher_Guide.md`.

- [ ] **Step 4: Commit the scaffolded shell**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/01_Vectors/
git commit -m "scaffold(kinematics): create 01_Vectors lesson skeleton"
```

## Task C2: Author Vectors Teacher_Guide.md

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/01_Vectors/Teacher_Guide.md`

- [ ] **Step 1: Replace placeholders with actual content**

Open the file and replace each `[…]` placeholder:

- **Curated Resources** must paste verbatim from `Scope_and_Sequence.md` line 23 (the Vectors row), keeping the bold NYSSLS performance expectation and the parenthesized CCC. The four sub-headings (NYSSLS Standards, Phenomenon, Javalab / Labs, Assessments) must each have content from the corresponding MD column.
- **CCC Focus:** "Cause and Effect — how the *direction* of a force changes motion, not just its magnitude."
- **Materials:** "Graph paper or vector grid; one ruler per pair; printed copy of Vector Golf course (linked); chart paper for VNPS-style station work; markers."
- **Safety:** "None"
- **Prior knowledge:** "Adding signed numbers; reading a coordinate grid; the difference between a measurement (number) and a measurement with direction."
- **Lesson Objectives:**
  - "I can describe a vector quantity using both magnitude and direction."
  - "I can add two vectors graphically using the head-to-tail method."
  - "I can decompose a vector into its x- and y-components."
- **Agenda** (table rows): produce a row per minute-block totaling 42 min, including Opening Connection (SEL, 0–3 min), phenomenon (3–7), notice & wonder + TT#1 (7–12), initial model (12–17), investigate via Vector Golf stations (17–32), TT#2 + sense-making (32–37), vocab + revise model (37–40), exit ticket (40–42).
- **Discussion Prompts:**
  - "When two vectors point the same direction, what happens to their resultant? When they point opposite? When they're perpendicular?"
  - "Sample student response: 'When perpendicular, the resultant is the diagonal of a rectangle, so we use Pythagoras to get its size.'"
- **Common Misconceptions:**
  - "Misconception: 'Vectors with bigger numbers are always longer.' Correction: Two vectors of equal magnitude but different directions add to different resultants."
  - "Misconception: 'Adding vectors is the same as adding their magnitudes.' Correction: Only true when they point in the same direction."
- **ELL/ENL supports:** "Sentence frames: 'The resultant of A + B has magnitude ___ because ___.' Word-choice box: {magnitude, direction, resultant, components, scalar}. Visual-first lesson — start with arrows on grid before introducing the word 'vector'."
- **SPED supports:** "Use the printed Vector Golf course as a chunked, scaffolded organizer; pre-draw the first arrow for each problem."
- **Extensions:** "After Vector Golf, prompt students to find the *minimum* number of vector additions to reach the target — introduces optimization thinking."
- **Strategy Spotlight:**
  - "Restorative Circle (unit opener, 2 min): Pass a small object; each student answers, 'What is one experience you've had with motion this week?' Honor pass-rights."
  - "Active Learning (Vector Golf stations, 15 min): 4 stations, 3 students each, 3-minute rotations. Each station has a different course; students leave their solution on chart paper for the next group to verify."
- **Exit Ticket:**
  - "A boat sails 5 km east, then 12 km north. Sketch the resultant displacement and find its magnitude. Show one sentence of reasoning."
- **Key Vocabulary (max 3):** vector, magnitude, direction.

- [ ] **Step 2: Run validators**

Run: `source .venv/bin/activate && python -c "
from pathlib import Path
from tools.validators import validate_teacher_guide
validate_teacher_guide(
    Path('Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/01_Vectors/Teacher_Guide.md'),
    Path('tools/lesson_schema.yaml')
)
print('OK')
"`
Expected: prints `OK`.

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/01_Vectors/Teacher_Guide.md
git commit -m "feat(kinematics/vectors): author Teacher_Guide content"
```

## Task C3: Author Vectors Answer_Key.md

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/01_Vectors/Answer_Key.md`

- [ ] **Step 1: Replace placeholders**

The student page's three Make-It-Make-Sense questions are authored in Task C4. For now, plan three answer entries:

- MIMS 1 answer: "Resultant magnitude = √(3² + 4²) = 5 units; direction = arctan(4/3) ≈ 53° above the x-axis. Rubric: full credit if both magnitude and direction shown with units; half credit if only magnitude. NYSSLS: HS-PS2-1."
- MIMS 2 answer: "When the two vectors point in the same direction, the resultant magnitude equals the sum of magnitudes. When they point in opposite directions, the resultant equals the absolute difference. Rubric: full credit if both same-direction and opposite-direction cases addressed. NYSSLS: HS-PS2-1."
- MIMS 3 answer: "x-component = 10 cos(30°) ≈ 8.66; y-component = 10 sin(30°) = 5. Rubric: full credit if both components correct to 1 decimal place; tolerance ±0.2. NYSSLS: HS-PS2-1."
- Exit ticket answer: "5² + 12² = 169 ⇒ resultant = 13 km. Direction: arctan(12/5) ≈ 67° north of east. Rubric: full credit if magnitude correct (13 km, ±0.5 km), reasoning sentence references Pythagorean theorem or head-to-tail rule, and a sketch is present. NYSSLS: HS-PS2-1."

- [ ] **Step 2: Run validator**

Run: `source .venv/bin/activate && python -c "
from pathlib import Path
from tools.validators import validate_answer_key
validate_answer_key(
    Path('Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/01_Vectors/Answer_Key.md'),
    Path('tools/lesson_schema.yaml')
)
print('OK')
"`
Expected: prints `OK`.

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/01_Vectors/Answer_Key.md
git commit -m "feat(kinematics/vectors): author Answer_Key content"
```

## Task C4: Author Vectors Student_Exploration.html (interactive + storyboard)

**Files:**
- Modify: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/01_Vectors/Student_Exploration.html`

- [ ] **Step 1: Replace `{{INTERACTIVE_PLACEHOLDER}}` with the live interactive**

Inside `<div data-interactive="true">`, paste:

```html
<svg id="vec-canvas" width="480" height="360" viewBox="0 0 480 360" role="img" aria-label="Vector addition canvas">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#662e80"/>
    </marker>
    <marker id="arrow-vs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2ea3f2"/>
    </marker>
    <marker id="arrow-r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a1a"/>
    </marker>
  </defs>
  <!-- grid -->
  <g stroke="#e6e6e6" stroke-width="1">
    <line x1="0" y1="180" x2="480" y2="180"/>
    <line x1="240" y1="0" x2="240" y2="360"/>
  </g>
  <!-- A -->
  <line id="vec-a" x1="240" y1="180" x2="320" y2="180" stroke="#662e80" stroke-width="3" marker-end="url(#arrow)"/>
  <text id="lab-a" x="280" y="170" font-family="Inter" font-size="14" fill="#662e80">A</text>
  <!-- B (head-to-tail) -->
  <line id="vec-b" x1="320" y1="180" x2="320" y2="120" stroke="#2ea3f2" stroke-width="3" marker-end="url(#arrow-vs)"/>
  <text id="lab-b" x="325" y="150" font-family="Inter" font-size="14" fill="#2ea3f2">B</text>
  <!-- Resultant -->
  <line id="vec-r" x1="240" y1="180" x2="320" y2="120" stroke="#1a1a1a" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#arrow-r)"/>
  <text id="lab-r" x="270" y="145" font-family="Inter" font-size="14" fill="#1a1a1a">R</text>
</svg>
<div class="controls">
  <label>A magnitude <input id="ax" type="range" min="-8" max="8" step="1" value="4"> <span id="ax-r" class="readout">4</span></label>
  <label>B magnitude (vertical) <input id="by" type="range" min="-8" max="8" step="1" value="3"> <span id="by-r" class="readout">3</span></label>
  <p>Resultant magnitude: <span id="res" class="readout">5.0</span> units · direction: <span id="dir" class="readout">36.9°</span> above x-axis</p>
</div>
<script>
  const SCALE = 20, CX = 240, CY = 180;
  const ax = document.getElementById("ax");
  const by = document.getElementById("by");
  const vecA = document.getElementById("vec-a");
  const vecB = document.getElementById("vec-b");
  const vecR = document.getElementById("vec-r");
  function update() {
    const a = parseFloat(ax.value), b = parseFloat(by.value);
    const ahx = CX + a * SCALE, ahy = CY;
    vecA.setAttribute("x2", ahx); vecA.setAttribute("y2", ahy);
    vecB.setAttribute("x1", ahx); vecB.setAttribute("y1", ahy);
    vecB.setAttribute("x2", ahx); vecB.setAttribute("y2", ahy - b * SCALE);
    vecR.setAttribute("x2", ahx); vecR.setAttribute("y2", ahy - b * SCALE);
    document.getElementById("ax-r").textContent = a;
    document.getElementById("by-r").textContent = b;
    const mag = Math.sqrt(a * a + b * b);
    const ang = Math.atan2(b, a) * 180 / Math.PI;
    document.getElementById("res").textContent = mag.toFixed(1);
    document.getElementById("dir").textContent = ang.toFixed(1) + "°";
  }
  ax.addEventListener("input", update);
  by.addEventListener("input", update);
  update();
</script>
```

- [ ] **Step 2: Replace `{{STORYBOARD_PLACEHOLDER}}` with three SVG frames**

Inside `<noscript class="noscript-storyboard">`, paste:

```html
<p><strong>Storyboard frame 1.</strong> Vector A points right, magnitude 4 units. Vector B points up, magnitude 3 units, drawn head-to-tail from the tip of A.</p>
<svg width="240" height="180" viewBox="0 0 240 180"><line x1="20" y1="160" x2="100" y2="160" stroke="#662e80" stroke-width="3" marker-end="url(#arrow)"/><line x1="100" y1="160" x2="100" y2="100" stroke="#2ea3f2" stroke-width="3" marker-end="url(#arrow-vs)"/></svg>
<p><strong>Storyboard frame 2.</strong> The resultant R is the dashed arrow from the tail of A to the head of B. Its magnitude is √(4² + 3²) = 5 units.</p>
<svg width="240" height="180" viewBox="0 0 240 180"><line x1="20" y1="160" x2="100" y2="160" stroke="#662e80" stroke-width="3"/><line x1="100" y1="160" x2="100" y2="100" stroke="#2ea3f2" stroke-width="3"/><line x1="20" y1="160" x2="100" y2="100" stroke="#1a1a1a" stroke-width="2" stroke-dasharray="4 3"/></svg>
<p><strong>Storyboard frame 3.</strong> If B were 6 units instead of 3, R would be √(16 + 36) ≈ 7.2 units — the resultant grows when either input vector grows.</p>
<svg width="240" height="180" viewBox="0 0 240 180"><line x1="20" y1="160" x2="100" y2="160" stroke="#662e80" stroke-width="3"/><line x1="100" y1="160" x2="100" y2="40" stroke="#2ea3f2" stroke-width="3"/><line x1="20" y1="160" x2="100" y2="40" stroke="#1a1a1a" stroke-width="2" stroke-dasharray="4 3"/></svg>
```

- [ ] **Step 3: Replace remaining placeholders**

- `{{PHENOMENON_DESCRIPTION}}` → "Watch this short animation: arrows from Physics Classroom show two vectors being added head to tail. Notice that the order in which you add them does not change the result."
- `{{DRIVING_QUESTION}}` → "How can we add two quantities that have direction, not just size?"
- `{{TURN_AND_TALK_1}}` → "Turn to your partner. One thing you noticed about the arrows. One thing you wondered."
- `{{TURN_AND_TALK_2}}` → "If A points right (magnitude 4) and B points up (magnitude 3), why does the resultant come out to 5? Use the grid to convince your partner."
- `{{MIMS_Q1}}` → "Slide the controls so A = 3 and B = 4. What is the magnitude and direction of the resultant?"
- `{{MIMS_Q2}}` → "Describe what happens to the resultant when A and B point in the same direction. What about opposite directions?"
- `{{MIMS_Q3}}` → "If a vector has magnitude 10 and points 30° above the x-axis, what are its x- and y-components?"
- `{{VOCAB_1}}` → "**vector** — a quantity with both magnitude and direction"
- `{{VOCAB_2}}` → "**magnitude** — the size or length of a vector"
- `{{VOCAB_3}}` → "**direction** — the way a vector points, often given as an angle"
- `{{RETURN_PROMPT}}` → "Return to the original animation. Using what you just learned, predict the resultant of the two arrows shown."
- `{{EXIT_Q}}` → "A boat sails 5 km east, then 12 km north. Sketch the resultant and find its magnitude."
- `{{CURATED_LINKS}}` → bulleted list of: "PhET Vector Addition Simulation (link from MD)", "Physics Classroom Vector Addition Interactive (link from MD)", "Vector Golf (Google Doc, link from MD)" with the actual MD URLs.

- [ ] **Step 4: Run student-html validator**

Run: `source .venv/bin/activate && python -c "
from pathlib import Path
from tools.validators import validate_student_html
validate_student_html(
    Path('Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/01_Vectors/Student_Exploration.html'),
    Path('tools/lesson_schema.yaml')
)
print('OK')
"`
Expected: prints `OK`.

- [ ] **Step 5: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/01_Vectors/Student_Exploration.html
git commit -m "feat(kinematics/vectors): author interactive + storyboard"
```

## Task C5: Build Vectors and verify all artifacts

**Files:**
- Generated: 6 build outputs in `01_Vectors/`

- [ ] **Step 1: Build the lesson**

Run: `source .venv/bin/activate && python tools/build_lessons.py 01_Kinematics/01_Vectors`
Expected: prints `Built 5 artifacts.` (Student onenote.html + 2× docx + 2× onenote.html for the markdown sources).

- [ ] **Step 2: Verify outputs exist**

Run: `ls Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/01_Vectors/`
Expected: lists all 8 files (3 sources + 5 build outputs).

- [ ] **Step 3: Open Student_Exploration.html in a browser, manual smoke test**

Run: `open Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/01_Vectors/Student_Exploration.html`
Expected: page renders co-branded header, sliders move and update the SVG, vocab list shows three terms, and the curated PhET/Physics-Classroom/Vector-Golf links are present in "Explore Further".

- [ ] **Step 4: Manual QA pass against `tools/lesson_qa_checklist.md`**

Walk through all 7 checklist steps. Note any deviations.

- [ ] **Step 5: Commit the build outputs**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/01_Vectors/
git commit -m "build(kinematics/vectors): pilot lesson green build + manual QA"
```

---

# Phase D: Remaining Lessons (02 – 09)

Each lesson follows the same shape as Vectors. Phase D has 8 tasks — one per lesson. Each task uses scaffold + author + build + commit. The strategy chips for each lesson come from the spec §5.6 rotation, already documented in `Unit_Plan.md`.

For each lesson, the engineer:
1. Removes the empty placeholder folder.
2. Runs `python tools/scaffold_lesson.py 01_Kinematics NN "Title" --strategies "..."`.
3. Authors all four `[…]` placeholder regions in each of the three files (Teacher_Guide.md, Answer_Key.md, Student_Exploration.html), pulling Curated Resources verbatim from `Scope_and_Sequence.md`.
4. Runs `python tools/build_lessons.py 01_Kinematics/NN_<slug>` and confirms green build.
5. Walks the QA checklist.
6. Commits as `feat(kinematics/<slug>): author lesson`.

The interactive widget for each lesson (the JS/SVG inside `data-interactive`) is unique. Use this guide:

| Lesson | Interactive concept | Storyboard frames |
|---|---|---|
| 02 Distance and Displacement | Path on a grid; toggle "show displacement vs. show distance" | walk-around-the-block path; straight-line displacement; net distance vs. displacement comparison |
| 03 Average Speed and Velocity | Two cars on a track; sliders for speeds; readouts for both quantities | both at constant speed; one stops mid-trip; same average speed but different average velocities |
| 04 Acceleration | Slider for a; dot accelerates from rest; live v(t) readout | a > 0; a < 0 (deceleration); a = 0 |
| 05 Motion Graphs | Press play to animate a moving dot; live position-time and velocity-time graphs draw alongside | constant velocity; constant acceleration; reversal |
| 06 Freefall | Drop button; ball falls with g = 9.8; v and y readouts every 0.5 s | t=0 release; t=1 s; t=2 s with v and y labelled |
| 07 Vertical Projectiles | Slider for initial velocity v₀; ball thrown straight up; symmetry highlighted | upward; peak (v=0); symmetric descent |
| 08 Horizontal Projectile Motion | Slider for horizontal v₀; ball drops while moving forward; constant horizontal v, accelerating vertical v | horizontal launch only; same fall time as a dropped ball; trajectory visualization |
| 09 Projectiles at an Angle | Sliders for v₀ and θ; trajectory traces; range and time-of-flight readouts | low angle, short range; 45°, max range; high angle, long air time |

## Task D1: Lesson 02 — Distance and Displacement

**Files:**
- Replace: `01_Kinematics/02_Distance_and_Displacement/`

- [ ] **Step 1: Reset and scaffold**

```bash
rm -rf Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/02_Distance_and_Displacement
source .venv/bin/activate && python tools/scaffold_lesson.py 01_Kinematics 02 "Distance and Displacement" --strategies ""
```

- [ ] **Step 2: Author all three files**

Follow the authoring discipline from Tasks C2–C4. Curated Resources for this row of `Scope_and_Sequence.md`: Topic="Distance/Displacement"; NYSSLS=blank (carry HS-PS2-1 thread from unit-level); Phenomenon=blank; Lab="Vector Walk Physics Classroom"; Assessment=blank. Where the MD row is empty, mark the sub-heading "(no curated content for this topic; teacher discretion)".

Interactive concept (per the table above): grid + path drawing; "show distance" sums segments, "show displacement" draws straight line from start to end with magnitude.

Storyboard: 3 frames as described.

- [ ] **Step 3: Build and QA**

Run: `python tools/build_lessons.py 01_Kinematics/02_Distance_and_Displacement` → expect green build.
Walk QA checklist.

- [ ] **Step 4: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/02_Distance_and_Displacement/
git commit -m "feat(kinematics/distance-displacement): author lesson"
```

## Task D2: Lesson 03 — Average Speed and Velocity

- [ ] **Step 1: Reset and scaffold**

```bash
rm -rf Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/03_Average_Speed_and_Velocity
source .venv/bin/activate && python tools/scaffold_lesson.py 01_Kinematics 03 "Average Speed and Velocity" --strategies "HOCHMAN"
```

- [ ] **Step 2: Author all three files**

Strategy Spotlight: Hochman *sentence expansion*. Provide a kernel sentence ("The car moves.") and walk students through expansions adding (1) speed, (2) direction, (3) time. Final target sentence: "The red car moves east at 30 m/s for 4 seconds."

Interactive: two-cars track described in Phase D table.

- [ ] **Step 3: Build, QA, commit**

```bash
python tools/build_lessons.py 01_Kinematics/03_Average_Speed_and_Velocity
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/03_Average_Speed_and_Velocity/
git commit -m "feat(kinematics/avg-speed-velocity): author lesson with Hochman strategy"
```

## Task D3: Lesson 04 — Acceleration

- [ ] **Step 1: Reset and scaffold**

```bash
rm -rf Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/04_Acceleration
source .venv/bin/activate && python tools/scaffold_lesson.py 01_Kinematics 04 "Acceleration" --strategies "BTC"
```

- [ ] **Step 2: Author all three files**

Strategy Spotlight: BTC. *Random groups of 3* (visibly random — playing-cards method). *Vertical non-permanent surfaces* (whiteboards or chart paper at standing height). *Thin-slicing task*: start with "constant velocity vs. constant acceleration — which graph is which?", then 3 progressively harder graph-matching puzzles.

Interactive: slider for a; dot accelerates; readouts.

Curated Resources from MD row: NYSSLS HS-PS2-1; Phenomenon = "Physics Classroom: Acceleration"; Labs = "OPhysics: Uniform Acceleration in 1D" + "Speeding up/Slowing Down Google Doc"; Assessment = "Newton's Second Law in 1-D Motion (Better Lesson)".

- [ ] **Step 3: Build, QA, commit**

```bash
python tools/build_lessons.py 01_Kinematics/04_Acceleration
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/04_Acceleration/
git commit -m "feat(kinematics/acceleration): author lesson with BTC strategy"
```

## Task D4: Lesson 05 — Motion Graphs

- [ ] **Step 1: Reset and scaffold**

```bash
rm -rf Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/05_Motion_Graphs
source .venv/bin/activate && python tools/scaffold_lesson.py 01_Kinematics 05 "Motion Graphs" --strategies "ACTIVE LEARNING"
```

- [ ] **Step 2: Author all three files**

Strategy Spotlight: Active Learning *gallery walk*. Five station prompts: "draw the v-t graph that matches this position-t graph"; "match the story to the graph"; etc. Students rotate every 4 minutes, leaving comments on sticky notes.

Interactive: animated dot + co-evolving x-t and v-t graphs.

Curated Resources from MD: NYSSLS HS-PS2-1; Lab = PhET Moving Man + Physics Classroom Graph that Motion (concept builder + interactive).

- [ ] **Step 3: Build, QA, commit**

```bash
python tools/build_lessons.py 01_Kinematics/05_Motion_Graphs
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/05_Motion_Graphs/
git commit -m "feat(kinematics/motion-graphs): author lesson with Active Learning gallery walk"
```

## Task D5: Lesson 06 — Freefall

- [ ] **Step 1: Reset and scaffold**

```bash
rm -rf Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/06_Freefall
source .venv/bin/activate && python tools/scaffold_lesson.py 01_Kinematics 06 "Freefall" --strategies "HOCHMAN"
```

- [ ] **Step 2: Author all three files**

Strategy Spotlight: Hochman *because/but/so*. Misconception kernel: "Heavier objects fall faster ___". Students complete with "because… but… so…". Target final sentence: "Heavier objects fall faster *because* they weigh more, *but* the acceleration of gravity is the same for all masses, *so* they actually fall at the same rate (ignoring air resistance)."

Phenomenon (from MD): "Jumping from Space! (YouTube)".

Interactive: drop ball, g=9.8, readouts every 0.5 s.

- [ ] **Step 3: Build, QA, commit**

```bash
python tools/build_lessons.py 01_Kinematics/06_Freefall
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/06_Freefall/
git commit -m "feat(kinematics/freefall): author lesson with Hochman because/but/so"
```

## Task D6: Lesson 07 — Vertical Projectiles

- [ ] **Step 1: Reset and scaffold**

```bash
rm -rf Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/07_Vertical_Projectiles
source .venv/bin/activate && python tools/scaffold_lesson.py 01_Kinematics 07 "Vertical Projectiles" --strategies ""
```

- [ ] **Step 2: Author all three files**

Title in artifacts: "Thrown Upwards / Vertical Projectiles" (verbatim MD wording).

Interactive: slider for v₀; ball thrown straight up; symmetric trajectory; v=0 highlighted at peak.

- [ ] **Step 3: Build, QA, commit**

```bash
python tools/build_lessons.py 01_Kinematics/07_Vertical_Projectiles
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/07_Vertical_Projectiles/
git commit -m "feat(kinematics/vertical-projectiles): author lesson"
```

## Task D7: Lesson 08 — Horizontal Projectile Motion

- [ ] **Step 1: Reset and scaffold**

```bash
rm -rf Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/08_Horizontal_Projectile_Motion
source .venv/bin/activate && python tools/scaffold_lesson.py 01_Kinematics 08 "Horizontal Projectile Motion" --strategies "BTC,HOCHMAN"
```

- [ ] **Step 2: Author all three files**

Strategy Spotlight: BTC *thin-slicing*: 4 progressively harder puzzles ("how long to fall 5m", "how far does it travel horizontally", "if you double the height, what happens to time", "if you double the height, what happens to range"). Hochman *paragraph topic sentence*: students write a topic sentence for a 3-sentence paragraph explaining why horizontal velocity does not affect fall time.

Phenomenon (from MD): MythBusters Bullet Fired/Dropped + Shoot-n-Drop.

Interactive: horizontal v slider; ball drops + moves; trajectory traces; alongside a comparison ball that's dropped (no horizontal motion) — both hit the floor at the same time.

- [ ] **Step 3: Build, QA, commit**

```bash
python tools/build_lessons.py 01_Kinematics/08_Horizontal_Projectile_Motion
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/08_Horizontal_Projectile_Motion/
git commit -m "feat(kinematics/horizontal-projectiles): author lesson with BTC and Hochman"
```

## Task D8: Lesson 09 — Projectiles at an Angle

- [ ] **Step 1: Reset and scaffold**

```bash
rm -rf Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/09_Projectiles_at_an_Angle
source .venv/bin/activate && python tools/scaffold_lesson.py 01_Kinematics 09 "Projectiles at an Angle" --strategies "ACTIVE LEARNING"
```

- [ ] **Step 2: Author all three files**

Strategy Spotlight: Active Learning *project-based design challenge*. Students design a paper "catapult" that launches a marshmallow into a target box across the room. They use their understanding of launch angle (45° gives max range on flat ground) to predict and calibrate.

Phenomenon (from MD): Jamaal Murray hail mary catch.

Interactive: sliders for v₀ (5–20 m/s) and angle (0°–90°); trajectory traces in real time; readouts for range and time-of-flight; toggle "show optimal angle" highlights 45°.

Curated link (from MD): PhET Projectile Motion + Projectile Lab worksheet (Google Doc).

- [ ] **Step 3: Build, QA, commit**

```bash
python tools/build_lessons.py 01_Kinematics/09_Projectiles_at_an_Angle
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/09_Projectiles_at_an_Angle/
git commit -m "feat(kinematics/angled-projectiles): author lesson with Active Learning design challenge"
```

---

# Phase E: Polish and Documentation

## Task E1: Top-level README.md

**Files:**
- Create: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/README.md`

- [ ] **Step 1: Author the README**

```markdown
# Physics — East Meadow × Valley Stream Central HSD Refactor

This curriculum mirrors the **NEW East Meadow Physics Scope and Sequence**
verbatim. The pilot delivers Unit: Kinematics (9 lessons). The remaining
9 units are stubbed and will follow the same template after pilot acceptance.

## Unit index

- 00 Math in Science (stub)
- **01 Kinematics — pilot** (9 lessons, complete)
- 02 Forces (stub)
- 03 Momentum / Impulse (stub)
- 04 Energy (stub)
- 05 Thermodynamics (stub)
- 06 Electrostatics (stub)
- 07 Current Electricity (stub)
- 08 Waves (stub)
- 09 Modern Physics (stub)

## Per-lesson artifacts

Every lesson ships in two flavors:

| Artifact | Filename | Where it's hosted |
|---|---|---|
| Rich interactive student page | `Student_Exploration.html` | SharePoint document library (Permissive mode) or GitHub Pages fallback |
| OneNote-paste static student page | `Student_Exploration.onenote.html` | Pasted into OneNote Class Notebook |
| Teacher guide | `Teacher_Guide.docx` + `.onenote.html` | SharePoint inline preview / OneNote teacher section |
| Answer key | `Answer_Key.docx` + `.onenote.html` | Same |

## Hosting

### SharePoint (primary)

1. In the target document library, confirm with district IT that **Browser File Handling** is set to **Permissive** (so `.html` files render inline rather than downloading).
2. Drop the unit folder into the library.
3. Teachers and students get clickable links to `.html` (interactive) and `.docx` (preview inline) artifacts.

### GitHub Pages (fallback)

If SharePoint is forced to Strict:

```
source .venv/bin/activate && python tools/publish_pages.py
```

Then publish `gh_pages_out/` to the repo's `gh-pages` branch. Replace the SharePoint links inside OneNote pages with the public Pages URLs.

### OneNote Class Notebook

For each lesson:
1. Open `Student_Exploration.onenote.html` in a browser.
2. Select All → Copy → Paste into the lesson's OneNote page in the Content Library.
3. Distribute the page to Student Sections via Class Notebook.
4. Repeat with `Teacher_Guide.onenote.html` into the teacher section.

A one-page walkthrough lives at `OneNote_Import_Guide.md`.

## Building artifacts

```
source .venv/bin/activate && python tools/build_lessons.py 01_Kinematics
```

Validation rules (in `tools/lesson_schema.yaml`) are enforced — the build fails if any lesson is missing required headings, exceeds the 3-vocab cap, or is missing the `<noscript>` storyboard fallback.

## Authoring a new lesson

```
python tools/scaffold_lesson.py 01_Kinematics NN "Lesson Title" --strategies "HOCHMAN,ACTIVE LEARNING"
```

Then fill in the placeholders in the three generated source files; build; QA per `tools/lesson_qa_checklist.md`.

## Brand assets

Co-branded for **East Meadow Schools × Valley Stream Central HSD**. Brand tokens live in `_assets/brand/brand.css` and the Pandoc reference DOCX. Placeholder logos are at `_assets/brand/em_logo.svg` and `vs_logo.svg` — replace with official SVGs as they become available.

## Open questions

See `docs/superpowers/specs/2026-05-08-physics-east-meadow-refactor-design.md` §9.
```

- [ ] **Step 2: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/README.md
git commit -m "docs: add Physics refactor README with hosting workflow"
```

## Task E2: OneNote Import Guide

**Files:**
- Create: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/OneNote_Import_Guide.md`

- [ ] **Step 1: Author the import guide**

```markdown
# OneNote Class Notebook — Import Guide (one page)

Use this for every lesson once you've built it.

## You'll need

- Microsoft 365 OneNote (web, desktop, or iPad)
- A Class Notebook for the course (one-time setup via OneNote Class Notebook app)
- The two `.onenote.html` files for the lesson:
  - `Student_Exploration.onenote.html`
  - `Teacher_Guide.onenote.html`

## Steps (per lesson)

1. **Create the page.** In your Class Notebook → Content Library → Unit: Kinematics → New Page. Title it `Lesson NN — Topic`.
2. **Open the static student page.** In a browser, open `Student_Exploration.onenote.html` (double-click it on disk, or open from your SharePoint library).
3. **Copy.** Cmd+A (or Ctrl+A) to Select All → Cmd+C / Ctrl+C to Copy.
4. **Paste into OneNote.** Click into the page body → Cmd+V / Ctrl+V. The page renders co-branded header, all sections, and the storyboard SVGs.
5. **Embed videos.** For each "Video — in OneNote: Insert → Online Video" callout in the pasted content, click the URL, copy it, then in OneNote: **Insert → Online Video → paste**. Delete the callout once the video is embedded.
6. **Distribute.** Use Class Notebook → Distribute Page to push it to all student sections.
7. **Teacher section.** Repeat steps 2–4 for `Teacher_Guide.onenote.html`, pasting into your *teacher-only* section.

## Tips

- **OneNote web** sometimes downgrades layout fidelity. If the page looks off, open the same notebook in OneNote desktop or iPad — the paste fidelity is usually better there.
- **Distribution** copies the page once. Subsequent edits to the Content Library page do *not* propagate to already-distributed student copies.
- For lessons where the student writes directly on the page (Initial Model, Notice & Wonder), the textareas in the static HTML render as gray boxes. OneNote ink and typing on top of them work normally.
```

- [ ] **Step 2: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/OneNote_Import_Guide.md
git commit -m "docs: add one-page OneNote Class Notebook import guide"
```

## Task E3: Visuals/Visual_Prompts.md

**Files:**
- Create: `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/Visuals/Visual_Prompts.md`

- [ ] **Step 1: Author the prompts file**

```markdown
# Kinematics — Visual Prompts

Source prompts for any AI-generated images used in this unit. Re-runnable so visuals are reproducible.

## Unit cover image

Prompt: "Stylized vector arrows arranged in a kinematics motif — head-to-tail addition, a parabolic projectile arc, and a small graph axis. Flat illustration, two-color palette: deep purple (#662e80) and bright blue (#2ea3f2). 16:9, no text."

## Lesson-level prompts

(Add per lesson if AI-generated visuals are used. The pilot lessons rely on hand-authored inline SVG; this file is currently empty by design.)
```

- [ ] **Step 2: Commit**

```bash
git add Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics/Visuals/Visual_Prompts.md
git commit -m "docs: add Kinematics visual prompts seed"
```

## Task E4: Final pilot integration build

**Files:** none new

- [ ] **Step 1: Run the full unit build**

Run: `source .venv/bin/activate && python tools/build_lessons.py 01_Kinematics`
Expected: prints `Built XX artifacts.` with no failures.

- [ ] **Step 2: Run the full pytest suite**

Run: `source .venv/bin/activate && python -m pytest tests/tools/ -v`
Expected: all tests pass.

- [ ] **Step 3: Verify directory has the full set**

Run:
```bash
find Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/01_Kinematics \
  -type f \( -name "*.html" -o -name "*.docx" -o -name "*.md" \) | sort
```
Expected: lists for each lesson `Student_Exploration.html`, `Student_Exploration.onenote.html`, `Teacher_Guide.md`, `.docx`, `.onenote.html`, `Answer_Key.md`, `.docx`, `.onenote.html` — plus the Unit_Plan trio and the Assessments trio.

- [ ] **Step 4: Open the README and skim**

Run: `open Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/README.md`

- [ ] **Step 5: Pilot-acceptance commit**

```bash
git add -u Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/
git commit -m "build: pilot Kinematics unit — all 9 lessons green" --allow-empty
```

---

## Done criteria for the pilot

The pilot is complete when:
1. All Phase A–E tasks are checked.
2. `python tools/build_lessons.py 01_Kinematics` exits 0.
3. `python -m pytest tests/tools/ -v` exits 0.
4. Manual QA checklist passes for all 9 lessons.
5. README, OneNote Import Guide, and Visual Prompts seed file exist.
6. The `_archive/` folder still contains the previous partial work (untouched).

After acceptance, the same template (Phase D pattern) scales to Units 0 and 2–9.
