# Chemistry East Meadow Refactor — Design Spec

**Date:** 2026-06-01
**Status:** Approved design → pending implementation plan
**Author:** Claude (brainstormed with user)
**Pilot:** Unit 1 — Safety & Measurement

---

## 1. Goal

Refactor the Chemistry curriculum into the same phenomenon-based 5E format the
Physics curriculum was rebuilt into on the `physics-east-meadow-refactor`
branch, producing **attractive DOCX teacher/student documents with rich,
brand-styled visuals** (diagrams, graphs, charts, particle models). This spec
covers a **single pilot unit** — Unit 1, Safety & Measurement — that establishes
the chemistry pattern end-to-end. Units 2–11 follow in later cycles using the
same machinery.

This mirrors how Physics piloted **Kinematics** before fanning out to Forces,
Momentum, Energy, and Thermodynamics.

## 2. Authoritative source documents

Two files are the single source of truth (both confirmed by the user):

| Source | Role |
|---|---|
| `Publisher_Ready_Curriculum/02_Chemistry/Valley_Stream_Chemistry_Scope_Sequence.docx` | **Sequence + content.** Defines the unit/topic order, NYSSLS standards, anchoring phenomena, labs, and assessments. |
| `Publisher_Ready_Curriculum/02_Chemistry/Copy of 1. East Meadow Valley Stream Chem 5_6_26.pptx` | **Instructional framework.** The NYSSLS Lesson Observation Checklist (slides 5 & 41), ABCs (Activity Before Content), phenomenon-first / "don't kill the wonder," ≤3 vocab in the 2nd half, literacy strategies (OPTIC, CER, Regents-verb decoder), and Regents format (60% MC / 40% CR). |

**Unit 1 — Safety & Measurement** (from the Scope & Sequence, Table 0) has eight
topics, each with its own anchoring phenomenon:

1. Lab Safety — *How do scientists work safely with hazardous substances?*
2. Measurement & SI Units — *Why does the whole world use the same units?* (HS-PS1-7)
3. Significant Figures & Scientific Notation — *Why does measurement precision limit a calculated result?*
4. Dimensional Analysis — *How can we convert between very large and very small quantities (atoms ↔ grams)?* (HS-PS1-7)
5. Density — *Why does ice float on water when most solids sink?* (HS-PS2-6)
6. Gram Formula Mass — *Why do equal numbers of atoms of different elements have such different masses?* (HS-PS1-2)
7. Percent Composition — *How can we tell what a compound is made of without taking it apart?*
8. 2025 Chemistry Reference Tables — *How does a single reference document support every chemistry concept?*

## 3. Output location & structure

A new parallel track, sibling to the physics refactor. The original
`Chemistry/Units/` and the existing `Publisher_Ready_Curriculum/02_Chemistry/`
trees are **left untouched** as references.

```
Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor/
├── _assets/brand/reference.docx          # copied from the physics brand
├── README.md                             # authoring notes for the chem track
└── 01_Safety_and_Measurement/
    ├── Unit_Plan.md
    ├── 01_Lab_Safety/
    │   ├── Teacher_Guide.md
    │   ├── Student_Worksheet.md
    │   ├── Student_Notes.md
    │   ├── Answer_Key.md
    │   └── figures/                       # generated PNGs
    ├── 02_Measurement_and_SI_Units/
    ├── 03_Significant_Figures_and_Scientific_Notation/
    ├── 04_Dimensional_Analysis/
    ├── 05_Density/
    ├── 06_Gram_Formula_Mass/
    ├── 07_Percent_Composition/
    └── 08_Chemistry_Reference_Tables/
```

Each lesson is **DOCX-only** mode (no interactive HTML / web edition), exactly
like the Forces and Thermodynamics units. The builder auto-detects this by the
absence of `Student_Exploration.html`.

## 4. Document templates & schema conformance

All documents conform to the existing `tools/lesson_schema.yaml` (no schema
changes needed — the schema is course-agnostic). Per lesson:

- **`Teacher_Guide.md`** — 14 required headings: Cover; Curated Resources (from
  East Meadow Scope & Sequence) with the four sub-headings NYSSLS Standards /
  Phenomenon / Javalab / Labs / Assessments; Lesson Overview; Phase 1 Engage →
  Phase 5 Evaluate (minute-by-minute facilitation script, sample teacher
  language, anticipated student responses); Common Misconceptions; Access &
  Differentiation; Strategy Spotlight; **NYSSLS Observation Checklist
  Crosswalk**; Companion Materials; Key Vocabulary (max 3).
- **`Student_Worksheet.md`** — Phenomenon, Notice & Wonder, Initial Model,
  Investigation, Make It Make Sense, Vocabulary in Action, Revise Your Model,
  Exit Ticket. **No answers** (those live in the Answer Key).
- **`Student_Notes.md`** — Learning Targets, Key Vocabulary, Guided Notes,
  Worked Example, Summary.
- **`Answer_Key.md`** — Cover, Make-It-Make-Sense Answers, Exit Ticket Answer,
  Closing Reflection (rubric).
- **`Unit_Plan.md`** (one per unit) — Cover, Unit Scope (from East Meadow Scope
  & Sequence), Pacing Calendar, Strategy Rotation, NYSSLS Coverage Matrix,
  Vocabulary Scope.

**Strategy chips** use the existing allowed set (HOCHMAN, ACTIVE LEARNING, BTC,
RESTORATIVE CIRCLE). For foundational lessons whose Scope & Sequence standard is
"—" (Lab Safety, Sig Figs, Percent Composition, Reference Tables), the NYSSLS
Standards sub-heading names the foundational SEP/skill it serves and the later
standard it feeds (e.g. "Foundational measurement skill — supports HS-PS1-7
mathematical representations"), so the heading is never empty.

## 5. Figure library (broad, upfront)

A new module `tools/figures_chem.py` in the same brand palette as
`tools/figures.py` (purple `#662e80`, blue `#2ea3f2`, ink `#222`, matplotlib
Agg, 150 dpi, deterministic — no `Date.now`/random). It imports and reuses the
existing `line_graph` / `bar_chart` helpers where a generic chart suffices.

Builders (broad enough to seed Units 2–11, not only the pilot):

- **Models:** `particle_model` (grids of atoms/molecules — element vs compound
  vs mixture, and the three states of matter), `bohr_model` (nucleus + electron
  shells), `lewis_structure` (element symbol with valence dots).
- **Diagrams:** `classification_tree` (matter classification flowchart),
  `graduated_cylinder` (meniscus reading), `dimensional_analysis_track`
  (railroad-track factor-label conversions), `separation_apparatus`
  (distillation / filtration / chromatography), `reaction_energy_diagram`
  (reaction-coordinate, activation energy, exo/endothermic).
- **Graphs:** `density_graph` (mass-vs-volume scatter with slope = density
  annotated), `heating_curve` (temperature-vs-time with phase plateaus),
  `titration_curve` (pH-vs-volume), `periodic_trend` (atomic radius / ionization
  energy / electronegativity — thin wrappers over `line_graph`).

Unit 1 consumes roughly six of these (`particle_model`, `classification_tree`,
`graduated_cylinder`, `dimensional_analysis_track`, `density_graph`, plus a
`bar_chart` for precision-vs-accuracy and a percent-composition pie/bar). The
rest are built now and exercised by a smoke test so later units inherit them.

A per-unit generator `tools/_gen_chem_unit01_figures.py` (mirroring
`tools/_gen_forces_figures.py`) renders the specific PNG instances into each
lesson's `figures/` directory. Markdown references them with relative paths
(`![alt](figures/name.png)`); pandoc embeds them into the DOCX.

Every figure carries descriptive alt text (accessibility + the OPTIC literacy
strategy from the PowerPoint).

## 6. Build pipeline changes

The chosen approach is **(A) parameterize the existing
`tools/build_lessons.py`** rather than fork it, so both courses build through
one validated pipeline.

- Add an **optional `--root` argument** to `build_lessons.py main()`, defaulting
  to the current physics `DEFAULT_REFACTOR`. When supplied, it resolves the
  target and the default reference doc relative to that root. This is **additive
  and backward-compatible** — the existing 30 tests and all physics invocations
  keep working unchanged.
- Copy `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/_assets/brand/reference.docx`
  to `…/02_Chemistry_East_Meadow_Refactor/_assets/brand/reference.docx` (shared
  co-brand styling).
- Build command:
  `python tools/build_lessons.py --root Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor 01_Safety_and_Measurement`

No changes to `pandoc_runner.py`, `static_ifier.py`, `validators.py`, or
`lesson_schema.yaml`.

## 7. PowerPoint fidelity requirements

Every Teacher Guide must demonstrably satisfy the 8-point NYSSLS Lesson
Observation Checklist (PowerPoint slides 5 & 41), surfaced explicitly in the
**NYSSLS Observation Checklist Crosswalk** table that maps each criterion to
where it appears in the lesson:

1. Local, relatable phenomenon
2. Turn and Talk (2–3×)
3. Students develop questions / models / procedures
4. CCC defined and used
5. ENL — key vocabulary (≤3) defined toward the 2nd half
6. Revisit phenomenon using evidence from the lesson
7. ENL/SPED supports (guiding questions, graphic organizers, sentence frames,
   word-choice boxes)
8. Assessment check (Exit Ticket)

Additional PowerPoint moves baked in:

- **ABCs — Activity Before Content:** the 5E flow runs Explore (investigation)
  before Explain (vocabulary/equation), so the activity precedes the content.
- **Literacy strategies** in Strategy Spotlight / Differentiation: **OPTIC** for
  reading the density and precision graphs; the **"when you see ___ = do ___"**
  Regents-verb decoder (slide 33); **CER** reasoning structure in worksheets.
- **Regents alignment:** any Regents-style assessment items follow 60% MC / 40%
  CR and keep answer-revealing emphasis out of MC option lines (enforced by the
  existing validator).

## 8. Testing & verification

The build passing cleanly is the gate:

- `python tools/build_lessons.py --root … 01_Safety_and_Measurement` →
  **0 validation failures**, all DOCX written, `build_report.md` clean.
- Add a `figures_chem.py` smoke test under `tests/tools/` that renders one of
  each builder to a temp dir and asserts the files exist and are non-empty.
- The existing **30 tests stay green** (changes are additive).
- Manual spot-check: open 2–3 generated DOCX to confirm figures embed correctly
  and styling matches the physics brand.

## 9. Scope boundaries

**In scope (this pilot):** Unit 1 Safety & Measurement — 8 lessons (4 docs each)
+ Unit Plan + figure library + per-unit figure generator + `--root` pipeline
change + smoke test + README.

**Out of scope (future cycles):** Units 2–11; Required Lab Investigations
rebuild; Regents-style cluster assessments; any web/HTML edition for chemistry;
modifying the original `Chemistry/Units/` tree.

## 10. Open questions

None blocking. The brand `reference.docx` is reused as-is; if the district later
supplies chemistry-specific cover art or a distinct chem accent color, the
`_assets/brand/` swap is a one-file change that re-flows on the next build.
