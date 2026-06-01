# STP & Standard Conditions — Teacher Guide

## Cover

**Unit: Solutions — Lesson 07: STP & Standard Conditions**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: ACTIVE LEARNING

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

No new content performance expectation is introduced in this lesson; it establishes a measurement convention that every later gas-law and solution calculation depends on. The work is anchored in the Science and Engineering Practice of **Using Mathematics and Computational Thinking** and the Cross-Cutting Concept of **Scale, Proportion, and Quantity**. Students learn that gas volume — unlike mass or the number of particles — changes with temperature and pressure, so a measured gas volume is meaningless unless the conditions are stated. STP (standard temperature and pressure) is the agreed-upon reference point that lets chemists report and compare results that anyone can reproduce.

For the 2025 NYSSLS-aligned Regents, students must read **standard temperature (273 K, 0 °C)** and **standard pressure (101.3 kPa, 1 atm)** from Reference Table A, and use the **molar volume of a gas at STP (22.4 L/mol)** from Table A as a conversion factor between moles of gas and liters of gas. Per East Meadow guidance, fluency with standard conditions is prerequisite to the combined-gas-law and molar-volume problems later in this unit and to molarity work, where "concentration" is only comparable when the temperature is fixed.

The Cross-Cutting Concept of **Scale, Proportion, and Quantity** is the explicit lens: at a fixed temperature, pressure and volume of a gas are inversely proportional (Boyle's Law), so the *same* sample of gas reports a different volume at different pressures. A standard reference removes that ambiguity.

### Phenomenon

Two lab groups each measure "the volume of one mole of carbon dioxide gas." Group A works on a cold morning near sea level and reports 22.4 L. Group B works in a hot classroom at a higher elevation and reports 25.1 L. Same amount of gas — the same 6.02 × 10²³ molecules, the same one mole — but two different volumes on the report sheet. Neither group made a mistake. Project the figure `figures/boyles_law_stp.png`: as a fixed sample of gas is squeezed to a smaller volume, its pressure climbs; let it expand and the pressure drops. The volume of a gas is a moving target.

**Driving question:** Why do scientists need a common "standard" set of conditions for reporting their results?

### Javalab / Labs

- **STP reference-table use:** Using Reference Table A from the 2025 NYS Chemistry Reference Tables, students locate and record the three standard-conditions values: standard temperature (273 K / 0 °C), standard pressure (101.3 kPa / 1 atm), and molar volume of a gas at STP (22.4 L/mol). They then convert moles of a gas to liters at STP, and liters of a gas at STP back to moles, using 22.4 L/mol as the conversion factor.
- **Standard-conditions discussion / Boyle's Law trace:** Students read `figures/boyles_law_stp.png` (an inverse pressure–volume curve for one mole of gas held at the STP temperature) and answer: at what volume does the curve cross 101.3 kPa? What happens to the volume if the pressure doubles? Why can't you report a gas volume without also reporting the temperature and pressure?
- **Javalab "Boyle's Law" gas simulation (optional digital):** the Javalab pressure–volume piston simulation lets students drag a piston and watch pressure change in real time, reproducing the inverse curve in the figure. No external URL is required for the core lesson; the printed figure carries the same evidence.

### Assessments

- **STP quick check** (district checkpoint, this lesson): students state standard temperature and standard pressure in two unit systems each, recall molar volume at STP, and convert between moles and liters of a gas at STP. See `Answer_Key.docx`.
- **Exit Ticket** (Phase 5): three items — state standard temperature and pressure with units; convert a given number of moles of gas to liters at STP; one sentence explaining why a reported gas volume is meaningless without stated conditions. The Exit Ticket values are deliberately distinct from the worksheet practice. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | SEP — Using Mathematics and Computational Thinking; no new content PE (measurement convention foundational to gas-law and solution work) |
| **CCC focus** | Scale, Proportion, and Quantity — at fixed temperature, gas pressure and volume are inversely proportional, so a measured gas volume depends on conditions; a standard reference (STP) makes results comparable and reproducible |
| **Strategy chips** | ACTIVE LEARNING — students physically trace the Boyle's Law curve and run their own mole↔liter conversions before any term is defined |
| **Materials** | 2025 NYS Chemistry Reference Tables (Table A) one per student, calculators, two sealed syringes or a balloon for the "squeeze" demo, `figures/boyles_law_stp.png` projected |
| **Safety** | Low-hazard lesson. If using a syringe, cap the tip and do not exceed gentle hand pressure; no needles. Standard lab conduct applies. |
| **Prior knowledge** | The mole as a counting unit (6.02 × 10²³ particles); gram formula mass / molar mass (Unit 1, Lesson 06); reading numeric values from the Reference Tables; particle model of gases (gas particles spread to fill their container). |

**Lesson objectives — students can:**

- State standard temperature (273 K, 0 °C) and standard pressure (101.3 kPa, 1 atm) and locate both on Reference Table A.
- Recall and use the molar volume of a gas at STP (22.4 L/mol) as a conversion factor between moles and liters of a gas.
- Convert a given number of moles of a gas to its volume in liters at STP, and a volume in liters at STP back to moles.
- Explain, using Scale, Proportion, and Quantity, why a reported gas volume (or a solution result) is meaningless unless the temperature and pressure are also stated.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers in one sentence: *"Think of a time two people measured or counted the same thing but got different answers because they did it differently — steps to school, a recipe, a score. What happened?"* One round, one sentence each, pass allowed. This surfaces the everyday intuition that a number means nothing until you agree on how it was taken — the exact idea behind a standard.

Then post the **Do Now**:

> *"Two lab groups each measure the volume of exactly one mole of CO₂ gas. Group A reports 22.4 L. Group B reports 25.1 L. Neither group made a mistake, and both had exactly one mole. Write one sentence: how can the same amount of gas have two different volumes?"*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "One group measured wrong." — gently redirect: I promise neither group made an error. What else could change the volume if the amount of gas is identical?
- "Maybe the room was warmer for one of them." — excellent; affirm and hold it: temperature changes gas volume. What else might be different between two rooms?
- "I don't get it — a mole is always the same." — exactly the tension we want; validate: a mole is always the same *count* and the same *mass*, but the *volume* of a gas is not fixed. That is what today is about.

### 3–8 min · Phenomenon hook — same gas, different volume

**Teacher actions.** Hold up a sealed, capped syringe (or a partly inflated balloon). Push the plunger in slowly: the gas inside takes up less space. Let it back out: the gas spreads again. Same gas — same number of particles trapped inside — but the volume you can read off the syringe barrel keeps changing as you change the pressure.

> "Nothing left the syringe. Nothing got added. Same gas particles the whole time. But the volume keeps changing as I push. So if I asked you 'what is the volume of this gas?', what would you have to ask me back before you could answer?"

Project the `figures/boyles_law_stp.png` figure:

![Line graph titled 'Pressure vs. volume for one mole of gas at STP' showing a smooth inverse curve for 1.00 mole of gas held at the STP temperature of 273 K; the x-axis is labeled 'Volume (L)' from 0 to about 46, and the y-axis is labeled 'Pressure (kPa)' from 0 to about 220; as volume increases the pressure falls along a 1/V curve; a marked point with dashed guide lines to both axes labels the STP point at 22.4 L and 101.3 kPa.](figures/boyles_law_stp.png)

**Sample teacher language:**

> "This curve is one mole of gas, kept at the same temperature, while we change the pressure on it. Follow it: when the volume is small — squeezed down on the left — the pressure is high. Let the gas expand to the right, and the pressure drops. Pressure and volume trade off. There is one special point marked on the curve: 22.4 liters at 101.3 kilopascals. Hold on to that point — it is going to turn out to be very important."

**Anticipated student responses:**

- "So the volume depends on how hard you push?" — exactly; pressure changes volume, and so does temperature. Volume is not a fixed property of a gas the way mass is.
- "Why is that one point marked?" — great question; that is the point we will all agree to call 'standard,' and we will name it in a little while.
- "Is the line going to hit zero?" — it gets closer and closer but the curve never touches either axis — squeeze harder, the volume keeps shrinking but never reaches zero. That shape is the clue that pressure and volume are inversely related.

**Driving question** (post on the board and leave it there):

> *Why do scientists need a common "standard" set of conditions for reporting their results?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the curve or the syringe demo. Then:

> "Turn to your partner: the two lab groups both had exactly one mole of CO₂ but reported different volumes. Using the curve, what would have to be true for *every* group, in every classroom, to report the *same* volume for one mole of gas?"

Target insight (leave open if no one lands it): everyone would have to agree to measure at the same temperature and the same pressure. The volume only becomes comparable when the conditions are fixed — that agreement is what a 'standard' is.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–16 min · ACTIVE LEARNING — trace the curve before any term is defined

**Before any formal vocabulary is introduced**, students physically work the Boyle's Law curve to build the intuition that gas volume is condition-dependent.

Each student gets a copy of `figures/boyles_law_stp.png` (or works from the projection). The task — do this with a finger or a pencil tip, not a calculator:

**Part 1 — Trace and predict:**

> "Put your pencil on the marked point at 22.4 L. Now slide left along the curve so the volume gets smaller. What happens to the pressure? Now slide right so the volume gets bigger. What happens to the pressure? Write a sentence describing the trade-off you see."

**Part 2 — Read the special point:**

Have students record, by reading the dashed guide lines on the figure:

| Quantity at the marked point | Value from the figure |
|---|---|
| Volume of 1 mole of gas |  |
| Pressure |  |

> "Everyone should read 22.4 L and 101.3 kPa off the dashed lines. That marked point is one mole of gas at one specific temperature and one specific pressure. It is the point the whole world of chemistry has agreed to use as a reference."

**Teacher facilitation language (circulate):**

> "As you slide left, is the pressure going up or down? Say it as a rule: 'When I make the volume smaller, the pressure gets ___.'"

> "Why can't you write down a single 'volume of one mole of gas' from this curve? Point to three different volumes on the curve — they are all one mole. The volume only has a definite answer once you also pin down the pressure."

**Anticipated student responses during ACTIVE LEARNING:**

- "When the volume goes down, the pressure goes up." — exactly; that is the inverse relationship. Squeeze the gas, the particles hit the walls more often, pressure rises.
- "So the volume of a mole of gas is anything I want?" — along this curve, yes — until you fix the pressure (and temperature). Then it has one answer. That is why we need a standard.
- "The marked point is 22.4 — is that going to be on the test?" — yes; and you will not memorize it, you will read it from Reference Table A. We will get there.

### 16–22 min · Initial Model — find the standard conditions on Reference Table A

**Prompt on the board:**

> *"Before we name anything: open Reference Table A in the 2025 Reference Tables. Find the row for standard pressure and the row for standard temperature. Write down each value — and notice each one is given in TWO different units. Then find the molar volume of a gas at STP."*

Students work individually for 3 minutes, then compare with a partner.

Target answers (students read these directly from Table A):

> Standard temperature: 273 K = 0 °C
> Standard pressure: 101.3 kPa = 1 atm
> Molar volume of a gas at STP: 22.4 L/mol

**Teacher facilitation language:**

> "Compare the temperature you found, 273 K, with the marked point's conditions on the curve. The curve was drawn at the standard temperature. Now compare 101.3 kPa from Table A with the pressure at the marked point. Do they match?"

> "Why does the table give each value twice — 273 K *and* 0 °C, 101.3 kPa *and* 1 atm? Because different instruments and different countries report in different units. The standard is the same physical condition written two ways."

**Anticipated student responses:**

- "Table A says 101.3 kPa AND 1 atm — which one do I use?" — both are the same pressure; use whichever matches the units in the problem. They are equal.
- "I found 22.4 L but it says 'molar volume of a gas at STP' — what does molar volume mean?" — hold that thought; that is exactly the term we will define in Phase 3, and you have already found its value.
- "Is 0 °C the freezing point of water?" — yes; standard temperature is literally the freezing point of water, which is a convenient, reproducible benchmark.

### 22–30 min · Investigation — mole ↔ liter conversions at STP

Groups of three or four work a structured set. Each student does the arithmetic individually, then the group compares. Calculators are expected; the skill target is setting up the conversion factor 22.4 L/mol, not the multiplication.

**Practice set (board or half-sheet).** Use molar volume at STP (22.4 L/mol) as the conversion factor.

**Problem A — moles to liters.** What volume does 2.00 mol of O₂ gas occupy at STP?

> 2.00 mol × 22.4 L/mol = **44.8 L**

**Problem B — moles to liters (fraction).** What volume does 0.500 mol of N₂ gas occupy at STP?

> 0.500 mol × 22.4 L/mol = **11.2 L**

**Problem C — liters to moles.** How many moles of He gas are in 67.2 L of He at STP?

> 67.2 L ÷ 22.4 L/mol = **3.00 mol**

**Teacher facilitation prompts (circulate):**

> "For Problem A, what are you multiplying *by*? The molar volume, 22.4 liters per mole. Watch the units cancel: moles × (liters / mole) leaves liters. If your answer comes out in moles, you divided when you should have multiplied."

> "For Problem C you are going the other way — liters back to moles. So 22.4 goes in the denominator: liters ÷ (liters/mole) = moles. Check: does 67.2 ÷ 22.4 give a clean whole number?"

> "Every one of these only works because we agreed on STP. Off the standard, 22.4 L/mol would be the wrong factor."

**Anticipated student responses:**

- On Problem A: "I got 0.089 — I divided instead of multiplied." — redirect to unit cancelling: you have moles and want liters, so multiply by 22.4 L/mol; division is for going from liters to moles.
- On Problem C: "67.2 ÷ 22.4 = 3 exactly — is that right?" — yes, exactly 3.00 mol; the numbers are chosen to be clean so you can focus on setting up the factor.
- "What if the gas isn't at STP?" — great question and a real limitation; the 22.4 L/mol factor only applies at STP. Off STP you would need the combined gas law, which is next.

### 28–30 min · Reconnect + surface the method

Bring groups back together. Ask one group to put Problem A's setup on the board. Ask the class:

> "What single number turned moles into liters? (22.4 L/mol.) Where did that number come from? (Reference Table A — molar volume of a gas at STP.) And what had to be true about the conditions for that number to work?"

Surface the key idea: at STP, one mole of *any* gas occupies 22.4 L. That single conversion factor only holds because everyone agreed on the same temperature and pressure. Take away the standard and the factor falls apart.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look back at your conversions and the curve. Turn to your partner: we used 22.4 L/mol for O₂, for N₂, and for He — three different gases. Why does the *same* volume per mole work for gases that have completely different molar masses?"

Target consensus: at the same temperature and pressure, equal numbers of gas particles take up equal volumes, regardless of what the particles are — heavier molecules don't take more room. So one mole (the same count) of *any* gas occupies the same 22.4 L *at STP*. The condition "at STP" is doing essential work in that sentence.

> "If two groups both report 'one mole of gas = 22.4 L,' what must be true about how they each measured?"

Target: both measured at standard conditions. Without that agreement, one might report 22.4 L and another 25.1 L — exactly our phenomenon.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name what we've been using all period. The agreed-upon reference conditions — 273 K and 101.3 kPa — have a name: **STP**, which stands for *standard temperature and pressure*. STP is the single set of conditions chemists agree to use so that a gas measurement taken in one lab can be compared to a measurement taken in another lab. Standard temperature is 273 K (0 °C); standard pressure is 101.3 kPa (1 atm). You read both straight off Reference Table A."

> "The space that one mole of a gas takes up at STP has its own name: **molar volume**. The molar volume of a gas at STP is 22.4 liters per mole — that is the number you used in every conversion today, and it is on Table A. One mole of *any* gas, at STP, fills 22.4 L."

> "And the reason any of this matters comes down to a third idea: a **standard** — an agreed-upon reference value or condition that everyone uses so results are comparable and reproducible. A meter, a kilogram, and STP are all standards. Without a standard, the same one mole of gas could honestly be reported as 22.4 L or 25.1 L, and neither group would be wrong — but their numbers could not be compared. The standard is what makes science a shared, checkable enterprise."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "If a problem says 'a gas at STP,' what three things do you immediately know?" — *Expected response:* temperature is 273 K (0 °C), pressure is 101.3 kPa (1 atm), and one mole of it occupies 22.4 L.
- "Where do you find standard temperature, standard pressure, and molar volume?" — *Expected response:* Reference Table A in the 2025 NYS Chemistry Reference Tables. They are given values; you do not memorize or derive them.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the model + Because/But/So expansion

Students return to their Initial Model (the standard-conditions values from Table A) and annotate it: label 273 K and 101.3 kPa as "standard temperature" and "standard pressure," and label 22.4 L/mol as "molar volume — only valid at STP." Then they connect the standard back to the conversions they ran.

Run a **Because / But / So** sentence about the phenomenon. Starter on the board:

> *"Two lab groups each measured one mole of CO₂ gas and reported different volumes (22.4 L vs. 25.1 L)."*

Model one aloud:

> "Two groups reported different volumes for one mole of CO₂ **because** the volume of a gas changes with temperature and pressure, and the two rooms were not at the same conditions — **but** both groups measured exactly one mole, the same 6.02 × 10²³ molecules — **so** the difference is not an error; it is exactly why chemists agree to report gas volumes at STP, where one mole of any gas occupies 22.4 L and every lab's result can be compared."

Then have students write their own B/B/S using one of these starters:

- *"A student reports 'the volume of this gas is 30 L' but does not say at what temperature or pressure…"* (hint: the number is not reproducible)
- *"At STP, one mole of O₂ and one mole of He occupy the same 22.4 L even though O₂ is much heavier…"*

**Anticipated student responses:**

- "Because they didn't say the conditions, so nobody can repeat it." — good start; push for the full frame: "because gas volume depends on temperature and pressure, but those were never stated, so another scientist cannot reproduce or check the measurement."
- "Because equal moles take equal volume at the same conditions." — excellent; push for the So: "so at STP both gases occupy 22.4 L per mole, even though their molar masses differ, because volume depends on particle count and conditions, not on the kind of particle."

### 39–40 min · Return to the phenomenon

> "Return to our two lab groups. Group A got 22.4 L, Group B got 25.1 L, both with one mole of CO₂. Now you have the tools. Which group was working at STP? How do you know? And if both groups had agreed to report at STP, what volume would they both have written down?"

Target: Group A was at (or very near) STP, because 22.4 L is exactly the molar volume of a gas at STP. If both reported at STP, both would write 22.4 L — and their results would finally be comparable.

> "The volume on the report sheet isn't wrong — it just isn't comparable until everyone uses the same reference. That reference is STP, and it is what turns three different lab measurements into one shareable scientific result."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud:

> *(a) State standard temperature and standard pressure, each with correct units (give both unit systems if you can).*
> *(b) What volume does 4.00 mol of CH₄ gas occupy at STP? Show the conversion using molar volume.*
> *(c) In one sentence, explain why a reported gas volume is meaningless unless the temperature and pressure are also stated.*

Expected answers are in `Answer_Key.docx`. (These values are deliberately different from the worksheet practice.)

**Closing Reflection (SEL, 30 seconds):**

> "Today we found out that a number can be correct and still not be useful until everyone agrees on how it was taken. In one sentence: where else in your life would a shared 'standard' make things fairer or clearer, and who helped you see it today?"

Collect worksheets; note which students multiplied by 22.4 L/mol when converting moles→liters versus dividing (the most common procedural slip), and which students can correctly state both unit systems for standard temperature and pressure. Target any student who divided instead of multiplied for a brief one-on-one at the start of the next lesson, since the combined-gas-law work depends on this setup.

---

## Common Misconceptions

- **Misconception:** "One mole of a gas always takes up 22.4 L." → **Correction:** One mole of a gas occupies 22.4 L *only at STP*. The molar volume of 22.4 L/mol is a conditions-specific value; change the temperature or pressure and the volume changes (that is exactly what the Boyle's Law curve shows). The phrase "at STP" is not optional — it is the condition that makes 22.4 L/mol valid.
- **Misconception:** "STP is a kind of gas, or a property of a particular gas." → **Correction:** STP is a set of *conditions* — standard temperature (273 K) and standard pressure (101.3 kPa) — not a substance and not a property of any one gas. Any gas can be "at STP." STP describes the surroundings, not the sample.
- **Misconception:** "Standard temperature is room temperature (about 25 °C / 298 K)." → **Correction:** Standard temperature is 0 °C (273 K), the freezing point of water — not room temperature. (Students may later meet "SATP" at 25 °C in other courses; for the NYS Regents and Reference Table A, standard temperature is 273 K.)
- **Misconception:** "To convert liters of gas to moles you multiply by 22.4." → **Correction:** Direction matters. Moles → liters multiplies by 22.4 L/mol; liters → moles divides by 22.4 L/mol (or multiplies by 1 mol / 22.4 L). The unit cancellation tells you which: keep the unit you want and cancel the unit you have.
- **Misconception:** "A measurement is wrong if two groups get different numbers." → **Correction:** Two correct measurements of the same gas can differ if the conditions differ — neither is an error. They become comparable only when reported at a shared standard. The disagreement is information about conditions, not a mistake, and it is precisely why standards exist.

---

## Access & Differentiation

- **ELL/ENL supports:** Conversion template pre-printed with the setup: *"___ mol × 22.4 L/mol = ___ L (at STP)"* and *"___ L ÷ 22.4 L/mol = ___ mol (at STP)."* Sentence frame: *"A gas volume is only comparable when the ___ and ___ are stated, so chemists use ___."* Word-choice box displayed throughout: {STP, molar volume, standard, standard temperature, standard pressure, 22.4 L/mol, 273 K, 101.3 kPa}. Pair every numeric value with its Reference Table A location so students can self-verify.
- **IEP/SPED supports:** Pre-highlight the standard-temperature, standard-pressure, and molar-volume rows on a copy of Reference Table A so the table lookup is removed as a barrier. Provide the conversion as a two-box flow: "moles" box → "× 22.4" arrow → "liters" box (and the reverse), so students choose a direction rather than recalling an operation. Calculators expected for all arithmetic; the conceptual target is choosing multiply vs. divide and recognizing that 22.4 L/mol only applies at STP.
- **Extensions:** (1) The molar volume 22.4 L/mol comes from the ideal gas law PV = nRT at 273 K and 101.3 kPa — verify it: with n = 1 mol, R = 8.314 L·kPa/(mol·K), T = 273 K, P = 101.3 kPa, solve for V. (2) Group B reported 25.1 L for one mole of CO₂ — was their room warmer or their pressure lower than STP? Justify using the Boyle's Law curve and the idea that warming a gas expands it. (3) Research why "STP" was redefined by IUPAC in 1982 to 100 kPa, and explain why the NYS Reference Tables still use 101.3 kPa — what does this tell you about the nature of a "standard"?

---

## Strategy Spotlight

**ACTIVE LEARNING — trace, predict, and convert before being told.** Active learning means students *do* the cognitive work — observe, predict, manipulate, and calculate — before the teacher names or explains the concept. In this lesson, students never passively receive "STP = 273 K and 101.3 kPa." Instead they (1) physically trace the pressure–volume curve with a pencil and articulate the inverse trade-off in their own words, (2) hunt down the standard-conditions values on Reference Table A themselves, and (3) run their own mole↔liter conversions — all before the terms STP, molar volume, and standard are formally introduced in Phase 3.

**How to run it in this lesson (Phase 2 → Phase 3):**

1. In Phase 2, withhold the vocabulary. Students trace the curve (Part 1), read the special point off the dashed guide lines (Part 2), locate the values on Table A (Initial Model), and complete three conversions (Investigation) — generating the evidence and the procedure themselves.
2. Circulate with questions, not answers: *"When the volume drops, what does the pressure do?"* and *"What had to be true for 22.4 to work?"* Let students put the rule into words.
3. Only in Phase 3, once students have already used 22.4 L/mol successfully, attach the names: STP, molar volume, standard. The term now labels something the student already understands, rather than a definition to be memorized cold.

**Why active learning fits standard conditions:** The concept of a "standard" is abstract until a student has personally hit the problem it solves — the same mole of gas honestly reporting two different volumes. By tracing the curve and seeing the volume move, students *feel* the ambiguity before they are handed the fix. The conversions then make the standard concrete and useful, not just memorized. Research on active learning in science (Freeman et al., 2014) shows measurable gains in retention and transfer when students do the reasoning before the lecture, exactly the sequence used here.

**CRSE connection:** The opening circle (two people measuring the same thing and getting different answers) invites students' own experiences of disagreement that turned out not to be anyone's fault — a recipe that "didn't work," a distance measured in steps. Framing STP as a *fairness* tool — a shared agreement that lets everyone's work count equally — connects an abstract chemistry convention to students' lived sense of what makes comparison fair. The closing reflection deliberately asks where a shared standard would make life "fairer or clearer," honoring students' insight that standards are a social as well as a scientific tool.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — two lab groups report different volumes for one mole of CO₂; syringe "squeeze" demo; Boyle's Law curve `boyles_law_stp.png`; return in Phase 4 with the "which group was at STP?" check |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — what must be true for every group to report the same volume?); Phase 3 (TT#2 — why does 22.4 L/mol work for three different gases?) |
| 3 | Students develop questions/models/procedures | Phase 2 ACTIVE LEARNING (trace the curve, read the STP point); Initial Model (locate values on Table A); group Investigation (mole↔liter conversions) |
| 4 | CCC defined and used | Lesson Overview · *Scale, Proportion, and Quantity*; explicit in Phase 3 (equal moles → equal volume at fixed conditions) and Phase 4 (B/B/S on condition-dependent volume) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: STP / molar volume / standard |
| 6 | Revisit phenomenon with evidence | Phase 4 — students determine which group measured at STP using the molar-volume value (22.4 L) and the Boyle's Law curve |
| 7 | ENL/SPED supports | Access & Differentiation block: conversion template, sentence frames, word-choice box, pre-highlighted Table A rows, two-box flow for direction |
| 8 | Assessment check | Phase 5 — Exit Ticket (state STP with units; convert 4.00 mol CH₄ to liters at STP; one sentence on why conditions must be stated) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked conversion example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **STP (standard temperature and pressure)** — the agreed-upon reference conditions for reporting gas measurements: standard temperature 273 K (0 °C) and standard pressure 101.3 kPa (1 atm), both read from Reference Table A; a gas measurement is comparable across labs only when reported at STP
- **molar volume** — the volume occupied by one mole of a gas; at STP the molar volume of *any* gas is 22.4 L/mol (Reference Table A), which serves as the conversion factor between moles of a gas and liters of a gas at STP
- **standard** — an agreed-upon reference value or set of conditions that everyone uses so that results are comparable and reproducible; STP is the standard for gas measurements, just as the meter and the kilogram are standards for length and mass
