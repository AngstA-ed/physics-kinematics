# Concentration of Solutions — Teacher Guide

## Cover

**Unit: Solutions — Lesson 05: Concentration of Solutions**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: HOCHMAN

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

**HS-PS1-10** — *"Concentrations can be quantitatively expressed in parts per million (ppm), molarity (M), and percent by mass."* For the 2025 NYSSLS-aligned Regents, students are expected to compute the concentration of a solution three ways — molarity (moles of solute per liter of solution), parts per million (mass of solute per million parts of solution), and percent by mass — and to carry out dilution calculations using M₁V₁ = M₂V₂. Per East Meadow guidance, concentration is the quantitative spine of the entire Solutions unit: it is prerequisite to titration, to the colligative-properties lessons later in the unit, and to any equilibrium or acid–base work in the spring.

The Cross-Cutting Concept of **Scale, Proportion, and Quantity** is the explicit lens. The same amount of dissolved solute is "a lot" or "a little" only relative to the amount of solution it is spread through. A teaspoon of salt is dangerous in a glass of water and undetectable in a swimming pool — concentration, not raw amount, is what governs whether a substance helps, does nothing, or harms. The "5 ppm of lead" phenomenon makes that proportional reasoning urgent and real.

### Phenomenon

A city sends out a water-quality notice: the tap water tested at **5 ppm of lead**. To most students, "5" sounds like a small, harmless number — five out of what? Put the number in context. One ppm means one milligram of lead dissolved in one liter (one kilogram) of water — one part in a million. So 5 ppm is 5 mg of lead in a 1-liter bottle. The U.S. EPA "action level" — the point at which a water system must act — is **15 ppb**, which is **0.015 ppm**. That means 5 ppm is more than **300 times** the level at which the government forces a city to intervene. The "small" number is, in fact, a public-health emergency.

Project `figures/lead_concentration_ppb.png`. The phenomenon's 5 ppm bar (5,000 ppb) towers hundreds of times over the EPA action-level line. The visceral hook: the danger of a dissolved substance is never the number alone — it is the number *per unit of solution*. That is exactly what concentration measures.

**Driving question:** What does "5 ppm of lead" actually mean — and how do chemists turn a vague "a little" or "a lot" into an exact number?

### Javalab / Labs

- **Molarity lab — preparing a standard solution:** Each group prepares a known volume of a solution of a colored salt (e.g., CuSO₄ or NaCl with a dye) at a target molarity. Students calculate the mass of solute needed (mass = molarity × volume × gram formula mass), weigh it on a balance, dissolve it, and fill a volumetric flask to the calibration line. The lab makes molarity physical: students *make* a 0.50 M solution and see that "0.50 mol per liter" is a recipe, not an abstraction. Tie the volumetric-flask "fill to the line" step back to the Lesson 06 (Gram Formula Mass) skill — they need GFM to convert moles to the grams they weigh out.
- **Dilution practice — serial dilution demo:** Starting from a concentrated colored stock, students dilute by factors of ten (1 mL stock + 9 mL water, repeated). The color fades visibly at each step, giving a sensory anchor for M₁V₁ = M₂V₂: as volume goes up, concentration comes down in exact proportion. Connect the faintest tube to "5 ppm looks like nothing, but it is still there."
- **ppm reading from a label:** Students read the parts-per-million figures on a real bottled-water or sports-drink label (sodium, fluoride) and convert mg/L ↔ ppm to confirm 1 mg/L = 1 ppm in dilute water solutions.

### Assessments

- **Concentration calculation quiz** (district checkpoint, following lesson; see `Assessments/` folder once created): students compute molarity from moles and volume, convert a mass of solute and a mass of solution into percent by mass and ppm, and solve one dilution problem with M₁V₁ = M₂V₂.
- **Exit Ticket** (Phase 5): three items — molarity of a NaOH solution; percent by mass of a sugar solution; a dilution calculation. Values are deliberately different from the worksheet practice. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | HS-PS1-10 (express concentration as molarity, ppm, and percent by mass; dilution with M₁V₁ = M₂V₂) |
| **CCC focus** | Scale, Proportion, and Quantity — concentration is an *intensive* ratio: amount of solute per amount of solution; the same solute is harmless or dangerous depending on the solution it is spread through |
| **Strategy chips** | HOCHMAN — appositive sentence to define molarity crisply; B/B/S sentence in Phase 4 |
| **Materials** | 2025 NYS Chemistry Reference Tables (Reference Table T — concentration formulas), calculators, two clear cups (one with a pinch of dye in 50 mL, one with the same pinch in 500 mL) for the live concentration demo, `figures/lead_concentration_ppb.png` projected |
| **Safety** | The dye demo uses food coloring and water — food-safe. The molarity lab (separate period) requires goggles and aprons; standard lab safety applies. No open flame. |
| **Prior knowledge** | Lesson 06 (Gram Formula Mass) — converting between moles and grams using GFM; Lesson 04 (Dimensional Analysis) — unit conversions (mL ↔ L, mg ↔ g); students should be fluent reading the Periodic Table for atomic masses before this lesson. |

**Lesson objectives — students can:**

- Calculate the molarity of a solution as moles of solute divided by liters of solution (M = mol ÷ L) and state the unit (mol/L).
- Express a concentration as percent by mass (mass of solute ÷ mass of solution × 100) and as parts per million (mass of solute ÷ mass of solution × 1,000,000).
- Solve a dilution problem using M₁V₁ = M₂V₂.
- Explain, using Scale, Proportion, and Quantity, why "5 ppm of lead" is dangerous even though 5 sounds like a small number — because concentration is a ratio of solute to solution, not a raw amount.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers: *"Think of a time when 'how much' depended on what it was mixed into — one drop of hot sauce in a big pot vs. on a single chip, a little perfume in a small room. What came to mind?"* One round, one sentence each, no judgment. This surfaces the core intuition: the *effect* of an amount depends on what it is spread through — the seed of concentration as a ratio.

Then post the **Do Now**:

> *"A city's water tests at 5 ppm of lead. A student says, 'Only 5? That's basically nothing.' In one sentence: do you agree, and what would you need to know to decide whether 5 ppm is a lot or a little?"*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "5 is a small number, so it's probably fine." — capture without correcting; ask: 5 out of what? A small number of *what*, compared to *what*?
- "I'd need to know what 'ppm' means." — exactly the right instinct; validate. The unit is the whole point — it tells you what the 5 is being compared to.
- "I'd need to know how much water — maybe 5 in a tiny amount is bad." — strong; that is precisely the idea of concentration as a ratio. Hold onto it.

### 3–8 min · Phenomenon hook — what "5 ppm" actually means

**Teacher actions.** Hold up a 1-liter water bottle. Tell the class: one part per million of lead means one milligram of lead — about the mass of a single grain of salt — dissolved in this entire liter of water. So 5 ppm is five grains' worth of lead spread through the whole bottle. Then drop the comparison: the EPA *action level*, the point where a city is legally required to act, is **15 ppb — that is 0.015 ppm**. So 5 ppm is more than **300 times** the action level.

Project `figures/lead_concentration_ppb.png`:

![Bar chart on a logarithmic scale titled 'How much is 5 ppm of lead in water? (1 ppm = 1000 ppb)' comparing lead concentration in parts per billion for four reference points: WHO guideline at 10 ppb, EPA action level at 15 ppb, the Flint crisis peak at about 13,000 ppb, and the phenomenon value '5 ppm' at 5,000 ppb; a dashed horizontal line marks the 15 ppb EPA action level, and the '5 ppm' bar towers hundreds of times above that line.](figures/lead_concentration_ppb.png)

**Sample teacher language:**

> "Look at this chart. The blue dashed line is the EPA action level — 15 parts per billion. Below that line, water is considered acceptable. The green and blue bars sit right at the line. But our phenomenon — 5 ppm — is 5,000 parts per billion. It is hundreds of times over the line, in the same range as the Flint, Michigan crisis. The number 5 looked tiny. But concentration is never about the raw number — it is about how much solute is dissolved in how much solution. That ratio is what we are going to learn to calculate three different ways today."

**Anticipated student responses:**

- "Wait — 5 ppm is *worse* than I thought?" — yes; the number sounds small but the unit hides the comparison. ppm means parts per million; 5 ppm of lead in water is genuinely dangerous.
- "Why is ppm written in 'billion' on the chart?" — great catch; the chart uses ppb (parts per billion) so all four bars fit. 1 ppm = 1,000 ppb, so 5 ppm = 5,000 ppb. Same quantity, finer unit.
- "How do they even measure something that small?" — sensitive instruments; but our job today is to understand what the number *means*, and to calculate it.

**Driving question** (post on the board and leave it there):

> *What does "5 ppm of lead" actually mean — and how do chemists turn a vague "a little" or "a lot" into an exact number?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the chart or the bottle demonstration. Then do the live dye demo: drop one drop of food coloring into a 50-mL cup and the *same single drop* into a 500-mL cup. Same amount of dye; very different color intensity.

> "Turn to your partner: the same one drop of dye went into both cups. Why is the small cup so much darker than the big cup, if the *amount* of dye is identical?"

Target insight: color intensity tracks *concentration*, not the raw amount of dye. The same solute spread through more solution is more dilute — fewer dye particles per unit of liquid. That is the heart of concentration.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–15 min · ABCs Activity — rank concentration before any formula

**Before any formal definition or formula is introduced**, students build the ratio intuition by ranking solutions by how concentrated they are — using only counting, no equations.

Each student examines this set of four "solution recipes" (project or hand out). The task:

**Part 1 — Predict and rank:**

> "Without any formula — just by reasoning about solute spread through solution — rank these four solutions from *most dilute* to *most concentrated*. Write your reasoning."

| Solution | Solute | Amount of solution |
|---|---|---|
| A | 1 spoon of salt | 1 cup of water |
| B | 1 spoon of salt | 4 cups of water |
| C | 2 spoons of salt | 1 cup of water |
| D | 2 spoons of salt | 4 cups of water |

**Part 2 — Check by reasoning about the ratio:**

> "For each one, write the ratio: spoons of salt ÷ cups of water. Which solution has the biggest ratio? Does the biggest ratio match your prediction for 'most concentrated'?"

**Teacher facilitation language (circulate):**

> "Before I give you a formula, just compare A and B. Same salt — one spoon each. But B has four times the water. Which one tastes saltier? Which one has salt packed more tightly into each sip?"

> "Now compare A and C. Same water — one cup each. But C has twice the salt. What does that do to the ratio of salt to water?"

**Anticipated student responses during ABCs:**

- "C is the most concentrated — most salt, least water." — affirm; push for the ratio language: salt ÷ water is biggest for C (2 ÷ 1 = 2). That ratio *is* concentration.
- "A and D are the same because both ratios are 1." — excellent; A is 1÷1 = 1 and D is 2÷4 = 0.5… have them recompute. This is the productive error: D is actually half as concentrated as A. The ratio, not the totals, decides.
- "So it's not how much salt — it's salt compared to water?" — exactly. That comparison is the whole idea of concentration.

### 15–22 min · Initial Model — first molarity calculation from a recipe

**Prompt on the board:**

> *"Before we name the process: a solution is made by dissolving 0.50 mol of NaCl in enough water to make 1.0 L of solution. Another is made by dissolving 0.50 mol of NaCl in enough water to make 2.0 L of solution. For each, write the ratio: moles of solute ÷ liters of solution. Which is more concentrated?"*

Students work individually for 3 minutes, then compare with a partner.

Target answer:

> Solution 1: 0.50 mol ÷ 1.0 L = 0.50 mol/L
> Solution 2: 0.50 mol ÷ 2.0 L = 0.25 mol/L
> Solution 1 is more concentrated — same moles, less volume, bigger ratio.

**Teacher facilitation language:**

> "You just computed a ratio of moles to liters. That ratio has a name we'll learn in a few minutes — but you already built it yourself. What unit did your answer come out in? Moles divided by liters — mol/L."

> "Look at your partner's setup. Did they divide moles by liters, or liters by moles? Which order gives a number that gets *bigger* when the solution gets *more crowded* with solute?"

**Anticipated student responses:**

- "I divided 1.0 ÷ 0.50 and got 2." — redirect: that's liters per mole, the upside-down ratio. We want how much solute per liter, so moles go on top: 0.50 ÷ 1.0.
- "Both have 0.50 mol, so aren't they the same concentration?" — same *amount* of solute, but spread through different volumes. The ratio differs. Same trap as the dye demo.
- "This is just like the salt-and-water ratios from before." — exactly; same idea, now with chemistry units (moles and liters).

### 22–30 min · Investigation — three ways to express concentration

Groups of three or four work through a structured practice set. Each student computes individually, then compares with the group. **All three sub-problems use the same physical solution**, so students see that one solution can be described three ways.

**The shared solution:** A solution is made by dissolving **40.0 g of NaOH** in water to make **0.500 L of solution**. The total mass of the solution is **520 g**. (GFM of NaOH = 40.0 g/mol, from Lesson 06.)

**Compound problem — fill in all three:**

**(a) Molarity (M = moles of solute ÷ liters of solution):**

> moles of NaOH = 40.0 g ÷ 40.0 g/mol = 1.00 mol
> Molarity = 1.00 mol ÷ 0.500 L = **2.00 mol/L (2.00 M)**

**(b) Percent by mass (mass of solute ÷ mass of solution × 100):**

> Percent by mass = (40.0 g ÷ 520 g) × 100 = **7.69 %**

**(c) Parts per million (mass of solute ÷ mass of solution × 1,000,000):**

> ppm = (40.0 g ÷ 520 g) × 1,000,000 = **76,900 ppm**

**Teacher facilitation prompts (circulate):**

> "For molarity, what do you need before you can divide? Moles — not grams. Where do you get moles from grams? Gram formula mass, from Lesson 06. NaOH is 40.0 g/mol, so 40.0 g is exactly 1.00 mol."

> "Notice (b) and (c) use the *same* fraction — solute mass over solution mass. Percent multiplies it by 100; ppm multiplies it by a million. ppm is just percent's more sensitive cousin, for when the amounts are tiny."

> "What unit does molarity carry? mol/L. What about percent by mass and ppm? They're ratios of mass over mass — the grams cancel, so they're unitless (we just label them % or ppm)."

**Anticipated student responses:**

- On (a): "I divided 40.0 g by 0.500 L and got 80." — redirect: molarity needs *moles* on top, not grams. Convert 40.0 g to 1.00 mol first using GFM.
- On (b) vs (c): "Why are (b) and (c) so different — 7.69 vs 76,900?" — same fraction, different multiplier. × 100 gives percent; × 1,000,000 gives ppm. 7.69 % = 76,900 ppm describe the identical solution.
- "Do I use 0.500 L or 520 g?" — molarity uses *volume* (liters); percent by mass and ppm use *mass* (grams). Match the formula to the quantity it asks for.

### 28–30 min · Reconnect + surface the method

Bring groups back together. Ask one group to put the molarity work on the board. Ask the class:

> "Every one of these three formulas is a ratio: something *of the solute* divided by something *of the whole solution*. What is on top each time? What is on the bottom? Why does dividing by the whole solution capture 'concentration'?"

Surface the key idea: concentration is always solute-per-solution. Molarity uses moles-per-liter; percent by mass and ppm use mass-per-mass scaled up. They differ only in *units* and *scale factor* — the underlying idea (solute relative to solution) is identical, which is exactly the ratio intuition from the dye demo and the salt recipes.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look at the NaOH solution — we said it is 2.00 M, 7.69 % by mass, and 76,900 ppm, all at once. Turn to your partner: how can one solution have three different concentration numbers? What is the same underneath all three?"

Target consensus: the three numbers describe the *same* ratio of solute to solution, just measured with different units (moles vs. grams) and scaled differently (× 1, × 100, × 1,000,000). The physical crowding of solute is one thing; the three expressions are three lenses on it.

> "Back to the phenomenon. If our lead-water is 5 ppm, what does that tell you in plain English about the ratio of lead to water?"

Target: 5 parts of lead for every 1,000,000 parts of water — 5 mg of lead in every 1 L (≈ 1,000,000 mg) of water. Tiny ratio, but for a toxin, still hundreds of times over the safe limit.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name what we've been calculating. When we found moles of solute divided by liters of solution, we found the **molarity** — the number of moles of solute dissolved in one liter of solution, with the unit mol/L, sometimes written M. Molarity is the chemist's standard concentration unit because moles connect directly to particles and to reactions."

> "Here is the Hochman appositive move that will help you write and remember the definition. An appositive is a phrase set off by dashes that renames or explains the noun next to it. Say this with me:

> *Molarity — the number of moles of solute dissolved in one liter of solution — is found by dividing moles of solute by liters of solution.*

> The phrase between the dashes is the appositive: it defines 'molarity' in the same sentence. You'll use this structure on the Exit Ticket and in your notes."

> "Two more terms name the things every concentration formula compares. The **solute** is the substance being dissolved — the lead, the salt, the NaOH. The **solution** is the whole mixture — solute plus the water it dissolves into. Every concentration is solute measured against solution: molarity is moles of solute per liter of solution; percent by mass and ppm are mass of solute per mass of solution. Same pattern, three units."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "In the phrase '2.00 M NaOH solution,' which word is the solute and which is the solution?" — *Expected response:* NaOH is the solute (the dissolved substance); the solution is the NaOH-plus-water mixture as a whole. The 2.00 M is the molarity.
- "Where on the Reference Tables do you find the three concentration formulas?" — *Expected response:* Reference Table T (Important Formulas and Equations) in the 2025 NYS Chemistry Reference Tables lists molarity, percent by mass, and parts per million.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the model + Appositive + Because/But/So expansion + dilution

Students return to their Initial Model (the 0.50 mol NaCl molarity comparison). They annotate it: label moles ÷ liters as "concentration ratio," write the molarity in mol/L, and write an appositive sentence defining the result.

**Appositive sentence (model on board):**

> *"Molarity — the number of moles of solute dissolved in one liter of solution — is found by dividing moles of solute by liters of solution."*

Ask students to write a parallel appositive for the NaOH solution:

> *"The molarity of the sodium hydroxide solution — ___ M — is found by dividing ___ mol of NaOH by ___ L of solution."*

**Introduce dilution (the M₁V₁ = M₂V₂ skill) with a worked model:**

> "When you add water to a solution, you do not add any solute — you just spread the same solute through more solution. So moles of solute stay constant. That gives the dilution equation: M₁V₁ = M₂V₂, where moles (M × V) before equals moles after."

Model one aloud, tied to the serial-dilution demo:

> "Suppose you take 50.0 mL of 2.00 M NaOH and dilute it to 200. mL. What is the new molarity? M₁V₁ = M₂V₂ → (2.00 M)(50.0 mL) = M₂(200. mL) → M₂ = (2.00 × 50.0) ÷ 200. = **0.500 M**. The volume quadrupled, so the concentration dropped to one-fourth — exactly what we saw when the dye faded."

Then run a **Because / But / So** sentence about the phenomenon. Starter on the board:

> *"A city's water tests at 5 ppm of lead, even though 5 sounds like a tiny number."*

Model one aloud:

> "5 ppm of lead is dangerous **because** ppm is a concentration — a ratio of solute to solution — so 5 ppm means 5 mg of lead in every liter of water you actually drink — **but** the EPA action level is only 0.015 ppm, more than 300 times lower — **so** the raw number 5 is misleading; what matters is that the concentration is hundreds of times above the safe limit."

Then have students write their own B/B/S using one of these starters:

- *"A student dilutes a solution by adding water and is surprised the concentration drops…"*
- *"Two solutions both contain 0.50 mol of solute, but one is more concentrated than the other…"*

**Anticipated student responses:**

- "Because adding water doesn't remove solute, it just spreads it out." — good start; push for the So: "so the molarity goes down even though the moles of solute never changed."
- "Because concentration is a ratio, not a total." — excellent; push for the contrast: "but two solutions can have the same moles of solute and different concentrations, so the volume of solution decides which is more concentrated."

### 39–40 min · Return to the phenomenon

> "Return to the water notice — 5 ppm of lead. Now you have three tools: molarity, percent by mass, and ppm. ppm told us the lead is 5 parts per million — 5 mg per liter. The EPA action level is 0.015 ppm. Quickly: about how many times over the action level is the city's water?"

Target: 5 ÷ 0.015 ≈ 333 times over the action level. The "small" number is a serious problem.

> "That is the power of concentration. The same word — 'a little' — means safe in one solution and a crisis in another. Concentration turns a vague feeling into an exact, decidable number. That is what makes water safety, medicine dosing, and chemistry itself quantitative."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud:

> *(a) Calculate the molarity of a solution made by dissolving 0.25 mol of KCl in enough water to make 0.50 L of solution. Show your work and the unit.*
> *(b) A solution contains 15 g of sugar dissolved in a solution with a total mass of 300 g. Calculate the percent by mass of sugar.*
> *(c) You take 100. mL of 6.0 M HCl and dilute it to 300. mL. Use M₁V₁ = M₂V₂ to find the new molarity.*

Expected answers are in `Answer_Key.docx`.

**Closing Reflection (SEL, 30 seconds):**

> "Today a number that looked small — 5 ppm — turned out to be dangerous once we understood concentration. In one sentence: what is one place in your own life where 'how much' depends on what it's mixed into, and who helped you see the idea today?"

Collect worksheets; note which students convert grams to moles before computing molarity versus students who divide grams by liters directly. The grams-to-moles step (using GFM) is the main procedural stumbling block — target those students for a brief one-on-one check at the start of the molarity lab.

---

## Common Misconceptions

- **Misconception:** "Molarity is grams of solute per liter of solution." → **Correction:** Molarity is *moles* of solute per liter, not grams. You must convert grams to moles first using the gram formula mass (Lesson 06). A solution with 40.0 g of NaOH in 0.500 L is 2.00 M, not 80 M — because 40.0 g of NaOH is only 1.00 mol.
- **Misconception:** "A solution with more solute is always more concentrated." → **Correction:** Concentration is a *ratio* of solute to solution, not a raw amount. Two spoons of salt in four cups of water is *less* concentrated than one spoon in one cup, because the ratio (0.5 vs. 1) is smaller. The amount of solution in the denominator matters just as much as the solute on top.
- **Misconception:** "Percent by mass and ppm are completely different formulas." → **Correction:** They are the *same* fraction — mass of solute ÷ mass of solution — scaled by different factors. Percent multiplies by 100; ppm multiplies by 1,000,000. ppm is simply the unit chemists reach for when the percent would be a tiny decimal, as with trace contaminants like lead.
- **Misconception:** "Diluting a solution removes some of the solute, so there is less of it." → **Correction:** Dilution adds *solvent* (water), not solute. The moles of solute stay exactly the same; they are just spread through a larger volume, so the concentration drops. That conservation of moles is precisely why M₁V₁ = M₂V₂ works.
- **Misconception:** "5 ppm is a small number, so it must be safe." → **Correction:** ppm is a concentration unit, and whether a concentration is safe depends entirely on the substance. 5 ppm of dissolved oxygen is healthy for fish; 5 ppm of lead in drinking water is over 300 times the EPA action level and a serious hazard. The number alone tells you nothing — you need the substance and the comparison standard.

---

## Access & Differentiation

- **ELL/ENL supports:** Concentration formula card pre-printed with the three formulas and what each variable means (M = mol ÷ L; % by mass = solute mass ÷ solution mass × 100; ppm = solute mass ÷ solution mass × 1,000,000) and sentence frame: *"The ___ of this solution is ___ because there are ___ of solute in ___ of solution."* Word-choice box displayed on the board throughout: {molarity, solute, solution, concentration, dilute, ppm}. Pair each formula with the dye-cup visual so students self-check: darker cup = higher concentration.
- **IEP/SPED supports:** Pre-fill the gram formula masses needed for practice (NaOH = 40.0, KCl = 74.6, NaCl = 58.5) on the student's card so the GFM lookup is removed as a barrier. Provide a labeled "solute on top, solution on bottom" template for every ratio so students never invert the fraction. For dilution, give a pre-drawn M₁V₁ = M₂V₂ box with the four slots labeled. Calculator use expected for all arithmetic; the conceptual work (identifying solute vs. solution, choosing the right formula) is the skill target.
- **Extensions:** (1) Convert the NaOH solution's ppm (76,900 ppm) back to percent by mass and confirm it equals 7.69 % — what is the exact relationship between ppm and percent? (Answer: ppm = percent × 10,000.) (2) A doctor orders a 0.90 % by mass saline drip. If a patient receives 1,000 g of this solution, how many grams of NaCl enter their body? (3) Research: why do environmental agencies report lead in ppb instead of ppm or molarity? How does the choice of unit make a trace contaminant easier to discuss?

---

## Strategy Spotlight

**HOCHMAN — Appositive sentence.** The Hochman Writing Method (Judith Hochman and the Writing Revolution) treats sentence-level writing as a thinking tool. For this lesson the featured technique is the **appositive**, a noun phrase set off by dashes (or commas) that renames or defines the noun it follows. The appositive is ideal for concentration vocabulary because the terms (molarity, ppm, percent by mass) are easy to confuse — embedding a precise definition inside a subject-verb sentence forces the student to commit to what each one actually measures.

**The target appositive for this lesson:**

> *Molarity — the number of moles of solute dissolved in one liter of solution — is found by dividing moles of solute by liters of solution.*

This sentence structure does three things simultaneously: (1) names the term, (2) defines it in a concise phrase between the dashes, and (3) describes the procedure (how to find it) in the main clause. Students who can write and say this sentence — not just recite the definition separately — are integrating the term into their active vocabulary.

**How to run it in this lesson (Phase 3 → Phase 4):**

1. Post and read aloud the model appositive sentence together (Phase 3 vocabulary).
2. Ask students to write a parallel appositive for a specific solution: *"The molarity of the sodium hydroxide solution — ___ M — is found by..."* This requires them to substitute in the value they calculated in Phase 2, confirming that the abstract definition connects to their concrete work.
3. In Phase 4, students write their own appositive for percent by mass or ppm. Cold-call two or three students; ask: does the appositive phrase correctly define the term? Does the main clause describe the process?

**Why the appositive fits concentration:** The three concentration terms share one structure — solute over solution — but differ in unit and scale. The appositive makes the distinction explicit in a single sentence: *molarity — moles per liter —*, *percent by mass — grams of solute per 100 grams of solution —*, *parts per million — grams of solute per million grams of solution —*. Students who can write all three appositives are far less likely to plug a mass into the molarity formula or confuse the × 100 and × 1,000,000 scale factors.

**CRSE connection:** The opening circle prompt (hot sauce in a pot, perfume in a room) invites students to bring everyday "how much depends on what it's in" experiences into the conversation. The anchoring phenomenon — lead in drinking water — is a live environmental-justice issue in many communities, including cities near the district. Grounding an abstract ratio in a real public-health story honors students' awareness of their own water and communities and makes the math feel consequential rather than arbitrary. Treat the topic with care: frame it as *why chemistry literacy is power* — knowing what a number on a water report means lets a person advocate for their family.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — "5 ppm of lead" water notice; `lead_concentration_ppb.png`; live dye-cup demo; return in Phase 4 with the 333× action-level comparison |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — same drop of dye, why is the small cup darker?); Phase 3 (TT#2 — how can one solution have three concentration numbers?) |
| 3 | Students develop questions/models/procedures | Phase 2 ABCs (rank solutions by ratio before any formula); Initial Model (molarity ratio comparison); group investigation (molarity, percent by mass, ppm of one NaOH solution) |
| 4 | CCC defined and used | Lesson Overview · *Scale, Proportion, and Quantity*, explicit in Phase 3 (vocabulary) and Phase 4 (B/B/S on 5 ppm of lead) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: molarity / solute / solution |
| 6 | Revisit phenomenon with evidence | Phase 4 — students compute 5 ÷ 0.015 ≈ 333× over the EPA action level using the ppm concept they built |
| 7 | ENL/SPED supports | Access & Differentiation block: formula card, sentence frame, word-choice box, pre-filled GFMs, solute-over-solution template, dilution box |
| 8 | Assessment check | Phase 5 — Exit Ticket (molarity of KCl; percent by mass of sugar; dilution of HCl with M₁V₁ = M₂V₂) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked molarity/percent/ppm example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **molarity** — the number of moles of solute dissolved in one liter of solution; found by dividing moles of solute by liters of solution; the unit is mol/L, abbreviated M; the chemist's standard concentration measure
- **solute** — the substance that is dissolved in a solution (e.g., the NaOH, the salt, the lead); it is the quantity that goes on top of every concentration ratio
- **solution** — a homogeneous mixture of a solute dissolved in a solvent (the whole mixture, solute plus solvent); it is the quantity in the denominator of every concentration ratio, so concentration always measures solute relative to the whole solution
