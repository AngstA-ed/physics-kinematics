# Potential Energy Diagrams — Teacher Guide

## Cover

**Unit: Kinetics and Equilibrium — Lesson 03: Potential Energy Diagrams**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: BTC

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

**DC1.B** — *"Chemical processes, their rates, and whether or not energy is stored or released can be understood in terms of the collisions of molecules and the rearrangements of atoms into new molecules."* A potential energy (PE) diagram is the graphical tool that makes this idea visible: it plots the potential energy of the chemical system as bonds break and re-form along the reaction pathway. Reading a PE diagram lets students see *where* energy is stored (the energy "hill" the reactants must climb) and *whether* the overall process stores or releases energy (the relative heights of reactants and products).

**PS3-1** — the boundaries of the system and the reference level for potential energy. A PE diagram is drawn for a defined chemical system, and the energy axis is a *relative* scale. The dashed "energy = 0" reference level is a choice, not a physical constraint: the potential energy of the initial state (reactants) or the final state (products) does **not** have to be zero. What matters physically is the *differences* — the height of the activation-energy barrier and the height change from reactants to products (ΔH).

The Cross-Cutting Concept of **Energy and Matter** is the explicit lens: in every chemical change, energy is transferred into or out of the system as atoms are rearranged into new molecules. The PE diagram tracks that transfer. A second CCC, **Stability and Change**, appears in the activation-energy idea: a fast or slow start does not change where the reaction ends up.

### Phenomenon

Hold up a small open dish of gasoline (or describe one — **do not** actually open gasoline indoors; use a sealed photo/video or a verbal scenario). Point out: gasoline burning is one of the most energy-*releasing* reactions we use every day — it powers cars, lawnmowers, and generators. Then ask the puzzle: if burning gasoline releases so much energy, why doesn't the dish just burst into flame the moment it is exposed to air? Why does it sit there, perfectly calm, until a single spark touches it — and *then* releases all that energy at once?

The contrast is striking: a reaction that is *overall* downhill in energy still refuses to start until you give it a push. A match, a spark plug, a hot wire — each one supplies a small amount of energy to get over an invisible "hill" before the much larger release happens. The PE diagram is the map of that hill.

**Driving question:** If burning gasoline releases energy, why won't it start until you give it a spark?

### Javalab / Labs

- **PE-diagram drawing practice:** Students sketch and label a complete PE diagram from a short data set (energy of reactants, energy of products, peak energy). They mark reactants, products, the activated complex, the activation energy (Ea), and ΔH, then decide whether the reaction is exothermic or endothermic. Use the brand figure `figures/pe_diagram_exothermic.png` as the model. No external URL required.
- **Catalyst-effect investigation:** Students compare two pathways for the *same* reaction — one with a catalyst, one without — using `figures/pe_diagram_catalyst.png`. They identify what changes (the activation-energy barrier) and what stays exactly the same (reactant level, product level, ΔH). For a digital option, the Javalab "Reaction Energy / Activation Energy" simulation lets students drag the catalyst in and watch the barrier shrink while the start and end levels hold.
- **Spark demo (teacher-run, safe version):** A piezo lighter clicked over a small candle, or a "whoosh bottle" video, makes the activation-energy idea physical: nothing happens until the spark adds energy, then the exothermic release sustains itself.

### Assessments

- **PE diagram interpretation quiz** (district checkpoint, following lesson; see `Assessments/` folder once created): students read a labeled diagram to identify Ea, ΔH, reactants, products, and the activated complex, and decide exothermic vs. endothermic.
- **Exit Ticket** (Phase 5): three items built on a *new* endothermic diagram (distinct from the exothermic practice diagram used all period) — read Ea, read ΔH, and explain in one sentence why a catalyst speeds the reaction without changing ΔH. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | DC1.B (energy stored/released via bond rearrangement); PS3-1 (system boundary + PE reference level is relative, not necessarily zero) |
| **CCC focus** | Energy and Matter — a PE diagram tracks energy transferred into the system to start a reaction (activation energy) and out of the system overall (ΔH) as atoms rearrange into new molecules |
| **Strategy chips** | BTC (Building Thinking Classrooms) — visibly random groups at vertical non-permanent surfaces (whiteboards) build and defend PE diagrams from data |
| **Materials** | Vertical whiteboards or chart paper + markers (one station per group of 3), 2025 NYS Chemistry Reference Tables (Table I — heats of reaction — for the extension), `figures/pe_diagram_exothermic.png` and `figures/pe_diagram_catalyst.png` projected, piezo lighter + candle for the optional safe demo |
| **Safety** | **Do not** open or ignite gasoline indoors. The phenomenon is delivered verbally or via sealed image/video. The optional candle demo uses a piezo lighter at the teacher's station only, away from papers; have a cover ready to extinguish. Goggles for anyone near the flame. |
| **Prior knowledge** | Lesson 01 (Collision theory — reactions need particles to collide with enough energy) and Lesson 02 (Energy in reactions — exothermic releases energy, endothermic absorbs it; ΔH sign convention). Students should recognize "exothermic / endothermic" and the idea that bonds store energy before this lesson. |

**Lesson objectives — students can:**

- Read a potential energy diagram to identify the energy of the reactants, the energy of the products, the activated complex, the activation energy (Ea), and ΔH.
- Use the relative heights of reactants and products to classify a reaction as exothermic (ΔH < 0) or endothermic (ΔH > 0).
- Explain, using the activation-energy barrier, why an energy-releasing reaction (like burning gasoline) still needs a spark to start.
- Describe how a catalyst lowers the activation energy without changing the reactants, products, or ΔH.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers: *"Think of something that took one hard push to get started, but then kept going on its own — pushing a stalled car, getting out of bed on a cold morning, starting a big project. What was the 'push'?"* One round, one sentence each, pass allowed. This surfaces the everyday intuition that a system can be "ready" to release energy yet still need an initial input to get over the start — exactly the activation-energy idea.

Then post the **Do Now**:

> *"Gasoline burning releases a huge amount of energy — it powers cars and generators. A small dish of gasoline sits in the open air. Air has plenty of oxygen. Yet the gasoline does not burst into flame on its own. Write one sentence: why do you think it waits until a spark touches it?"*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "Because it needs heat to start." — affirm; and press: heat to start *what*, exactly? If burning gives off heat, why does it need heat first? That tension is today's whole lesson.
- "Because the spark lights it." — close; ask what the spark *does* — what does it provide that the room-temperature gasoline didn't have?
- "I thought fuels just catch fire on their own." — validate the surprise: most fuels are perfectly stable at room temperature even surrounded by oxygen. There is an invisible "barrier" before the release. We are going to draw that barrier today.

### 3–8 min · Phenomenon hook — the spark puzzle

**Teacher actions.** Present the gasoline scenario (verbally or via the sealed image/video — **never** open gasoline indoors). Optionally run the safe piezo-lighter-over-candle demo: the wick sits in oxygen-rich air doing nothing, then a single spark starts a flame that sustains itself.

> "Here is the puzzle. Burning gasoline is *downhill* in energy — it ends up at a much lower energy than it started, releasing the difference as heat and light. So if it's downhill, why doesn't it just roll down on its own? Why does it sit at the top, totally calm, until a spark gives it a tiny push?"

**Anticipated student responses:**

- "Because there's a little hill before the downhill part." — excellent intuition; capture it word-for-word. That "little hill" is what we'll formally name in Phase 3.
- "The spark gives it the energy to climb the hill." — perfect; that energy has a name we'll learn, and we'll measure its height on a graph.
- "Once it starts, the energy it releases keeps it going." — yes — the downhill release feeds the next push. That is why one spark is enough.

**Driving question** (post on the board and leave it there):

> *If burning gasoline releases energy, why won't it start until you give it a spark?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the spark puzzle. Then:

> "Turn to your partner: a reaction can end up at a *lower* energy than it started — it gives energy off — and *still* need an energy push to begin. Draw a quick sketch with your finger in the air: what would the energy 'path' from start to finish look like? Is it a straight slide down, or does it do something else first?"

Target insight (leave open if no one lands it): the path goes *up* first — over a hump — and *then* down to a level below where it started. The spark gets the system over the hump. That hump is the activation energy, and the down-step is the energy released (ΔH). We will name both in Phase 3.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–14 min · BTC launch — random groups to the boards

**Before any formal vocabulary is introduced**, students build the energy "path" from raw data using **Building Thinking Classrooms (BTC)** routines (see Strategy Spotlight). Form **visibly random groups of three** (deck of cards or random-grouper). Send each group to a **vertical non-permanent surface** (whiteboard / chart paper) with **one marker**. Standing, shared surface, no seats.

Post the launch task — keep it verbal and minimal, no worked example:

> "On your board, draw an energy graph for one reaction. The horizontal axis is *reaction progress* (start on the left, finish on the right). The vertical axis is *potential energy*. Use exactly these three facts: the starting mixture sits at **30 kJ**; partway through, the system reaches a high point of **85 kJ**; the finished mixture settles at **10 kJ**. Plot those three points in order and connect them into a smooth path. Then, with your group: what does the high point in the middle mean physically?"

### 14–24 min · BTC build — draw, defend, revise

Groups draw the curve: a plateau at 30, rising to a peak at 85, falling to a plateau at 10. Circulate and **answer questions with questions** (BTC move) — do not hand out the labels yet.

**Teacher facilitation language (circulate):**

> "Your curve goes up to 85 before it comes down to 10. What has to be *true* about the reaction for the energy to climb that high before it falls? Where would the spark fit on your picture?"

> "You drew the finish *lower* than the start — 10 versus 30. So the system ended up with *less* stored energy than it began with. Where did that energy go?"

> "Point to the highest spot on your curve. That single instant — halfway between reactants and products, bonds partly broken and partly formed — is real. What would you call the thing that exists right at that peak?"

**Anticipated student responses during the build:**

- "We don't know what units kJ are." — kilojoules, a unit of energy; the *relative heights* are what matter, not the absolute number. Notice we could have started the bottom of the axis anywhere.
- "Is the start supposed to be at zero?" — great question — no. The energy axis is a *relative* scale; the reactants do **not** have to start at zero. (This is PS3-1 — flag it, you'll return to it in Phase 3.)
- "The peak is the spark, right?" — close — the peak is how *high* the spark has to push the system. The spark supplies the climb; the peak is the top of the climb.
- "The drop at the end is the energy it releases." — yes — capture that on their board; you'll name it ΔH.

**Second task (post once most groups have the curve):**

> "Now a *different* reaction uses the SAME starting mixture (30 kJ) and the SAME finished mixture (10 kJ), but a chemist adds a **catalyst** — a substance that speeds it up. With the catalyst, the high point in the middle is only **60 kJ** instead of 85 kJ. Add this second path to your board, in a different color. What changed? What stayed exactly the same?"

**Teacher facilitation prompts (circulate):**

> "Compare the two peaks: 85 versus 60. The catalyzed path needs a *smaller* climb. Now compare the start and finish of the two paths — did the catalyst move the 30 or the 10?"

> "If the start and finish are unchanged, did the catalyst change how much energy the reaction releases overall? Defend your answer to your group."

**Anticipated student responses:**

- "The catalyst made the hill shorter." — exactly; capture it. The shorter hill is the key idea.
- "It changed the start to make it lower." — productive error; redirect to their own board: did you move the 30? No — both paths start at 30 and end at 10. Only the *peak* moved.
- "So the reaction gives off the same energy either way?" — yes — the overall release (start minus finish) is identical. The catalyst only lowers the barrier to *getting started*.

### 24–30 min · Gallery walk + consensus build

Run a short **BTC gallery walk**: groups rotate once to a neighboring board and find one thing done well and one question. Reconvene at the front.

> "Every board has the same shape: up over a hump, then down to a level below the start. Let's agree on what the parts mean before we name them. The flat start? (reactant energy.) The flat finish? (product energy.) The hump? (the energy you must add to get going.) The very top? (a real, fleeting in-between state.) The drop from start to finish? (energy released.)"

Leave the curves up — Phase 3 attaches vocabulary to the students' own drawings.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look at your two curves — the slow one (peak 85) and the catalyzed one (peak 60). Turn to your partner: which one would react *faster*, and why? Use the height of the hump in your answer."

Target consensus: the catalyzed path reacts faster because its hump is *lower* — fewer collisions need to be that energetic to get over it, so more collisions succeed per second. The catalyst does **not** change where the reaction starts or ends; it only lowers the barrier to starting.

> "And one more — did either curve start at zero on the energy axis? No. Why is that okay?"

Target: the energy scale is *relative* — we read **differences** (the height of the hump, the drop from start to finish), not absolute values. The reference level is a choice (PS3-1). Reactants do not have to sit at zero.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Now let's name what is already on your boards. The graph you drew — potential energy on the vertical axis, reaction progress on the horizontal — is a **potential energy diagram**. It is the map of energy stored in the system as bonds break and re-form. The flat left side is the reactants; the flat right side is the products."

> "The hump you all drew — the energy the system has to climb before it can react — is the **activation energy (Ea)**. It is measured from the reactants up to the peak. The spark provides exactly this. Burning gasoline is downhill overall, but it still needs the activation energy to get started. That is why it waits for the spark."

> "And the single point at the very top of the hump — bonds half-broken, half-formed, the unstable in-between — is the **activated complex**. It exists for an instant at the peak and then either falls forward to products or back to reactants."

Post the three terms on the board next to the curves. Students fill them in on their notes and label their own diagrams.

![Potential energy diagram for an exothermic reaction: a smooth purple curve rises from a flat reactant plateau at 30 kJ, peaks at an activated complex marked at 85 kJ, then falls to a flat product plateau at 10 kJ; an orange double-headed arrow from the reactant level to the peak is labeled activation energy (Ea); a green double-headed arrow from the reactant level down to the product level is labeled ΔH < 0 (energy released); the x-axis is reaction progress and the y-axis is potential energy in kJ.](figures/pe_diagram_exothermic.png)

**Discussion prompts to deploy here:**

- "On this diagram, where is the activation energy, and where is ΔH?" — *Expected response:* Ea is the climb from the reactant level (30) up to the peak (85), so Ea = 55 kJ. ΔH is the change from reactants (30) to products (10), so ΔH = −20 kJ — negative because the products are *lower*, meaning energy was released.
- "Is this reaction exothermic or endothermic, and how do you know from the picture alone?" — *Expected response:* exothermic — the products sit *lower* than the reactants, so the system released energy (ΔH is negative). You can read it straight off the diagram without any numbers.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Catalyst diagram + Because/But/So expansion

Project the catalyst figure. Students label both Ea values and confirm what is unchanged.

![Potential energy diagram comparing two pathways for the same reaction: a solid purple curve (without catalyst) rises from a reactant plateau at 30 kJ to a peak of 85 kJ then falls to a product plateau at 10 kJ; a dashed blue curve (with catalyst) shares the same 30 kJ start and 10 kJ finish but peaks lower, at only 60 kJ; a purple arrow marks the taller uncatalyzed activation energy and a blue arrow marks the shorter catalyzed activation energy; reactant level, product level, and ΔH are identical for both paths.](figures/pe_diagram_catalyst.png)

> "Two paths, same reaction. The purple (no catalyst) climbs to 85; the blue (with catalyst) climbs only to 60. Label both activation energies. Now check: did the catalyst change the reactant level? The product level? The ΔH?"

Target: reactant (30) unchanged, product (10) unchanged, ΔH (−20 kJ) unchanged. Only Ea dropped — from 55 kJ to 30 kJ.

Then run a **Because / But / So** sentence. Starter on the board:

> *"A catalyst makes a reaction go faster."*

Model one aloud:

> "A catalyst makes a reaction go faster **because** it lowers the activation energy — the height of the hump the reactants must climb — **but** it does not change the energy of the reactants, the energy of the products, or ΔH — **so** the reaction reaches the *same* finished state and releases the *same* total energy, just sooner."

Then have students write their own B/B/S using one of these starters:

- *"Gasoline does not catch fire on its own at room temperature…"* (hint: room-temperature collisions rarely have enough energy to clear the activation barrier)
- *"This reaction is exothermic even though it needs a spark to start…"* (hint: the spark supplies Ea; the products still end up lower than the reactants)

**Anticipated student responses:**

- "Because the collisions don't have enough energy to get over the hump." — strong; push for the So: "so almost no molecules react until a spark adds the activation energy and gets them over the barrier."
- "Because the products are lower than the reactants." — good for the exothermic starter; push: "but it still needs Ea to start, so 'needs a spark' and 'releases energy overall' are both true at once."

### 39–40 min · Return to the phenomenon

> "Return to the gasoline. We can now draw the whole story. The gasoline-plus-oxygen mixture sits at the reactant level — stable, calm — because room-temperature collisions almost never have enough energy to climb the activation barrier. The spark supplies that activation energy for a few molecules. Once they're over the hump and fall to the much lower product level, the energy they release supplies the activation energy for the *next* molecules — and the reaction sustains itself. In one sentence: why does it need a spark even though it releases energy?"

Target: "The reaction is downhill overall (exothermic), but there is an activation-energy barrier between reactants and products, so the spark is needed to push the first molecules over the barrier; after that, the energy released keeps it going."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud. The Exit Ticket uses a **new, endothermic** diagram (reactants 20 kJ, peak 70 kJ, products 50 kJ) — deliberately distinct from the exothermic practice diagram used all period:

> *A reaction has reactants at 20 kJ, an activated complex (peak) at 70 kJ, and products at 50 kJ.*
> *(a) What is the activation energy (Ea) of this reaction? Show how you found it.*
> *(b) What is ΔH, and is the reaction exothermic or endothermic? How do you know from the energy levels?*
> *(c) In one sentence, explain why adding a catalyst would speed this reaction up without changing its ΔH.*

Expected answers are in `Answer_Key.docx`.

**Closing Reflection (SEL, 30 seconds):**

> "Today we turned an invisible 'why won't it start?' puzzle into a graph you can read. In one sentence: what is one thing that finally clicked for you today about energy and reactions, and who — a groupmate or an idea — helped it click?"

Collect whiteboards (photograph for records) and Exit Tickets. Note which students read Ea as "peak minus reactants" versus "just the peak value" — the from-the-reactants subtraction is the main reading error; target those students at the start of the next lesson.

---

## Common Misconceptions

- **Misconception:** "If a reaction releases energy (exothermic), it shouldn't need any energy to start." → **Correction:** Overall energy release (ΔH < 0) and a start-up barrier (Ea) are two different parts of the diagram. The reactants must first climb the activation-energy hump before the system can fall to the lower product level. Gasoline is the everyday proof: hugely exothermic, yet stable until a spark supplies Ea.
- **Misconception:** "The activation energy is the height of the peak above zero." → **Correction:** Ea is measured from the **reactant** level up to the peak, not from the bottom of the axis. On the practice diagram, the peak is at 85 and the reactants are at 30, so Ea = 85 − 30 = 55 kJ, not 85. The energy axis is relative; only the *difference* is the activation energy.
- **Misconception:** "A catalyst changes how much energy the reaction releases (changes ΔH)." → **Correction:** A catalyst lowers Ea only. The reactant level, the product level, and therefore ΔH are all unchanged. The reaction reaches the same final state and releases the same total energy — it just gets there faster by way of a lower barrier.
- **Misconception:** "The reactants always start at zero on the energy axis." → **Correction:** The reference level (energy = 0) is a *choice*, not a physical requirement (PS3-1). The reactants — or the products — can sit at any level. What is physically meaningful is the *differences*: the height of the activation barrier (Ea) and the change from reactants to products (ΔH).
- **Misconception:** "The activated complex is a stable product you could bottle." → **Correction:** The activated complex exists only for an instant at the very peak — bonds are half-broken and half-formed and it is highly unstable. It immediately falls forward to products or back to reactants; it is never isolated as a stable substance.

---

## Access & Differentiation

- **ELL/ENL supports:** Pre-print a labeled "skeleton" PE diagram (axes, a blank curve, and blank label boxes) so students attach the five labels — reactants, products, activated complex, activation energy, ΔH — rather than drawing from scratch. Sentence frames: *"The activation energy is the energy from the ___ up to the ___."* and *"This reaction is ___ because the products are ___ than the reactants."* Word-choice box displayed all period: {potential energy diagram, activation energy, activated complex, reactants, products, exothermic, endothermic, catalyst}. Pair each term with a gesture: hand climbs a hill for activation energy, hand drops for exothermic.
- **IEP/SPED supports:** Provide a partially-completed diagram with the reactant and product plateaus already drawn; the student's task is to add the peak and the two arrows (Ea and ΔH). Give a labeled "reading checklist" card: (1) find reactants on the left, (2) find products on the right, (3) higher or lower? = endo or exo, (4) Ea = peak minus reactants. For BTC, assign a clear marker-rotation order so every student writes. Calculator not needed; subtraction values are kept small and whole.
- **Extensions:** (1) Using Table I (Heats of Reaction) from the 2025 NYS Chemistry Reference Tables, look up the ΔH for the combustion of a fuel and decide which way its PE diagram tilts. (2) Sketch the *reverse* reaction of the practice diagram (products → reactants): what is the new ΔH, the new Ea, and is it exo- or endothermic? (3) Reaction A has Ea = 55 kJ and Reaction B has Ea = 30 kJ at the same temperature — which proceeds faster, and connect your answer to collision theory from Lesson 01 (fraction of collisions with enough energy).

---

## Strategy Spotlight

**BTC — Building Thinking Classrooms (Peter Liljedahl).** BTC restructures the room so that *thinking* — not note-copying — is the default activity. For this lesson the three core BTC moves are: **visibly random groups**, **vertical non-permanent surfaces (VNPS)**, and a **thin-sliced task with no worked example up front**. Students build the PE diagram *before* they have any vocabulary, which is exactly the ABCs sequence (Activity Before Content): the graph is constructed from data first, then named in Phase 3.

**How to run it in this lesson (Phase 2):**

1. **Form visibly random groups of three** with a deck of cards or a random-grouper — *visibly* random so students trust the process and mix daily. New groups every lesson.
2. **Send each group to a vertical whiteboard with ONE marker.** Standing and a single shared marker force every voice into the work; the writer rotates. The vertical surface makes thinking public, so you can read all groups' progress in one glance and groups can borrow ideas from neighbors.
3. **Give the task verbally and thin-sliced** — three energy values, "plot and connect, then tell me what the peak means." No example diagram is shown first. This keeps the cognitive work with the students.
4. **Answer questions with questions.** When a group asks "is the start at zero?", reflect it back: "does it have to be? what would change if it weren't?" This protects the productive struggle (and surfaces PS3-1 organically).
5. **Run a short gallery walk** so groups see other representations of the same data and self-correct.

BTC pairs naturally with the **catalyst comparison**: the second task ("same start, same finish, lower peak — what changed?") is a perfect VNPS prompt because groups can literally overlay a second curve on their existing one and argue about it at the board.

**CRSE connection:** Visibly random grouping disrupts fixed status hierarchies — students who rarely volunteer in a whole-class setting contribute at the board, and competence is distributed rather than concentrated. The opening-circle prompt ("something that took one hard push to start") invites students' lived experiences (a stalled car, a cold morning) into the science, honoring out-of-school knowledge as a legitimate on-ramp to the activation-energy concept.

**Connection to Hochman literacy:** The B/B/S sentence in Phase 4 ("a catalyst makes a reaction faster **because** it lowers Ea, **but** it does not change ΔH, **so**…") gives students a sentence-level structure to hold a *cause* (lower barrier), a *contrast* (but ΔH is unchanged), and a *consequence* (same release, sooner) in one sentence — the precise reasoning the quiz will ask for in prose.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — the gasoline/spark puzzle (and optional safe candle demo); returned to in Phase 4 with the full reactant→barrier→product story |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — what does the energy path look like?); Phase 3 (TT#2 — which curve reacts faster and why?) |
| 3 | Students develop questions/models/procedures | Phase 2 BTC build — groups construct the PE curve from three data points at vertical whiteboards, then add the catalyzed path; gallery walk and revision |
| 4 | CCC defined and used | Lesson Overview · *Energy and Matter*; explicit in Phase 3 (reading Ea and ΔH off the diagram) and Phase 4 (B/B/S on catalyst and energy release) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: potential energy diagram / activation energy / activated complex |
| 6 | Revisit phenomenon with evidence | Phase 4 — students return to the gasoline puzzle and explain it with their own labeled diagram (Ea barrier + exothermic drop) |
| 7 | ENL/SPED supports | Access & Differentiation block: skeleton diagram, sentence frames, word-choice box, reading checklist card, marker-rotation roles |
| 8 | Assessment check | Phase 5 — Exit Ticket on a *new* endothermic diagram (read Ea, read ΔH, explain catalyst effect) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked PE-diagram example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **potential energy diagram** — a graph of the potential energy stored in a chemical system (vertical axis) versus reaction progress (horizontal axis); it shows the reactant level, the product level, the activation-energy barrier, and ΔH; the energy axis is a *relative* scale, so the reference level need not be zero
- **activation energy (Ea)** — the minimum energy that colliding reactant molecules must have to react; on a PE diagram it is the height of the barrier measured from the reactant level up to the peak; a catalyst lowers it, and a spark or heat can supply it
- **activated complex** — the unstable, high-energy arrangement of atoms that exists for an instant at the peak of the diagram, with bonds partly broken and partly formed; it immediately falls forward to products or back to reactants and is never isolated as a stable substance
