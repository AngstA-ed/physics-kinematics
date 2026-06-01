# Parallel Circuits — Teacher Guide

## Cover

**Unit: Current Electricity — Lesson 04: Parallel Circuits**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: ACTIVE LEARNING

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

This lesson supports **HS-PS3-6**: *"Analyze data to support the claim that Ohm's Law describes the mathematical relationship among the potential difference, current, and resistance of an electric circuit."* Students apply V = I·R to a multi-path circuit, discover that each branch sees the full source voltage, that branch currents add to the total, and that the equivalent resistance follows 1/R_total = Σ(1/R). It completes the series/parallel pair begun in Lesson 03.

### Phenomenon

- Home outlets — unplug one lamp and the others stay lit (house wiring is parallel): <https://www.youtube.com/results?search_query=why+are+house+circuits+wired+in+parallel>
- Parallel-resistor walkthrough (Khan Academy, "Parallel resistors"): <https://www.khanacademy.org/science/physics/circuits-topic/circuits-resistance/a/ee-parallel-resistors>

### Javalab / Labs

- PhET Circuit Construction Kit: DC — build a battery with two or three resistor branches; measure the voltage across each branch and the current in each branch and in the main wire: <https://phet.colorado.edu/en/simulations/circuit-construction-kit-dc>

### Assessments

- PhET CCK-DC parallel data table (branch voltages; branch and total currents) — formative during Explore.
- Exit ticket below; full key in `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | HS-PS3-6 (core — Ohm's Law across parallel branches) |
| **CCC focus** | Systems and System Models — multiple independent paths; a system can keep functioning when one branch fails. |
| **Strategy chips** | ACTIVE LEARNING (build-measure-predict at PhET stations) |
| **Materials** | Devices for PhET CCK-DC; whiteboards; calculators; (optional) a power strip with several plugged-in lamps for the hook. |
| **Safety** | Low-voltage / simulated circuits only. Never demonstrate house wiring with real mains. |
| **Prior knowledge** | Lessons 01–03 — Ohm's Law V = I·R; series rules (single path, current same, R adds). |

**Lesson objectives — students can:**

- Identify a **parallel circuit** and explain why each **branch** has the same voltage across it.
- Explain why branch currents add to the total current, and why one branch can fail while others keep working.
- Compute the **equivalent resistance** of parallel resistors using 1/R_total = 1/R₁ + 1/R₂ + … and find branch currents.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–2 min · Opening Connection (SEL)

One-sentence whip-around: *"Name a system in your life with a 'backup path' — where if one option fails, you still have another way through."* Hold the idea of independent paths.

### 2–7 min · Phenomenon hook — home outlets

**Teacher actions.** Plug three lamps into a power strip; all are lit. Unplug one — the other two stay bright. Contrast with yesterday's series string, where one removal killed everything.

**Sample teacher language:**

> "Yesterday one missing bulb killed the whole string. Today I unplug one lamp and the others don't even flicker. What's different about how these are wired?"

**Anticipated student responses:**

- "They each have their own wire." — yes; separate branches / paths.
- "The electricity has another way to go." — capture; multiple paths.
- "Each one is connected straight to the outlet." — each branch sees the full voltage.

### 7–10 min · Notice & Wonder + Turn-and-Talk #1

> "Turn to your partner: if each lamp has its own path to the source, what must be true about the voltage each lamp gets? Use the word *branch*."

Target: each branch gets the full source voltage.

### Bridge to Phase 2

Each student writes a one-sentence **initial model**: "Unplugging one lamp leaves the others lit because ______."

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–14 min · Initial Model (silent / individual)

Prompt on the board:

> *"Sketch three lamps each wired directly across the same battery (three branches). Predict: does each lamp get the full battery voltage or a share of it? Does the same current flow through all three?"*

### 14–30 min · Investigation — PhET CCK-DC parallel circuit

Students build a 12 V battery with three parallel resistor branches (6 Ω, 3 Ω, 2 Ω).

1. **Measure the voltage** across each branch. Are they equal?
2. **Measure the current** in each branch and in the main wire. How do the branch currents relate to the total?
3. **Open one branch** — what happens to the other branches?

**Teacher facilitation language:**

> "Is the voltmeter reading the same across all three branches? What does that tell you?"
> "Add the three branch currents — how do they compare to the current in the main wire?"
> "When you open one branch, do the others change? Why does that match the lamp demo?"

Use the schematic and the branch-current bar chart to consolidate:

![Schematic of a parallel circuit: a 12-volt battery on the left connects to a top rail and a bottom rail, with three vertical resistor branches between them labeled R-one 6 ohms, R-two 3 ohms, and R-three 2 ohms; the total current splits among the branches.](figures/parallel_circuit.png)

![Bar chart of branch currents in a parallel circuit: 2 amps, 4 amps, and 6 amps in the three branches, summing to a 12-amp total.](figures/parallel_branch_currents.png)

### Teacher facilitation during Explore

- **What to look for** — groups stating "the voltage is the same across every branch" and "the branch currents add to the main current."
- **What to resist** — handing them 1/R_total = Σ1/R; let them compute each branch current with I = V/R first, then add.
- **What to redirect** — students surprised that R_total is *less* than the smallest resistor: more paths means less total opposition.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Across your measurements, what three rules describe a parallel circuit?"

Target consensus:

> "(1) The voltage is the same across every branch. (2) The branch currents add up to the total. (3) The equivalent resistance is *less* than any single branch."

### 33–36 min · Vocabulary introduction (≤ 3 terms)

**Sample teacher language:**

> "A circuit with more than one path is a **parallel circuit**. Each separate path is a **branch**, and every branch has the full source voltage across it. The single resistor that could replace them all is the **equivalent resistance** — but in parallel you combine reciprocals: 1/R_total = 1/R₁ + 1/R₂ + 1/R₃. Because you're adding paths, R_total comes out *smaller* than any one branch."

Reference relationships to post: **V = I·R**; parallel **1/R_total = 1/R₁ + 1/R₂ + …**; power **P = V·I = I²·R**.

### Discussion prompts to deploy here

- "Two 4 Ω resistors are in parallel across 8 V. Find each branch current and the total."
  - *Sample response:* "Each branch: I = 8/4 = 2 A; total = 4 A; R_total = 2 Ω."
- "Why is R_total smaller than the smallest branch resistor?"
  - *Sample response:* "Every added branch gives charge another path, so overall it's easier for current to flow."

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–38 min · Apply — add a branch

> *"You add a fourth lamp in parallel. Predict what happens to the total current drawn from the battery and to the equivalent resistance. Explain in one sentence."*

Target: equivalent resistance drops further, so the total current the battery delivers *increases*.

### 38–40 min · Return to the phenomenon

> "Explain, in one sentence using *parallel* and *branch*, why unplugging one lamp leaves the others lit."

Target: "The lamps are in parallel — each on its own branch — so opening one branch leaves the other branches (and their full voltage) untouched."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

> *"A 12 V battery is connected to two parallel resistors: 4 Ω and 6 Ω.
> (a) What is the voltage across each resistor?
> (b) Find the current in each branch.
> (c) Find the total current and the equivalent resistance (1/R_total = 1/4 + 1/6)."*

Expected: (a) 12 V across each; (b) I₄ = 3 A, I₆ = 2 A; (c) total = 5 A, R_total = 12/5 = 2.4 Ω. See `Answer_Key.docx`.

**Closing Reflection (SEL, 30 seconds):**

> "What surprised you most about parallel circuits compared with yesterday's series circuits?"

---

## Common Misconceptions

- **Misconception:** "The voltage splits among the parallel branches." → **Correction:** Each branch gets the *full* source voltage; it's the *current* that splits among the branches.
- **Misconception:** "Adding a parallel branch raises the total resistance." → **Correction:** Adding branches *lowers* the equivalent resistance (more paths for current), so the battery delivers more total current.
- **Misconception:** "Opening one branch changes the others." → **Correction:** Branches are independent; opening one leaves the others' voltage and current unchanged.

---

## Access & Differentiation

- **ELL/ENL supports:** Sentence frames: *"In a parallel circuit, the voltage across each branch is ___."* / *"The branch currents ___ to the total."* Word box: {same, add, branch, multiple paths, full voltage}. Color-code each branch a different color on the schematic.
- **IEP/SPED supports:** Provide a pre-built PhET file and a fill-in table (branch voltages, branch currents). Give a step-by-step reciprocal template for 1/R_total with the fractions pre-set.
- **Extensions:** Have students show that for two parallel resistors R_total = (R₁·R₂)/(R₁+R₂), and explain why home circuits use parallel wiring (each device gets full voltage and operates independently) while computing the power each branch draws (P = V²/R).

---

## Strategy Spotlight

**ACTIVE LEARNING.** As in Lesson 03, students build-measure-predict at PhET stations. The active hinge here is *opening one branch* and watching the others stay lit — the experiential counterpart to yesterday's series break. Run a predict → measure → reconcile loop on branch voltage (predict equal, confirm) and on total current (predict the sum, confirm). Have groups post their three-rule consensus side-by-side with the series rules from Lesson 03 to make the contrast explicit.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — home outlets / power strip |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — branch voltage), Phase 3 (TT#2 — three parallel rules) |
| 3 | Students develop questions/models/procedures | Phase 1 (initial model), Phase 2 (build/measure/predict), Phase 4 (revise) |
| 4 | CCC defined and used | Lesson Overview · *Systems and System Models*, used in Phase 2 |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — parallel circuit / branch / equivalent resistance at 33–36 min |
| 6 | Revisit phenomenon with evidence | Phase 4 — why other lamps stay lit |
| 7 | ENL/SPED supports | Access & Differentiation block |
| 8 | Assessment check | Phase 5 — parallel Ohm's-law exit ticket |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **parallel circuit** — a circuit with more than one path for charge, so every branch has the same full source voltage across it
- **branch** — one of the separate parallel paths between the same two points; its current is set by its own resistance (I = V/R)
- **equivalent resistance** — the single resistance that could replace the branches; in parallel, 1/R_total = 1/R₁ + 1/R₂ + … (smaller than any branch)
