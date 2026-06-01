# Temperature–Volume & Temperature–Pressure Relationships — Teacher Guide

## Cover

**Unit: Gas Laws — Lesson 04: Temperature–Volume & Temperature–Pressure Relationships**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: ACTIVE LEARNING

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

This lesson develops the **direct relationships** between the temperature of a fixed sample of gas and its volume (at constant pressure, Charles's Law) and between temperature and pressure (at constant volume, Gay-Lussac's Law). Per the East Meadow Scope & Sequence for the Gas Laws unit, students learn that volume and pressure each rise and fall *directly* with **absolute (Kelvin) temperature** — not with Celsius temperature — and they practice both qualitative reasoning and quantitative T–V and T–P calculations. No discrete content performance expectation is tagged in the Scope & Sequence for this lesson; it builds the proportional-reasoning toolkit that later combined-gas-law and ideal-gas work depends on.

The Cross-Cutting Concept of **Scale, Proportion, and Quantity** is the explicit lens: when temperature is measured on the absolute (Kelvin) scale, doubling the temperature of a trapped gas doubles its volume (constant P) or doubles its pressure (constant V). The proportionality only works because the Kelvin scale starts at **absolute zero** — the temperature at which the extrapolated volume and pressure of an ideal gas both reach zero. Students see that *the choice of temperature scale changes whether the relationship looks proportional*, which is why chemists always convert to Kelvin before reasoning about gases.

### Phenomenon

You check your tires on a warm afternoon: 32 psi, right on spec. The next morning is the first hard freeze of the season, and the dashboard light glows: low tire pressure. You did not lose any air — no nail, no leak. By that afternoon, once the sun has warmed the car, the light goes off on its own and the gauge reads 32 psi again. **The same air, the same sealed tire, but the pressure dropped overnight and recovered by afternoon — and the only thing that changed was the temperature.**

For a vivid in-class version, run two demos. **Balloon in liquid nitrogen:** an inflated balloon is dipped into liquid nitrogen (−196 °C) and visibly shrinks to a fraction of its size, then re-inflates as it warms back to room temperature — the same air, a dramatic volume change driven by temperature alone (constant pressure). **Collapsing can:** a few milliliters of water are boiled inside an empty soda can; the can is inverted into ice water; the can implodes instantly as the trapped steam cools and its pressure drops below the surrounding air pressure. Both demos make the same point as the tire: cool a trapped gas and its volume (or pressure) falls; warm it and they rise.

**Driving question:** Why do tire pressures drop on cold winter mornings, even though no air escaped?

### Javalab / Labs

- **Balloon-in-liquid-nitrogen demonstration (teacher-led, constant pressure):** Inflate a balloon, record its approximate circumference, then lower it into a dewar of liquid nitrogen. Students observe the balloon collapse, then re-expand as it warms. Discussion: the air inside is the same; only temperature changed; volume followed temperature. **Safety: liquid nitrogen requires cryo-gloves, goggles, and a face shield; teacher demonstration only.** Connect to `figures/volume_vs_temperature.png`.
- **Collapsing-can demonstration (teacher-led, constant volume → pressure drop):** Boil a small amount of water in an empty soda can, then invert it quickly into ice water using tongs. The can implodes as the steam cools and condenses and the internal pressure drops. Discussion: cooling a trapped gas drops its pressure; here the outside air pressure crushes the can. **Safety: hot can and steam; use tongs and goggles; teacher demonstration only.**
- **T–V / T–P graph reading (student):** Using `figures/volume_vs_temperature.png` and `figures/pressure_vs_temperature.png`, students extend each straight line back to where volume (or pressure) would reach zero and read off the temperature: −273 °C. This is the empirical route to absolute zero — students *find* it on the graph rather than being told.
- **Optional Javalab gas-property simulation:** any virtual gas-law module that lets students hold pressure constant and vary temperature (watching volume change), then hold volume constant and vary temperature (watching pressure change), reinforces the two relationships before the calculation practice.

### Assessments

- **T–V and T–P calculation quiz** (district checkpoint, following lesson; see `Assessments/` folder once created): students convert Celsius to Kelvin, then solve V₁/T₁ = V₂/T₂ and P₁/T₁ = P₂/T₂ problems, showing the Kelvin conversion explicitly.
- **Exit Ticket** (Phase 5): three items — one T–V calculation, one T–P calculation, and a one-sentence explanation of why the tire pressure recovered by afternoon. The Exit Ticket values are deliberately different from the worksheet practice. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | Gas Laws unit — direct T–V (constant P) and T–P (constant V) relationships; absolute (Kelvin) temperature scale. No discrete content PE tagged in the Scope & Sequence. |
| **CCC focus** | Scale, Proportion, and Quantity — volume and pressure are each directly proportional to absolute temperature; doubling the Kelvin temperature doubles the volume (constant P) or pressure (constant V); the proportionality requires the Kelvin scale because it begins at absolute zero |
| **Strategy chips** | ACTIVE LEARNING — students predict each demo's outcome, then test their prediction by reading and extrapolating the graphs and running the calculations themselves before any formula is named |
| **Materials** | `figures/volume_vs_temperature.png` and `figures/pressure_vs_temperature.png` projected; calculators; demo materials (inflated balloon + liquid nitrogen with cryo-PPE; empty soda can, hot plate, tongs, ice-water bath); the 2025 NYS Chemistry Reference Tables |
| **Safety** | **Both demos are teacher-led only.** Liquid nitrogen: cryo-gloves, goggles, face shield; never seal LN₂ in a closed container. Collapsing can: boiling water and steam burns; handle the can with tongs; keep students back. |
| **Prior knowledge** | Earlier Gas Laws lessons — pressure as collisions of gas particles with container walls (kinetic molecular theory); Pressure–Volume (Boyle's Law) inverse relationship. Students should recognize that gas particles move faster at higher temperature. Celsius temperature is familiar; Kelvin is introduced here. |

**Lesson objectives — students can:**

- Describe the **direct relationship** between the temperature and volume of a fixed gas sample at constant pressure, and between temperature and pressure at constant volume.
- Convert a Celsius temperature to Kelvin (K = °C + 273) and explain why gas-law calculations require the **Kelvin scale**.
- Extrapolate a volume-vs-temperature (or pressure-vs-temperature) graph to locate **absolute zero** at −273 °C (0 K).
- Solve T–V problems with V₁/T₁ = V₂/T₂ and T–P problems with P₁/T₁ = P₂/T₂, using Kelvin temperatures.
- Explain, using Scale, Proportion, and Quantity, why a tire's pressure drops on a cold morning and recovers when it warms.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers in one sentence: *"Tell us about a time the cold (or the heat) made something behave differently than you expected — a phone that died in the cold, a jar lid that wouldn't budge, a door that stuck in summer. What happened?"* One round, no judgment. This surfaces the everyday intuition that temperature changes the physical behavior of matter — exactly what today formalizes for gases.

Then post the **Do Now**:

> *"You fill your tires to exactly 32 psi on a warm afternoon. The next morning is the first freeze of the year and the low-pressure warning light comes on — but there is no leak and no nail. By afternoon the light goes off by itself. In one sentence: where did the pressure go overnight, and where did it come back from?"*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "The cold made the air shrink, so there was less pressure." — affirm the direction; sharpen later: the *amount* of air did not change, but the cold air pushes less hard. We'll explain why.
- "Some air must have leaked out at night and leaked back in." — validate the reasoning, then create tension: if air leaked out, how could it come back in through a sealed tire? Hold that question.
- "The gauge was just wrong / the cold broke the sensor." — fair guess; note it and promise the graph will settle whether temperature alone can explain the whole swing.

### 3–8 min · Phenomenon hook — two demos, same idea

**Teacher actions.** Run the two demos as a matched pair (or describe them clearly if doing a projected version). First the **balloon in liquid nitrogen**: hold up the inflated balloon, ask for a prediction, then lower it into the LN₂. The balloon collapses to a fraction of its size; lift it out and it re-inflates as it warms. Then the **collapsing can**: boil a little water in the can, invert it into ice water, and it implodes. Tie the two together out loud.

**Sample teacher language:**

> "Watch the balloon. I did not let any air out — the knot is tied. I just made the air cold, and the balloon shrank. Now the can: I trapped hot steam inside, then cooled it fast, and the can crushed itself. In both cases the gas is sealed in, nothing escaped, and *the only thing I changed was the temperature.* So what is temperature doing to a trapped gas?"

**Anticipated student responses:**

- "Cold makes gases get smaller and hot makes them get bigger." — capture this as the headline; we'll make it precise (volume *and* pressure, and *how much*).
- "The cold slowed the air particles down." — excellent; that is the kinetic picture. Slower, less-frequent collisions mean less push — less volume needed, or less pressure.
- "The can got crushed by the air outside." — exactly right; when the inside pressure dropped, the outside air pressure won. Note it for the constant-volume case.

**Driving question** (post on the board and leave it there):

> *Why do tire pressures drop on cold winter mornings, even though no air escaped?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the balloon, the can, or the tire. Then:

> "Turn to your partner: the balloon shrank when it got cold, and the can's pressure dropped when it got cold. Both gases got *smaller* or *weaker* in the cold. Make a prediction — if you kept cooling a gas down, colder and colder, is there a temperature where its volume or its pressure would hit *zero*? Where might that be?"

Target insight (leave open if no one lands it yet): there should be a lowest possible temperature, where the gas's volume and pressure both extrapolate to zero. That temperature is **absolute zero** — and in Phase 2 students will *find* it on a graph.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–16 min · ACTIVE LEARNING — predict, then read the two graphs

**Before any formula or vocabulary is introduced**, students make predictions and then test them against real graphs. Hand out (or project) the worksheet and the two figures.

![Line graph titled 'Volume vs. Temperature (constant pressure)' for a fixed sample of gas. A solid purple line with circular data points runs from 0 °C (about 22.4 L) up to 100 °C (about 30.6 L); a dashed purple line extrapolates the same straight trend leftward and downward, crossing zero volume at −273 °C. An orange marked point and label at (−273 °C, 0 L) reads 'absolute zero (−273 °C = 0 K), V → 0'. The x-axis is Temperature in degrees Celsius and the y-axis is Volume in liters.](figures/volume_vs_temperature.png)

![Line graph titled 'Pressure vs. Temperature (constant volume)' for the air sealed in a tire. A solid blue line with circular data points runs across a realistic temperature window (about −20 °C to +40 °C), with the pressure rising as temperature rises; a dashed blue line extrapolates the straight trend down to zero pressure at −273 °C. Purple labels mark a 'cold morning −10 °C' point at lower pressure and a 'warm day +30 °C' point at higher pressure. An orange marked point and label at (−273 °C, 0 psi) reads 'absolute zero (−273 °C = 0 K), P → 0'. The x-axis is Temperature in degrees Celsius and the y-axis is Pressure in psi (absolute).](figures/pressure_vs_temperature.png)

**The task — Part 1, predict (no calculation yet):**

> "Look only at the *solid* part of each line — the part where we actually measured. As temperature goes up, what does volume do? What does pressure do? Now, *before you look at the dashed part*, predict with your partner: if we kept cooling the gas, where would the line eventually hit the bottom — where volume or pressure would be zero?"

**The task — Part 2, check by extrapolating:**

> "Now look at the dashed line. Both lines, if you extend them straight back, cross zero at the same temperature. Read it off the x-axis. What temperature is it?"

**Teacher facilitation language (circulate):**

> "Notice both lines are *straight* — that is what a direct relationship looks like. But also notice: neither line passes through the origin of the Celsius graph. They hit zero volume and zero pressure way out at −273 °C, not at 0 °C. That gap is the whole reason chemists invented a new temperature scale."

**Anticipated student responses during ACTIVE LEARNING:**

- "Volume goes up when temperature goes up — it's a straight line." — affirm; that is the direct relationship, made visible.
- "Both lines hit zero at −273." — exactly; you just located absolute zero by extending a graph. That is how scientists first found it.
- "Why doesn't 0 °C give zero volume? The line is still way up at 0 °C." — terrific observation; this is the key tension. 0 °C is *not* 'no temperature' — the gas is still warm enough to have volume and pressure. Only −273 °C empties it out.

### 16–24 min · Initial Model — find the proportion with Kelvin

**Prompt on the board:**

> *"Read two points off the volume graph: at 0 °C the volume is about 22.4 L; at 100 °C it is about 30.6 L. Convert each Celsius temperature to its distance above −273 °C (add 273): 0 °C → 273, 100 °C → 373. Now divide volume by that number for each point. What do you notice about the two ratios?"*

Students work individually for 3–4 minutes, then compare with a partner.

Target result:

> 22.4 ÷ 273 ≈ 0.082
> 30.6 ÷ 373 ≈ 0.082
> The ratio Volume ÷ (°C + 273) is the **same** at both points.

**Teacher facilitation language:**

> "Look at your two ratios. They match. That means V divided by (temperature measured from −273 °C) is constant. In other words, V is *directly proportional* to temperature — but only when you measure temperature starting from −273 °C. That shifted scale, starting at absolute zero, is what we'll name in a few minutes. For now: every gas calculation starts by adding 273."

**Anticipated student responses:**

- "The two numbers are basically equal." — yes — that equality is the proportionality. Same ratio everywhere on the line.
- "What if I used the Celsius number by itself — 22.4 ÷ 0 and 30.6 ÷ 100?" — try it: 22.4 ÷ 0 is undefined and 30.6 ÷ 100 = 0.306. The ratios do *not* match. That is exactly why Celsius fails and we must shift to start at −273.
- "So I always add 273 to the temperature first?" — yes; that is the non-negotiable first step of every gas-law problem.

### 24–30 min · Investigation — group T–V and T–P calculation practice

Groups of three or four work through a structured practice set. Each student converts to Kelvin first, then solves. Two worked relationships are on the board:

> **Constant pressure (T–V):** V₁ / T₁ = V₂ / T₂
> **Constant volume (T–P):** P₁ / T₁ = P₂ / T₂
> In both, **T must be in Kelvin (K = °C + 273).**

**Practice set (distributed as a half-sheet; full solutions in `Answer_Key.docx`):**

**Problem A (T–V, the balloon).** A balloon holds 2.0 L of air at 27 °C (300 K). It is cooled to −123 °C (150 K) at constant pressure. Find the new volume.

> Convert: 27 °C → 300 K; −123 °C → 150 K. Set up: 2.0 / 300 = V₂ / 150. Solve: V₂ = 2.0 × (150 / 300) = **1.0 L**. The volume halved because the Kelvin temperature halved.

**Problem B (T–P, the tire).** Air in a tire is at 30. psi (gauge) and 300 K on a warm day. The temperature drops to 270 K overnight at constant volume. Find the new pressure (treat 30. psi as the working pressure for the proportion).

> Set up: 30. / 300 = P₂ / 270. Solve: P₂ = 30. × (270 / 300) = **27 psi**. A 30 K drop knocked off 3 psi — enough to trip the warning light.

**Problem C (T–V, warming).** A gas occupies 5.0 L at 200 K. It is heated to 400 K at constant pressure. Find the new volume.

> Set up: 5.0 / 200 = V₂ / 400. Solve: V₂ = 5.0 × (400 / 200) = **10.0 L**. Doubling the Kelvin temperature doubled the volume.

**Teacher facilitation prompts (circulate):**

> "First thing on every problem: did you add 273? Circle your two Kelvin temperatures before you set up the proportion."

> "For Problem A, the temperature went from 300 K to 150 K — half. So what should happen to the volume? Halve it. Does your answer agree?"

> "Notice that in Problem B, a 30-degree drop on the Kelvin scale (300 → 270) is only a 10% drop, so pressure drops about 10%, from 30 to 27. The warning light is sensitive enough to catch that."

**Anticipated student responses:**

- "I got 0.66 L for the balloon — I used 27 and −123 as the temperatures." — redirect: those are Celsius; you must convert to Kelvin first (300 and 150). A negative temperature in the proportion is a red flag that you skipped the +273 step.
- On Problem C: "Doubling the temperature doubled the volume — is it supposed to be that clean?" — yes, when you work in Kelvin the proportion is exact. That is the payoff of the absolute scale.
- "Why does cooling the tire drop the pressure but not the volume?" — great distinction: the tire's volume is fixed (the rubber holds its shape), so cooling shows up as lower pressure, not lower volume. The balloon can change shape, so cooling shows up as lower volume at constant pressure.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look back at your two ratios from the Initial Model and your three solved problems. Turn to your partner: what one step made every problem work — and what would go wrong if you skipped it?"

Target consensus:

> "Every problem worked because we measured temperature from −273 °C instead of from 0 °C — we added 273 to get Kelvin. If you skip that and use Celsius, the ratios don't match and you can even divide by zero or by a negative number. Volume and pressure are proportional to temperature *only on the Kelvin scale*."

> "If a gas's Kelvin temperature is cut in half, what happens to its volume at constant pressure? To its pressure at constant volume?"

Target: both are cut in half. Direct proportion, both ways.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Now let's name what we have been doing all period. First — the temperature where the volume and pressure of an ideal gas both extrapolate to zero, the one you read off both graphs at −273 °C — is called **absolute zero**. It is the coldest temperature possible; nothing can go below it."

> "Second — the temperature scale that *starts* at absolute zero is the **Kelvin scale**. Zero Kelvin is absolute zero. To convert: **K = °C + 273.** That is why every gas calculation begins by adding 273 — it shifts you onto the scale where the proportion works. A change of one kelvin is the same size as a change of one Celsius degree; the scales are just shifted by 273."

> "Third — the connection we found between temperature and volume (constant P) and between temperature and pressure (constant V) is a **direct relationship**: when one goes up, the other goes up *in proportion*. Double the absolute temperature and you double the volume, or double the pressure. On a graph, a direct relationship is a straight line; in a calculation, the ratio V/T or P/T stays constant."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "We said volume and temperature have a *direct* relationship. Earlier in the unit, pressure and volume had an *inverse* relationship (Boyle). How is a direct relationship different from an inverse one on a graph?" — *Expected response:* direct = straight line sloping up (both increase together); inverse = a curve where one rises as the other falls. Accept either described in words.
- "If absolute zero is −273 °C, what is room temperature (about 25 °C) on the Kelvin scale?" — *Expected response:* 25 + 273 = 298 K. There is no negative number; everything is positive on the Kelvin scale, which is part of why it works for proportions.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the model + Because/But/So expansion

Students return to their Initial Model (the two matching ratios). They annotate it with vocabulary: label the +273 step as "convert to **Kelvin**," label the matching ratios as "evidence of a **direct relationship**," and mark −273 °C on the graph as "**absolute zero**, 0 K."

Then run a **Because / But / So** sentence about the phenomenon. Starter on the board:

> *"A tire reads 32 psi on a warm afternoon but trips the low-pressure light after a freezing night, even though no air escaped."*

Model one aloud:

> "The tire pressure drops on a cold morning **because** pressure has a *direct relationship* with absolute temperature — cooling the air lowers its Kelvin temperature, so its pressure falls in proportion — **but** no air actually escaped; the same number of gas particles are still sealed in the tire — **so** when the afternoon sun warms the tire back up, the Kelvin temperature rises again and the pressure recovers to 32 psi all on its own."

Then have students write their own B/B/S using one of these starters:

- *"A balloon shrinks to a fraction of its size when dipped in liquid nitrogen, then re-inflates on the counter…"* (hint: constant pressure, T–V)
- *"A sealed soda can with a little steam inside implodes when plunged into ice water…"* (hint: constant volume, the inside pressure drops below the outside air pressure)

**Anticipated student responses:**

- "Because the cold made the air shrink." — good start; push for the Because frame and the vocabulary: "because cooling lowers the Kelvin temperature, and volume has a direct relationship with absolute temperature, so the volume drops in proportion."
- "Because the steam cooled and its pressure dropped below the outside air." — excellent; push for the So: "so the higher outside air pressure crushed the can inward."

### 39–40 min · Return to the phenomenon

> "Return to the tire. We started not knowing whether air leaked out overnight. Now you have evidence. Using the graph and one quick proportion, can you show that a 300 K → 270 K overnight drop is enough to explain a low-pressure light without losing a single molecule of air?"

Target: P₁/T₁ = P₂/T₂ → 30 psi at 300 K becomes 30 × (270/300) = 27 psi at 270 K. The pressure drops by about 10% from temperature alone — no leak required — and rises back when the tire rewarms.

> "That warning light isn't telling you about a leak. It's telling you about *temperature.* The amount of air never changed; only its Kelvin temperature did, and pressure follows temperature directly."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud:

> *(a) A gas occupies 4.0 L at 250 K at constant pressure. It is warmed to 500 K. Find the new volume. Show the Kelvin step and the proportion V₁/T₁ = V₂/T₂.*
> *(b) A sealed rigid container holds gas at 200 kPa and 400 K. It is cooled to 200 K at constant volume. Find the new pressure. Show the proportion P₁/T₁ = P₂/T₂.*
> *(c) In one sentence, explain why the tire's pressure came back to 32 psi by the afternoon without anyone adding air.*

Expected answers are in `Answer_Key.docx`. **These values are deliberately different from the worksheet practice** (which used 2.0 L / 300 K / 150 K and 30 psi tire numbers), so the Exit Ticket measures transfer, not recall.

**Closing Reflection (SEL, 30 seconds):**

> "Today we explained an everyday mystery — the cold-morning tire light — with a straight line and one proportion. In one sentence: what is one thing that surprised you about how temperature controls a gas, and who helped you figure something out?"

Collect worksheets; note which students converted to Kelvin before setting up the proportion versus students who used Celsius (the appearance of a negative or zero temperature in a setup is the tell). The Kelvin-conversion step is the main procedural stumbling block — target those students for a brief check at the start of the next lesson.

---

## Common Misconceptions

- **Misconception:** "You can plug Celsius temperatures straight into the gas-law proportion." → **Correction:** The direct proportion V/T = constant and P/T = constant only holds when T is on the absolute (Kelvin) scale, because that scale starts at absolute zero. Using Celsius gives the wrong ratio and can produce division by zero (0 °C) or by a negative number. **Always convert: K = °C + 273.**
- **Misconception:** "Absolute zero is just 'really cold,' like the coldest day ever." → **Correction:** Absolute zero (−273 °C, 0 K) is the *lowest temperature that can exist* — the point where the extrapolated volume and pressure of an ideal gas reach zero. You cannot go below it. It is a hard floor, not just an extreme.
- **Misconception:** "When the tire pressure drops overnight, air must have leaked out." → **Correction:** No air escaped. The same number of gas particles are sealed inside; cooling lowers their Kelvin temperature, so they collide with the walls less often and less hard, dropping the pressure. Warm the tire and the pressure returns — impossible if air had actually leaked.
- **Misconception:** "Doubling the temperature in Celsius doubles the volume." → **Correction:** Going from 20 °C to 40 °C does *not* double the volume, because on the Kelvin scale that is only 293 K → 313 K (a 7% rise). To double the volume you must double the *Kelvin* temperature, e.g., 200 K → 400 K. Proportional reasoning only works in Kelvin.
- **Misconception:** "Temperature changes volume *and* pressure at the same time, always." → **Correction:** It depends on what is held constant. In a flexible balloon (constant pressure), cooling shows up as smaller *volume*. In a rigid sealed container or tire (constant volume), cooling shows up as lower *pressure*. The variable that is free to change is the one that responds.

---

## Access & Differentiation

- **ELL/ENL supports:** Two-step solution template pre-printed for every problem: **Step 1 — Convert: K = °C + 273.** **Step 2 — Set up: ___ / ___ = ___ / ___.** Sentence frame: *"When the temperature ___, the ___ (volume / pressure) ___ because they have a direct relationship."* Word-choice box displayed throughout: {absolute zero, Kelvin scale, direct relationship, constant pressure, constant volume, K = °C + 273}. Pair each demo with a gesture: hands closing together for the shrinking balloon, hands collapsing inward for the can.
- **IEP/SPED supports:** Provide a Celsius-to-Kelvin conversion strip (a number line showing −273 °C = 0 K, 0 °C = 273 K, 100 °C = 373 K) so the +273 step is concrete and visual. Pre-fill the proportion skeleton (V₁/T₁ = V₂/T₂) with the known values already placed, so the student's task is to solve for the unknown, not to set up. Calculator expected for all arithmetic; the conceptual targets are converting to Kelvin and recognizing the direct relationship. One problem at a time on separate cards.
- **Extensions:** (1) Combine both relationships: a gas at 1.0 L, 100 kPa, and 250 K is changed to 500 K at constant pressure, then squeezed to half its volume at constant temperature — track the pressure and volume through both steps. (2) Research why liquid nitrogen is −196 °C (77 K) and explain, using the Kelvin scale, how close that is to absolute zero compared with a winter day. (3) Real-gas check: at very low temperatures real gases liquefy before reaching absolute zero, so the straight line bends. Explain why the *extrapolation* to −273 °C still defines absolute zero even though no real gas stays a gas all the way down.

---

## Strategy Spotlight

**ACTIVE LEARNING — predict, test, explain.** The featured strategy is a predict-test-explain cycle that puts the cognitive work on students *before* any formula or definition is supplied. Research on active learning in science (Freeman et al., 2014; the East Meadow active-learning framework) consistently shows that students who commit to a prediction and then confront real data retain the concept far better than students who are shown the rule first. This lesson is built around that sequence.

**The active-learning moves in this lesson:**

1. **Predict (Phase 1–2):** Before the dashed extrapolation is revealed, students predict where each line would hit zero. Before any calculation, they predict the direction of each demo's outcome. Commitment to a prediction is what makes the later evidence *land*.
2. **Test (Phase 2):** Students extend the lines themselves and read −273 °C off the x-axis — they *discover* absolute zero rather than being told it. They compute V/T ratios at two points and find them equal — they *discover* the proportionality.
3. **Explain (Phase 3):** Only after the discovery does the teacher name the three terms (absolute zero, Kelvin scale, direct relationship). The vocabulary now labels something students have already seen, so it sticks.

**How to run it well:** Resist the urge to "rescue" students with the formula during Phase 2. The productive struggle of finding that Celsius ratios *don't* match — and Kelvin ratios *do* — is the whole point; it builds the felt need for the Kelvin scale. When you circulate, ask questions ("what happens if you use the Celsius number?") rather than giving answers. Save the synthesis for Phase 3.

**CRSE connection:** The opening circle (a time the cold or heat made something behave unexpectedly) invites students to bring lived experience — a dead phone in winter, a stuck jar lid, a car that wouldn't start — into the science. The anchoring phenomenon (a tire warning light on a cold morning) is something many students have seen in a family car, honoring out-of-school knowledge and making an abstract proportionality feel like an explanation for their own world rather than a textbook rule.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — cold-morning tire warning light; balloon-in-LN₂ and collapsing-can demos; return in Phase 4 with the 300 K → 270 K tire calculation |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — where would volume/pressure hit zero?); Phase 3 (TT#2 — what one step made every problem work?) |
| 3 | Students develop questions/models/procedures | Phase 2 ACTIVE LEARNING (predict, then extrapolate the graphs to find absolute zero); Initial Model (compute V/T ratios at two points); group T–V / T–P calculations |
| 4 | CCC defined and used | Lesson Overview · *Scale, Proportion, and Quantity*, explicit in Phase 3 (vocabulary, proportional reasoning) and Phase 4 (B/B/S tire explanation) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: absolute zero / Kelvin scale / direct relationship |
| 6 | Revisit phenomenon with evidence | Phase 4 — students use P₁/T₁ = P₂/T₂ to show a 300→270 K drop explains the low-pressure light without any leak; graph used to confirm |
| 7 | ENL/SPED supports | Access & Differentiation block: two-step template, Celsius→Kelvin strip, sentence frame, word-choice box, pre-filled proportion skeleton, calculator |
| 8 | Assessment check | Phase 5 — Exit Ticket (T–V calculation, T–P calculation, one-sentence tire explanation; values distinct from worksheet practice) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked T–V / T–P examples
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **absolute zero** — the lowest possible temperature, −273 °C (0 K), at which the extrapolated volume and pressure of an ideal gas both reach zero; no substance can be cooled below it
- **Kelvin scale** — the absolute temperature scale that begins at absolute zero, where 0 K = −273 °C; convert with K = °C + 273; gas-law proportions only work when temperature is expressed in kelvins
- **direct relationship** — a proportional connection in which two quantities rise and fall together, graphing as a straight line; for a fixed gas, volume is directly proportional to absolute temperature at constant pressure, and pressure is directly proportional to absolute temperature at constant volume
