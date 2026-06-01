# Dimensional Analysis — Teacher Guide

## Cover

**Unit: Safety and Measurement — Lesson 04: Dimensional Analysis**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: HOCHMAN

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

**HS-PS1-7** — *"Use mathematical representations to support the claim that atoms, and therefore mass, are conserved during a chemical reaction."* Dimensional analysis is the quantitative engine beneath that standard. Before students can reason about moles, atoms, or grams in a reaction context, they must be able to move fluently between those scales using conversion factors. The 2025 NYS Chemistry Reference Tables supply Avogadro's number (6.02 × 10²³ particles/mol) as a given constant — students are expected to set up factor-label tracks and cancel units correctly, not derive the constant. Per East Meadow guidance, dimensional analysis appears in every stoichiometry, density, and solution concentration problem on the Regents assessment; fluency here pays dividends for the entire course.

The Cross-Cutting Concept of **Scale, Proportion, and Quantity** is the explicit lens: a conversion factor is a proportion — a ratio equal to exactly 1 — that lets you rescale a quantity without changing its physical meaning. That proportional bridge is what allows us to cross from the macroscopic scale (grams you can weigh) to the atomic scale (particles you cannot count individually).

### Phenomenon

A copper penny contains about 3.1 grams of copper. You could weigh that mass on a lab balance in thirty seconds. But how many individual copper atoms is that? The answer — roughly 2.9 × 10²² atoms — is a number so large it defies intuition. You cannot count it directly; you can only *convert* to it. The pathway from "3.1 g" to "2.9 × 10²² atoms" requires two conversion factors (g → mol, mol → atoms) set up so every unwanted unit cancels and only the target unit remains. That is the power, and the demand, of dimensional analysis.

**Driving question:** How do we convert between very large and very small quantities — atoms ↔ grams — using only multiplication and unit cancellation?

### Javalab / Labs

- **Factor-label card trains:** Pre-cut cards show quantities and conversion factors (1 mol / 6.02 × 10²³ atoms; 1 km / 1000 m; 1000 mL / 1 L). Students physically arrange cards in a chain so that unwanted units cancel diagonally (numerator of one card, denominator of the next), and only the target unit survives. The tactile act of flipping a card to cancel a unit builds the schema that the algebraic notation formalizes.
- **Metric-prefix conversion ladder:** Students convert across the metric prefix family (km ↔ m ↔ cm ↔ mm; L ↔ mL; kg ↔ g ↔ mg) by writing each step as a conversion factor and multiplying across the track. The Reference Table prefix list is used throughout.
- **Mol ↔ atoms using Avogadro's number:** Using the `figures/atoms_to_moles.png` image as a model, students set up tracks converting given moles to atoms and given atom counts to moles. Calculators required; scientific notation from Lesson 03 is applied to express final answers.

### Assessments

- **Conversions quiz** (district checkpoint, following lesson; see `Assessments/` folder once created): Avogadro's number ↔ moles; metric prefix conversions (unit-factor setup required, not just mental math).
- **Exit Ticket** (Phase 5): three items — convert 3.0 mol Cu to atoms; convert 5,400 mg to g; explain in one sentence how you know the units are right. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | HS-PS1-7 (mathematical representations linking atomic and macroscopic scales) |
| **CCC focus** | Scale, Proportion, and Quantity — a conversion factor is a ratio equal to 1 that acts as a proportional bridge between scales; using it does not change the physical quantity, only the unit used to express it. |
| **Strategy chips** | HOCHMAN — Because/But/So expansion on WHY units cancel; kernel sentence → elaboration sequence in Phase 4 |
| **Materials** | Factor-label cards (pre-cut, one set per group), metric-prefix reference (or 2025 NYS Chemistry Reference Table), calculators, `figures/atoms_to_moles.png` projected |
| **Safety** | No hazardous chemicals. Pencils, cards, and calculators only. |
| **Prior knowledge** | Lessons 01–03 — SI units and metric prefixes (Lesson 02); scientific notation (Lesson 03). Students should be comfortable moving a decimal and writing powers of ten before this lesson builds on those skills. |

**Lesson objectives — students can:**

- Set up a factor-label conversion track so that unwanted units cancel diagonally (numerator × denominator), leaving only the target unit.
- Convert between metric units (km, m, cm, mm; L, mL; kg, g, mg) using conversion factors written as ratios.
- Convert between moles and atoms (or molecules or ions) using Avogadro's number from the Reference Table.
- Explain, using Scale, Proportion, and Quantity, why a conversion factor equals 1 and why multiplying by it does not change the physical quantity.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers: *"Think of a time you had to convert something in your life — money, a recipe, a sports stat, miles vs. kilometers. What did you do?"* One round, one sentence each, no judgment. This surfaces the intuition that converting is universal, not exotic — students already do it. Keep it moving; the goal is connection, not thoroughness.

Then post the **Do Now**:

> *"A copper penny has a mass of about 3.1 grams. A scale can measure that in seconds. But the same penny contains roughly 29,000,000,000,000,000,000,000 copper atoms — a number with 22 zeros. Write one sentence: how would you even begin to figure out a number that large from a mass that small?"*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "I would need some kind of formula or equation." — affirm; ask: does that formula need to connect grams and atoms somehow? What connects them?
- "I don't know, that number is impossible to count." — exactly right; validate the intuition, and tell them that is the whole point: you cannot count atoms, but you *can* convert to them if you know the right ratio.
- "You divide or multiply by something?" — close; the question for today is: what do you multiply by, and how do you know you set it up in the right direction?

### 3–8 min · Phenomenon hook — the penny and the uncountable

**Teacher actions.** Hold up a penny (or project a close-up image). Tell the story:

> "This penny has a mass of about 3.1 grams. I can measure that with a balance in this room. But copper is made of atoms. Each copper atom has a mass of about 1.06 × 10⁻²² grams — so small it is invisible. The question is: how many of them are there in 3.1 grams? The answer is about 2.9 × 10²² atoms. That's roughly 29 sextillion. Nobody has ever counted them one at a time. But a chemist can *calculate* that number from the mass — in about thirty seconds — using a tool called dimensional analysis."

Project the `figures/atoms_to_moles.png` figure:

![A factor-label railroad-track grid showing the conversion 2.5 mol Cu × (6.02 × 10²³ atoms / 1 mol); the numerator of the first box contains 2.5 mol Cu, the numerator of the second box contains 6.02 × 10²³ atoms, the denominator of the second box contains 1 mol; diagonal slashes show that "mol" in the numerator of the first box cancels with "mol" in the denominator of the second box, leaving atoms as the surviving unit; the result 1.505 × 10²⁴ atoms appears after the equals sign.](figures/atoms_to_moles.png)

**Sample teacher language:**

> "Look at this figure. The boxes form a track — like railroad cars. The first car holds what you *have*: 2.5 mol of copper. The second car holds a conversion factor: 6.02 × 10²³ atoms on top, 1 mol on the bottom. Do you see how 'mol' appears on the top of the first car and the bottom of the second car? Those cancel — they cross each other out diagonally. What's left? Only 'atoms.' That's your target unit. That's dimensional analysis."

**Anticipated student responses:**

- "Why do you put it upside down?" — great question; the conversion factor can be written either way. You choose the orientation that puts the unit you want to cancel in the denominator. You'll see why when you try it.
- "Where does 6.02 × 10²³ come from?" — it's Avogadro's number, the number of atoms (or molecules or formula units) in one mole. It's on the Reference Table — you don't have to memorize it.
- "Is this just like the metric prefixes from Lesson 02?" — yes, exactly. Converting km to m is the same tool. You'll practice both today.

**Driving question** (post on the board and leave it there):

> *How do we convert between very large and very small quantities — atoms ↔ grams — using only multiplication and unit cancellation?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the figure. Then:

> "Turn to your partner: Look at the track in the figure again. If I had set up the conversion factor as (1 mol / 6.02 × 10²³ atoms) instead of (6.02 × 10²³ atoms / 1 mol), what would the surviving unit be? Would that give me what I want?"

Target insight: flipping the fraction flips the surviving unit — if "atoms" goes in the denominator, the answer would come out in mol²/atom, which is meaningless. The direction you write the fraction decides the direction of travel.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–15 min · ABCs Activity — building conversion trains before the vocabulary

**Before any formal vocabulary is introduced**, students build intuition through a card-sequencing challenge. Each pair or trio receives a small set of pre-cut factor-label cards and a starting quantity. The task is purely physical: arrange the cards in a line so that the unit you want to get rid of cancels, and only the unit you want survives.

**Card set A — metric conversions (easier entry):**

Starting quantity: **2.5 km**

Cards available (each printed on a half-index card):

| Card | Numerator | Denominator |
|---|---|---|
| Card 1 | 1000 m | 1 km |
| Card 2 | 1 km | 1000 m |
| Card 3 | 100 cm | 1 m |
| Card 4 | 1 m | 100 cm |

Task: arrange the cards to convert 2.5 km → cm. Students write the chain on their worksheet.

**Teacher facilitation language (circulate):**

> "You have 2.5 km on the left. What unit do you want on the right? Centimeters. So work backwards: what card gets you from meters to centimeters? Now what gets you from km to meters? Now put them in order."

> "Look at where the km unit is sitting — is it in the numerator or denominator? For it to cancel, you need km to appear once on top and once on the bottom. Which card puts km on the bottom?"

**Card set B — atoms/moles (one step, using the figure as a reference):**

Starting quantity: **4.0 mol Cu**

Cards available:

| Card | Numerator | Denominator |
|---|---|---|
| Card 5 | 6.02 × 10²³ atoms | 1 mol |
| Card 6 | 1 mol | 6.02 × 10²³ atoms |

Task: convert 4.0 mol Cu → atoms. Then: convert 1.204 × 10²⁴ atoms Cu → mol (flip the card).

**Anticipated student responses during ABCs:**

- Students who flip Card 2 to cancel km → correct move; praise the insight that you control the orientation.
- "I get km² in the denominator — that's wrong." — right observation; ask what went wrong: two km units in the same position instead of canceling.
- "Can I use more than two cards?" — yes; multi-step conversions use more cars on the track. That's the power of the method.

### 15–22 min · Initial Model — the railroad track

**Prompt on the board:**

> *"Before we name the method: draw a railroad track (factor-label grid) that converts 750 mL into liters. Use the conversion 1 L = 1000 mL. Show the unit cancellation with diagonal slashes."*

Students work individually on their worksheets for 3 minutes, then compare with a partner.

Target answer:

> 750 mL × (1 L / 1000 mL) = 0.75 L

The "mL" in the numerator of the starting quantity cancels with the "mL" in the denominator of the conversion factor; only "L" survives.

**Teacher facilitation language:**

> "Look at your partner's track. Are the units canceling diagonally? If 'mL' appears in the numerator of box 1 and the numerator of box 2, do they cancel? No — they only cancel when one is on top and the other is on the bottom. That is the whole rule. Everything else follows from that."

**Anticipated student responses:**

- "I got 750,000." — they multiplied instead of dividing; ask: which unit survived? If they get "mL²/L," the setup was wrong. Work backwards from the unit.
- "I set it up as (1000 mL / 1 L) and got 750,000 mL²/L." — name the unit they got; it's not liters. Ask: what change to the fraction would put mL on the bottom instead?
- "I just moved the decimal — I didn't need the track." — fair; for one step you might do it mentally. Ask: can you do the mol → atoms problem mentally? The track is what keeps you honest when the numbers get large.

### 22–30 min · Investigation — group conversion practice

Groups of three or four work through a set of practice conversions. Each group writes their complete factor-label track (including all units at every step), not just the numerical answer.

**Practice set (written on the board or distributed as a half-sheet):**

1. Convert 2.5 km → cm (two-step: km → m → cm).
2. Convert 0.75 mol of water molecules → molecules (one-step: mol → molecules, using Avogadro's number).
3. Convert 250 mL → L (one-step: mL → L).
4. Convert 1.806 × 10²⁴ atoms of copper → mol (one-step: atoms → mol, Avogadro's number inverted).

**Teacher facilitation prompts (circulate):**

> "For problem 1, your first conversion factor should cancel km. Write the unit you want to cancel in the denominator. Now what survives? Now write a second conversion factor to cancel that surviving unit and leave cm."

> "For problem 4, you're going backwards — from atoms to mol. Look at your card set: which orientation of the Avogadro card gets atoms in the denominator?"

> "For all four: write the unit at every step. If you skip units, you can't check whether they cancel."

**Anticipated student responses:**

- On problem 1: many students will write only one conversion factor (km → m) and stop. Ask: "The question asked for centimeters. What unit do you have now? What do you still need to cancel?"
- On problem 2: "What's Avogadro's number again?" — redirect to the Reference Table. "It's there. What page? What does it say?"
- On problem 4: "Do I divide or multiply?" — name the unit: "atoms × (1 mol / 6.02 × 10²³ atoms). What cancels?" Let the unit-tracking answer the question.

### 28–30 min · Reconnect + surface the method

Bring groups back together. Ask one group to write problem 1's track on the board. Ask the class:

> "Look at this track. At every slash, what happened? What survived? Could we have done it in one step?"

Surface the key idea: dimensional analysis is not about arithmetic — it is about *unit tracking*. The arithmetic is what a calculator does. The thinking is the track.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look at problem 2 from the practice set — 0.75 mol → molecules. Turn to a partner: in your own words, explain why the conversion factor (6.02 × 10²³ molecules / 1 mol) equals exactly 1. How can a fraction with such different-looking numbers on top and bottom be equal to 1?"

Target consensus: a conversion factor equals 1 because the numerator and denominator represent the *same amount* — 6.02 × 10²³ molecules and 1 mol are two different ways of expressing the same quantity, just as 12 inches and 1 foot are the same length. Multiplying by 1 never changes the value of a quantity.

> "If the conversion factor equals 1, and multiplying anything by 1 leaves it unchanged, then why does the *number* change when we multiply by it?"

Target: the number changes because the unit changes. 0.75 mol and 4.515 × 10²³ molecules represent the same amount of substance — you just changed the units used to express it, the same way 1 foot and 12 inches are the same length with different units.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name what we've been doing. Every conversion track we built started by asking: what ratio of units equals 1? That ratio — any fraction where the numerator and denominator represent the same quantity — is a **conversion factor**. 1 mol / 6.02 × 10²³ atoms is a conversion factor. 1000 m / 1 km is a conversion factor. 1 L / 1000 mL is a conversion factor. Each one equals 1, so multiplying by it is safe — you never change the quantity, only the label."

> "The method itself — solving a problem by tracking units across multiplied ratios, and canceling the units you don't want — is called **dimensional analysis**. 'Dimension' is another word for unit type. 'Analysis' means you are systematically working through the dimensions until only the one you want survives. Every conversion problem in chemistry, physics, biology, engineering, and everyday life can be solved this way."

> "The third term connects back to Lesson 02. The prefixes — kilo-, centi-, milli- — are **metric prefixes**. Each one scales a base unit by a power of ten. Kilo- means 1000 (10³), centi- means 1/100 (10⁻²), milli- means 1/1000 (10⁻³). These are the conversion factors built into the metric system. When you convert 2.5 km to cm, you are applying two metric prefixes in sequence — each one is a ratio equal to 1."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "If a conversion factor equals 1, why can't you just multiply by any fraction — like (2 / 3)?" — *Expected response:* because 2/3 does not represent the same quantity on top and bottom. A conversion factor must express a genuine equality — 1 km = 1000 m, so the fraction (1 km / 1000 m) is truly equal to 1.
- "What would happen if you multiplied 3.0 mol × (6.02 × 10²³ atoms / 1 mol) on a calculator but forgot to write the units?" — *Expected response:* you might get the right number but have no way to know whether the answer is in atoms, mol, or something else entirely. The units are the check.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the model + Because/But/So expansion

Students return to their Initial Model conversion (750 mL → L). They annotate it with vocabulary: label the conversion factor, label the metric prefix relationship, and write the unit cancellation using the term "dimensional analysis."

Then run a **Because / But / So** sentence. Starter on the board:

> *"A student sets up the conversion 0.75 mol × (1 mol / 6.02 × 10²³ atoms)."*

Model one aloud:

> "This setup gives the wrong answer **because** the unit 'mol' appears in the *numerator* of the starting quantity and the *numerator* of the conversion factor — they cannot cancel — **but** a conversion factor can be written either way (upright or inverted), **so** you should flip the fraction to (6.02 × 10²³ atoms / 1 mol), which puts 'mol' in the denominator and allows it to cancel, leaving 'atoms' as the surviving unit."

Then have students write their own B/B/S using one of these starters:

- *"A student converts 4.5 km to meters by multiplying 4.5 km × (1 km / 1000 m)…"*
- *"A student skips writing units in their conversion track and gets 2500 as an answer…"*

**Anticipated student responses:**

- "Because the km is on the wrong side." — good start; ask them to be more specific: "which side and why?" The B/B/S frame demands a causal chain.
- "Because there are no units, you don't know if 2500 is meters, centimeters, or something else." — excellent; that is the strongest version of the second starter. Push: "so what should they do?" (write units at every step and check the cancellation before calculating).

### 39–40 min · Return to the phenomenon

> "Return to our copper penny. I told you at the start that 3.1 grams of copper contains about 2.9 × 10²² atoms. Could you now set up the conversion track to check that? You'd need two steps: grams → mol (molar mass of Cu ≈ 63.5 g/mol from the Periodic Table), then mol → atoms (Avogadro's number). You don't need to calculate it — just draw the track and check that the right units cancel."

Target: 3.1 g Cu × (1 mol / 63.5 g) × (6.02 × 10²³ atoms / 1 mol). The "g" cancels in the first step, the "mol" cancels in the second step, and "atoms" survives.

> "That two-step track is how a chemist goes from something you can weigh on a balance to a number of atoms you can never count directly. That's the power — and the point — of dimensional analysis."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud:

> *(a) Convert 3.0 mol of Cu to atoms. Show the complete factor-label track.*
> *(b) Convert 5,400 mg to g.*
> *(c) In one sentence, how do you know your units are right?*

Expected answers are in `Answer_Key.docx`.

**Closing Reflection (SEL, 30 seconds):**

> "Today we built a method for crossing between scales — from the grams you can see to the atoms you cannot. In one sentence: what is one thing that surprised you today, and who did you figure something out with?"

Collect worksheets; note which students wrote complete unit tracks (with labels at every step) versus students who wrote only final numerical answers. Unit tracking is the skill — students who skip it are likely to make direction errors on multi-step conversions. Target those students for a brief check-in at the start of the next lesson.

---

## Common Misconceptions

- **Misconception:** "I can just move the decimal to convert metric units — I don't need a track." → **Correction:** For single-step metric conversions you can often do this mentally, but the track-building habit is what keeps students correct on multi-step conversions and on mol ↔ atoms ↔ grams chains. Students who skip the track reliably make direction errors ("I multiplied when I should have divided") because they have no unit-check to catch the error. Reinforce the track even when it feels redundant.
- **Misconception:** "The conversion factor (6.02 × 10²³ atoms / 1 mol) always goes numerator-on-top." → **Correction:** A conversion factor can be written either way. The choice depends on what you need to cancel. If you are going from mol → atoms, atoms goes on top. If you are going from atoms → mol, mol goes on top. The rule is: put the unit you want to *eliminate* in the denominator so it cancels with the numerator of the previous step.
- **Misconception:** "Multiplying by a conversion factor changes the amount of substance." → **Correction:** A conversion factor equals exactly 1 — numerator and denominator represent the same quantity in different units. Multiplying by 1 never changes the physical quantity; it only changes the label (unit) used to express it. 0.75 mol and 4.515 × 10²³ molecules describe exactly the same amount of substance.
- **Misconception:** "Dimensional analysis only works for the mole — it's a chemistry thing." → **Correction:** Dimensional analysis is a universal problem-solving method. Currency exchange, cooking conversions, speed/time/distance problems, and engineering design all use conversion factors and unit cancellation. The mole is just one application.
- **Misconception:** "I can check my answer by plugging numbers in — I don't need to check units." → **Correction:** Unit checking is the self-correction built into the method. If the surviving unit is not the target unit, the setup is wrong — regardless of what numerical result the calculator displays. Students who skip the unit check lose the main advantage of dimensional analysis.

---

## Access & Differentiation

- **ELL/ENL supports:** Pre-printed factor-label track template with cells labeled "numerator" and "denominator" in each box, and diagonal slash marks pre-drawn to show where cancellation happens. Sentence frame for explaining cancellation: *"I cancel ___ because it appears on the top and the bottom."* Word-choice box displayed on the board throughout: {conversion factor, dimensional analysis, metric prefix, cancel, numerator, denominator}. Pair the card-train activity with a visual reference showing the metric prefix ladder (kilo- ↔ base ↔ centi- ↔ milli-) with the multiplicative relationship (×1000, ×100, ×10) on each arrow.
- **IEP/SPED supports:** Begin with one-step conversions only (mL → L; g → mg) before introducing two-step or mol ↔ atoms conversions. Color-code units to cancel: mark the unit to cancel in red on both the numerator of one box and the denominator of the next; mark the surviving target unit in green. Provide the metric ladder visual at the student's desk (not just posted on the board). Calculator use permitted and expected for all arithmetic.
- **Extensions:** (1) Set up a two-step chain: grams of copper → mol → atoms (use 3.1 g Cu; molar mass of Cu = 63.5 g/mol from the Periodic Table). (2) Use dimensional analysis to convert a density problem: if the density of copper is 8.96 g/cm³, what is the mass of a 4.5 cm³ block? Show the conversion factor clearly. (3) How many seconds have elapsed in your lifetime? Set up a full multi-step chain: years → days → hours → minutes → seconds. This is the longest factor-label track in Unit 1 — try it.

---

## Strategy Spotlight

**HOCHMAN — Because/But/So expansion.** The Hochman Writing Method (Joan Hochman and the Writing Revolution) focuses on sentence-level writing as a thinking tool, not an assessment afterthought. The core technique for this lesson is the **Because / But / So** (B/B/S) sentence, which requires students to articulate a causal-consequential chain in a single compound sentence. In a conversion context, the chain is precisely the logic of dimensional analysis:

- **Because** names the reason a specific unit needs to cancel (the unit appears in the wrong position for the target; the conversion factor needs to be oriented so the unwanted unit sits in the denominator).
- **But** names the mechanism that is available (a conversion factor can be written either way — you choose the orientation).
- **So** names the action and result (flip the fraction; the unwanted unit cancels; the target unit survives).

**How to run it in this lesson (Phase 4):**

1. Post the starter on the board: *"A student sets up the conversion 0.75 mol × (1 mol / 6.02 × 10²³ atoms)."*
2. Model the complete B/B/S aloud (script in Phase 4 above) before asking students to write independently.
3. Give students 2 minutes to write their own B/B/S from one of the two provided starters. Circulate and look for: (a) does "because" name a unit-level error or a logical reason? (b) does "but" describe the mechanism, not just say "but it's wrong"? (c) does "so" give the correct action?
4. Cold-call two or three students to read aloud. Push for precision: "When you said 'because the unit is in the wrong place' — which unit, and which place? Top or bottom of which box?"

**Why B/B/S fits dimensional analysis:** The most common student error in conversion problems is a direction error — multiplying when they should divide, or vice versa — which is equivalent to writing the conversion factor upside-down. The B/B/S sentence forces students to name the *reason* a particular orientation is correct, which is a deeper level of understanding than correctly executing the arithmetic. A student who can write a grammatically complete and causally accurate B/B/S for a direction error is demonstrating that they understand the structure of the method, not just the procedure.

**CRSE connection:** The opening circle prompt (conversions in everyday life — money, recipes, sports stats) invites students to locate dimensional analysis in contexts that may be more culturally central to some students than metric-unit chemistry. Currency exchange is a literal conversion factor; recipe scaling is dimensional analysis. Acknowledging those contexts before the formal method honors the quantitative reasoning students already bring and makes the algebra feel like a formalization of something already known.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — copper penny atom count; return in Phase 4 with the two-step g → mol → atoms track |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — what happens if you flip the Avogadro fraction?); Phase 3 (TT#2 — why does a conversion factor equal 1?) |
| 3 | Students develop questions/models/procedures | Phase 2 ABCs card-train activity builds conversion intuition before vocabulary; Initial Model track; group investigation practice set |
| 4 | CCC defined and used | Lesson Overview · *Scale, Proportion, and Quantity*, explicit in Phase 3 vocabulary introduction and Phase 4 return-to-phenomenon |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: conversion factor / dimensional analysis / metric prefix |
| 6 | Revisit phenomenon with evidence | Phase 4 — students sketch the two-step g → mol → atoms track for 3.1 g of Cu; Phase 5 Exit Ticket applies the method to new values |
| 7 | ENL/SPED supports | Access & Differentiation block: pre-printed track template, sentence frame, word-choice box, color-coding, metric ladder visual, one-step scaffolding |
| 8 | Assessment check | Phase 5 — Exit Ticket (mol → atoms with full factor-label track; mg → g; unit-check explanation) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked conversion example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **conversion factor** — a ratio equal to 1 that relates two equivalent quantities expressed in different units (e.g., 1 mol / 6.02 × 10²³ atoms, or 1 km / 1000 m); because the numerator and denominator represent the same amount, multiplying by a conversion factor changes the unit without changing the physical quantity
- **dimensional analysis** — a problem-solving method in which units are tracked and canceled across a chain of multiplied ratios (the factor-label track) until only the target unit survives; it is universal — currency exchange, recipe scaling, stoichiometry, and engineering unit conversions all use the same structure
- **metric prefix** — a prefix attached to a base unit that scales it by a power of ten (kilo- = 10³, centi- = 10⁻², milli- = 10⁻³); each prefix relationship is a conversion factor equal to 1 (e.g., 1 km = 1000 m, so 1 km / 1000 m = 1)
