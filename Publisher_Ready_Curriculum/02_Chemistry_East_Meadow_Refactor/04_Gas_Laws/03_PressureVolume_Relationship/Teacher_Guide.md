# Pressure–Volume Relationship (Boyle's Law) — Teacher Guide

## Cover

**Unit: Gas Laws — Lesson 03: Pressure–Volume Relationship (Boyle's Law)**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: BTC

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

This lesson sits inside the Gas Laws unit and develops the kinetic-molecular account of gas behavior that the 2025 NYSSLS-aligned Regents expects students to reason with quantitatively. Students model the inverse relationship between pressure and volume at constant temperature — Boyle's Law — both qualitatively (a syringe gets harder to push as the trapped air is squeezed) and quantitatively (P₁V₁ = P₂V₂). The Science and Engineering Practices in play are **Analyzing and Interpreting Data** (reading a P–V curve and recognizing that PV stays constant) and **Using Mathematics and Computational Thinking** (solving for an unknown pressure or volume with the Boyle's Law equation). No single content performance expectation is assigned in the East Meadow Scope & Sequence for this day; the lesson builds the gas-law fluency that later combined-gas-law and stoichiometry work depend on.

The Cross-Cutting Concept of **Scale, Proportion, and Quantity** is the explicit lens: when temperature and the amount of gas are held constant, pressure and volume are *inversely proportional* — halve the volume and the pressure doubles, so their product stays the same. Students learn to distinguish an inverse proportion (P up, V down, product fixed) from the direct proportions they have met before.

### Phenomenon

Cap a plastic syringe full of air by sealing the tip (a finger over the nozzle, or a rubber stopper). Push the plunger in. It moves at first, then fights back — the harder you push, the harder it pushes back, and you can never quite reach the bottom. Now pull the plunger out against the seal: it resists in the other direction and springs back when released. The amount of air never changed; no air went in or out. Yet the same trapped gas behaves like a spring. Why does squeezing the air make it harder and harder to push?

**Driving question:** Why does a syringe get harder to push as you compress the air inside?

### Javalab / Labs

- **Gas Properties – PhET Interactive Simulations** (`https://phet.colorado.edu/en/simulations/gas-properties`). Use the "Ideal" screen with the temperature and particle count held constant. Students drag the wall to shrink the container's volume and watch the pressure gauge climb, then read off paired (P, V) values to test whether PV stays constant. The simulation makes the particle picture visible — fewer cubic centimeters means particles strike the walls more often, so pressure rises.
- **Syringe-pressure exploration** (hands-on, no chemicals): each group gets a 30–60 mL plastic syringe. Seal the tip, record the starting volume, then push the plunger to set volumes (e.g., 60 → 40 → 30 → 20 mL) and feel how the resistance grows. Pair with the PhET pressure readings, or with a low-cost pressure sensor if available, to collect a real (P, V) data set. Connect the felt resistance to the rising bars in `figures/pressure_volume_curve.png`.
- **Graph reading:** students interpret `figures/pressure_volume_curve.png` to answer: what happens to pressure as volume drops? Why is the curve a smooth bend rather than a straight line? Pick any two points on the curve and check that P × V gives the same number.

### Assessments

- **P–V graphing & calculation problem set** (district checkpoint, following lesson; see `Assessments/` folder once created): students solve for an unknown P or V using P₁V₁ = P₂V₂, sketch or read a P–V curve, and write one sentence explaining why pressure and volume are inversely related.
- **Exit Ticket** (Phase 5): two Boyle's-Law calculations (one solving for pressure, one solving for volume) using values **distinct** from the worksheet practice, plus a one-sentence particle-level explanation of the syringe phenomenon. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | Gas Laws — Boyle's Law (P–V inverse relationship at constant T); SEP Analyzing Data + Using Mathematics; no single content PE assigned for this day |
| **CCC focus** | Scale, Proportion, and Quantity — at constant temperature and amount, pressure and volume are inversely proportional, so their product P × V stays constant; halving V doubles P |
| **Strategy chips** | BTC — visibly random groups, vertical non-permanent surfaces, a thinking task launched with minimal instructions (Phase 2 syringe + PhET exploration) |
| **Materials** | One sealable plastic syringe (30–60 mL) per group, rubber stoppers or caps to seal the tip, whiteboards / windows / chart paper for vertical surfaces and markers (BTC), devices for the PhET Gas Properties simulation, calculators, `figures/pressure_volume_curve.png` projected |
| **Safety** | Low-hazard. Do not seal a syringe and push with body weight on a hard surface — push by hand only; an over-pressurized syringe can pop the plunger or crack. No chemicals, no flame. Eye protection optional. |
| **Prior knowledge** | Gas Laws Lessons 01–02 — gases are mostly empty space and are compressible; gas pressure comes from particles colliding with container walls; temperature relates to average particle speed. Students should recognize "pressure" as force per area and have seen the kinetic-molecular picture of a gas. |

**Lesson objectives — students can:**

- Describe qualitatively how the pressure of a trapped gas changes as its volume changes at constant temperature (volume down → pressure up).
- State Boyle's Law in words and as an equation (P₁V₁ = P₂V₂; equivalently PV = constant at fixed T and amount).
- Solve for an unknown pressure or volume using P₁V₁ = P₂V₂, carrying correct units.
- Explain, using Scale, Proportion, and Quantity and the particle model, *why* pressure and volume are inversely proportional.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Do Now

Post the **Do Now**:

> *"You seal the tip of a syringe full of air with your finger, then push the plunger in. The plunger moves at first, then fights back harder and harder, and you can't reach the bottom. No air went in or out. In one sentence: why do you think it gets harder to push?"*

Give students 2 minutes to write silently, then take two or three responses. (No opening circle today — this is a mid-unit lesson, not a unit opener; the strategy chip in focus is BTC.)

**Anticipated student responses to Do Now:**

- "The air is pushing back." — affirm; and ask: pushing back *harder* as you go — why would it push back harder the more you squeeze?
- "There's less room, so it's more squished." — close; that's the seed of the whole idea. Probe: what are the air particles doing when there's less room?
- "You're compressing it, so the pressure goes up." — strong; ask them to hold that word *pressure* — we will make it precise and put numbers on it today.

### 3–8 min · Phenomenon hook — the syringe as a spring

**Teacher actions.** Hold up a sealed syringe. Push the plunger in slowly so the class sees it resist, then release and let it spring back. Then pull it out against the seal and let it spring back the other way. Narrate: same air, no air in or out, yet it acts like a spring in both directions.

**Sample teacher language:**

> "Nothing went in or out of this syringe — the amount of air is fixed. The temperature in this room isn't changing either. The only thing I'm changing is how much *space* the air has. When I push in, it fights back. When I pull out, it fights back the other way. So the space the gas takes up and how hard it pushes are tied together somehow. Today we find the exact rule that ties them together."

**Anticipated student responses:**

- "It's like a spring." — excellent; that is exactly the felt experience. We'll explain the spring with particles in Phase 3.
- "The particles are hitting the walls more." — capture this; we will sharpen it into the particle explanation later. Don't confirm the full mechanism yet.
- "Does pulling it out make a vacuum?" — good instinct; pulling out lowers the pressure below room pressure, which is why it springs back inward. Note it and move on.

**Driving question** (post on the board and leave it there):

> *Why does a syringe get harder to push as you compress the air inside?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses. Then:

> "Turn to your partner: as I push the plunger in, the volume of the trapped air goes *down*. What is happening to the pressure — and how do you know from what you just felt?"

Target insight (leave open if no one lands it yet): as volume decreases, pressure increases — they move in *opposite* directions. That opposite-direction pattern is the inverse relationship we will name and put numbers on.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–13 min · BTC launch — visibly random groups + the thinking task

**Before any vocabulary or equation is introduced**, launch the Explore as a **Building Thinking Classrooms** task (see Strategy Spotlight). Form **visibly random groups of three** (deal cards or use a randomizer on screen), send each group to a **vertical non-permanent surface** (whiteboard, window, or chart paper), and give **one marker per group**. Launch the task verbally with minimal instructions — do not pre-teach Boyle's Law or the equation:

> "Each group has a sealed syringe and the PhET Gas Properties simulation. Change the volume of the trapped gas — by hand on the syringe and by dragging the wall in the simulation — and record what happens to the pressure. Find the *rule*. Write any pattern you can find between the two numbers on your surface."

### 13–24 min · Investigation Part 1 — syringe + PhET data collection

Groups collect paired (volume, pressure) readings. From the syringe they feel the resistance and read the volume marks; from PhET they read the pressure gauge while holding temperature and particle count fixed. Have each group record at least four (V, P) pairs on their vertical surface and look for a pattern.

A clean reference data set (PhET "Ideal" screen, constant T, constant particle count) looks like this — your students' exact numbers will differ, but the *product* should stay nearly constant:

| Volume (mL) | Pressure (kPa) | P × V |
|---|---|---|
| 120 | 1.0 | 120 |
| 60 | 2.0 | 120 |
| 40 | 3.0 | 120 |
| 30 | 4.0 | 120 |
| 20 | 6.0 | 120 |

**Teacher facilitation language (circulate — BTC keeps you asking, not telling):**

> "What happens to the pressure number every time the volume number drops? Do they move the same way or opposite ways?"

> "You found pressure goes up when volume goes down. Can you find a number that *doesn't* change? Try multiplying the volume by the pressure each time — what do you get?"

> "When you cut the volume in half — 60 to 30 — what exactly happened to the pressure? Is that a coincidence?"

**Anticipated student responses during the BTC task:**

- "When volume goes down, pressure goes up." — affirm; push: by how much? Cut volume in half and check the pressure.
- "Every time we multiply them we get about the same number." — that is the discovery. Ask them to write that as a rule in their own words on the surface.
- "Our syringe numbers aren't as clean as PhET." — validate: real gas, friction in the plunger, leaks at the seal. The *trend* is what matters; PhET removes the messiness so the rule is visible.

### 24–28 min · Investigation Part 2 — read the P–V curve

Project the curve and have groups compare it to the pattern on their surfaces.

![Line graph titled 'Pressure vs. Volume at constant temperature' showing a smooth downward-curving line: pressure in kilopascals on the y-axis (from 0 to 6) falls steeply as volume in milliliters on the x-axis (from 20 to 120) increases; the curve passes through (20 mL, 6 kPa), (40 mL, 3 kPa), (60 mL, 2 kPa), and (120 mL, 1 kPa); the legend labels the line 'P × V = constant (T fixed)', indicating an inverse proportion where the product of pressure and volume stays the same at every point.](figures/pressure_volume_curve.png)

> "On your surface you found a rule. Here is the same rule as a graph. Pick any two points on this curve — read off the volume and the pressure — and multiply them. Then do it again for two different points. What do you notice about the products?"

Target: every point on the curve gives the same product (≈120 in these units). The curve bends because the relationship is inverse, not straight — pressure never reaches zero and never quite hits the wall, it just keeps trading off against volume.

### 28–30 min · Reconnect + surface the pattern

Bring groups back. Ask one group to read their (V, P) table and their product column aloud.

> "Across every group, two things happened: pressure went *up* when volume went *down*, and their *product* stayed about the same. Those two statements are actually one rule. Let's name it."

Surface the key idea without yet giving the term: at constant temperature and amount of gas, P and V move in opposite directions and their product is constant. That sentence *is* Boyle's Law — we name it next.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look at your data table and the curve. Turn to your partner: when volume goes from 60 mL to 30 mL — cut in half — what happens to the pressure, and what stays the same? State it as precisely as you can."

Target consensus: cutting the volume in half *doubles* the pressure (2.0 → 4.0 kPa), while the product P × V stays the same (120). Pressure and volume are *inversely proportional*: as one is multiplied by a factor, the other is divided by that same factor.

> "What would happen if I tripled the volume instead — from 20 mL to 60 mL? Predict the pressure before you check the table."

Target: pressure is divided by three (6.0 → 2.0 kPa). The product is still 120. The rule holds in both directions.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name what you discovered. The rule that pressure and volume move in opposite directions at constant temperature — and that their product stays constant — is **Boyle's Law**. In words: for a fixed amount of gas at constant temperature, pressure and volume are inversely proportional. As an equation we write **P₁V₁ = P₂V₂** — the product before a change equals the product after the change."

> "The pattern itself — when one quantity goes up by a factor and the other goes down by the *same* factor, so the product is constant — is called an **inverse proportion** (or inverse relationship). That is different from the direct proportions you've seen, where both quantities rise together. Boyle's Law is the inverse proportion between pressure and volume."

> "And the reason behind it lives in the third term: **gas pressure**. Gas pressure is the force per area that gas particles exert by colliding with the walls of their container. When you shrink the volume, the same number of particles are packed into less space, so they hit the walls *more often* per second — and more collisions per area means higher pressure. That is *why* the syringe fights back harder: you've crowded the particles, so they strike back more frequently."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "If I push the syringe to half its volume, the equation says the pressure doubles. Using particles, why does it double?" — *Expected response:* the same number of particles in half the space hit the walls about twice as often per second, so the force per area roughly doubles. That's Boyle's Law from the particle view.
- "Why does Boyle's Law require constant temperature?" — *Expected response:* if temperature changed, the particle speeds would change too, and pressure would shift for a second reason. Holding temperature fixed isolates the volume effect so the inverse proportion is clean. (Accept partial answers; this previews the next gas law.)

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Apply the equation + Because/But/So expansion

Groups return to their vertical surfaces and **apply** the rule to a new calculation — the first time they use P₁V₁ = P₂V₂ to solve for an unknown.

> "A trapped gas occupies 50.0 mL at 100. kPa. You compress it to 25.0 mL at constant temperature. Use P₁V₁ = P₂V₂ to find the new pressure."

Work it as a class once on the board:

> P₁V₁ = P₂V₂ → (100. kPa)(50.0 mL) = P₂(25.0 mL) → P₂ = (100. × 50.0) / 25.0 = **200. kPa**

Point out the proportional check: volume was halved, so pressure doubled — the arithmetic and the proportion agree.

Then run a **Because / But / So** sentence (Hochman support inside the BTC frame). Starter on the board:

> *"When you squeeze a sealed syringe to half its volume, the pressure doubles."*

Model one aloud:

> "When you squeeze a sealed syringe to half its volume, the pressure doubles **because** the same number of gas particles are now packed into half the space, so they collide with the walls about twice as often per second — **but** the temperature and the amount of gas never changed — **so** pressure and volume stay inversely proportional and their product P × V holds constant, which is exactly Boyle's Law."

Then have students write their own B/B/S using one of these starters:

- *"A student triples the volume of a trapped gas at constant temperature…"* (hint: pressure is divided by three)
- *"A diver's air bubble grows larger as it rises toward the surface…"* (hint: pressure on the bubble drops as it rises, so its volume grows — inverse relationship)

**Anticipated student responses:**

- "Because there's less room so more hits." — good start; push for the So: "so the product P × V stays the same and the pressure doubles when volume halves."
- "Tripling the volume divides the pressure by three." — excellent; push for the Because: "because the same particles spread over three times the space hit the walls one-third as often."

### 39–40 min · Return to the phenomenon

> "Return to the sealed syringe from the start of class. You now have the rule and the reason. In one sentence using the word *pressure*: why did the plunger get harder and harder to push the further you pushed it in?"

Target: "As I pushed the plunger in, the volume shrank, so the same air particles were crowded into less space and struck the walls more often — the pressure rose (inversely with volume), and that rising pressure is what pushed back harder."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud:

> *(a) A gas occupies 8.0 L at 1.5 atm. At constant temperature it is compressed to 3.0 L. Use P₁V₁ = P₂V₂ to find the new pressure. Show your work.*
> *(b) A gas is at 200. kPa in a 2.0 L container. At constant temperature the pressure drops to 50. kPa. Find the new volume. Show your work.*
> *(c) In one sentence, use the particle model to explain why decreasing a gas's volume increases its pressure.*

(These values are deliberately different from the worksheet practice.) Expected answers are in `Answer_Key.docx`.

**Closing Reflection (SEL, 30 seconds):**

> "Today you discovered a rule by feeling it in your own hand and then proving it with numbers. In one sentence: what is one thing that surprised you about how pressure and volume trade off, and who — a groupmate or an idea on the board — helped you see it?"

Collect the vertical-surface photos or worksheets; note which students wrote pressure and volume as a *direct* relationship (both up together) — that reversed-direction error is the main misconception to revisit next lesson.

---

## Common Misconceptions

- **Misconception:** "When you compress a gas, you are squeezing the particles themselves smaller." → **Correction:** The particles do not shrink. Compressing reduces the *empty space between* particles, so the same number of particles occupy less volume. Gas is mostly empty space, which is why it compresses; the particles themselves keep their size.
- **Misconception:** "Pressure and volume go up together (a direct relationship)." → **Correction:** Boyle's Law is an *inverse* relationship. When volume goes down, pressure goes *up*. The product P × V stays constant. Students who graph or describe both rising together have the direction reversed — point them back to the syringe (less room, more push-back).
- **Misconception:** "Boyle's Law works no matter what." → **Correction:** Boyle's Law holds only when temperature *and* the amount of gas are constant. Change the temperature, and pressure shifts for a separate reason; add or remove gas, and the count of particles changes. The inverse P–V proportion is specifically the constant-temperature, fixed-amount case.
- **Misconception:** "If you keep compressing, the pressure eventually stops rising / the volume can reach zero." → **Correction:** On the ideal P–V curve, pressure keeps climbing as volume shrinks and never reaches zero volume — the curve bends but never touches the axes. (Real gases eventually liquefy, but that is beyond Boyle's Law.) The relationship is a smooth inverse curve, not a line that flattens out.
- **Misconception:** "P₁V₁ = P₂V₂ means you add the pressure and volume." → **Correction:** You *multiply* pressure by volume on each side, then solve for the unknown. The equation is a statement that the *product* is conserved, not a sum.

---

## Access & Differentiation

- **ELL/ENL supports:** Sentence frames for the BTC task and Exit Ticket: *"When the volume ___, the pressure ___ because ___ ."* and *"P times V stays ___ because ___ ."* Word-choice box displayed throughout: {pressure, volume, inverse, inversely proportional, compress, constant, product, collide, particles, Boyle's Law}. Pair each idea with a gesture: hands moving together for "compress / pressure up," hands moving apart for "expand / pressure down." Allow students to draw the particle picture (fewer dots in a smaller box) on the vertical surface, not only words.
- **IEP/SPED supports:** Provide a pre-printed data table with the volume column already filled (120, 60, 40, 30, 20) so the student records only the pressure and the product. Give a worked P₁V₁ = P₂V₂ template with the equation and the substitution boxes pre-drawn, so the task is the reasoning and arithmetic, not recalling the formula. Assign clear BTC group roles: one operates the syringe/simulation, one reads numbers, one writes on the surface. Calculator use expected for all arithmetic.
- **Extensions:** (1) On the P–V curve, prove algebraically that doubling V always halves P by showing P × V is constant — pick three pairs of points and compute. (2) Real-world transfer: explain why a sealed bag of chips puffs up at high altitude (lower outside pressure → bag's trapped gas expands). (3) Research and explain how Boyle's Law sets a hard rule for scuba divers ("never hold your breath while ascending") — connect rising volume to falling pressure as a diver surfaces.

---

## Strategy Spotlight

**BTC — Building Thinking Classrooms (Peter Liljedahl).** BTC restructures the room so that *students*, not the teacher, do the thinking. Three of its core practices anchor this lesson: **visibly random groups** (formed in front of the class so students trust the process and mix with everyone), **vertical non-permanent surfaces** (whiteboards, windows, or chart paper — vertical and erasable, which lowers the stakes of being wrong and makes thinking public), and **tasks launched with minimal instructions** (the teacher poses the problem, then steps back and asks questions instead of demonstrating the method).

**How to run it in this lesson (Phase 2):**

1. Form visibly random groups of three (deal cards / randomizer on screen). Each group gets one marker, one syringe, the PhET simulation, and one vertical surface.
2. Launch the task verbally in one sentence: *"Change the volume of the trapped gas, record the pressure, and find the rule that connects them."* Resist the urge to state Boyle's Law or write P₁V₁ = P₂V₂ first — the whole point is that students build the rule from their own data.
3. Circulate and ask, never tell: *"Do pressure and volume move the same way or opposite ways?" "Find a number that doesn't change — try multiplying them." "You halved the volume; what happened to the pressure exactly?"* When a group is stuck, give a hint that keeps the thinking with them.
4. Use the vertical surfaces as the class's shared thinking record in Phase 3 — groups literally point to their (V, P) products as the constant that becomes Boyle's Law.

Because the surfaces are non-permanent and public, students revise freely in Phase 4 — turning their discovered pattern into the equation P₁V₁ = P₂V₂ is a low-stakes edit on a board, not a crossed-out mess on private paper. Research on BTC (Liljedahl, *Building Thinking Classrooms in Mathematics*, and its cross-disciplinary extensions) finds that random groups + vertical surfaces sharply increase the proportion of students actively reasoning rather than copying.

**Connection to Hochman literacy:** the Because/But/So sentence in Phase 4 captures the exact reasoning students just made visible on the board — a *cause* (particles crowded into less space), a *contrast* (but temperature and amount unchanged), and a *consequence* (so pressure doubles and P × V stays constant). The vertical-surface argument becomes the sentence.

**CRSE connection:** the syringe is cheap, tactile, and culturally neutral — every student can push a plunger and *feel* the gas push back, regardless of prior science background or home language. Grounding an abstract proportional rule in a sensation students generate with their own hands honors the principle that scientific knowledge should be built, not received. The diver and chip-bag extensions connect the law to lived experiences (swimming, snacks, travel) that students already carry into the room.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — sealed syringe acting like a spring; return in Phase 4 to explain why the plunger fought back |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — what happens to pressure as volume drops?); Phase 3 (TT#2 — halve the volume, what doubles, what stays constant?) |
| 3 | Students develop questions/models/procedures | Phase 2 BTC task on vertical surfaces (collect (V, P) data from syringe + PhET, discover the rule before any equation); Phase 4 apply P₁V₁ = P₂V₂ to a new case |
| 4 | CCC defined and used | Lesson Overview · *Scale, Proportion, and Quantity*; explicit in Phase 3 (inverse proportion, halve V → double P) and Phase 4 (B/B/S) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: Boyle's Law / inverse proportion / gas pressure |
| 6 | Revisit phenomenon with evidence | Phase 4 — students return to the syringe armed with their data, the curve, and the particle model to explain the rising resistance |
| 7 | ENL/SPED supports | Access & Differentiation block: sentence frames, word-choice box, gestures, pre-filled data table, P₁V₁ = P₂V₂ template, BTC group roles, calculator |
| 8 | Assessment check | Phase 5 — Exit Ticket (solve for P; solve for V; particle-model sentence), values distinct from worksheet |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked Boyle's-Law example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **Boyle's Law** — for a fixed amount of gas at constant temperature, pressure and volume are inversely proportional, so their product is constant; written P₁V₁ = P₂V₂. Halving the volume doubles the pressure.
- **inverse proportion (inverse relationship)** — a relationship in which one quantity is multiplied by a factor exactly as the other is divided by that same factor, so their product stays constant; pressure and volume relate this way at constant temperature (P up, V down).
- **gas pressure** — the force per unit area that gas particles exert by colliding with the walls of their container; packing the same particles into a smaller volume means more collisions per second per area, so the pressure rises.
