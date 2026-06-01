"""Generate the multi-agent workflow script for authoring all remaining
chemistry lessons (Units 2-14) from the scope-sequence manifest.

Reads tools/chem_scope_manifest.json and emits tools/chem_build_workflow.mjs,
where every lesson gets a fully-populated authoring prompt. Run:

    python tools/gen_chem_workflow.py
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = "Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor"
MANIFEST = json.loads(Path("tools/chem_scope_manifest.json").read_text(encoding="utf-8"))

CHIPS = ["ACTIVE LEARNING", "HOCHMAN", "BTC"]

# Map topic keywords -> a suggested tools.figures_chem builder + call hint.
def figure_hint(topic: str, sub: str) -> str:
    t = (topic + " " + sub).lower()
    def h(s): return "FIGURE HINT: " + s
    if "heating" in t or "cooling curve" in t:
        return h("use `heating_curve(path, substance='water')` from tools.figures_chem (temp-vs-time with melting/boiling plateaus).")
    if "titration" in t:
        return h("use `titration_curve(path)` from tools.figures_chem (pH vs volume, equivalence point).")
    if "potential energy" in t or "energy in reaction" in t or "collision" in t or "rates of reaction" in t:
        return h("use `reaction_energy_diagram(path, reactant=30, product=10, activation=55, title='...')` from tools.figures_chem.")
    if "lewis" in t:
        return h("use `lewis_structure(path, 'O', valence=6)` (and/or several) from tools.figures_chem.")
    if "periodic trend" in t or ("trend" in t and "periodic" in t):
        return h("use `periodic_trend(path, elements=[...], values=[...], ylabel='atomic radius (pm)', title='...')` from tools.figures_chem.")
    if "classification of matter" in t or "distinguishing elements" in t or "classes of elements" in t:
        return h("use `classification_tree(path)` and/or `particle_model(path, [('element','single'),('compound','AB'),('mixture','A+B')])` from tools.figures_chem.")
    if "states of matter" in t or "phase change" in t:
        return h("use `particle_model(path, [('solid','single'),('liquid','single'),('gas','A+B')])` and optionally `heating_curve` from tools.figures_chem.")
    if "atomic model" in t or "subatomic" in t or "isotope" in t or "ions" == topic.strip().lower() or "electron configuration" in t:
        return h("use `bohr_model(path, protons=.., neutrons=.., shells=[2,8,..], label='..')` from tools.figures_chem.")
    if "bright" in t or "spectra" in t or "spectrum" in t or "electromagnetic" in t:
        return h("no library builder fits; write a small CUSTOM matplotlib figure in the brand palette (import PURPLE, BLUE, INK, ACCENT2 from tools.figures) showing discrete bright lines / an EM-spectrum band.")
    if "separating mixtures" in t or "separation" in t:
        return h("use `separation_apparatus(path, kind='distillation')` (or 'filtration'/'chromatography') from tools.figures_chem.")
    if "molecular geometry" in t or "vsepr" in t:
        return h("use `lewis_structure` from tools.figures_chem, or a small CUSTOM matplotlib molecular-shape sketch in the brand palette.")
    if "intermolecular" in t or "polar" in t:
        return h("write a small CUSTOM matplotlib figure (brand palette) showing partial charges / dipoles, or use `lewis_structure`.")
    if "gas" in t or "pressure" in t or "volume" in t or "kinetic molecular" in t:
        return h("use `line_graph(path, [('PV', xs, ys)], xlabel=..., ylabel=...)` from tools.figures (e.g. an inverse P-V curve) — import from tools.figures.")
    if "solubility" in t or "concentration" in t or "vapor pressure" in t or "colligative" in t or "classifying solutions" in t or "precipitation" in t:
        return h("use `line_graph` or `bar_chart` from tools.figures (e.g. a solubility-vs-temperature curve), or `composition_pie` from tools.figures_chem.")
    if "half-life" in t or "half life" in t or "radioactiv" in t or "transmutation" in t or "nuclear" in t:
        return h("use `line_graph(path, [('decay', xs, ys)], xlabel='time (half-lives)', ylabel='amount remaining (%)')` from tools.figures for a decay curve.")
    if "redox" in t or "oxidation" in t or "reduction" in t or "half-reaction" in t or "electrochemical" in t:
        return h("write a small CUSTOM matplotlib figure (brand palette) of an electrochemical cell (two electrodes, electron flow), or a simple oxidation-number number line.")
    if "balancing" in t or "equation" in t or "conservation" in t or "types of chemical" in t:
        return h("use `particle_model` from tools.figures_chem (before/after particle counts to show conservation), or a `bar_chart` of atom counts.")
    if "mole" in t or "stoichiometry" in t or "empirical" in t or "percent" in t:
        return h("use `bar_chart` from tools.figures (e.g. molar masses) or `dimensional_analysis_track`/`composition_pie` from tools.figures_chem.")
    if "ph" in t or "indicator" in t or "arrhenius" in t or "bronsted" in t or "neutralization" in t:
        return h("use `titration_curve` from tools.figures_chem, or a CUSTOM pH-scale color bar in the brand palette.")
    if "review" in t:
        return h("use `classification_tree` from tools.figures_chem as a course concept-map anchor.")
    return h("choose any fitting builder from tools.figures_chem (particle_model, bar_chart via tools.figures, line_graph) or a clean CUSTOM brand-palette figure; include at least one figure.")


SCHEMA_BLOCK = """\
REQUIRED HEADINGS (the build FAILS if any are missing — match the Unit 1 exemplar exactly):
- Teacher_Guide.md (14, in order): `# <Title> — Teacher Guide`; `## Cover`; `## Curated Resources (from East Meadow Scope & Sequence)` with sub-headings `### NYSSLS Standards`, `### Phenomenon`, `### Javalab / Labs`, `### Assessments`; `## Lesson Overview`; `## Phase 1 · Engage *(0 – 10 min)*`; `## Phase 2 · Explore *(10 – 30 min)*`; `## Phase 3 · Explain *(30 – 36 min)*`; `## Phase 4 · Elaborate *(36 – 40 min)*`; `## Phase 5 · Evaluate *(40 – 42 min)*`; `## Common Misconceptions`; `## Access & Differentiation`; `## Strategy Spotlight`; `## NYSSLS Observation Checklist Crosswalk`; `## Companion Materials`; `## Key Vocabulary (max 3)`.
- Student_Worksheet.md (8): `## Phenomenon`, `## Notice & Wonder`, `## Initial Model`, `## Investigation`, `## Make It Make Sense`, `## Vocabulary in Action`, `## Revise Your Model`, `## Exit Ticket` (+ title block + `Name: ___  Date: ___  Period: ___`).
- Student_Notes.md (5): `## Learning Targets`, `## Key Vocabulary`, `## Guided Notes`, `## Worked Example`, `## Summary` (+ title block).
- Answer_Key.md (4): `## Cover`, `## Make-It-Make-Sense Answers`, `## Exit Ticket Answer`, `## Closing Reflection (rubric)`.
RULES: minute-by-minute phase sub-headings with block-quoted sample teacher language + anticipated student responses; ABCs = Explore (activity) BEFORE Explain (vocabulary); introduce EXACTLY ≤3 vocabulary terms in Phase 3 (second half); fill the 8-row NYSSLS Observation Checklist Crosswalk; keep the Exit Ticket values/examples DISTINCT from the worksheet practice; never bold the correct option in any multiple-choice list; embed the figure(s) with descriptive alt text in the Teacher Guide and at least one student doc."""


def lesson_prompt(unit, L, chip):
    path = f"{ROOT}/{unit['unitDir']}/{L['lessonDir']}"
    return f"""You are authoring ONE chemistry lesson for the East Meadow refactor — four finished, classroom-ready Markdown documents that build to DOCX, plus its figure(s). Repo root: /Users/hoopie/Projects/Curricula. Branch chemistry-east-meadow-refactor is checked out. venv: `source .venv/bin/activate`. DO NOT run any git command — the orchestrator commits.

CONTEXT — this lesson:
- Unit: {unit['unitName']} (folder {unit['unitDir']})
- Lesson topic: {L['topic']}
- Key sub-topics (from the Scope & Sequence): {L['subTopics'] or '—'}
- NYSSLS standard(s): {L['nyssls'] or 'Foundational skill supporting this unit (state the SEP/CCC it builds).'}
- Anchoring phenomenon (from the Scope & Sequence — expand it into a vivid 5E hook): {L['phenomenon'] or '(none given — craft a local, relatable phenomenon for this topic)'}
- Suggested activities / labs: {L['labs'] or '—'}
- Suggested assessments: {L['assessments'] or '—'}
- Strategy chip to feature (use this one; you may add RESTORATIVE CIRCLE if it is a natural unit-opener): {chip}

FIRST, read for format/voice/depth (do not skip): the Unit 1 exemplars
`{ROOT}/01_Safety_and_Measurement/01_Lab_Safety/` (qualitative) and
`{ROOT}/01_Safety_and_Measurement/06_Gram_Formula_Mass/` (quantitative) — all four .md each — and the schema `tools/lesson_schema.yaml`.

WRITE the four files into: `{path}/`
(Create the folder and a `figures/` subfolder if needed.)

{SCHEMA_BLOCK}

FIGURE: create the `figures/` dir and render at least one clean, brand-styled figure into it, then reference it. {figure_hint(L['topic'], L['subTopics'])}
Use the project sys.path bootstrap when running a render snippet, e.g.:
```
source .venv/bin/activate
python - <<'PY'
import sys; sys.path.insert(0, '.')
from tools.figures_chem import *   # particle_model, bohr_model, lewis_structure, classification_tree, heating_curve, titration_curve, reaction_energy_diagram, periodic_trend, composition_pie, separation_apparatus, density_graph
from tools.figures import PURPLE, BLUE, INK, ACCENT2, GREEN, GRID, line_graph, bar_chart
# render into {path}/figures/<name>.png with a descriptive filename
PY
```
Figures must be deterministic (no random / datetime). The chemistry MUST be correct (formulas, masses, balanced equations, signs).

BUILD (the gate):
```
source .venv/bin/activate
python tools/build_lessons.py --root {ROOT} {unit['unitDir']}/{L['lessonDir']}
```
Expected `Built 4 artifacts`, 0 FAILED. If a validation error prints, FIX the markdown and rebuild until clean. Confirm the figure(s) embed.

Return a StructuredOutput with: status ("DONE" or "BLOCKED"), the lesson path, figureCount, and a one-line note. Do NOT git commit."""


def unit_plan_prompt(unit):
    lessons_tbl = "\n".join(
        f"  {L['topicIdx']+1:02d} | {L['topic']}" for L in unit["topics"])
    path = f"{ROOT}/{unit['unitDir']}"
    return f"""You are authoring the Unit Plan for a chemistry unit. Repo root: /Users/hoopie/Projects/Curricula. Branch chemistry-east-meadow-refactor checked out. venv: `source .venv/bin/activate`. DO NOT run git — the orchestrator commits.

Unit: {unit['unitName']} (folder {unit['unitDir']}), {len(unit['topics'])} lessons:
{lessons_tbl}

FIRST read the exemplar `{ROOT}/01_Safety_and_Measurement/Unit_Plan.md` and the schema `tools/lesson_schema.yaml` (`unit_plan_required_headings`: `Cover`, `Unit Scope (from East Meadow Scope & Sequence)`, `Pacing Calendar`, `Strategy Rotation`, `NYSSLS Coverage Matrix`, `Vocabulary Scope`).

WRITE `{path}/Unit_Plan.md` with ALL SIX required H2 headings, mirroring the exemplar's table style:
- Cover: "Unit {unit['unitIdx']}: {unit['unitName']}", "East Meadow Schools × Valley Stream Central High School District", "{len(unit['topics'])} lessons · ~{len(unit['topics'])} periods (42 min)", "Format: DOCX (Teacher Guide · Student Worksheet · Student Notes · Answer Key per lesson)".
- Unit Scope: 1-paragraph overview + a lesson table (number | lesson | core idea) for the {len(unit['topics'])} lessons above.
- Pacing Calendar: Day | Lesson | Phenomenon anchor | Strategy (one row per lesson).
- Strategy Rotation: which lessons use HOCHMAN / ACTIVE LEARNING / BTC / RESTORATIVE CIRCLE; note SEL + ELL/SPED + literacy appear every lesson.
- NYSSLS Coverage Matrix: PE/Focus | Description | Lessons (use the standards from this unit's topics).
- Vocabulary Scope: "Three terms maximum per lesson, introduced in the second half." + a table (lesson | its ≤3 terms). If a lesson's docs already exist in `{path}/`, read their `## Key Vocabulary (max 3)` to fill this accurately; otherwise give your best terms.

BUILD (gate):
```
source .venv/bin/activate
python tools/build_lessons.py --root {ROOT} {unit['unitDir']}
```
This builds the Unit Plan plus all lessons in the unit. Expected: no FAILED line (it prints the artifact count). If the Unit Plan fails validation, fix and rebuild. (Lessons were authored separately; if a lesson fails, just note it — do not rewrite it.)

Return a StructuredOutput with status ("DONE"/"BLOCKED"), the unit path, and a one-line note. Do NOT git commit."""


def build_units():
    units = []
    for u in MANIFEST:
        lessons = []
        for i, L in enumerate(u["topics"]):
            chip = CHIPS[i % len(CHIPS)]
            lessons.append({"lessonDir": L["lessonDir"], "prompt": lesson_prompt(u, L, chip)})
        units.append({
            "unitIdx": u["unitIdx"], "unitDir": u["unitDir"],
            "lessons": lessons, "unitPlanPrompt": unit_plan_prompt(u),
        })
    return units


JS_TEMPLATE = """export const meta = {{
  name: 'chem-units-build',
  description: 'Author all remaining chemistry lessons (Units 2-14) as 5E DOCX',
  phases: [{{ title: 'Lessons', detail: 'one agent per lesson: figures + 4 docs + build' }},
           {{ title: 'UnitPlans', detail: 'one agent per unit plan' }}],
}}

const STATUS_SCHEMA = {{
  type: 'object',
  properties: {{
    status: {{ type: 'string' }},
    path: {{ type: 'string' }},
    figureCount: {{ type: 'number' }},
    note: {{ type: 'string' }},
  }},
  required: ['status', 'note'],
}}

const UNITS = {units_json}

const targetIdx = (typeof args === 'object' && args && args.unitIdx) ? args.unitIdx : null
const units = targetIdx ? UNITS.filter(u => u.unitIdx === targetIdx) : UNITS
const nLessons = units.reduce((n, u) => n + u.lessons.length, 0)
log(`Building ${{units.length}} unit(s), ${{nLessons}} lessons + ${{units.length}} unit plans`)

phase('Lessons')
const pairs = units.flatMap(u => u.lessons.map(L => ({{ u, L }})))
const lessonResults = await parallel(pairs.map(({{ u, L }}) => () =>
  agent(L.prompt, {{ label: u.unitDir + '/' + L.lessonDir, phase: 'Lessons', schema: STATUS_SCHEMA }})))

phase('UnitPlans')
const planResults = await parallel(units.map(u => () =>
  agent(u.unitPlanPrompt, {{ label: u.unitDir + '/Unit_Plan', phase: 'UnitPlans', schema: STATUS_SCHEMA }})))

const lessons = lessonResults.filter(Boolean)
const plans = planResults.filter(Boolean)
const blocked = lessons.filter(r => r && r.status !== 'DONE')
log(`Lessons done: ${{lessons.filter(r => r && r.status === 'DONE').length}}/${{pairs.length}}; plans: ${{plans.length}}/${{units.length}}; blocked: ${{blocked.length}}`)
return {{ lessons, plans, blocked }}
"""


def main():
    units = build_units()
    js = JS_TEMPLATE.format(units_json=json.dumps(units, ensure_ascii=False))
    out = Path("tools/chem_build_workflow.mjs")
    out.write_text(js, encoding="utf-8")
    print(f"Wrote {out} ({len(js)//1024} KB) — {len(units)} units, "
          f"{sum(len(u['lessons']) for u in units)} lessons")


if __name__ == "__main__":
    main()
