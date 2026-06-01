# Using Solubility Tables — Teacher Guide

## Cover

**Unit: Solutions — Lesson 03: Using Solubility Tables**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: BTC

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

This lesson builds the data-reading practice that the NYSSLS-aligned 2025 Regents expects of every chemistry student: interpreting **Reference Table G — Solubility Curves of Selected Substances**. There is no single content performance expectation tied to reading a reference table; instead the lesson develops SEP-4 (Analyzing and Interpreting Data) and SEP-2 (Developing and Using Models) using the table as the data source. Students read a curve to find the maximum mass of solute that dissolves in 100 g of water at a given temperature, compare solids against gases, and predict how solubility changes when temperature changes.

The Cross-Cutting Concept of **Patterns** is the explicit lens. Reference Table G is a picture of two patterns at once: for almost every **solid** (NaNO₃, KNO₃, KCl, NaCl…), solubility *rises* as temperature rises; for every **gas** (NH₃, HCl, SO₂), solubility *falls* as temperature rises. Students who internalize that the slope direction tells you "solid or gas" can predict solubility behavior they have never been taught directly — that is the heart of using a reference table rather than memorizing values.

### Phenomenon

Two identical cans of soda are opened at the same instant. One has been sitting in a warm car (about 35 °C); the other came straight from the refrigerator (about 4 °C). The warm one fizzes violently, foams over, and within minutes tastes flat. The cold one stays quietly carbonated and keeps its fizz far longer. Same soda, same pressure when sealed, same act of opening — but the warm can loses its dissolved carbon dioxide gas dramatically faster.

The contrast is everyday and visceral: every student has tasted a warm flat soda. The science underneath it is exactly a Reference Table G reading — carbon dioxide is a **gas**, and gas solubility goes *down* as temperature goes *up*. Warm water (warm soda) simply cannot hold as much dissolved CO₂, so the gas escapes faster. The same table that explains the soda also tells you the opposite story for a dissolved solid like sugar, which gets *more* soluble when you heat the water.

**Driving question:** Why does a warm soda go flat faster than a cold one?

### Javalab / Labs

- **Solubility — Javalab simulation** (`javalab.org`, "Solubility" / "Saturated solution" module): students add solute to water and adjust temperature, watching the dissolved amount and any undissolved excess respond in real time. Use it to let groups *test* a prediction they first made from Reference Table G — e.g., "If KNO₃ holds 32 g at 20 °C, what happens when we heat to 60 °C?" — then confirm the curve's prediction against the simulation. No login required; a projector version works if devices are limited.
- **Reference Table interpretation practice:** groups read `figures/reference_table_g_solid_vs_gas.png` (and the full classroom Reference Table G if available) to extract solubility values at named temperatures, decide saturated vs. unsaturated for a given mass, and classify each curve as solid or gas by its slope direction. This is the core skill the lesson assesses.

### Assessments

- **Reference Table G interpretation quiz** (district checkpoint, following lesson): students read solubility values at given temperatures, decide whether a stated solution is saturated, unsaturated, or supersaturated, and classify curves as solids or gases by slope. See the `Assessments/` folder once created.
- **Exit Ticket** (Phase 5): three items — read the solubility of a solid at a stated temperature; predict whether warming or cooling makes a *gas* more soluble; and write one sentence connecting the slope of a curve to the soda phenomenon. The Exit Ticket values are deliberately different from the worksheet practice values. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | SEP-4 (Analyzing & Interpreting Data) + SEP-2 (Developing & Using Models) using Reference Table G; no single content PE |
| **CCC focus** | Patterns — a rising curve means a solid whose solubility increases with temperature; a falling curve means a gas whose solubility decreases with temperature. The slope direction *is* the pattern that lets you predict. |
| **Strategy chips** | BTC — random groups at vertical non-permanent surfaces read Table G and build the solid-vs-gas pattern themselves before any vocabulary is named |
| **Materials** | 2025 NYS Chemistry Reference Tables (Table G for every student), `figures/reference_table_g_solid_vs_gas.png` projected, vertical whiteboard/window space + dry-erase markers for random groups, the Javalab "Solubility" simulation on student devices or projector, two cans of soda (one warm, one chilled) for the live hook if available |
| **Safety** | Standard lab conduct. If opening soda for the live demo, open the warm can over a tray or sink — it will foam. No chemicals are handled by students; the Javalab simulation is virtual. |
| **Prior knowledge** | Lesson 01 (Classifying Solutions) — solute, solvent, solution; saturated vs. unsaturated. Lesson 02 (Precipitation) — what it means for a solid to come out of solution. Students should recognize "g per 100 g water" as a concentration before this lesson. |

**Lesson objectives — students can:**

- Read Reference Table G to find the maximum mass of a named solute that dissolves in 100 g of water at a given temperature.
- Decide whether a stated solution is saturated, unsaturated, or supersaturated by comparing the stated mass to the curve value.
- Classify a curve on Reference Table G as a solid or a gas by the direction of its slope, and predict how its solubility changes when temperature changes.
- Explain, using the Patterns CCC, why a warm soda loses its dissolved gas faster than a cold one.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers: *"What is a drink or food that is way better cold than warm — or warm than cold? What changes about it?"* One round, one sentence each, no judgment. This surfaces everyday intuition that temperature changes a substance's physical behavior, which is exactly what Reference Table G captures.

Then post the **Do Now**:

> *"You open two cans of the same soda at the same time. One has been baking in a warm car; the other is straight from the fridge. In one sentence: which one fizzes over and goes flat faster, and why do you think temperature would matter?"*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "The warm one goes flat faster because warm things fizz more." — affirm the prediction; probe: *what is actually leaving the soda when it "goes flat"?* (Dissolved gas.)
- "The cold one stays fizzy because cold keeps the bubbles in." — close; rephrase toward the science: cold water *holds* more dissolved gas. Why might that be?
- "I'm not sure temperature matters — maybe it's the shaking." — validate the alternative; note that we'll isolate temperature with a reference table and a simulation today, no shaking involved.

### 3–8 min · Phenomenon hook — two sodas, same start, different fizz

**Teacher actions.** If you have the cans, open them side by side over a sink/tray. The warm one foams and quiets quickly; the cold one stays carbonated. If you don't have cans, describe it vividly and project the figure. Either way, name the key fact: the fizz is dissolved **carbon dioxide gas** leaving the liquid.

Project `figures/reference_table_g_solid_vs_gas.png`:

![Line graph titled 'Reference Table G: solid vs. gas solubility' with temperature in degrees Celsius on the x-axis (0 to 100) and solubility in grams of solute per 100 grams of water on the y-axis (0 to about 250). A purple curve labeled KNO₃ (solid) rises steeply from about 14 g at 0 °C to about 246 g at 100 °C. A blue curve labeled NH₃ (gas) falls from about 90 g at 0 °C to about 7 g at 100 °C. The two curves cross near 30 °C at about 45 g per 100 g of water.](figures/reference_table_g_solid_vs_gas.png)

**Sample teacher language:**

> "This is part of Reference Table G — a tool you get on every Regents exam. The y-axis is how many grams of a substance will dissolve in 100 grams of water; the x-axis is temperature. Look at the two curves. One goes *up* as we heat the water — that's potassium nitrate, a solid. One goes *down* as we heat the water — that's ammonia, a gas. Soda's carbon dioxide is a gas, so which curve does it act like? Watch what happens to a gas curve as temperature rises."

**Anticipated student responses:**

- "The gas curve goes down, so warm water holds less gas." — exactly; that is the whole soda explanation in one sentence. We'll formalize it in Phase 3.
- "Why does the solid go the opposite way?" — great observation; most solids dissolve *more* in hot water (think sugar in hot tea). The table shows both behaviors at once.
- "Where do the curves cross?" — near 30 °C at about 45 g per 100 g water. We'll use crossing points and specific temperatures when we read the table closely.

**Driving question** (post on the board and leave it there):

> *Why does a warm soda go flat faster than a cold one?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the graph. Then:

> "Turn to your partner: one curve climbs and one curve falls as we heat the water. Without reading any numbers yet — what do you think the *direction* of a curve tells you about the substance? Try to name the rule."

Target insight (leave open if no one lands it yet): the *slope direction* sorts the substances — rising curves are solids that dissolve more when hot, falling curves are gases that dissolve less when hot. That pattern is the tool students will build at the boards in Phase 2.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–13 min · BTC launch — random groups to vertical surfaces

**Before any vocabulary is named**, launch the Building Thinking Classrooms structure (see Strategy Spotlight). Use a card randomizer or digital spinner to form **random groups of three**. Each group claims a vertical non-permanent surface (whiteboard panel, window with dry-erase marker, or chart paper at standing height). One marker per group; the marker passes so all three students write.

Distribute Reference Table G (the classroom copy) and direct groups to the projected `figures/reference_table_g_solid_vs_gas.png`.

**Teacher launch language:**

> "These are your groups for the next 17 minutes. One marker, and it has to move between all three of you. I'm not going to tell you the rule for reading this table — you're going to build it. Your first job is on the board in front of you."

### 13–22 min · ABCs thin-slice — read the table, build the pattern (activity before vocabulary)

Post the **thin-slice task** (project or read aloud). Groups work it at the boards:

> **Part A — Read exact values.** Using the curves, write the solubility (g per 100 g water) of KNO₃ at 20 °C, at 40 °C, and at 60 °C. Then write the solubility of NH₃ (the gas) at those same three temperatures.

> **Part B — Find the pattern.** As temperature goes UP, what happens to the KNO₃ numbers? What happens to the NH₃ numbers? Write one sentence for each curve describing the direction.

> **Part C — Sort by slope.** A new substance's curve on Table G goes *down* as temperature rises. Is it more likely a solid or a gas? How do you know? Write your reasoning.

Target readings from the figure (your facilitation key):

| Substance | 20 °C | 40 °C | 60 °C | Direction as temp ↑ |
|---|---|---|---|---|
| KNO₃ (solid) | ≈ 32 g | ≈ 64 g | ≈ 110 g | rises (more dissolves when hot) |
| NH₃ (gas) | ≈ 56 g | ≈ 34 g | ≈ 20 g | falls (less dissolves when hot) |

**Teacher facilitation language (circulate — ask, never tell):**

> "Put your finger on the KNO₃ curve at 40 °C. Read straight across to the y-axis. What number? Now do 60 °C — bigger or smaller?"

> "Compare your two sentences. One curve goes up, one goes down. If I handed you a brand-new curve that goes down, what would you bet — solid or gas? What's your evidence?"

> "Where do the two curves cross? What's special about that temperature — what's true about both substances right there?" (Both ≈ 45 g at ≈ 30 °C.)

**Anticipated student responses during the thin-slice:**

- "KNO₃ keeps getting bigger — solids must like hot water." — affirm the pattern in their own words; this is exactly the slope rule. Push: "So a curve that goes up means…?"
- "We got NH₃ at 60 °C as about 20 — so gases get worse in hot water?" — yes; connect to soda: warm water can't hold as much CO₂, a gas.
- "We can't tell if the new substance is a solid or gas." — redirect to Part C evidence: the *direction* of the curve is the clue. Down-sloping curves on Table G are gases.

### 22–28 min · Investigation — Javalab check + saturated/unsaturated decision

Groups now move from the board to the **Javalab "Solubility" simulation** (or the projector version). The task ties the table reading to a testable prediction:

> "From the table, KNO₃ holds about 32 g at 20 °C. In the simulation, dissolve 32 g of solute in 100 g of water at 20 °C — is it exactly full (saturated)? Now add 10 more grams without changing temperature. What happens to the extra? Now heat the water to 60 °C — does the extra dissolve?"

Then a **saturated-vs-unsaturated decision** at the boards, read straight off the curve:

| Scenario (use KNO₃) | Curve value | Stated amount | Saturated / unsaturated? |
|---|---|---|---|
| 30 g in 100 g water at 20 °C | ≈ 32 g | 30 g | unsaturated (below the curve) |
| 32 g in 100 g water at 20 °C | ≈ 32 g | 32 g | saturated (on the curve) |
| 40 g in 100 g water at 20 °C | ≈ 32 g | 40 g | excess undissolved → 8 g settles out |

**Teacher facilitation language:**

> "The curve is the *maximum* a solvent can hold at that temperature. Below the curve, more can still dissolve — unsaturated. Right on the curve — saturated. Above the curve, the extra can't dissolve and falls out as solid. The simulation lets you watch the excess settle."

**Anticipated student responses:**

- "In the sim the extra 10 g just sat at the bottom." — exactly; that's an over-saturated attempt at fixed temperature. What did heating do to it?
- "When we heated it, the leftover dissolved!" — yes — heating raised the curve value, so the same mass became unsaturated.
- "Does the gas curve work the same way?" — same reading method, opposite direction: heating a gas solution *lowers* the maximum, so dissolved gas leaves. That's the soda.

### 28–30 min · Reconnect + surface the method

Bring groups back. Ask one group to read KNO₃ at 40 °C aloud (≈ 64 g) and explain how they read it (find temperature on x-axis, go up to the curve, read across to y-axis). Ask the class:

> "What single feature of a curve told you whether a substance was a solid or a gas? And what does the height of the curve tell you about a specific solution — saturated or not?"

Surface the two ideas the vocabulary will name: (1) the **slope direction** sorts solids from gases, and (2) the **curve height** is the saturation boundary for that temperature.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look at your board. The KNO₃ curve climbs; the NH₃ curve falls. Turn to your partner: in one sentence each, what does a *rising* curve tell you, and what does a *falling* curve tell you, about the substance and about heating the water?"

Target consensus: a rising curve is a **solid** — heating the water dissolves more of it; a falling curve is a **gas** — heating the water drives it out. The slope direction is the pattern that lets you predict behavior for any curve on the table.

> "Now apply it: soda's fizz is dissolved carbon dioxide, a gas. Which way does a gas curve go as the water warms? So in a warm soda, the water can hold ___ dissolved gas, which is why it ___."

Target: less; goes flat faster.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name what we've been reading. Reference Table G is a set of **solubility curves**. A solubility curve is a line that shows the maximum mass of a solute that dissolves in 100 grams of water at each temperature — the height of the curve is the limit at that temperature."

> "When a solution holds exactly that maximum amount — sitting right on the curve — we call it **saturated**. A saturated solution cannot dissolve any more solute at that temperature; any extra stays undissolved. Below the curve, the solution is unsaturated and could still dissolve more."

> "And the rule you built at the boards has a name. The fact that solids climb and gases fall is the **temperature-solubility relationship**: for most *solids*, solubility increases as temperature increases; for *gases*, solubility decreases as temperature increases. That single relationship is what tells you a warm soda goes flat — carbon dioxide is a gas, so warming the water lowers how much it can hold."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "If a curve is flat — barely changing with temperature — what does that tell you?" — *Expected response:* the substance's solubility is nearly independent of temperature (NaCl on the full Table G is famously almost flat). The slope rule still applies: very little change either way.
- "Why does the soda fizz *over* — not just slowly lose gas — when it's warm?" — *Expected response:* warm water's maximum dissolved-gas value is much lower, so a large amount of CO₂ is suddenly above the limit and escapes quickly. The temperature-solubility relationship for gases predicts exactly that.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the model + Because/But/So expansion

Students return to their Initial Model (their first guess about why warm soda goes flat). They revise it using table evidence: add the word *gas*, add that gas solubility *falls* with temperature, and reference the falling curve they read. Then run a **Because/But/So** sentence. Starter on the board:

> *"A warm soda goes flat faster than a cold one."*

Model one aloud:

> "A warm soda goes flat faster than a cold one **because** carbon dioxide is a gas, and on Reference Table G the gas curves fall as temperature rises — **but** the carbon dioxide doesn't disappear, it simply exceeds the smaller amount warm water can hold — **so** the excess gas escapes quickly out of the warm soda, leaving it flat, while the colder soda's water still holds its dissolved gas."

Then have students write their own B/B/S using one of these starters:

- *"A student dissolves 40 g of KNO₃ in 100 g of water at 20 °C, but only about 32 g dissolves…"* (hint: above the curve → saturated, excess settles out)
- *"Heating the water makes more sugar dissolve but makes dissolved carbon dioxide leave…"* (hint: solid curve rises, gas curve falls)

**Anticipated student responses:**

- "Because the gas curve goes down when it gets hot." — good start; push for the full chain: "so warm water holds less dissolved CO₂, and the extra escapes as fizz."
- "Because 40 g is above the curve, so 8 g can't dissolve." — excellent; that's the saturation reading turned into a sentence. Push the So: "so the solution is saturated and 8 g settles out as solid."

### 39–40 min · Return to the phenomenon

> "Return to the two cans. We can now answer the driving question with the table, not just a guess. Point to where a gas curve is on the graph at fridge temperature versus warm-car temperature. Which temperature lets the water hold more dissolved carbon dioxide? So which can keeps its fizz?"

Target: the cold can — the gas curve is higher (more dissolved gas held) at low temperature, so the cold soda retains more CO₂ and stays carbonated longer.

> "That number on the curve isn't a guess — it's the maximum the water can hold at that temperature. Reading the curve turns 'warm soda tastes flat' into a prediction you can make for any gas, any temperature, before you ever open the can."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud:

> *(a) Using Reference Table G (the projected graph), read the solubility of KNO₃ at 80 °C. Is a solution of 150 g of KNO₃ in 100 g of water at 80 °C saturated, unsaturated, or with excess undissolved? Explain in one sentence.*
> *(b) A bottle of carbonated water is moved from the refrigerator to a warm room. Does the water now hold MORE or LESS dissolved carbon dioxide? Explain using the temperature-solubility relationship for gases.*
> *(c) In one sentence, explain how the slope of a curve on Reference Table G tells you whether a substance is a solid or a gas.*

Expected answers are in `Answer_Key.docx`. (Exit Ticket values — 80 °C, 150 g, carbonated water — are deliberately distinct from the 20/40/60 °C and 30/32/40 g practice in the worksheet.)

**Closing Reflection (SEL, 30 seconds):**

> "Today a graph you'll have on every exam explained something from your everyday life — warm flat soda. In one sentence: what is one thing that clicked for you today, and who in your group helped you read the curve?"

Collect worksheets; note which students confidently read a value straight off a curve versus students who struggled to go x-axis → curve → y-axis. The straight-line reading is the procedural skill to spot-check at the start of the next lesson.

---

## Common Misconceptions

- **Misconception:** "Everything dissolves better in hot water." → **Correction:** Most *solids* do, but *gases* do the opposite — gas solubility *decreases* as temperature increases. Reference Table G shows both behaviors: rising curves (solids) and falling curves (gases). The soda phenomenon depends entirely on the gas case.
- **Misconception:** "The solubility curve tells you how fast something dissolves." → **Correction:** The curve shows the *maximum amount* that can dissolve (the saturation limit) at each temperature, not the speed. Stirring and surface area change speed; the curve only sets the ceiling.
- **Misconception:** "If I add more solute than the curve allows, it just keeps dissolving slowly." → **Correction:** Above the curve at a fixed temperature, the excess cannot dissolve — it stays as undissolved solid (a saturated solution with excess). To dissolve more of a solid, you must raise the temperature to raise the curve.
- **Misconception:** "Warm soda goes flat because the bubbles are bigger." → **Correction:** It goes flat because warm water holds *less* dissolved carbon dioxide. The dissolved gas exceeds the new lower limit and escapes. The bubble size is a symptom; the cause is the falling gas-solubility curve.
- **Misconception:** "A point below the curve means the solution is saturated." → **Correction:** Below the curve is *unsaturated* (it could dissolve more). *On* the curve is saturated. *Above* the curve cannot be reached at that temperature for a solid — the extra precipitates out.

---

## Access & Differentiation

- **ELL/ENL supports:** Sentence frames posted throughout: *"At ___ °C, ___ g of ___ dissolves in 100 g of water."* and *"This solution is ___ because the amount is ___ the curve."* (above / on / below). Word-choice box displayed on the board: {solubility curve, saturated, unsaturated, solid, gas, temperature, dissolve, Reference Table G}. Pair each curve with a gesture: hand rising for solids, hand falling for gases. Allow bilingual labeling of the axes; record the data readings in English.
- **IEP/SPED supports:** Provide a Table G reading guide card that shows the three-step method as arrows: (1) find the temperature on the x-axis, (2) go straight up to the curve, (3) read straight across to the y-axis. Pre-mark the three practice temperatures (20, 40, 60 °C) with light vertical lines on a printed copy so the lookup is structured. Assign clear BTC group roles: one student finds the temperature, one traces to the curve, one reads and records. Offer the saturated/unsaturated decision as a checkbox (above / on / below the curve) rather than open response.
- **Extensions:** (1) Using the *full* classroom Reference Table G, find a substance whose curve is nearly flat (NaCl) and write what that means about heating its solution. (2) Two curves cross near 30 °C at about 45 g. Find another crossing point on the full table and explain what is true about both substances at that temperature. (3) Research: deep-sea soda machines and aquarium aerators both rely on the gas-solubility relationship — explain how cold water and pressure each help keep more gas dissolved, connecting temperature to Henry's law qualitatively.

---

## Strategy Spotlight

**BTC — Building Thinking Classrooms.** The Building Thinking Classrooms framework (Peter Liljedahl, *Building Thinking Classrooms in Mathematics*, 2021) centers three practices that reliably raise student thinking: (1) **random grouping** removes status hierarchies and breaks up friend-group comfort zones; (2) **vertical non-permanent surfaces** (whiteboards, windows, chart paper) make thinking visible, erasable, and collaborative; and (3) **thin-slice problems** launch students into the work *before* direct instruction, so thinking happens before consolidation.

**How BTC runs in this lesson (Phase 2, minutes 10–30):**

1. **Random groups:** Use a card randomizer or digital spinner to assign groups of three. Announce: "These are your working groups for the next 17 minutes. Find your vertical surface."
2. **Vertical surfaces:** Each group claims a whiteboard panel, a window section with a dry-erase marker, or standing-height chart paper. One marker per group — it passes between members so all three contribute reading and writing.
3. **Thin-slice prompt:** The Table G reading task (Parts A → B → C) is built to be *just* beyond what a student can do alone but reachable as a group. Students are not told "rising means solid, falling means gas." They read the values, compare directions, and *derive* the slope rule themselves before Phase 3 names it.
4. **Teacher as knowledge-withholder:** While groups work, circulate and ask only questions — never give the rule. Ask: "Bigger or smaller as it heats?" "If a new curve falls, what would you bet — solid or gas?" "Where do the curves cross, and what's true there?" The aim is for students to state the temperature-solubility pattern themselves.
5. **Gallery glance (built in):** As groups finish Part C, have each take a quick look at one neighboring board to compare how another group classified the "new" falling curve — exposing them to a second articulation of the same pattern before the debrief.

**Why BTC fits using solubility tables:** Reading Table G is a single, repeatable pattern (slope direction → solid vs. gas; curve height → saturation) that *emerges from the data itself*. That makes it an ideal thin-slice: students who derive "falling curve = gas" at the board own the rule when Phase 3 attaches the vocabulary, instead of copying a definition cold. Liljedahl's research shows students who derive a pattern before seeing it stated retain it more reliably than students who transcribe it from the board.

**CRSE connection:** The soda phenomenon and the opening-circle prompt ("a drink better cold than warm") draw on food and drink every student knows from home — sweet tea, fizzy drinks, cold juice — honoring out-of-school knowledge and making an exam tool feel continuous with lived experience. Random grouping is itself a CRSE move: it disrupts the social sorting that concentrates academic authority in a few students and signals that every student's reading of the curve belongs on the board.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — warm vs. cold soda going flat; Reference Table G graph `reference_table_g_solid_vs_gas.png`; return in Phase 4 reading the gas curve at fridge vs. warm temperatures |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — what does a curve's *direction* tell you?); Phase 3 (TT#2 — what do rising vs. falling curves mean?) |
| 3 | Students develop questions/models/procedures | Phase 2 BTC thin-slice (read values, derive the slope rule); Javalab saturation test; Phase 4 model revision |
| 4 | CCC defined and used | Lesson Overview · *Patterns*, explicit in Phase 3 (TT#2 + vocabulary) and Phase 4 (B/B/S on the falling gas curve) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: solubility curve / saturated / temperature-solubility relationship |
| 6 | Revisit phenomenon with evidence | Phase 4 — students read the gas curve at refrigerator vs. warm-room temperature to explain which soda keeps its fizz |
| 7 | ENL/SPED supports | Access & Differentiation block: sentence frames, word-choice box, Table G reading-guide card, pre-marked temperatures, BTC group roles, checkbox saturation decision |
| 8 | Assessment check | Phase 5 — Exit Ticket (read KNO₃ at 80 °C + saturation decision; gas solubility on warming; slope-to-classification sentence) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at the start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked Table G reading
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **solubility curve** — a line on Reference Table G showing the maximum mass of a solute that dissolves in 100 g of water at each temperature; the height of the curve is the saturation limit at that temperature, and the direction of its slope tells you whether the substance is a solid (rising) or a gas (falling)
- **saturated** — describing a solution that holds exactly the maximum amount of dissolved solute for its temperature (sitting right on the curve); a saturated solution cannot dissolve more solute unless the temperature changes, and any extra stays undissolved
- **temperature-solubility relationship** — the pattern on Reference Table G that for most *solids* solubility increases as temperature increases, while for *gases* solubility decreases as temperature increases; this relationship explains why a warm soda (dissolved gas) goes flat faster than a cold one
