# Chemistry & Physics Curriculum Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Generate complete Regents-level Chemistry and Physics curricula (22 units, ~140 lessons, ~100 CER worksheets, ~50 labs) as .docx files aligned to NYSSLS standards for Valley Stream CHSD.

**Architecture:** A Python generator script reads course data (JSON configs per unit/lesson) and produces formatted .docx files using templates. Each course has a JSON config defining units, lessons, standards, phenomena, circle prompts, do nows, learning targets, differentiation notes, CRSE connections, and Hochman activities. The generator iterates over configs and outputs the full folder structure.

**Tech Stack:** Python 3.14, python-docx 1.2.0, venv at `.venv/`

**Reference docs:**
- Design: `docs/plans/2026-03-09-chemistry-physics-curriculum-design.md`
- Chemistry educator guide: `Chem/chemistry-educator-guide-2025.pdf`
- Chemistry PLDs: `Chem/physical-science-chemistry-plds.pdf`
- Chemistry sample clusters: `Chem/sample-chemistry-clusters-2025.pdf`
- Physics educator guide: `Physics/physics-educator-guide-2025.pdf`
- Physics PLDs: `Physics/physical-science-physics-plds.pdf`
- Physics sample clusters: `Physics/sample-physics-clusters-2025.pdf`
- ESS examples: `ESS/` folder (for format reference, quality baseline to exceed)

---

## Task 1: Create the Document Generator Script

**Files:**
- Create: `generator/generate_docx.py`
- Create: `generator/styles.py`
- Create: `generator/templates.py`

**Step 1: Create generator directory**
```bash
mkdir -p generator
```

**Step 2: Write `generator/styles.py`**
Defines consistent Word document styles (fonts, headings, table formatting, colors) used across all document types. Should define:
- Heading styles (Unit title, Lesson title, Section headers)
- Body text style (11pt Calibri)
- Table styles (for differentiation boxes, pacing calendars, standards maps)
- Highlight/callout box styles (for Learning Target, Circle Prompt, Do Now)

**Step 3: Write `generator/templates.py`**
Functions that create each document type:
- `create_unit_plan(unit_data) -> Document`
- `create_lesson_plan(lesson_data) -> Document`
- `create_student_notes(lesson_data) -> Document`
- `create_cer_worksheet(cer_data) -> Document`
- `create_lab_document(lab_data) -> Document`

Each function builds a full .docx using the styles module. The lesson plan function must include all sections from the design doc:
1. Header (Unit, Lesson #, Title, PE codes)
2. Opening Circle prompt
3. Do Now
4. Learning Target ("At the end of 42 minutes I can...")
5. Standards Alignment (PE, SEP, CCC, DCI)
6. Materials & Preparation
7. 5E Instructional Sequence (Engage, Explore, Explain, Elaborate, Evaluate)
8. Differentiation Box (Approaching, On-Level, Advanced, ELL, IEP)
9. CRSE Connections
10. Hochman Integration

**Step 4: Write `generator/generate_docx.py`**
Main script that:
- Reads a course config JSON file
- Iterates over units and lessons
- Calls template functions to generate each .docx
- Saves to the correct folder structure
- Prints progress as it goes

**Step 5: Test with a minimal config**
Create a test JSON with one unit, one lesson. Run generator. Open the .docx and verify formatting.

**Step 6: Commit**
```bash
git add generator/
git commit -m "feat: add docx generator for curriculum documents"
```

---

## Task 2: Build Chemistry Course Configuration

**Files:**
- Create: `generator/configs/chemistry.json`

This is the largest content task. The JSON config defines ALL chemistry content:

```json
{
  "course": "Chemistry",
  "units": [
    {
      "number": 1,
      "title": "Matter, Measurement & Lab Safety",
      "days": 12,
      "performance_expectations": [],
      "anchoring_phenomenon": "...",
      "essential_questions": ["..."],
      "crse_theme": "...",
      "lessons": [
        {
          "number": 1,
          "title": "...",
          "learning_target": "At the end of 42 minutes I can...",
          "circle_prompt": "...",
          "do_now": "...",
          "standards": { "pe": [], "sep": [], "ccc": [], "dci": [] },
          "five_e": {
            "engage": "...",
            "explore": "...",
            "explain": "...",
            "elaborate": "...",
            "evaluate": "..."
          },
          "differentiation": {
            "approaching": "...",
            "on_level": "...",
            "advanced": "...",
            "ell": "...",
            "iep": "..."
          },
          "crse_connection": "...",
          "hochman_activity": "...",
          "materials": ["..."],
          "cer": {
            "phenomenon": "...",
            "claim_starter": "...",
            "evidence_source": "...",
            "reasoning_frame": "..."
          }
        }
      ]
    }
  ]
}
```

Build configs for all 11 chemistry units with all lessons. Use the educator guide, PLDs, and sample clusters to ensure standards coverage and phenomena-driven content.

**Unit breakdown with estimated lessons:**

| Unit | Lessons | Topics |
|------|---------|--------|
| 1: Matter, Measurement & Lab Safety | 5 | Classification of matter, physical/chemical properties, measurement, significant figures, lab safety |
| 2: Atomic Structure & Periodic Table | 9 | Atomic models, subatomic particles, isotopes, electron configuration, periodic trends, nuclear chemistry intro |
| 3: Chemical Bonding & Molecular Structure | 8 | Ionic bonding, covalent bonding, metallic bonding, Lewis structures, molecular geometry, intermolecular forces, bulk properties |
| 4: Chemical Formulas, Nomenclature & the Mole | 7 | Formula writing, naming compounds, mole concept, molar mass, percent composition, empirical/molecular formulas |
| 5: Chemical Reactions & Stoichiometry | 10 | Reaction types, balancing equations, conservation of mass, mole ratios, stoichiometric calculations, limiting reagent, percent yield |
| 6: Energy in Chemical Reactions | 7 | Exothermic/endothermic, enthalpy, calorimetry, potential energy diagrams, Hess's law, activation energy |
| 7: Reaction Rates & Equilibrium | 6 | Collision theory, factors affecting rate, dynamic equilibrium, Le Chatelier's principle, equilibrium expressions |
| 8: Acids, Bases & Salts | 6 | Acid-base theories, pH scale, neutralization, titration, indicators, salts |
| 9: Redox & Electrochemistry | 5 | Oxidation numbers, half-reactions, electrochemical cells, electrolysis, activity series |
| 10: Waves, EM Radiation & Nuclear Chemistry | 4 | Wave properties, EM spectrum, photon energy, nuclear reactions, fission/fusion |
| 11: Engineering Design & Review | 3 | Engineering design process, applying chemistry to real-world problems, course review |

**Total: ~70 lessons**

**Step 1:** Build Unit 1 config completely with all lesson details.
**Step 2:** Build Units 2-3 configs.
**Step 3:** Build Units 4-5 configs.
**Step 4:** Build Units 6-7 configs.
**Step 5:** Build Units 8-9 configs.
**Step 6:** Build Units 10-11 configs.
**Step 7:** Commit.

---

## Task 3: Build Physics Course Configuration

**Files:**
- Create: `generator/configs/physics.json`

Same structure as chemistry. All 11 physics units:

| Unit | Lessons | Topics |
|------|---------|--------|
| 1: Scientific Inquiry, Measurement & Vectors | 4 | Scientific method, measurement, vector addition, graphical analysis |
| 2: Kinematics | 10 | Distance/displacement, speed/velocity, acceleration, free fall, projectile motion, motion graphs |
| 3: Newton's Laws & Forces | 10 | Newton's 1st/2nd/3rd laws, free body diagrams, friction, inclined planes, circular motion |
| 4: Momentum & Impulse | 6 | Impulse, momentum, conservation of momentum, collisions (elastic/inelastic) |
| 5: Gravity, Electrostatics & Magnetism | 7 | Universal gravitation, Coulomb's law, electric fields, magnetic fields, electromagnetism |
| 6: Work, Energy & Power | 9 | Work, kinetic energy, potential energy, conservation of energy, power, simple machines |
| 7: Thermal Energy & Conservation | 6 | Temperature, heat transfer, specific heat, phase changes, calorimetry |
| 8: Waves & Sound | 8 | Wave properties, wave behavior (reflection, refraction, diffraction, interference), sound waves, resonance, Doppler effect |
| 9: Light, Optics & EM Spectrum | 7 | Reflection, refraction, mirrors, lenses, EM spectrum, photon energy, color |
| 10: Nuclear Physics | 3 | Radioactive decay, fission, fusion, mass-energy equivalence |
| 11: Engineering Design & Review | 3 | Engineering design process, applying physics to real-world problems, course review |

**Total: ~73 lessons**

**Steps:** Same sub-steps as Task 2 — build unit by unit, commit when complete.

---

## Task 4: Generate Chemistry Documents

**Files:**
- Create: All files under `Chem/Templates/`, `Chem/Units/`

**Step 1:** Run generator for Chemistry templates
```bash
source .venv/bin/activate
python generator/generate_docx.py --course chemistry --templates-only
```

**Step 2:** Run generator for all Chemistry units
```bash
python generator/generate_docx.py --course chemistry
```

**Step 3:** Verify output folder structure matches design
```bash
find Chem/Units -name "*.docx" | head -20
```

**Step 4:** Spot-check a few documents by opening them

**Step 5:** Commit
```bash
git add Chem/Templates/ Chem/Units/
git commit -m "feat: generate complete Chemistry curriculum (11 units)"
```

---

## Task 5: Generate Physics Documents

**Files:**
- Create: All files under `Physics/Templates/`, `Physics/Units/`

**Steps:** Same as Task 4 but for Physics.

```bash
python generator/generate_docx.py --course physics
```

**Commit:**
```bash
git add Physics/Templates/ Physics/Units/
git commit -m "feat: generate complete Physics curriculum (11 units)"
```

---

## Task 6: Required Lab Investigations

**Files:**
- Create: `Chem/Required Lab Investigations/` documents
- Create: `Physics/Required Lab Investigations/` documents

The educator guides specify that investigations are required for admission to the Regents exam. Research the specific required investigations for each course from the NYSED website and create:
- Student Directions (.docx)
- Teacher Materials (.docx)
- Answer Packets (.docx)
- Rubrics (.docx)

Model after the ESS Required Lab Investigations (Unearthing Mars, The Ripple Effect, The Sky is the Limit).

**Commit:**
```bash
git add Chem/Required\ Lab\ Investigations/ Physics/Required\ Lab\ Investigations/
git commit -m "feat: add required lab investigations for Chemistry and Physics"
```

---

## Execution Notes

- **Python venv:** Always activate with `source .venv/bin/activate` before running generator
- **Content quality:** Each lesson must have substantive, specific content — not placeholder text. Circle prompts should be genuine community builders. Do Nows should activate prior knowledge. CRSE connections should reference real scientists and real community contexts. Hochman activities should use actual science vocabulary from the lesson.
- **Phenomena-driven:** Every unit needs an authentic anchoring phenomenon. Lessons within the unit should build toward explaining/investigating that phenomenon, matching the NYSSLS cluster assessment approach.
- **Parallelization:** Tasks 2 and 3 (chemistry and physics configs) can be built in parallel. Tasks 4 and 5 (document generation) can run in parallel after the generator is tested.
