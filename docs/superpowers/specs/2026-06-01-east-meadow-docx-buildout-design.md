# Design — East Meadow DOCX-only build-out (all 9 remaining units)

**Date:** 2026-06-01
**Branch:** `physics-east-meadow-refactor`
**Status:** Approved (Approach A); user waived per-step review and review gate ("do everything autonomously, do not ask for permission").

## 1. Goal

Extend the East Meadow 5E phenomenon-based refactor — currently a Kinematics-only
pilot — to the **9 remaining units**. Deliver **DOCX only** (no HTML student
pages). Each lesson ships **four documents**:

| Doc | Source | Role |
|---|---|---|
| Teacher Guide | `Teacher_Guide.md` | 5E phenomenon-based lesson plan (existing 15-section schema) |
| Student Worksheet | `Student_Worksheet.md` | Student-facing investigation/activity (the "worksheet") |
| Student Notes | `Student_Notes.md` | Guided note-guide (the "note guide") |
| Answer Key | `Answer_Key.md` | Teacher answers/rubrics for worksheet + exit ticket |

Each unit also ships a `Unit_Plan.md`. All sources are Markdown; all outputs are
DOCX built through the existing pandoc + brand reference-doc pipeline. The legacy
`Student_Exploration.html` interactive is **not** produced for the new units.

## 2. Approach A — extend the existing pipeline

Reuse `tools/build_lessons.py`, `tools/validators.py`, `tools/scaffold_lesson.py`,
`tools/pandoc_runner.py`, and `tools/lesson_schema.yaml`. Changes:

1. **Schema** (`lesson_schema.yaml`): add `student_worksheet_required_headings`
   and `student_notes_required_headings`.
2. **Templates**: add `student_worksheet.md.tmpl`, `student_notes.md.tmpl`.
3. **Validators**: add `validate_student_worksheet`, `validate_student_notes`
   (H2-heading presence checks, same style as the others).
4. **build_lessons.py**: treat a folder as a lesson when it contains
   `Teacher_Guide.md` (Student_Exploration.html becomes optional). Build the new
   markdown sources to DOCX. Only run the HTML/static-ify path when
   `Student_Exploration.html` exists (preserves the Kinematics pilot unchanged).
5. **scaffold_lesson.py**: a `--docx-only` flag writes Teacher Guide + Worksheet
   + Notes + Answer Key and skips the HTML page.

**Backward compatibility:** Kinematics (which has Student_Exploration.html) keeps
building exactly as before; the existing 30 pytest tests must stay green.

## 3. Student Worksheet structure (H2 sections)

Mirrors the student-facing 5E flow:
Header · Phenomenon & Driving Question · Notice & Wonder · Initial Model ·
Investigation · Make It Make Sense · Vocabulary in Action · Revise Your Model ·
Exit Ticket. Answers are NOT printed (they live in the Answer Key).

## 4. Student Notes structure (H2 sections)

Guided note-guide:
Header · Learning Targets · Key Vocabulary (≤3, with room to define) ·
Guided Notes (concept outline with fill-in blanks) · Worked Example ·
Summary (Hochman Because/But/So sentence). Aligns to the Teacher Guide content.

## 5. Lesson breakdown (~49 lessons)

| Unit | Lessons |
|---|---|
| 00 Math in Science | 4 — Algebra & Trig; Graphing & Data; Scientific Notation & Fermi; Units, Prefixes & Dimensional Analysis |
| 02 Forces | 6 — 1st Law/Inertia; 2nd Law/Net Force; 3rd Law; Friction; Centripetal/Circular; Universal Gravitation |
| 03 Momentum/Impulse | 4 — Momentum & Impulse; Impulse–Momentum Theorem; Conservation of Momentum; Collisions (lab/review) |
| 04 Energy | 6 — Work; Power; Kinetic Energy; Gravitational PE; Conservation of Energy; Energy Systems (Wheels to Watts) |
| 05 Thermodynamics | 3 — Thermal Energy & Temperature; Heat Transfer & 2nd Law; Calorimetry (Thermal Tales) |
| 06 Electrostatics | 6 — Electric Charge; Conductors/Insulators & Conduction; Induction & Polarization; Coulomb's Law; Electric Fields; Field Lines |
| 07 Current Electricity | 5 — Current & Ohm's Law; Resistance in a Wire; Series Circuits; Parallel Circuits; Electromagnetism (Induction Junction) |
| 08 Waves | 10 — Wave Anatomy; Transverse vs Longitudinal; v=fλ; Standing Waves & Resonance; Interference; Doppler; EM Spectrum; Refraction & Snell's Law; Optics (Lenses & Mirrors); Digital Technologies |
| 09 Modern Physics | 5 — Photoelectric Effect; Models of the Atom; Energy Levels & Spectra; Standard Model; Fusion/Fission/Decay |

NYSSLS alignment, phenomena, labs, and assessment links are pulled verbatim from
`Scope_and_Sequence.md` for each topic row.

## 6. Execution

1. Build tooling (§2). Keep tests green.
2. Pilot Unit 02 Forces (6 lessons) authored to the Kinematics depth standard;
   build to DOCX; validate. This is the exemplar.
3. Author the remaining 8 units via parallel subagents, each given the exemplar +
   schema + the relevant Scope & Sequence row.
4. Full `build_lessons.py` run with 0 failures; pytest green; commit + push.

## 7. Non-goals

- No web/HTML student pages for the new units.
- No changes to the Kinematics pilot content.
- No changes to the separate `generator/` JSON pipeline or `Physics/Units/`.
