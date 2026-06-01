# Percent Composition — Teacher Guide

## Cover

**Unit: Safety and Measurement — Lesson 07: Percent Composition**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: BTC

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

**HS-PS1-2** — *"Construct and revise an explanation for the outcome of a simple chemical reaction based on the outermost electron states of atoms, trends in the periodic table, and knowledge of the patterns of chemical properties."* Percent composition is the foundational quantitative skill that connects a compound's formula to its mass-fraction makeup. For the 2025 NYSSLS-aligned Regents, students must calculate the percent by mass of each element in a compound using the gram formula mass (from Lesson 06) as the denominator: % element = (n × atomic mass ÷ GFM) × 100. This skill underpins stoichiometry, solution concentration, and the interpretation of fertilizer labels, food labels, and pharmaceutical dosages throughout the course.

The Cross-Cutting Concept of **Scale, Proportion, and Quantity** is the explicit lens: percent composition expresses each element's contribution as a proportion of the whole compound mass. The proportions are fixed by the formula — every sample of a given compound, regardless of size, has the same percent composition by mass. This fixed ratio is what makes percent composition a reliable way to identify and compare compounds.

### Phenomenon

Two fertilizer bags sit on the demonstration table. Both advertise "nitrogen" on the label. One grows noticeably greener, healthier grass than the other — even at the same application rate. The difference is not in whether nitrogen is present but in how much nitrogen there is per gram of fertilizer, i.e., the **percent nitrogen by mass** in each compound.

Alternative hook (if fertilizer bags are unavailable): two iron supplement tablets — one containing iron(II) sulfate, one containing iron(III) oxide — at the same labeled "iron" milligrams but different actual elemental iron per gram. The percent iron by mass differs because the compounds differ.

**Driving question:** How can we tell what a compound is made of — and how much of each element — without taking it apart?

### Javalab / Labs

- **Percent-composition calculation from formulas:** Using the 2025 Reference Tables, students apply % element = (n × atomic mass ÷ GFM) × 100 to a sequence of compounds. Each student shows the setup in a structured table: element | mass in formula (n × atomic mass) | GFM | percent. Connects directly to the fertilizer and iron-supplement phenomena.
- **Percent water in a hydrate (optional wet lab):** Pre-weigh a sample of a copper sulfate hydrate (CuSO₄ · 5H₂O). Heat to drive off the water of crystallization. Reweigh. Calculate percent water by mass using (mass lost ÷ original mass) × 100. Connects the formula-based calculation to an experimental determination.
- **Percent water in popcorn (low-infrastructure alternative):** Weigh unpopped kernels, pop them (microwave or hot plate with foil pouch), reweigh the popped corn. The mass lost is the water that escaped as steam. % water = (mass lost ÷ original mass) × 100. Edible, culturally accessible, zero safety hazard.

### Assessments

- **Percent-composition problem set** (district checkpoint following lesson; see `Assessments/` folder): students compute percent composition for a series of compounds from their formulas, show all steps, and interpret which of two compounds contains more of a specified element.
- **Exit Ticket** (Phase 5): three items — % Mg in MgO; % O in MgO; sentence explaining why percents sum to 100%. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | HS-PS1-2 (foundational quantitative skill: percent composition from a formula using GFM; supports mass fraction interpretation) |
| **CCC focus** | Scale, Proportion, and Quantity — percent composition is a fixed proportion; every gram of a given compound has the same fraction of each element regardless of sample size |
| **Strategy chips** | BTC (Building Thinking Classrooms) — random groups at vertical surfaces working a percent-composition thin-slice during the Explore phase |
| **Materials** | Periodic Table / 2025 NYS Chemistry Reference Tables, two fertilizer bags (or labels printed), calculators, `figures/water_composition.png` projected, vertical surfaces (whiteboards, windows with markers, or chart paper), random group cards |
| **Safety** | No chemicals opened. Fertilizer bags handled as props only — do not ingest. If doing the popcorn or hydrate lab, standard safety rules apply. |
| **Prior knowledge** | Lesson 06 (Gram Formula Mass) — students must be able to calculate GFM from a formula; GFM is the denominator in every percent-composition calculation. Lesson 04 (Dimensional Analysis) — percent is a ratio × 100, which parallels unit conversion logic. |

**Lesson objectives — students can:**

- State the percent composition formula: % element = (n × atomic mass of element ÷ gram formula mass of compound) × 100.
- Calculate the percent by mass of each element in a compound and verify that all percentages sum to 100%.
- Define mass ratio and explain its relationship to percent composition.
- Use Scale, Proportion, and Quantity to explain why two compounds containing the same element may differ in how much of that element they deliver per gram.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a **community-building opening circle** (2–3 min). Everyone — teacher included — answers: *"Think of a time you compared two similar products and found they weren't actually equal — same brand, different amount of something that mattered. What did you compare, and how did you figure out the difference?"* One round, one sentence each, no judgment. This surfaces the everyday experience of comparing proportions (unit price, nutrition labels, concentration), priming students to see percent composition as a real-world comparison tool.

Then post the **Do Now**:

> *"Two fertilizer bags are on the desk. Both say 'nitrogen' on the label. One costs more, but the grass it grows is noticeably greener. Write one sentence: what information would you need to figure out which bag actually delivers more nitrogen to the soil?"*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "You'd need to know how much nitrogen is in each bag." — affirm; and push: how would you express that amount so two bags of different total weight are comparable? What if one bag were twice as heavy?
- "You'd need to read the label or do a test." — good instinct; and today we'll learn the calculation that tells you — without any test — how much nitrogen is in every gram of a given compound, straight from the formula.
- "Maybe the more expensive one has more nitrogen." — possible; but price doesn't guarantee quality. We need a way to compare nitrogen per gram regardless of cost or total bag weight.

### 3–8 min · Phenomenon hook — percent nitrogen and the green-grass mystery

**Teacher actions.** Hold up both fertilizer bag labels (or project images of them). Point to the listed ingredient compounds — for example, one bag uses urea (CO(NH₂)₂) and the other uses ammonium nitrate (NH₄NO₃).

> "Both bags list nitrogen as the active ingredient. But when applied at the same rate — same number of scoops per square foot — one gives noticeably greener grass. The chemistry is in the formula. Today you're going to figure out exactly what fraction of each compound is actually nitrogen, and then we'll know which bag is doing more work per gram."

Project the `figures/water_composition.png` figure as the first worked example of percent composition — a familiar compound before we touch the fertilizer:

![Pie chart titled 'Percent by mass — water (H₂O)' showing two slices: hydrogen (H) at 11.2% in light blue and oxygen (O) at 88.8% in dark blue; each slice is labeled with the element symbol, the percentage, and the corresponding mass contribution (H: 2 g/mol out of 18 g/mol; O: 16 g/mol out of 18 g/mol); the chart title notes that percentages sum to 100%.](figures/water_composition.png)

**Sample teacher language:**

> "Look at this pie chart for water. The entire circle represents one gram formula mass of water — 18 g/mol. The light-blue slice is hydrogen's share: 2 g/mol out of 18, which is about 11.2%. The dark-blue slice is oxygen's share: 16 g/mol out of 18, about 88.9%. Two slices. They fill the whole circle — 100%. That's what percent composition means: every element's slice of the mass pie. The slices are fixed by the formula, not by the sample size. Whether you have 18 grams of water or 180 grams, hydrogen is always about 11% by mass."

> "Now think about a fertilizer compound. If nitrogen atoms are a big slice of the mass pie, the compound is nitrogen-rich. If they're a tiny slice, there's not much nitrogen per gram — even if the label says 'nitrogen.' Percent composition lets you compare the size of that nitrogen slice without opening the bag."

**Anticipated student responses:**

- "So the percentages always add up to 100?" — exactly; every gram of the compound is accounted for by its constituent elements, so the fractions must sum to 1, or 100%.
- "How do you calculate those percentages from the formula?" — that's the method we'll build in Phase 2; you already have the denominator from Lesson 06 (GFM).
- "Why is oxygen such a big slice in water if there's only one oxygen?" — great observation; because oxygen has a large atomic mass (16) compared to hydrogen (1). One heavy element beats two light ones.

**Driving question** (post on the board and leave it there):

> *How can we tell what a compound is made of — and how much of each element — without taking it apart?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the pie chart or the fertilizer scenario. Then:

> "Turn to your partner: in the water pie chart, oxygen's slice is 88.9% even though there is only one oxygen atom per water molecule and two hydrogen atoms. How can one atom outweigh two atoms?"

Target insight: it is the *mass* of each atom — not the count — that determines its share of the percent composition. Oxygen (atomic mass 16) is 16 times heavier than hydrogen (atomic mass 1), so even one oxygen outweighs two hydrogens. This is the same Scale, Proportion, and Quantity insight from Lesson 06, now expressed as a percentage.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–15 min · ABCs Activity — compute percent shares before formalizing the definition

**Before any formal vocabulary is introduced**, students build intuition by computing the mass fraction of each element in water and reading it off the pie chart.

**Part 1 — Examine the pie chart:**

> "Look at the water pie chart. Without any algebra: if the whole pie is 18 g/mol (the GFM of water), and hydrogen's contribution is 2 g/mol, what fraction of the total is that? Write it as a decimal, then as a percent."

Students write: 2/18 = 0.111 → 11.1%

> "Now oxygen: 16 g/mol out of 18 g/mol total. What fraction? What percent?"

Students write: 16/18 = 0.889 → 88.9%

> "What do those two percentages add up to? Why does that make sense?"

**Part 2 — Extend the thinking to a new element:**

> "Suppose a compound has one element that contributes 23 g/mol to a total GFM of 58.5 g/mol. What percentage of the compound's mass is that element? Don't name the formula yet — just compute the ratio."

Students compute: 23/58.5 × 100 ≈ 39.3%.

> "That element is sodium in table salt (NaCl). You just found the percent sodium by mass in table salt, before I defined anything. That ratio — element's mass contribution divided by the GFM, times 100 — is what we call percent composition."

**Teacher facilitation language (circulate):**

> "Before I give you the formula, can you tell me: in the water pie chart, what is being divided by what? What is the 'whole'? What is each 'part'?"

> "If you doubled your sample to 36 g of water, would the percentages change? Why not?"

**Anticipated student responses during ABCs:**

- "I got 11.1% for hydrogen — is that the same as the chart?" — yes; the chart shows 11.2% because of rounding to one decimal place. Both are correct. Accept either.
- "I don't understand why you divide by GFM." — rephrase: the GFM is the total mass of one formula unit. It's the whole pie. Each element's mass contribution is one slice. Divide slice by whole, multiply by 100 to get percent.
- "Wouldn't the percents change if I had a different amount?" — no, and this is the key insight: percent composition is a property of the compound, not the sample size. It's the same whether you have 18 g or 1800 g of water.

### 15–22 min · BTC Thin-Slice — vertical surfaces, random groups

**Strategy: Building Thinking Classrooms (BTC).**

Assign random groups of 3 using cards or a randomizer. Send each group to a vertical surface (whiteboard panel, window with dry-erase marker, or large chart paper taped to the wall). Each group gets one marker and solves the thin-slice problem on the surface — visible to the teacher and the class.

**Thin-slice prompt (written or projected):**

> *"A compound has gram formula mass 44 g/mol. Carbon contributes 12 g/mol of that; oxygen contributes 32 g/mol. (a) Calculate the percent carbon by mass. (b) Calculate the percent oxygen by mass. (c) Check: do your two percents sum to 100%?"*

(This is CO₂, but do not name it yet — let students compute first.)

**Teacher facilitation prompts (move between groups, do not give answers):**

> "What is the whole in this problem?" (44 g/mol = GFM)

> "What operation connects the slice to the whole as a percentage?" (divide, then × 100)

> "Before you write a formula, can you see this on the water pie chart? What would the CO₂ pie chart look like?"

**Anticipated student responses at vertical surfaces:**

- Correct: % C = 12/44 × 100 = 27.3%; % O = 32/44 × 100 = 72.7%; sum = 100%. — affirm; ask: what compound is this? How do you know?
- Error: 12/44 = 0.27, stop there without × 100 — gently ask: does 0.27 look like a percentage? What do you multiply by to convert a decimal to a percent?
- Error: adding % C + % O and getting slightly more or less than 100 due to rounding — acknowledge that rounding can shift the last decimal; the important conceptual check is that the sum should be ≈ 100%.

> After groups finish: "Reveal — this is CO₂. Carbon dioxide. Every gram of CO₂ is 27.3% carbon and 72.7% oxygen by mass. Now you can compare CO₂ to any other carbon compound and see which delivers more carbon per gram."

### 22–28 min · Investigation — percent composition from the formula

Each student (working individually at their seat after the BTC debrief) completes the following structured table for each compound:

**The general formula:** % element = (n × atomic mass of element ÷ GFM of compound) × 100

where n = number of atoms of that element per formula unit (the subscript).

**Compound A: H₂O** (the figure — confirm with the pie chart)

| Element | n (subscript) | Atomic mass (g/mol) | Mass in formula (n × at. mass) | GFM | % by mass |
|---|---|---|---|---|---|
| H | 2 | 1.0 | 2.0 | 18.0 | 11.1% |
| O | 1 | 16.0 | 16.0 | 18.0 | 88.9% |

Check: 11.1 + 88.9 = 100% ✓

**Compound B: CO₂** (confirm BTC result; name the formula now)

| Element | n (subscript) | Atomic mass (g/mol) | Mass in formula (n × at. mass) | GFM | % by mass |
|---|---|---|---|---|---|
| C | 1 | 12.0 | 12.0 | 44.0 | 27.3% |
| O | 2 | 16.0 | 32.0 | 44.0 | 72.7% |

Check: 27.3 + 72.7 = 100% ✓

**Teacher facilitation prompts (circulate):**

> "For every compound, your first step is to find the GFM — you practiced that in Lesson 06. Then use it as the denominator. What is the GFM of CO₂?"

> "Why do you use n × atomic mass in the numerator rather than just the atomic mass?" — because n (the subscript) tells you how many atoms of that element are in one formula unit; each contributes its full atomic mass.

**Anticipated student responses:**

- "I got 27.2% for carbon instead of 27.3%." — both acceptable; the slight discrepancy is rounding at different stages. Chemists typically report to one decimal place. The important thing is the method.
- "Does the GFM change for each element's row?" — no; GFM is the same number in every row — it's the denominator, the total mass of the compound.
- "What if I have three or four elements?" — same method: fill in one row per element; all rows share the same GFM in the denominator; the percents for all elements must sum to 100%.

### 28–30 min · Reconnect + surface the method

Bring the class back together. Ask one student to describe the pattern they noticed in the formula:

> "Every time, you took the element's total mass contribution — subscript times atomic mass — and divided it by the GFM, then multiplied by 100. What does dividing by the GFM do? Why does × 100 turn it into a percent?"

Surface the key ideas: dividing by the GFM makes the fraction a proportion of the whole (a number between 0 and 1); multiplying by 100 converts that proportion to a percent. The method works for any element in any compound — you always use the GFM as the denominator.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look at the CO₂ result: 27.3% carbon, 72.7% oxygen. Now consider: if I changed the formula from CO₂ to CO (carbon monoxide), would the percent carbon increase or decrease? Talk with your partner — predict first, then reason through the math."

Students predict and check:
- CO: GFM = 12 + 16 = 28 g/mol; % C = 12/28 × 100 = 42.9%
- CO₂: % C = 12/44 × 100 = 27.3%

Target consensus: Adding more oxygen to the formula (increasing the GFM) while keeping the carbon contribution constant makes carbon a smaller fraction of the whole — its percent decreases. Removing oxygen makes carbon a bigger slice. The percent composition changes when the formula changes.

> "So two compounds with the same elements can have very different percent compositions depending on the formula. This is why two fertilizer compounds containing nitrogen can deliver different amounts of nitrogen per gram — the formula determines the proportions."

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name what we've been calculating. Every time we took an element's mass contribution and divided by the GFM, then multiplied by 100, we were finding the **percent composition** — the percentage by mass of each element in a compound. Percent composition is a fixed property of the formula: it doesn't change with sample size, but it does change if the formula changes."

> "Here is the Hochman appositive that will anchor this definition. An appositive is a phrase between dashes that renames the noun next to it. Say this with me:

> *Percent composition — the percentage by mass of each element in a compound — is calculated by dividing each element's mass contribution by the gram formula mass and multiplying by 100.*

> The phrase between the dashes defines the term; the main clause describes the procedure."

> "The denominator in that calculation is the **gram formula mass** — the mass of one mole of the compound, which we calculated in Lesson 06. Today, GFM is revisited in its new role: it is the 'whole pie' — the total mass against which each element's slice is measured."

> "The numerator — the element's mass contribution — is a **mass ratio**: the ratio of one element's mass in the formula to the total mass of the compound. Before you multiply by 100, the mass ratio is a decimal between 0 and 1. Multiplying by 100 converts it to a percent. The mass ratio for hydrogen in water is 2/18 = 0.111; the percent composition is 11.1%."

Post all three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "If the percent composition of nitrogen in urea (CO(NH₂)₂) is about 46.7%, what does that mean in plain English?" — *Expected response:* for every 100 grams of urea, about 46.7 grams are nitrogen. Or: nearly half of every gram of urea is nitrogen by mass.
- "Could a compound have a percent composition of more than 100% for any element? Why or why not?" — *Expected response:* no; each element's mass contribution cannot exceed the total GFM, so the mass ratio is always ≤ 1, and the percent is always ≤ 100. The total for all elements is exactly 100%.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the model + Appositive + Because/But/So expansion

Students return to their water pie chart and H₂O calculation from Phase 2. They annotate: label the numerator as "element's mass contribution," label the denominator as "GFM," and label the result as "percent by mass."

**Appositive sentence (model on board):**

> *"Percent composition — the percentage by mass of each element in a compound — is calculated by dividing each element's mass contribution by the gram formula mass and multiplying by 100."*

Ask students to write a parallel appositive for CO₂:

> *"The percent carbon in carbon dioxide — ___% — is calculated by dividing ___ g/mol (C's contribution) by ___ g/mol (GFM) and multiplying by 100."*

Then run a **Because / But / So** sentence about the fertilizer phenomenon. Starter on the board:

> *"Urea (CO(NH₂)₂) and ammonium nitrate (NH₄NO₃) both contain nitrogen, but the same mass of each compound delivers different amounts of nitrogen to plants."*

Model one aloud:

> "Urea and ammonium nitrate both contain nitrogen **because** nitrogen atoms are part of both chemical formulas — **but** urea has a nitrogen percent composition of about 46.7% while ammonium nitrate has about 35.0% — **so** for every 100 grams of fertilizer applied, urea delivers about 12 more grams of nitrogen than ammonium nitrate, which explains the difference in grass color."

Then have students write their own B/B/S using one of these starters:

- *"The percent oxygen in CO₂ is higher than the percent oxygen in H₂O…"* (hint: use the mass-ratio comparison)
- *"A student calculates the percent hydrogen in H₂O as 2% instead of 11.1%…"* (hint: they forgot to multiply by 100)

**Anticipated student responses:**

- "Because CO₂ has two oxygens and water only has one." — partial; push for the mass-ratio comparison: 32/44 = 72.7% vs. 16/18 = 88.9%. Actually, oxygen's percent is *higher* in water! Probe: which oxygen fraction is bigger? This is a productive surprise.
- "Because they forgot to multiply by 100, so they got the mass ratio instead of the percent." — excellent. Push for the So: so the student would report 0.111 instead of 11.1%, which sounds like only 0.1% of the compound is hydrogen — a 100-fold understatement.

### 39–40 min · Return to the phenomenon

> "Return to the two fertilizer bags. We started the lesson with a mystery: same 'nitrogen' label, different grass color. Now you have the tool. Let's check urea: CO(NH₂)₂. The formula has 2 nitrogen atoms. Nitrogen's atomic mass is 14. What is the GFM of urea?"

Students calculate: GFM = 12 + 16 + 2(14 + 2) + 2 = 12 + 16 + 28 + 4 = 60 g/mol.

> "So the percent nitrogen in urea is (2 × 14)/60 × 100 = 28/60 × 100 ≈ 46.7%. The label on that green-grass bag just became a number you can verify from the formula alone. No lab test needed. The formula tells you everything."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud:

> *For magnesium oxide, MgO (calculate the gram formula mass first using Mg = 24 g/mol, O = 16 g/mol):*
> *(a) What is the percent by mass of Mg in MgO? Show your setup.*
> *(b) What is the percent by mass of O in MgO? Show your setup.*
> *(c) In one sentence, why do the two percentages add up to 100%?*

Expected answers are in `Answer_Key.docx`.

**Closing Reflection (SEL, 30 seconds):**

> "Today you used the formula — symbols on paper — to predict something you could verify: how much of a useful element is actually in a product. In one sentence: how does knowing percent composition change the way you might read a product label, and who in the room helped you reason through it today?"

Collect worksheets; note which students correctly use GFM as the denominator versus students who divide by the element's atomic mass alone. Also note students who forget to multiply by 100 — they are reporting mass ratios (correct proportions, wrong scale). Target both error types for a brief one-on-one check at the start of the next lesson.

---

## Common Misconceptions

- **Misconception:** "The percent composition changes if you have a bigger sample of the compound." → **Correction:** Percent composition is a fixed property of the formula, not the sample size. Whether you have 18 g or 1800 g of water, hydrogen is always 11.1% by mass because the ratio 2/18 is constant. A larger sample has proportionally more of every element.
- **Misconception:** "The element that appears most often in the formula has the highest percent by mass." → **Correction:** Percent composition depends on mass, not atom count. H₂O has two hydrogen atoms but oxygen (one atom, mass 16) outweighs both hydrogens combined (2 × 1 = 2). The element with the highest atomic mass makes the largest mass contribution per atom, not the element with the highest subscript.
- **Misconception:** "I should divide by the element's atomic mass, not the GFM." → **Correction:** The denominator must be the total mass of the compound (GFM) because percent composition asks "what fraction of the whole compound is this element?" Dividing by the element's own atomic mass would give a ratio greater than 1 for elements with small atomic masses and has no physical meaning.
- **Misconception:** "The percents don't have to add up to 100% — some mass might be unaccounted for." → **Correction:** Every gram of the compound is made up entirely of its constituent elements. There is no "leftover" mass. The sum of all elements' percent compositions must equal exactly 100% (small deviations are rounding, not missing mass).
- **Misconception:** "Percent composition and percent by mass are different things." → **Correction:** They are the same quantity. "Percent composition" is the general term; "percent by mass" specifies that we are comparing masses (not volume or mole fraction). In this course, percent composition always means percent by mass unless otherwise stated.

---

## Access & Differentiation

- **ELL/ENL supports:** Calculation template pre-printed with column headers (Element | n (subscript) | Atomic mass (g/mol) | n × atomic mass | ÷ GFM | × 100 = %) and sentence frame: *"___ makes up ___% of ___ because ___."* Word-choice box displayed on the board throughout: {percent composition, gram formula mass, mass ratio, by mass, total}. The water pie chart (`water_composition.png`) serves as a permanent visual anchor — students can check whether their decimal result matches the slice they see in the chart.
- **IEP/SPED supports:** Pre-computed gram formula masses provided for all practice compounds (H₂O = 18 g/mol; CO₂ = 44 g/mol; NaCl = 58.5 g/mol; NH₃ = 17 g/mol; NH₄NO₃ = 80 g/mol) so the GFM-lookup step is not a barrier. Offer one-element-at-a-time table structure: student computes one element's percent before moving to the next. Calculator use expected for all arithmetic. Work through percent of H in H₂O together before independent practice.
- **Extensions:** (1) Calculate the percent water by mass in a named hydrate: CuSO₄ · 5H₂O. How does the water of crystallization figure into the GFM and the percent? (2) Empirical-formula teaser: if you know the percent composition of an unknown compound, can you work backward to find the formula? Briefly: percent → grams (assume 100 g sample) → moles → mole ratio → formula. (3) Consumer application: compare the percent nitrogen by mass in three common fertilizers (urea CO(NH₂)₂, ammonium nitrate NH₄NO₃, ammonium sulfate (NH₄)₂SO₄). Which delivers the most nitrogen per dollar if price per kilogram is given?

---

## Strategy Spotlight

**BTC — Building Thinking Classrooms.** The Building Thinking Classrooms framework (Peter Liljedahl, *Building Thinking Classrooms in Mathematics*, 2021) centers on three core practices that consistently raise student thinking: (1) **random grouping** removes status hierarchies and prevents friend-group comfort zones; (2) **vertical non-permanent surfaces** (whiteboards, windows, chart paper) make thinking visible, erasable, and collaborative; and (3) **thin-slice problems** launch students into work immediately — before any direct instruction — so thinking happens before consolidation.

**How BTC runs in this lesson (Phase 2, minutes 15–22):**

1. **Random groups:** Use a card randomizer (index cards, a digital spinner, or the class roster shuffled) to assign students to groups of three. Announce: "These are your working groups for the next seven minutes. Find your vertical surface."
2. **Vertical surfaces:** Each group claims one whiteboard panel, a section of window with a dry-erase marker, or a sheet of chart paper taped at standing height. One marker per group — the marker passes between group members so all three contribute writing.
3. **Thin-slice prompt:** The task is designed to be *just* beyond what students can do individually with prior knowledge alone, but *just* reachable with the group's collective thinking. The percent-composition thin-slice (CO₂ breakdown) is ideal: students know division and they know GFM from Lesson 06, but they haven't yet seen the percent-composition formula. The task forces them to invent the division themselves.
4. **Teacher as knowledge-withholder:** While groups work, circulate and ask only questions — never give the answer. Ask: "What's the whole?" "What operation gives you a fraction?" "Does your answer make sense?" The goal is for students to arrive at the correct method themselves before you formalize it in Phase 3.
5. **Gallery walk (optional, 2 min):** After groups finish, groups can briefly scan other groups' boards to see different setups before the class debrief.

**Why BTC fits percent composition:** The skill is a single, repeatable calculation, which makes it ideal for a thin-slice. Once students invent the ratio at the whiteboard — before seeing the formula — the vocabulary in Phase 3 names something they already understand. Research on BTC (Liljedahl, 2021) shows that students who derive a procedure before seeing it retain it more reliably than students who copy a procedure from a board.

**CRSE connection:** The fertilizer phenomenon connects to agricultural labor, food systems, and environmental justice — topics with deep resonance in communities where students' families work in food production or where nitrogen runoff affects local waterways. The random grouping practice is also a CRSE move: it disrupts the social sorting that often concentrates academic authority in a small group of students, signaling that every student's thinking is worth putting on the board.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — two fertilizer bags (same "nitrogen" label, different grass color); water pie chart as the model; return in Phase 4 with urea percent-nitrogen check |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — one oxygen vs. two hydrogens in water, who outweighs?); Phase 3 (TT#2 — CO vs. CO₂, does % C increase or decrease when oxygen is added?) |
| 3 | Students develop questions/models/procedures | Phase 2 ABCs (compute mass fractions from the pie chart before the formula); BTC thin-slice at vertical surfaces (groups invent the percent-composition calculation); individual investigation (H₂O, CO₂) |
| 4 | CCC defined and used | Lesson Overview · *Scale, Proportion, and Quantity*, explicit in Phase 3 (vocabulary) and Phase 4 (B/B/S: fixed proportion by formula, fertilizer application) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: percent composition / gram formula mass / mass ratio |
| 6 | Revisit phenomenon with evidence | Phase 4 — students calculate % nitrogen in urea and verify which fertilizer bag delivers more nitrogen per gram; pie chart used to self-check H₂O result |
| 7 | ENL/SPED supports | Access & Differentiation block: calculation template, sentence frame, word-choice box, pre-computed GFMs, one-element-at-a-time structure, calculator |
| 8 | Assessment check | Phase 5 — Exit Ticket (% Mg and % O in MgO; sentence explaining why percents sum to 100%) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked percent-composition example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **percent composition** — the percentage by mass of each element in a compound; calculated as (n × atomic mass of element ÷ gram formula mass of compound) × 100, where n is the subscript of the element in the formula; a fixed property of the compound that does not change with sample size
- **gram formula mass** — the mass of one mole of a compound (g/mol), revisited from Lesson 06 as the denominator in every percent-composition calculation; found by summing (atomic mass × subscript) for all elements in the formula; represents the "whole pie" against which each element's mass is compared
- **mass ratio** — the ratio of one element's mass contribution to the total mass (GFM) of the compound, expressed as a decimal between 0 and 1; multiplying the mass ratio by 100 converts it to percent composition; for hydrogen in water, the mass ratio is 2/18 = 0.111, giving a percent composition of 11.1%
