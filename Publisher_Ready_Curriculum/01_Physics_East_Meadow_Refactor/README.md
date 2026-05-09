# Physics — East Meadow × Valley Stream Central HSD Refactor

This curriculum mirrors the **NEW East Meadow Physics Scope and Sequence** verbatim. The pilot delivers **Unit: Kinematics (9 lessons + Unit Plan + Regents-style assessment cluster)**. The remaining 9 units are stubbed and follow the same template.

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

Every lesson ships in **two flavors per audience**:

| Artifact | Filename | Where it's hosted |
|---|---|---|
| Rich interactive student page | `Student_Exploration.html` | SharePoint document library (Permissive mode) or GitHub Pages fallback |
| OneNote-paste static student page | `Student_Exploration.onenote.html` | Pasted into OneNote Class Notebook |
| Teacher guide | `Teacher_Guide.docx` + `.onenote.html` | SharePoint inline preview / OneNote teacher section |
| Answer key | `Answer_Key.docx` + `.onenote.html` | SharePoint inline preview / OneNote teacher section |

Source files (`.md`, hand-authored `.html`) are committed alongside the build outputs. The sources are diffable in git; the built artifacts are what teachers receive.

## Pedagogical model

Every lesson follows the **NYSSLS phenomenon-based lesson flow** (slide 32 of the joint training PPTX):

1. Phenomenon (local/relatable)
2. Notice & Wonder + Turn and Talk #1
3. Question prioritization through a Crosscutting Concept (CCC) lens
4. Initial model
5. Investigation (interactive Explore + curated MD links)
6. Sense-making + Turn and Talk #2
7. Class consensus + revise the model
8. Vocabulary (≤ 3 terms, second half)
9. Transfer task (assessment)
10. Exit ticket + closing reflection

Every Teacher Guide includes the **NYSSLS Lesson Observation Checklist crosswalk** (slide 5 of the PPTX) showing where each of the 8 observation items appears in the lesson.

**Strategy chips** are tagged at the unit level so teachers see the rotation:

- **HOCHMAN** literacy moves — 1–2× per week
- **ACTIVE LEARNING** structures (gallery walks, station work, design challenges) — 1–2× per week
- **BTC** (Building Thinking Classrooms) — random groups + VNPS thin-slicing tasks, occasional
- **RESTORATIVE CIRCLE** — unit openers and post-assessment days

**Required every lesson:** SEL (Opening Connection + Closing Reflection), differentiation/ELL supports, Curated Resources block from `Scope_and_Sequence.md`.

## Hosting

### SharePoint (primary)

1. In the target document library, confirm with district IT that **Browser File Handling** is set to **Permissive** (so `.html` files render inline rather than downloading).
2. Drop the unit folder into the library.
3. Teachers and students get clickable links to `.html` (interactive) and `.docx` (preview inline) artifacts.

### GitHub Pages (fallback)

If your SharePoint tenant enforces Strict browser file handling and `.html` is forced to download:

```
source .venv/bin/activate
python tools/publish_pages.py
```

This writes a self-contained `gh_pages_out/` directory. Push it to the repo's `gh-pages` branch. Replace the SharePoint links inside OneNote pages with the public Pages URLs.

### OneNote Class Notebook

For each lesson:

1. Open `Student_Exploration.onenote.html` in a browser.
2. Select All → Copy → Paste into the lesson's OneNote page in the Content Library.
3. Distribute the page to Student Sections via Class Notebook.
4. Repeat with `Teacher_Guide.onenote.html` into the teacher section.

Detailed steps live in [`OneNote_Import_Guide.md`](./OneNote_Import_Guide.md).

## Building artifacts

```
source .venv/bin/activate
python tools/build_lessons.py 01_Kinematics       # build the whole pilot unit
python tools/build_lessons.py 01_Kinematics/01_Vectors    # build a single lesson
python tools/build_lessons.py                     # build everything
```

Validation rules in `tools/lesson_schema.yaml` are enforced — the build aborts if any lesson is missing required headings, exceeds the 3-vocab cap, lacks the `<noscript>` storyboard, or the OneNote HTML output contains a forbidden tag (`<script>`, `<iframe>`, external `<link>`).

A `build_report.md` is written at the repo root summarizing built / failed artifacts.

## Authoring a new lesson

```
python tools/scaffold_lesson.py 01_Kinematics NN "Lesson Title" --strategies "HOCHMAN,ACTIVE LEARNING"
```

This creates the lesson folder with three source files (Student_Exploration.html, Teacher_Guide.md, Answer_Key.md) pre-populated with all required section headings. Fill the placeholder text; build; QA per [`tools/lesson_qa_checklist.md`](../../tools/lesson_qa_checklist.md).

## Brand assets

Co-branded for **East Meadow Schools × Valley Stream Central HSD**.

- Color tokens, typography, and component styles → `_assets/brand/brand.css`
- Pandoc reference document → `_assets/brand/reference.docx` (regenerated by `tools/make_reference_docx.py` whenever brand tokens change)
- Placeholder logos → `_assets/brand/em_logo.svg`, `vs_logo.svg` (replace with official SVGs as they become available)

## Pilot-unit deliverables (Unit: Kinematics)

| File | Purpose |
|---|---|
| `Unit_Plan.md` / `.docx` / `.onenote.html` | Pacing calendar, strategy rotation, NYSSLS coverage matrix, vocabulary scope |
| `Assessments/Kinematics_Regents_Style_Set.*` | 15 multiple-choice + 1 cluster, aligned to HS-PS2-1 |
| 9 × lesson folders | `01_Vectors` through `09_Projectiles_at_an_Angle` |
| `Visuals/Visual_Prompts.md` | Source prompts for any AI-generated images (kept for reproducibility) |

## Open questions

See `docs/superpowers/specs/2026-05-08-physics-east-meadow-refactor-design.md` §9 for the in-progress list. None are blockers for using the pilot — teachers can confirm with district IT and supply official logos as those decisions land.

## Scope and Sequence (source of truth)

The verbatim copy of the **NEW East Meadow Physics Scope and Sequence** lives at [`Scope_and_Sequence.md`](./Scope_and_Sequence.md). All lesson Curated Resources blocks pull from that file. When the source MD updates, regenerate the Unit Plan and the affected lessons' Curated Resources blocks accordingly.
