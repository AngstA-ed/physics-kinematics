# Heat Calculations — Teacher Guide

## Cover

**Unit: Heat & Energy — Lesson 02: Heat Calculations**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: HOCHMAN

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

**PS3-1** — *"Create a computational model to calculate the change in the energy of one component in a system when the change in energy of the other component(s) and energy flows in and out of the system are known. The energy flows in or out of the system, including a quantification in an algebraic description (flow into the system defined as positive); and the final energies of the system components, including a quantification in an algebraic description to calculate the total final energy of the system."*

This lesson gives students the three algebraic tools that quantify energy flow: **q = mcΔT** (heating or cooling without a phase change), **q = mH_f** (melting or freezing), and **q = mH_v** (boiling or condensing). Students learn the sign convention required by PS3-1 — energy flowing *into* a sample is positive (it gets warmer or melts), energy flowing *out* is negative (it cools or freezes) — and they apply it inside a calorimeter, where the heat lost by a hot object equals the heat gained by the water around it (q_lost = −q_gained). Per East Meadow guidance, calorimetry calculations are the quantitative backbone of the Heat & Energy unit and a recurring item on the 2025 NYSSLS-aligned Chemistry Regents.

The Cross-Cutting Concept of **Energy and Matter** is the explicit lens: energy is conserved as it flows from a hotter component to a cooler one within a closed system. The total energy does not vanish — it is transferred. The specific heat capacity *c* and the heats of fusion and vaporization (H_f, H_v) are the material properties that set *how much* a given mass of a substance heats up, melts, or boils for a given quantity of energy.

### Phenomenon

It is the same sunny afternoon at Jones Beach. The Sun pours the same energy onto every square meter of the shore. Walk barefoot across the dry sand and it is scorching — you hop from foot to foot. Take three steps into the ocean and the water is cool, almost cold. Same Sun, same hours of daylight, same energy arriving on each surface — yet the sand burns and the water stays cool. Now flip it: after sunset, the sand cools off quickly and the ocean stays warm into the night.

The contrast is striking and familiar without any equipment: the energy input is identical, but the temperature *response* is completely different. The difference is a measurable property of the material — its **specific heat capacity**. Water has a specific heat about five times that of sand, so the same quantity of energy raises the water's temperature far less. Today students learn the equation that quantifies exactly this: q = mcΔT.

### Javalab / Labs

- **Specific heat lab (metal samples):** Heat known masses of aluminum, iron, and copper shot in boiling water, then drop each into a measured mass of room-temperature water in a calorimeter (foam cup). Record the water's temperature rise. Using q = mcΔT and q_lost = −q_gained, students solve for the metal's specific heat and compare to the accepted value. Connect results to the bar chart in `figures/specific_heat_capacities.png`.
- **Calorimetry of food / hand warmer:** Burn a peanut or cheese curl under a can of water (food calorimetry), or activate a chemical hand warmer in a cup of water, and use q = mcΔT on the water to measure the energy released. A clean, motivating real-world tie to the Nutrition Facts panel (Calories) and to exothermic reactions.
- **Ice-melting calorimetry:** Drop a known mass of ice into warm water and measure how much the water cools. The energy lost by the water (q = mcΔT) goes into melting the ice (q = mH_f). A direct, hands-on use of the heat-of-fusion equation.
- **Boiling Point (Ice or Water, Ethanol) — Javalab:** The Javalab "Boiling Point" simulation lets students watch temperature plateau during a phase change, reinforcing that energy added during boiling goes into H_v (breaking attractions) rather than into raising the temperature — the conceptual companion to the q = mH_v equation.

### Assessments

- **Calorimetry problem set** (district checkpoint, following lesson; see `Assessments/` folder once created): mixed items requiring q = mcΔT, q = mH_f, and q = mH_v, plus a calorimetry "heat lost = heat gained" problem and correct sign assignment.
- **Lab report** (specific heat of an unknown metal): students report measured *c*, identify the metal by comparison to reference values, and discuss sources of heat loss.
- **Exit Ticket** (Phase 5): three items — a q = mcΔT calculation for copper, a q = mH_v calculation for boiling water, and a one-sentence sign-convention explanation. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | PS3-1 (quantify energy flow algebraically; flow into the system = positive; total final energy by conservation) |
| **CCC focus** | Energy and Matter — energy is transferred, not destroyed; in a closed calorimeter the heat lost by the hot component equals the heat gained by the cool component (q_lost = −q_gained) |
| **Strategy chips** | HOCHMAN — appositive sentence to define specific heat capacity crisply; B/B/S sentence in Phase 4 |
| **Materials** | 2025 NYS Chemistry Reference Tables (Table B: specific heat of water = 4.18 J/g·°C, H_f = 334 J/g, H_v = 2260 J/g; Table T: q = mcΔT, q = mH_f, q = mH_v), calculators, foam-cup calorimeters, thermometers, hot plate or pre-heated water bath, metal shot samples (Al, Fe, Cu), `figures/specific_heat_capacities.png` projected |
| **Safety** | Hot water bath and metal shot are burn hazards — use tongs, goggles, and a heat-resistant surface. No open flame required for the core lesson. Standard lab safety applies. |
| **Prior knowledge** | Lesson 01 (Heating & Cooling Curves) — temperature plateaus during phase change; energy added during melting/boiling breaks attractions rather than raising temperature. Students should recognize the heating-curve shape before this lesson. Students should also be fluent reading values off the Reference Tables. |

**Lesson objectives — students can:**

- Calculate the heat absorbed or released when a sample changes temperature using **q = mcΔT**, and identify the unit of each variable.
- Calculate the heat absorbed or released during melting/freezing (**q = mH_f**) and boiling/condensing (**q = mH_v**).
- Apply the sign convention required by PS3-1: energy flowing *into* a sample is positive; energy flowing *out* is negative; and in a calorimeter, q_lost = −q_gained.
- Explain, using Energy and Matter, why the same energy input produces a small temperature change in water but a large one in sand — because water has a much larger specific heat capacity.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers: *"Think of a place or a day where one thing heated up fast and another thing right next to it stayed cool — hot pavement vs. grass, a metal seatbelt buckle vs. the cloth seat, a sandy beach vs. the water. What came to mind?"* One round, one sentence each, no judgment. This surfaces the everyday intuition that the same Sun heats different materials by very different amounts — the exact idea the lesson quantifies.

Then post the **Do Now**:

> *"At the beach on a sunny day, the dry sand is scorching hot but the ocean water just a few steps away is cool. The Sun shines the same on both. Write one sentence: why does the sand get so much hotter than the water if they're getting the same sunlight?"*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "Because water is wet / water cools things down." — affirm the observation; redirect: the water isn't *removing* heat, it's *absorbing* the same sunlight but barely warming. Why?
- "Sand is darker so it absorbs more." — a real factor (color/albedo), capture it; but note that even equal absorbed energy warms sand more than water. Today's answer is about a property of the material itself.
- "Water takes more energy to heat up." — exactly the target idea; validate and say: today we'll put a number on *how much* more.

### 3–8 min · Phenomenon hook — same Sun, different temperature

**Teacher actions.** Tell the beach story vividly. Same beach, same hour, same sunlight on every square meter. Barefoot on the dry sand: scorching, you hop. Three steps into the ocean: cool, almost cold. Then flip it — after sunset the sand cools quickly while the ocean holds its warmth into the night. Same energy in, completely different temperature response.

Project the `figures/specific_heat_capacities.png` figure:

![Bar chart titled 'Specific Heat Capacity — Why Water Resists Heating' showing the specific heat c in joules per gram per degree Celsius for four materials: water (ocean) at about 4.18, sand (beach) at about 0.84, iron at about 0.45, and aluminum at about 0.90; the water bar towers about five times taller than the sand bar; the y-axis is labeled 'Specific heat c (J/g·°C)' and the x-axis labels each material.](figures/specific_heat_capacities.png)

**Sample teacher language:**

> "Look at this chart. The number on each bar is the *specific heat* — how many joules it takes to raise one gram of that material by one degree Celsius. Water's bar is about 4.18. Sand's bar is about 0.84 — roughly five times smaller. That means for the *same* energy delivered to the same mass, the sand's temperature climbs about five times higher than the water's. The Sun isn't playing favorites. The materials just respond differently. By the end of today you'll be able to calculate exactly how many joules it takes to heat any sample — and how many it takes to melt ice or boil water."

**Anticipated student responses:**

- "So water just needs more energy per degree?" — exactly; that property is what we'll name and calculate.
- "Why is iron even lower than sand?" — great eye; metals heat up fast, which is why a metal bench in the sun burns you instantly. Lower specific heat = faster temperature change for the same energy.
- "How do you actually calculate the energy?" — that's Phase 2; we'll build the equation together with real masses and temperatures.

**Driving question** (post on the board and leave it there):

> *How much energy does it take to change the temperature of a sample — and why does the same energy heat some materials far more than others?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the bar chart or the beach story. Then:

> "Turn to your partner: water and sand are getting the same sunlight. The water's specific heat (4.18) is about five times the sand's (0.84). In one sentence, predict — if the Sun delivers the same energy to equal masses of each, which one heats up more, and by roughly how many times?"

Target insight: the sand heats up about five times more than the water for the same energy input, because a lower specific heat means each joule raises the temperature more. We will name this property formally in Phase 3.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–15 min · ABCs Activity — build the equation from data, before the formal definition

**Before any formal vocabulary is introduced**, students reason out the relationship from a small data table rather than being handed the formula.

Each student receives the data table below (projected or on the worksheet). The setup: a hot plate delivers a measured amount of heat energy to different water samples, and we record the temperature change.

**Part 1 — Find the pattern (no formula yet):**

| Sample | Mass of water (g) | Energy added (J) | Temperature change ΔT (°C) |
|---|---|---|---|
| 1 | 100 | 4180 | 10 |
| 2 | 200 | 4180 | 5 |
| 3 | 100 | 8360 | 20 |

> "Compare Sample 1 and Sample 2: same energy, but Sample 2 has *twice* the mass and *half* the temperature change. Compare Sample 1 and Sample 3: same mass, but Sample 3 got *twice* the energy and warmed *twice* as much. Write down: how does the temperature change depend on the mass? How does it depend on the energy added?"

**Part 2 — Assemble the relationship:**

> "If doubling the mass halves the temperature change, and doubling the energy doubles the temperature change, write a relationship connecting energy (q), mass (m), and temperature change (ΔT). For water, what single number do you have to multiply by to make the units work? (Hint: in Sample 1, 4180 J ÷ (100 g × 10 °C) = ?)"

**Teacher facilitation language (circulate):**

> "Don't reach for the formula sheet yet. Just look at the numbers. When mass goes up, what does ΔT do? When energy goes up, what does ΔT do?"

> "Take Sample 1: 4180 joules, 100 grams, 10 degrees. Divide the energy by the mass times the degrees: 4180 ÷ (100 × 10). What do you get? Now check it against Sample 3. Same number?"

**Anticipated student responses during ABCs:**

- "More mass means it heats up less." — exactly; the energy is spread over more grams, so each gram gets less. That's the inverse relationship.
- "I divided and got 4.18 every time." — that constant is the specific heat of water; you just discovered it from the data, before I named it.
- "So q equals mass times the degrees times 4.18?" — you've just built q = mcΔT. We'll name *c* officially in Phase 3.

### 15–22 min · Initial Model — first q = mcΔT calculation

**Prompt on the board:**

> *"Using the relationship you just built (q = m × c × ΔT, with c = 4.18 J/g·°C for water): how much energy is needed to heat 50.0 g of water from 20.0 °C to 70.0 °C? Show every step: write the formula, list m, c, and ΔT, then solve."*

Students work individually for 3 minutes, then compare with a partner.

Target answer:

> q = mcΔT
> m = 50.0 g, c = 4.18 J/g·°C, ΔT = 70.0 − 20.0 = 50.0 °C
> q = (50.0)(4.18)(50.0) = 10,450 J ≈ 1.05 × 10⁴ J

**Teacher facilitation language:**

> "First find ΔT — that's *final minus initial*, 70 minus 20. Then multiply mass × specific heat × ΔT. Watch your units: grams times J/g·°C times °C — the grams cancel, the degrees cancel, and you're left with joules. If your answer isn't in joules, a unit went missing."

> "Is q positive or negative here? The water got *warmer*, so energy flowed *in*. Energy in is positive. Hold onto that idea — it's the sign rule we'll formalize later."

**Anticipated student responses:**

- "I used ΔT = 70, not 50." — ask: what was the *starting* temperature? ΔT is the *change*: final minus initial, 70 − 20 = 50.
- "I got 10,450 — is that too big?" — no; heating 50 g of water by 50 °C really does take about ten thousand joules. Water resists heating, remember the beach.
- "Should I round?" — 10,450 J or 1.05 × 10⁴ J are both fine; keep three significant figures.

### 22–30 min · Investigation — q = mcΔT, q = mH_f, q = mH_v

Groups of three or four work through a structured practice set covering all three heat equations. Each student writes the formula and substitutes before solving; then the group compares.

**Practice set (written on the board or distributed as a half-sheet). Use Reference Table B values: c(water) = 4.18 J/g·°C, H_f = 334 J/g, H_v = 2260 J/g.**

**Problem A — Heating (q = mcΔT):** How much heat is absorbed when 120. g of water is heated from 25.0 °C to 100. °C?

> q = mcΔT = (120.)(4.18)(100. − 25.0) = (120.)(4.18)(75.0) = 37,620 J ≈ 3.76 × 10⁴ J  (positive — energy in)

**Problem B — Melting (q = mH_f):** How much heat is needed to melt 45.0 g of ice at 0 °C into water at 0 °C?

> q = mH_f = (45.0)(334) = 15,030 J ≈ 1.50 × 10⁴ J  (positive — energy in; temperature stays at 0 °C)

**Problem C — Boiling (q = mH_v):** How much heat is needed to boil 30.0 g of water at 100 °C into steam at 100 °C?

> q = mH_v = (30.0)(2260) = 67,800 J ≈ 6.78 × 10⁴ J  (positive — energy in; temperature stays at 100 °C)

**Teacher facilitation prompts (circulate):**

> "Which equation? If the *temperature is changing*, use q = mcΔT. If the substance is *melting or freezing* at a constant temperature, use q = mH_f. If it's *boiling or condensing*, use q = mH_v. Check the problem: is the temperature changing, or is it stuck at the melting or boiling point?"

> "Notice in B and C there's no ΔT and no *c* — during a phase change the temperature doesn't move. All the energy goes into breaking attractions between particles, exactly like the flat plateaus on yesterday's heating curve."

> "Compare your answers for B and C: melting 45 g took about 15,000 J, but boiling 30 g took almost 68,000 J. Why is boiling so much more energy per gram? Because H_v (2260) is far bigger than H_f (334) — pulling particles completely apart into a gas takes much more energy than just loosening a solid into a liquid."

**Anticipated student responses:**

- On A: "Do I use ΔT = 100?" — no; ΔT is the *change*, 100 − 25 = 75 °C.
- On B: "Where's the temperature in the formula?" — there isn't one; melting happens *at* 0 °C with no temperature change. That's the whole point of H_f.
- On C: "Why is this number so huge?" — vaporization takes the most energy of all; H_v for water is 2260 J/g, more than six times H_f. It connects to why steam burns are so severe.

### 28–30 min · Reconnect + surface the method

Bring groups back together. Ask one group to put Problem A on the board and another to put Problem C. Ask the class:

> "Look at the two solutions side by side. In Problem A the temperature *changed* and we used *c*. In Problem C the temperature *stayed at 100* and we used H_v. How did you decide which equation to use? What in the problem told you?"

Surface the key decision rule: **if the temperature changes, use q = mcΔT; if a phase change happens at constant temperature, use q = mH_f (melting/freezing) or q = mH_v (boiling/condensing).** Then preview the sign idea: every q above was positive because energy flowed *in*. When a sample cools or freezes, energy flows *out* and q is negative — the rule we formalize next.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look back at the ABCs data table — for water, every sample gave the constant 4.18. Turn to your partner: what does that number 4.18 actually *mean*? What is it the amount of energy to do?"

Target consensus: 4.18 is the energy in joules needed to raise one gram of water by one degree Celsius. It is a property of the material — different substances have different values (sand ≈ 0.84, iron ≈ 0.45). It's the number that explains the beach.

> "Now connect it to the sign convention. In the calorimeter lab, when a hot metal goes into cool water, the metal *cools* and the water *warms*. Which one has positive q, and which has negative q? And how are the two amounts related?"

Target: the water gains energy (q positive, energy in); the metal loses energy (q negative, energy out). By conservation, the heat lost by the metal equals the heat gained by the water: q_lost = −q_gained. Energy is transferred, not destroyed — the Energy and Matter CCC.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name what we've been working with. That constant 4.18 for water — the energy to raise one gram by one degree — is the **specific heat capacity** of water, the *c* in q = mcΔT. Every material has its own value, and that value is exactly why the sand and the ocean reach different temperatures under the same Sun."

> "Here's the Hochman appositive move to lock in the definition. An appositive is a phrase set off by dashes that renames or explains the noun beside it. Say this with me:

> *Specific heat capacity — the energy needed to raise one gram of a substance by one degree Celsius — is the value of c in the equation q = mcΔT.*

> The phrase between the dashes defines the term in the same sentence. You'll use this structure on the Exit Ticket and in your notes."

> "The second term is **heat of fusion**, symbol H_f — the energy needed to *melt* one gram of a solid into a liquid at its melting point, with no change in temperature. For water that's 334 J/g. It's the *c*'s cousin for the flat melting plateau."

> "The third term is **heat of vaporization**, symbol H_v — the energy needed to *boil* one gram of a liquid into a gas at its boiling point, again with no temperature change. For water that's 2260 J/g — far larger than the heat of fusion, which is why boiling and steam carry so much energy."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "Sand's specific heat is about 0.84 J/g·°C and water's is 4.18. In plain English, what does that comparison tell you about the beach?" — *Expected response:* it takes about five times more energy to warm the same mass of water by one degree, so under the same Sun the sand heats up about five times more than the water.
- "Why does q = mH_f and q = mH_v have no ΔT in them?" — *Expected response:* during melting and boiling the temperature does not change — the energy goes into breaking attractions between particles, not into raising temperature. So there is no ΔT to include.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the model + Appositive + Because/But/So expansion

Students return to their Initial Model q = mcΔT calculation (50 g of water, 20 → 70 °C). They annotate it with vocabulary: label *c* as "specific heat capacity," mark ΔT as "final minus initial," and note that q is positive because energy flowed *in*. Then they write an appositive sentence.

**Appositive sentence (model on board):**

> *"Specific heat capacity — the energy needed to raise one gram of a substance by one degree Celsius — is the value of c in q = mcΔT."*

Ask students to write a parallel appositive for heat of vaporization:

> *"Heat of vaporization — ___ — is the value of H_v in q = mH_v, equal to ___ J/g for water."*

Then run a **Because / But / So** sentence about the phenomenon. Starter on the board:

> *"At the beach, the same sunlight falls on the sand and the ocean, but the sand gets much hotter."*

Model one aloud:

> "The sand gets much hotter than the ocean under the same Sun **because** sand has a far lower specific heat capacity (about 0.84 J/g·°C) than water (4.18 J/g·°C) — **but** both surfaces receive the same energy from the same sunlight — **so** each joule raises the sand's temperature about five times more than the water's, which is why the sand scorches your feet while the ocean stays cool."

Then have students write their own B/B/S using one of these starters:

- *"Boiling 30 g of water takes far more energy than melting 30 g of ice…"* (hint: compare H_v = 2260 to H_f = 334)
- *"When a hot metal is dropped into cool water in a calorimeter, the water warms up…"* (hint: q_lost = −q_gained; energy is transferred, not destroyed)

**Anticipated student responses:**

- "Because H_v is bigger than H_f." — good start; push for the So: "so it takes about 2260 J to boil each gram but only 334 J to melt each gram, meaning boiling takes nearly seven times more energy per gram."
- "Because the metal loses heat and the water gains it." — excellent; push for the So: "so the heat lost by the metal equals the heat gained by the water (q_lost = −q_gained), because energy is transferred, not destroyed."

### 39–40 min · Return to the phenomenon

> "Return to the beach. We now have the number that explains it. The Sun delivers, say, the same 4180 J to 100 g of sand and 100 g of ocean water. Quickly estimate: using q = mcΔT rearranged to ΔT = q / (mc), how much does each one warm? For water: 4180 ÷ (100 × 4.18). For sand: 4180 ÷ (100 × 0.84)."

Target: water ΔT = 4180 / 418 = **10 °C**; sand ΔT = 4180 / 84 ≈ **50 °C**. Same energy, same mass — the sand warms about five times more.

> "That five-times difference on your calculator *is* the beach. The specific heat capacity isn't an abstract number on a chart — it's the reason the sand burns your feet and the water stays cool. The equation q = mcΔT turns a beach day into chemistry you can compute."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud:

> *(a) How much heat is absorbed when 80.0 g of copper (c = 0.385 J/g·°C) is heated from 25.0 °C to 75.0 °C? Show the formula and substitution.*
> *(b) How much heat is needed to boil 25.0 g of water at 100 °C into steam at 100 °C? (H_v = 2260 J/g.) Show the formula and substitution.*
> *(c) In one sentence, explain the sign convention: when a sample cools down, is its q positive or negative, and why?*

Expected answers are in `Answer_Key.docx`.

**Closing Reflection (SEL, 30 seconds):**

> "Today we turned a beach day into a calculation — the same Sun, two very different temperatures, explained by one number. In one sentence: what is one thing that surprised you today about how energy and temperature connect, and who helped you figure something out?"

Collect worksheets; note which students correctly chose q = mcΔT versus a phase-change equation, and which still compute ΔT as the final temperature rather than the change. The equation-selection decision and the ΔT = final − initial step are the two main stumbling blocks — target those students for a brief one-on-one check at the start of the next lesson.

---

## Common Misconceptions

- **Misconception:** "ΔT is the final temperature." → **Correction:** ΔT is the *change* in temperature: final minus initial. Heating water from 20 °C to 70 °C gives ΔT = 50 °C, not 70 °C. Students who use the final temperature consistently overestimate q. Always compute T_final − T_initial first, then substitute.
- **Misconception:** "You use q = mcΔT for everything, including melting and boiling." → **Correction:** q = mcΔT only applies when the temperature is *changing*. During a phase change the temperature stays constant (the flat plateau on a heating curve), so there is no ΔT — use q = mH_f for melting/freezing and q = mH_v for boiling/condensing instead. Pick the equation by asking: is the temperature changing, or is the substance changing phase at a constant temperature?
- **Misconception:** "Heat of fusion and heat of vaporization are about the same size." → **Correction:** For water, H_v (2260 J/g) is nearly seven times H_f (334 J/g). Boiling a gram of water into steam takes far more energy than melting a gram of ice, because vaporization pulls the particles completely apart into a gas while melting only loosens a solid into a liquid. This is why steam burns are far more severe than ice-water burns.
- **Misconception:** "A high specific heat means a substance gets hot easily." → **Correction:** The opposite. A *high* specific heat means a substance *resists* temperature change — it takes a lot of energy to warm it up (and it gives off a lot as it cools). Water's high specific heat (4.18) is exactly why the ocean stays cool in the sun and warm at night. Sand's *low* specific heat is why it heats and cools quickly.
- **Misconception:** "Energy disappears when something cools off." → **Correction:** Energy is transferred, not destroyed (Energy and Matter CCC). When a hot metal cools in a calorimeter, the energy it loses is gained by the surrounding water: q_lost = −q_gained. The negative sign is the bookkeeping for "flowed out," not "vanished." The total energy of the closed system is conserved.

---

## Access & Differentiation

- **ELL/ENL supports:** Heat-calculation template pre-printed with the three formulas (q = mcΔT · q = mH_f · q = mH_v) and a labeled substitution line: *"q = ___ (m) × ___ (c) × ___ (ΔT) = ___ J."* Sentence frame: *"I used the equation ___ because the temperature ___ (changed / stayed the same)."* Word-choice box displayed throughout: {specific heat capacity, heat of fusion, heat of vaporization, joule, ΔT = final − initial}. Pair each equation with a gesture — palm rising for heating (ΔT), flat hand for the constant-temperature phase change.
- **IEP/SPED supports:** Provide a decision flowchart for choosing the equation ("Is the temperature changing? → yes: q = mcΔT · no: melting? q = mH_f · boiling? q = mH_v"). Pre-fill the constants on the student's card (c_water = 4.18, H_f = 334, H_v = 2260, c_copper = 0.385) so the Reference Table lookup is removed as a barrier. Offer a worked example with one number blanked out at a time. Calculator use is expected for all arithmetic; the conceptual work (choosing the equation, computing ΔT, assigning the sign) is the skill target.
- **Extensions:** (1) Multi-step problem: how much total energy is needed to take 20.0 g of ice at 0 °C all the way to steam at 100 °C? (Melt with H_f, heat the liquid with q = mcΔT, then boil with H_v, and add the three.) (2) Calorimetry solve-back: a 50.0 g metal sample at 100 °C is dropped into 100. g of water at 20.0 °C; the water warms to 23.0 °C. Use q_lost = −q_gained to find the metal's specific heat. (3) Research: why does a coastal city like Long Beach have milder temperatures than an inland city at the same latitude? Connect to water's high specific heat.

---

## Strategy Spotlight

**HOCHMAN — Appositive sentence.** The Hochman Writing Method (Judith Hochman and the Writing Revolution) treats sentence-level writing as a thinking tool. For this lesson the featured technique is the **appositive**, a noun phrase set off by dashes (or commas) that renames or defines the noun it follows. The appositive is ideal for vocabulary-heavy, equation-driven science content because it forces the student to embed a definition into a complete subject-verb sentence rather than parking the definition in isolation.

**The target appositive for this lesson:**

> *Specific heat capacity — the energy needed to raise one gram of a substance by one degree Celsius — is the value of c in the equation q = mcΔT.*

This sentence does three things at once: (1) names the term, (2) defines it in a concise phrase between the dashes, and (3) connects it to the equation in the main clause. Students who can write and say this sentence — not just recite the definition separately — are integrating the term into their active vocabulary and tying it to the math.

**How to run it in this lesson (Phase 3 → Phase 4):**

1. Post and read aloud the model appositive sentence together (Phase 3 vocabulary).
2. Ask students to write a parallel appositive for *heat of vaporization*: *"Heat of vaporization — ___ — is the value of H_v in q = mH_v, equal to ___ J/g for water."* This requires them to substitute the definition and the constant, confirming the abstract term connects to their concrete calculation.
3. In Phase 4, students write their own appositive for the term they used most in the investigation. Cold-call two or three students; ask: does the appositive phrase correctly define the term? Does the main clause name the right equation?

**Why the appositive fits heat calculations:** The three terms — specific heat capacity, heat of fusion, heat of vaporization — are easy to confuse precisely because they sound similar and all measure "energy per gram." The appositive forces each one to carry its own distinguishing definition (per *degree* vs. per gram *melted* vs. per gram *boiled*) inside a single sentence, which is exactly the discrimination students need when they decide which equation a problem calls for.

**CRSE connection:** The beach phenomenon is universally accessible to Long Island students — Jones Beach, Long Beach, and the bays are part of nearly every student's lived experience. Grounding an abstract energy equation in a barefoot walk across hot sand into cool water honors students' out-of-school knowledge and makes calorimetry feel continuous with their real summers rather than confined to a foam cup. The opening circle invites students' own "one thing heated, the other stayed cool" examples, validating that the science describes their world.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — beach: same Sun, hot sand vs. cool ocean; bar chart `specific_heat_capacities.png`; return in Phase 4 with the ΔT = q/(mc) sand-vs-water estimate |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — which heats more for equal energy, and by how many times?); Phase 3 (TT#2 — what does 4.18 mean, and q_lost = −q_gained?) |
| 3 | Students develop questions/models/procedures | Phase 2 ABCs data table (derive the relationship before the formula); Initial Model q = mcΔT calculation; group investigation across q = mcΔT, q = mH_f, q = mH_v |
| 4 | CCC defined and used | Lesson Overview · *Energy and Matter*, explicit in Phase 3 (q_lost = −q_gained consensus) and Phase 4 (B/B/S calorimeter / phase-change sentence) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: specific heat capacity / heat of fusion / heat of vaporization |
| 6 | Revisit phenomenon with evidence | Phase 4 — students compute ΔT for sand vs. water from equal energy and recover the ~5× difference that explains the beach |
| 7 | ENL/SPED supports | Access & Differentiation block: formula template, equation-choice flowchart, pre-filled constants, sentence frames, word-choice box, calculator |
| 8 | Assessment check | Phase 5 — Exit Ticket (q = mcΔT for copper; q = mH_v for boiling water; sign-convention sentence) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked calorimetry/heat example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **specific heat capacity (c)** — the energy needed to raise the temperature of one gram of a substance by one degree Celsius, in J/g·°C; the value of *c* in q = mcΔT; water's high value (4.18) explains why the ocean resists heating while sand (≈ 0.84) heats quickly
- **heat of fusion (H_f)** — the energy needed to melt one gram of a solid into a liquid at its melting point, with no temperature change; the value used in q = mH_f; for water, 334 J/g
- **heat of vaporization (H_v)** — the energy needed to boil one gram of a liquid into a gas at its boiling point, with no temperature change; the value used in q = mH_v; for water, 2260 J/g — far larger than the heat of fusion
