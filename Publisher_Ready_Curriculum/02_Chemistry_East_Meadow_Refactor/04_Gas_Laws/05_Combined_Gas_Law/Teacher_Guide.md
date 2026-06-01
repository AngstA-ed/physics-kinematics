# Combined Gas Law — Teacher Guide

## Cover

**Unit: Gas Laws — Lesson 05: Combined Gas Law**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: HOCHMAN

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

**HS-PS1-9** — *"Analyze data to support the claim that the combined gas law describes the relationships among volume, pressure, and temperature for a sample of an ideal gas."* The combined gas law, P₁V₁/T₁ = P₂V₂/T₂, fuses Boyle's law (P–V), Charles's law (V–T), and Gay-Lussac's law (P–T) into one expression that handles a change in all three variables at once. For the 2025 NYSSLS-aligned Regents, students are expected to rearrange and solve the combined gas law for any one unknown, to convert all temperatures to Kelvin before substituting, and to use standard temperature and pressure (STP: 273 K and 101.3 kPa, from the 2025 NYS Chemistry Reference Tables) as a fixed reference state. Per East Meadow guidance, this lesson is the analytical capstone of the gas-law sequence: students stop memorizing three separate equations and start reasoning from one.

The Cross-Cutting Concept of **Scale, Proportion, and Quantity** is the explicit lens. Volume responds *proportionally* to absolute temperature and *inversely* to pressure. When two factors push in opposite directions — pressure rising while temperature also rises — students must track the proportional effect of each to predict whether the gas expands or contracts. The combined gas law is the bookkeeping system that keeps those competing proportions straight.

### Phenomenon

A scuba diver fills a 12-liter tank with compressed air and descends to 30 meters, where the surrounding water pushes on the gas with about four times the pressure at the surface (≈ 4 atm). The diver breathes calmly for twenty minutes. Back at the surface, the dive computer reports that the diver "used" far more than 12 liters of air — closer to 50 liters of surface-volume air drained from the tank. How can a 12-liter tank deliver 50 liters of breathing gas? The answer is not that the tank stretched. The same amount of gas occupies a *smaller volume* when squeezed by depth-pressure and a *slightly larger volume* as it warms toward body temperature on the way up. Every breath a diver takes at depth is denser, packing more gas into each lungful — which is exactly why dive planning is a combined-gas-law calculation, and why getting it wrong can leave a diver out of air before the surface.

**Driving question:** When pressure, volume, and temperature all change at once, how do we predict what happens to a sample of gas?

### Javalab / Labs

- **Combined gas law data analysis:** Provide students with a data table of a fixed gas sample at several (P, V, T) states — e.g., a weather balloon released at STP and tracked as it rises into colder, lower-pressure air. Students compute P·V/T for each row and discover that the quotient stays (nearly) constant, which is the empirical basis of HS-PS1-9. Connect to the inverse P–V curve in `figures/pressure_volume_inverse.png`.
- **Weather-balloon problem:** A latex sounding balloon is filled to 4.0 L at ground-level STP (101.3 kPa, 273 K) and rises to an altitude where pressure is 25.0 kPa and temperature is 220 K. Students predict, then calculate, the balloon's volume aloft (≈ 13 L) and reconcile the two competing effects: lower pressure inflates it, colder temperature shrinks it, and the pressure effect wins.
- **Scuba "air at depth" calculation:** Using the depth–pressure relationship illustrated in `figures/scuba_volume_vs_depth.png`, students compute the surface volume of gas a diver actually consumes from a tank at depth — the lesson's anchoring calculation.

### Assessments

- **Combined gas law problem set** (district checkpoint, following lesson; see `Assessments/` folder once created): a mixed set in which students solve for V₂, P₂, or T₂, convert Celsius to Kelvin, and identify STP as a reference state.
- **Lab data analysis** (formative): students analyze a (P, V, T) data table, compute P·V/T per row, and write a claim about whether the data support the combined gas law.
- **Exit Ticket** (Phase 5): three items — solve for V₂ with all three variables changing; an STP-reference problem; and a one-sentence explanation of why temperature must be in Kelvin. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | HS-PS1-9 (analyze data supporting the combined gas law relating P, V, and T for an ideal gas) |
| **CCC focus** | Scale, Proportion, and Quantity — volume scales directly with absolute temperature and inversely with pressure; when both change, the proportional effects combine in P₁V₁/T₁ = P₂V₂/T₂ |
| **Strategy chips** | HOCHMAN — appositive sentence to define the combined gas law crisply; Because/But/So sentence in Phase 4 to reconcile competing P and T effects |
| **Materials** | 2025 NYS Chemistry Reference Tables (Table A — Standard Temperature and Pressure), calculators, `figures/scuba_volume_vs_depth.png` and `figures/pressure_volume_inverse.png` projected, the combined-gas-law data table (projected or half-sheet) |
| **Safety** | No hazardous materials in this lesson; it is a data-analysis and calculation lesson. Standard classroom expectations apply. |
| **Prior knowledge** | Boyle's law (P₁V₁ = P₂V₂), Charles's law (V₁/T₁ = V₂/T₂), and Gay-Lussac's law (P₁/T₁ = P₂/T₂) from earlier lessons in this unit; students must already convert °C to K (K = °C + 273) and read STP from Reference Table A. |

**Lesson objectives — students can:**

- State the combined gas law, P₁V₁/T₁ = P₂V₂/T₂, and explain that it merges Boyle's, Charles's, and Gay-Lussac's laws into one expression.
- Convert all temperatures to Kelvin and substitute STP (273 K, 101.3 kPa) as a reference state when a problem specifies "at STP."
- Rearrange the combined gas law to solve for any one unknown (V₂, P₂, or T₂) and carry correct units.
- Analyze a (P, V, T) data table by computing P·V/T per row and use Scale, Proportion, and Quantity to argue whether the data support the combined gas law.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers: *"Tell us about a time two things were happening at once and you had to predict the result — traffic getting heavier while you also drove faster, a room getting crowded while it also got hotter. What did you expect to happen?"* One round, one sentence each, no judgment. This primes the central cognitive move of the lesson: holding two competing changes in mind at the same time.

Then post the **Do Now**:

> *"A scuba diver fills a 12-liter tank with air and goes deep, where the water squeezes the gas to about 4 times surface pressure. After the dive, the gauge shows the diver used about 50 liters of surface air. The tank never changed size. Write one sentence: how can a 12-liter tank give a diver 50 liters of air?"*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "The air got compressed, so more of it fit in the tank." — affirm; and ask: so when that compressed air comes back to the surface and spreads out, what happens to its volume?
- "The deeper you go, the more air you breathe per breath." — close; probe: why would each breath at depth contain more gas than a breath at the surface?
- "I don't get it — air is air." — validate the confusion: the *amount* of gas didn't change, but the *volume* it occupies depends on pressure and temperature. That is exactly what today is about.

### 3–8 min · Phenomenon hook — same air, different volume

**Teacher actions.** Project `figures/scuba_volume_vs_depth.png`. Walk down the depth axis: at the surface a single breath is about 6 L; at 10 m (2 atm) the same amount of gas is squeezed to 3 L; at 30 m (4 atm) it is only 1.5 L.

![Bar chart titled 'Same amount of air — smaller volume at depth' showing the volume of one breath of gas at four depths: 6.0 L at 0 m (1 atm), 3.0 L at 10 m (2 atm), 2.0 L at 20 m (3 atm), and 1.5 L at 30 m (4 atm); bars decrease from left to right; the y-axis is labeled 'Volume of one breath (L)' and the x-axis labels each depth with its pressure in atmospheres.](figures/scuba_volume_vs_depth.png)

**Sample teacher language:**

> "Look at these bars. The amount of gas — the number of molecules in one breath — is the same in every bar. What changes is the volume that gas occupies, because the pressure changes with depth. At four atmospheres, a breath is one-fourth the volume it would be at the surface. So a 12-liter tank of compressed air, when you let it expand back to surface pressure, releases far more than 12 liters of breathing gas. And we haven't even talked about temperature yet — the water at depth is cold, and the gas warms as the diver ascends. Pressure and temperature are *both* changing. We need one equation that handles all of it."

**Anticipated student responses:**

- "So if pressure goes up, volume goes down?" — yes — that is the inverse relationship from Boyle's law; today we combine it with temperature.
- "Does the cold water make the gas shrink too?" — exactly; colder gas occupies less volume (Charles's law). The two effects can push in opposite directions.
- "Is there one formula for all of this?" — there is, and you already know its three pieces. We are going to fuse them in Phase 2.

**Driving question** (post on the board and leave it there):

> *When pressure, volume, and temperature all change at once, how do we predict what happens to a sample of gas?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the scuba bar chart. Then:

> "Turn to your partner: a weather balloon is released at the ground and rises high into the sky, where the air pressure is much lower but the temperature is much colder. Lower pressure makes a gas expand; colder temperature makes it shrink. So does the balloon get bigger or smaller as it rises? You can't be sure yet — why not?"

Target insight (leave open if no one lands it yet): you cannot predict the result by intuition alone, because two effects oppose each other. You need to *quantify* each effect and combine them — which is exactly what the combined gas law does.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–16 min · ABCs Activity — build the combined law from data, before the formal name

**Before any formal vocabulary is introduced**, students discover the combined gas law empirically from a data table. Hand out (or project) the table below: one fixed sample of gas tracked through four states.

| State | Pressure P (kPa) | Volume V (L) | Temperature T (K) | P·V/T (kPa·L/K) |
|---|---|---|---|---|
| 1 (start) | 100 | 6.0 | 300 | |
| 2 | 200 | 3.0 | 300 | |
| 3 | 200 | 4.0 | 400 | |
| 4 | 50 | 12.0 | 250 | |

**The task:**

> "For each row, compute P × V ÷ T. Do not round harshly — keep one decimal. Write the result in the last column. Then look at your four answers. What do you notice?"

**Teacher facilitation language (circulate):**

> "State 1: 100 times 6.0 is 600, divided by 300 is 2.0. Now do State 2 the same way. What did you get? Keep going."

> "You changed the pressure, the volume, and the temperature across these rows — and yet that last column keeps doing something. What is it doing?"

**Anticipated student responses during ABCs:**

- "They're all 2.0!" — exactly the intended discovery. Probe: even though P, V, and T are different in every row, the quantity P·V/T stayed the same. What does that tell you about how these three variables are connected?
- "Row 3 gave me 2.0 also, but the numbers are bigger." — right: pressure and temperature both rose, and the combination kept P·V/T constant.
- "Is this a coincidence?" — no — it is a law. For a fixed amount of gas, P·V/T is a constant. That is the empirical heart of HS-PS1-9.

### 16–22 min · Initial Model — write the relationship as an equation

**Prompt on the board:**

> *"You just found that P·V/T is the same for every state of this gas sample. Before I name it: if P·V/T stays constant, write an equation that connects state 1 to state 2 using P₁, V₁, T₁ and P₂, V₂, T₂."*

Students work individually for 3 minutes, then compare with a partner.

Target answer:

> P₁V₁/T₁ = P₂V₂/T₂

**Teacher facilitation language:**

> "If the first state gives P·V/T = 2.0 and the second state also gives P·V/T = 2.0, then the two expressions equal each other. Set state 1's P·V/T equal to state 2's. What does that look like?"

> "This single equation is doing the work of three separate laws you already learned. If temperature never changes, the T's cancel and you're left with Boyle's law. If pressure never changes, you get Charles's law. If volume never changes, you get Gay-Lussac's law. One equation, three special cases."

**Anticipated student responses:**

- "Do I have to cross-multiply to solve it?" — yes — once you substitute the numbers, you cross-multiply and isolate the unknown. We'll practice that next.
- "What if only two things change?" — the equation still works; the variable that stays the same just appears identically on both sides. You can cancel it or leave it.
- "This is just the three laws stuck together." — exactly right. That is why it's called the *combined* gas law.

### 22–30 min · Investigation — solve the phenomenon problems

Groups of three or four work through the two anchor problems. Each student sets up the equation and substitutes individually, then the group reconciles.

**Investigation Problem 1 — Weather balloon (solve for V₂):**

A weather balloon holds 4.0 L of gas at ground-level STP (P₁ = 101.3 kPa, T₁ = 273 K). It rises to an altitude where P₂ = 25.0 kPa and T₂ = 220 K. Find the balloon's volume aloft.

> Set up: P₁V₁/T₁ = P₂V₂/T₂ → V₂ = (P₁V₁T₂)/(T₁P₂)
> V₂ = (101.3 × 4.0 × 220) / (273 × 25.0) = 89,144 / 6,825 ≈ **13.1 L**

The balloon **expands** to about 13 L: the large pressure drop more than offsets the cooling.

**Investigation Problem 2 — Scuba ascent (solve for V₂):**

A diver's regulator releases 12.0 L of air at depth, where P₁ = 4.0 atm and T₁ = 283 K (cold water, 10 °C). The air rises to the surface, where P₂ = 1.0 atm and T₂ = 293 K (20 °C). What volume does that air occupy at the surface?

> V₂ = (P₁V₁T₂)/(T₁P₂) = (4.0 × 12.0 × 293) / (283 × 1.0) = 14,064 / 283 ≈ **49.7 L**

The 12 L at depth becomes nearly **50 L** at the surface — the phenomenon resolved.

**Teacher facilitation prompts (circulate):**

> "First question every time: are the temperatures in Kelvin? In Problem 1 they're already in Kelvin. In Problem 2, 10 °C and 20 °C were converted to 283 K and 293 K. If you substitute Celsius, the answer is wrong — and you can divide by a temperature near zero, which blows the math up."

> "In the balloon problem, two things fight each other. Lower pressure (101.3 → 25.0) wants to expand the gas; lower temperature (273 → 220) wants to shrink it. Which wins? Let the equation decide — don't guess."

> "Notice the units: as long as P₁ and P₂ use the *same* pressure unit and V is consistent, the units cancel. You do not have to convert kPa to atm — you just can't mix them within one problem."

**Anticipated student responses:**

- "I got 13 for the balloon — does it really get bigger going up?" — yes; the pressure drop is enormous (to one-quarter of STP), so the balloon expands even though it's colder. That's why sounding balloons are filled loosely at the ground — they swell at altitude.
- "I forgot to convert Celsius and got a weird number." — redirect: K = °C + 273. Always convert *first*, before substituting.
- "Why is the scuba answer so much bigger than 12?" — because surface pressure is one-fourth of depth pressure, so the same gas expands roughly fourfold; the small warming nudges it a bit higher.

### 28–30 min · Reconnect + surface the method

Bring groups back together. Ask one group to put the balloon setup on the board. Ask the class:

> "Look at the rearranged equation: V₂ = P₁V₁T₂ ÷ (T₁P₂). Where did temperature go in the numerator versus the denominator? Why does the *new* temperature (T₂) end up on top and the *old* temperature (T₁) on the bottom?"

Surface the key idea: volume is *directly* proportional to absolute temperature (so the new temperature multiplies) and *inversely* proportional to pressure (so the new pressure divides). The structure of the rearranged equation is just Scale, Proportion, and Quantity made visible.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look at your data table from the start of Phase 2 — every row gave P·V/T = 2.0. Turn to your partner: in your own words, what does it *mean* that P·V/T stays constant for a fixed sample of gas? What is the equation really claiming about pressure, volume, and temperature?"

Target consensus: for a fixed amount of an ideal gas, the three variables are locked together so that the ratio P·V/T never changes. If you change any two, the third must adjust to keep the ratio constant. That single constraint is the combined gas law.

> "And here is the rule that makes it work every time: temperature has to be in Kelvin. Why can't we use Celsius?"

Target: the law says volume is *proportional* to temperature, which only holds on an absolute scale that starts at true zero (0 K). On the Celsius scale, 0 °C is not zero gas energy, and you can even get negative temperatures — which would give negative or undefined volumes. Kelvin fixes this.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name what we built. The equation P₁V₁/T₁ = P₂V₂/T₂ is the **combined gas law** — the single relationship that merges Boyle's, Charles's, and Gay-Lussac's laws so we can change pressure, volume, and temperature all at once."

> "Here is the Hochman appositive move that will help you write and remember it. An appositive is a phrase set off by dashes that renames or explains the noun next to it. Say this with me:
>
> *The combined gas law — the equation P₁V₁/T₁ = P₂V₂/T₂ — relates the pressure, volume, and temperature of a fixed gas sample at two different states.*
>
> The phrase between the dashes is the appositive: it states the equation in the same sentence that names the law. You'll use this structure on the Exit Ticket and in your notes."

> "The second term: **absolute temperature**, the temperature measured in Kelvin from absolute zero. The combined gas law only works with absolute temperature, because volume and temperature are proportional only when zero really means zero energy. Always convert: K = °C + 273."

> "The third term: **STP — standard temperature and pressure**, a fixed reference state of 273 K and 101.3 kPa defined on Reference Table A. When a problem says a gas is 'at STP,' it is handing you P and T for one of your two states for free."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "If a problem tells you a gas starts 'at STP,' which two numbers do you immediately write down?" — *Expected response:* P₁ = 101.3 kPa and T₁ = 273 K, from Reference Table A.
- "Why does the combined gas law reduce to Boyle's law when temperature is held constant?" — *Expected response:* if T₁ = T₂, the temperatures cancel from both sides, leaving P₁V₁ = P₂V₂, which is Boyle's law. The combined law contains all three simpler laws as special cases.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the model + Appositive + Because/But/So expansion

Students return to their Initial Model (the equation P₁V₁/T₁ = P₂V₂/T₂ they wrote in Phase 2). They annotate it: label which variable is directly proportional to volume (T) and which is inversely proportional (P), and write an appositive sentence defining the law.

**Appositive sentence (model on board):**

> *"The combined gas law — the equation P₁V₁/T₁ = P₂V₂/T₂ — relates the pressure, volume, and temperature of a fixed gas sample."*

Ask students to write a parallel appositive for STP:

> *"Standard temperature and pressure — ___ K and ___ kPa — is the reference state used when a problem says a gas is 'at STP.'"*

Then run a **Because / But / So** sentence about the phenomenon. Starter on the board:

> *"As a scuba diver ascends from 30 m to the surface, the gas in a released bubble expands even though the water also gets warmer."*

Model one aloud:

> "As a diver ascends, the released gas expands **because** the surrounding pressure drops to one-fourth of its value at depth, and volume is inversely proportional to pressure — **but** the warming water raises the temperature only slightly (from 283 K to 293 K), which adds just a small additional expansion — **so** the pressure effect dominates and the gas volume increases nearly fourfold, which is why divers must never hold their breath while ascending."

Then have students write their own B/B/S using one of these starters:

- *"A weather balloon rises into colder, lower-pressure air and gets bigger anyway…"* (hint: which effect wins, pressure or temperature?)
- *"A student solves a combined gas law problem using Celsius instead of Kelvin and gets a wildly wrong answer…"* (hint: what does the proportionality require?)

**Anticipated student responses:**

- "Because the pressure dropped a lot but the temperature barely changed." — good start; push for the So: "so the balloon's volume increases, because the inverse pressure effect outweighs the small temperature change."
- "Because Celsius can be negative, but Kelvin can't, so the volume came out negative." — excellent; refine the So: "so the temperature must be in Kelvin for the proportion to make physical sense."

### 39–40 min · Return to the phenomenon

> "Return to our diver. We started with a question: how does a 12-liter tank deliver 50 liters of air? Now you have the method. The air leaves the tank at depth — 4 atm, cold water — and expands as it reaches the surface — 1 atm, warmer. Quickly: which variable did the most work in that fourfold expansion, pressure or temperature?"

Target: pressure. The pressure dropped to one-fourth (4 atm → 1 atm), expanding the gas roughly fourfold; the temperature change (283 K → 293 K) added only about 3.5%. The combined gas law let us separate and combine the two effects.

> "That number on the dive computer isn't magic — it's P₁V₁/T₁ = P₂V₂/T₂. The combined gas law is how every diver, every weather forecaster, and every chemist predicts what a gas will do when conditions change."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud:

> *(a) A gas occupies 3.0 L at 100 kPa and 300 K. The pressure rises to 150 kPa and the temperature rises to 400 K. Calculate the new volume V₂. Show your setup.*
> *(b) A gas occupies 5.0 L at STP. It is moved to a new state where the pressure is 50.65 kPa and the temperature is 546 K. Calculate the new volume V₂. (Hint: write down P₁ and T₁ from the definition of STP.)*
> *(c) In one sentence, explain why the temperature must be converted to Kelvin before using the combined gas law.*

Expected answers are in `Answer_Key.docx`. These values are deliberately different from the worksheet practice problems.

**Closing Reflection (SEL, 30 seconds):**

> "Today we took three separate gas laws and combined them into one. In one sentence: what is one thing that clicked for you today about how pressure, volume, and temperature work together — and who helped you see it?"

Collect worksheets; note which students converted temperatures to Kelvin before substituting versus those who substituted Celsius or forgot the STP reference values. The Kelvin conversion and the STP-lookup are the two main procedural stumbling blocks — target those students for a brief one-on-one check at the start of the next lesson.

---

## Common Misconceptions

- **Misconception:** "I can plug temperatures in as Celsius — they're temperatures either way." → **Correction:** The combined gas law requires *absolute* temperature (Kelvin). Volume is proportional to temperature only on a scale that starts at absolute zero. Substituting Celsius gives wrong answers and can produce negative or undefined volumes (e.g., dividing by a temperature near 0 °C). Always convert first: K = °C + 273.
- **Misconception:** "The combined gas law is a brand-new fourth equation I have to memorize separately." → **Correction:** It is the *fusion* of the three laws students already know. Hold temperature constant and it becomes Boyle's law (P₁V₁ = P₂V₂); hold pressure constant and it becomes Charles's law (V₁/T₁ = V₂/T₂); hold volume constant and it becomes Gay-Lussac's law (P₁/T₁ = P₂/T₂). Learning the combined law *replaces* memorizing three.
- **Misconception:** "If pressure and temperature both increase, the volume must increase." → **Correction:** The two effects oppose each other. Higher pressure *shrinks* volume (inverse), while higher temperature *expands* it (direct). Only the equation can tell you which wins — you cannot predict the direction by intuition. This is exactly why HS-PS1-9 asks students to *analyze data* rather than guess.
- **Misconception:** "STP is just a vague phrase for 'normal conditions.'" → **Correction:** STP is a precise, defined reference state on Reference Table A: 273 K and 101.3 kPa. When a problem says "at STP," it is supplying exact values for one of your two states. Students who treat STP as approximate will fail to write down the correct P and T.
- **Misconception:** "I have to convert kPa to atm (or vice versa) before I can solve." → **Correction:** Pressure units cancel as long as P₁ and P₂ use the *same* unit. The ratio P₁/P₂ is unitless. You must not *mix* units within one problem, but you never need to convert to a single "official" unit. The same is true for volume units.

---

## Access & Differentiation

- **ELL/ENL supports:** A pre-printed solution scaffold with the steps labeled in order: (1) convert all T to Kelvin, (2) write down knowns and the unknown, (3) write the rearranged equation, (4) substitute, (5) solve, (6) label the unit. Sentence frame: *"As the pressure ___, the volume ___, because volume is ___ proportional to pressure."* Word-choice box displayed throughout: {combined gas law, absolute temperature, Kelvin, STP, directly proportional, inversely proportional}. Pair each problem with the relevant figure so students can sanity-check the *direction* of change (does the gas get bigger or smaller?) against the bar chart.
- **IEP/SPED supports:** Provide the rearranged forms of the equation pre-derived on a reference card (V₂ = P₁V₁T₂ ÷ T₁P₂; P₂ = P₁V₁T₂ ÷ T₁V₂; T₂ = P₂V₂T₁ ÷ P₁V₁) so the algebra is removed as a barrier and the conceptual work — identifying knowns, converting to Kelvin, substituting — remains the skill target. Pre-fill the Kelvin conversions for any Celsius values in the practice set. Offer one step at a time: the student completes the Kelvin conversion before seeing the substitution row. Calculator use expected for all arithmetic.
- **Extensions:** (1) Derive the combined gas law from the three individual laws algebraically — show how Boyle's, Charles's, and Gay-Lussac's laws multiply together to give P·V/T = constant. (2) A diver at 30 m (4 atm, 283 K) takes a full breath of 6.0 L and ascends to the surface (1 atm, 293 K) *holding their breath* — calculate the lung volume at the surface and explain why dive training forbids this. (3) Look up the *ideal gas law* (PV = nRT) and explain how the combined gas law is the special case where the amount of gas (n) stays constant.

---

## Strategy Spotlight

**HOCHMAN — Appositive sentence.** The Hochman Writing Method (Judith Hochman and the Writing Revolution) treats sentence-level writing as a thinking tool. For this lesson the featured technique is the **appositive**, a noun phrase set off by dashes (or commas) that renames or defines the noun it follows. The appositive is ideal for an equation-heavy lesson because it forces the student to embed the equation *and* its meaning into a single subject-verb sentence rather than reciting a formula in isolation.

**The target appositive for this lesson:**

> *The combined gas law — the equation P₁V₁/T₁ = P₂V₂/T₂ — relates the pressure, volume, and temperature of a fixed gas sample.*

This sentence does three things simultaneously: (1) names the law, (2) states the equation in the appositive phrase between the dashes, and (3) describes what the law *does* in the main clause. Students who can write and say this sentence — not just copy the formula — are integrating the law into their active understanding rather than treating it as an isolated string of symbols.

**How to run it in this lesson (Phase 3 → Phase 4):**

1. Post and read aloud the model appositive sentence together (Phase 3 vocabulary).
2. Ask students to write a parallel appositive for STP: *"Standard temperature and pressure — 273 K and 101.3 kPa — is the reference state used when..."* This requires them to recall the two defining values, reinforcing the Reference Table A lookup.
3. In Phase 4, students write their own appositive in their notes and a Because/But/So sentence reconciling the competing pressure and temperature effects from the phenomenon. Cold-call two or three students; ask: does the appositive phrase correctly state the equation? Does the B/B/S correctly identify which effect dominates?

**Why the appositive fits the combined gas law:** The phrase "combined gas law" sounds abstract until the appositive forces the writer to *put the equation inside the sentence* and then say what it relates. That move connects the symbolic form (P₁V₁/T₁ = P₂V₂/T₂) to the conceptual claim (these three variables are locked together for a fixed gas sample), which is precisely the relationship HS-PS1-9 asks students to articulate.

**CRSE connection:** The opening circle prompt (two things changing at once — traffic, a crowding room) invites students to bring everyday experiences of competing effects into the lesson. The scuba and weather-balloon contexts connect to careers and activities students may pursue or have family members involved in (diving, aviation, meteorology, the trades that fill and transport compressed-gas cylinders). Grounding an abstract three-variable equation in lived, high-stakes situations honors students' out-of-school knowledge and shows that the algebra protects real people in real situations.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — scuba "12 L tank delivers 50 L" puzzle with `scuba_volume_vs_depth.png`; return in Phase 4 with the diver-ascent resolution |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — does the rising balloon get bigger or smaller, and why can't you tell?); Phase 3 (TT#2 — what does it mean that P·V/T stays constant?) |
| 3 | Students develop questions/models/procedures | Phase 2 ABCs data table (compute P·V/T per row, discover the constant); Initial Model (write P₁V₁/T₁ = P₂V₂/T₂ from the data); group Investigation (balloon and scuba problems) |
| 4 | CCC defined and used | Lesson Overview · *Scale, Proportion, and Quantity*; explicit in Phase 2 reconnect (why T₂ is on top, P₂ on bottom) and Phase 4 B/B/S (which proportional effect dominates) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: combined gas law / absolute temperature / STP |
| 6 | Revisit phenomenon with evidence | Phase 4 — students return to the diver and use their calculated 49.7 L result and the bar chart to explain the fourfold expansion |
| 7 | ENL/SPED supports | Access & Differentiation block: solution scaffold, sentence frames, word-choice box, pre-derived rearranged equations, pre-filled Kelvin conversions, calculator |
| 8 | Assessment check | Phase 5 — Exit Ticket (solve for V₂ with all three variables changing; an STP-reference problem; one-sentence Kelvin explanation) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked combined-gas-law example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **combined gas law** — the equation P₁V₁/T₁ = P₂V₂/T₂, which merges Boyle's, Charles's, and Gay-Lussac's laws to relate the pressure, volume, and absolute temperature of a fixed sample of gas at two different states; for a fixed gas sample the quantity P·V/T is constant
- **absolute temperature** — temperature measured in Kelvin from absolute zero (K = °C + 273); the combined gas law requires absolute temperature because volume is directly proportional to temperature only on a scale whose zero is true zero
- **STP (standard temperature and pressure)** — the defined reference state of 273 K and 101.3 kPa (Reference Table A); when a gas-law problem specifies "at STP," it supplies the pressure and temperature for one of the two states
