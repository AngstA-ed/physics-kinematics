# Chemical Equilibrium — Teacher Guide

## Cover

**Unit: Kinetics & Equilibrium — Lesson 05: Chemical Equilibrium**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: HOCHMAN

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

**HS-PS1-B (PS1.B disciplinary core idea)** — *"In many situations, a dynamic and condition-dependent balance between a reaction and its reverse reaction determines the numbers of all types of molecules present."* This lesson establishes the concept of **chemical equilibrium**: a reversible reaction reaches a steady state in which the forward and reverse reactions continue at equal rates, so the concentrations of all species stay constant even though the reaction has not stopped. For the 2025 NYSSLS-aligned Regents, students are expected to recognize equilibrium as a *dynamic* condition (not a stopped reaction), to identify the two observable characteristics of a system at equilibrium (equal forward/reverse rates and constant concentrations), and to read the double arrow (⇌) as the symbol for a reversible reaction. Per East Meadow guidance, a correct mental model of dynamic equilibrium is the prerequisite for Le Châtelier's principle and equilibrium-shift reasoning in the lessons that follow.

The Cross-Cutting Concept of **Stability and Change** is the explicit lens: a system at equilibrium *looks* unchanging at the macroscopic scale (color, concentration, pressure are all constant), but at the particle scale it is anything but static — molecules are continuously converting in both directions. The apparent stability is the *result* of two opposing changes happening at the same rate, not the absence of change.

### Phenomenon

A sealed, unopened bottle of soda keeps its fizz on a store shelf for months. Open it, leave it on the counter overnight, and it goes flat. Nothing was added or removed when the seal was on — yet the dissolved carbon dioxide stayed put. The instant the cap comes off, the CO₂ escapes and never comes back. Inside the sealed bottle, dissolved CO₂ is constantly leaving the liquid into the small gas space above it *and* re-dissolving from that space back into the liquid, at equal rates: CO₂(aq) ⇌ CO₂(g). The amount of dissolved gas looks frozen because the two processes are perfectly balanced. Open the bottle and you destroy the balance — CO₂ escapes into the room and cannot return, so the forward process has nothing to oppose it and the soda goes flat.

**Driving question:** Why does a sealed bottle of soda keep its fizz indefinitely, but go flat once it is opened?

### Javalab / Labs

- **Cup-transfer equilibrium simulation:** Two cups (label them "reactants" and "products") and a supply of counters (beans, chips, or paper squares). Each round, students move a *fixed fraction* of each cup's contents to the other cup — e.g., transfer half of the reactant cup forward and a tenth of the product cup back. Students count and record both cups after each round. After several rounds the counts stop changing (equilibrium) even though counters keep moving every round. This makes the "dynamic" part of dynamic equilibrium concrete and countable.
- **CoCl₂ equilibrium color change (teacher demo or class set):** The cobalt(II) chloride equilibrium [Co(H₂O)₆]²⁺ (pink) ⇌ [CoCl₄]²⁻ (blue) shifts visibly with added water (pink) or added concentrated HCl/heat (blue). Students observe that the same solution sits at a stable intermediate color when undisturbed — and that the color holds steady, showing constant concentrations at equilibrium. (Today's lesson uses this only to *establish* equilibrium; the directional shifting is the hook for the next lesson on Le Châtelier's principle.)
- **Rate-graph reading:** Students read `figures/equilibrium_rates.png` to identify the moment the forward and reverse rates become equal and to articulate what is happening to concentrations after that moment.

### Assessments

- **Equilibrium concept quiz** (district checkpoint, following lesson; see `Assessments/` folder once created): students identify the two characteristics of a system at equilibrium, interpret the double arrow, and distinguish a dynamic equilibrium from a stopped reaction.
- **Exit Ticket** (Phase 5): three items — identify the two characteristics of equilibrium in a sealed beaker of water; explain why "equilibrium" does not mean equal concentrations; and write one appositive sentence defining dynamic equilibrium. The Exit Ticket uses a closed-flask water-evaporation system, distinct from the soda and cup-transfer contexts practiced on the worksheet. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | HS-PS1-B (dynamic, condition-dependent balance between a reaction and its reverse; constant concentrations at equilibrium) |
| **CCC focus** | Stability and Change — a system at equilibrium is macroscopically stable (constant concentrations, color, pressure) precisely because two opposing changes (forward and reverse reactions) occur at equal rates at the particle scale |
| **Strategy chips** | HOCHMAN — appositive sentence to define *dynamic equilibrium* crisply; Because/But/So sentence in Phase 4 |
| **Materials** | Two paper cups per group (or pair) labeled "reactants" and "products", ~40 counters per group (beans/chips/paper squares), `figures/equilibrium_rates.png` projected, optional CoCl₂ demo set-up in a sealed test tube, a sealed soda bottle and an opened/flat one for the hook |
| **Safety** | The cup-transfer simulation is hazard-free. If you run the CoCl₂ demo, cobalt(II) chloride is toxic and a suspected carcinogen — teacher demo only, in a sealed container, gloves and goggles, no student handling; concentrated HCl requires a fume hood. The soda bottle is food-safe; open it over a sink. |
| **Prior knowledge** | Lesson 01 (Collision Theory & Rates) — reaction rate depends on concentration; rate decreases as reactants are consumed. Lesson 02–04 (energy, PE diagrams, spontaneity) — reactions can proceed in a forward direction. Students should already know that a reaction *rate* is "how fast" and that rate drops as reactant concentration drops. |

**Lesson objectives — students can:**

- Describe a reversible reaction and read the double arrow (⇌) as "proceeds in both directions."
- State the two characteristics of a system at equilibrium: the forward and reverse rates are equal, and the concentrations of all species are constant.
- Explain that equilibrium is *dynamic* — both reactions continue at the particle scale — and is **not** a stopped reaction, and that "equal rates" does **not** mean "equal concentrations."
- Explain, using Stability and Change, why a sealed soda keeps its fizz while an open one goes flat.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers: *"Think of something that stays the same on the outside even though it is busy underneath — a crowded room where people keep entering and leaving but the count stays steady, a fountain that looks still but is always recirculating water. What came to mind?"* One round, one sentence each, no judgment. This surfaces the core intuition of the lesson: steady on the outside, busy underneath.

Then post the **Do Now**:

> *"An unopened bottle of soda keeps its fizz for months on a shelf. The moment you open it and leave it out, it goes flat. Nothing was added or taken away while the cap was on. Write one sentence: where does the fizz (the dissolved gas) go when the bottle is open that it could not go when the bottle was sealed?"*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "The gas escapes into the air when it's open." — affirm; and probe: when the bottle was sealed, was the gas escaping at all? Where did it go then?
- "When it's sealed the gas has nowhere to go, so it stays in." — close; sharpen: there *is* a little space above the soda. Is gas moving into that space even when sealed? (Yes — but it comes back.)
- "The pressure keeps it in when it's closed." — good observation; pressure is part of the story. Today we will see that the gas is constantly leaving *and* returning when sealed — that is the key idea.

### 3–8 min · Phenomenon hook — sealed vs. open soda

**Teacher actions.** Hold up a sealed bottle and an open, flat one. Tell the story. In the sealed bottle, dissolved CO₂ is constantly escaping out of the liquid into the small gas space at the top — *and* CO₂ from that space is constantly dissolving back into the liquid. Both happen at the same rate, so the amount of dissolved gas never changes. The soda looks "frozen" but it is actually busy in both directions. Write the reversible process on the board:

> CO₂(aq) ⇌ CO₂(g)

> "That double arrow is the whole point. It says the gas goes both ways at once."

**Sample teacher language:**

> "Here is the part that trips everyone up. In the sealed bottle, the fizz is not just sitting there doing nothing. Gas is leaving the liquid every second — and gas is coming back into the liquid every second — at exactly the same rate. The two cancel out, so the dissolved amount stays constant. Now I open the bottle. The escaping gas floats off into the room and never comes back. The 'return trip' is broken. So leaving wins, and the soda slowly goes flat."

**Anticipated student responses:**

- "So when it's open the gas just leaves and that's it?" — yes; the forward (escaping) process has nothing opposing it anymore, so the dissolved CO₂ keeps dropping until it's gone.
- "Why doesn't the sealed one go flat too if gas is escaping?" — excellent question; because in the sealed bottle the escaped gas is trapped right above the liquid and dissolves back in just as fast. Balanced both ways.
- "Is the reaction stopped in the sealed bottle?" — no — and that is exactly the misconception we'll fix today. It's balanced, not stopped.

**Driving question** (post on the board and leave it there):

> *Why does a sealed bottle of soda keep its fizz indefinitely, but go flat once it is opened?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the soda or the double-arrow process. Then:

> "Turn to your partner: in the *sealed* bottle, the amount of dissolved fizz stays constant — it doesn't change. Does 'doesn't change' mean nothing is happening? Or could something be happening that we just can't see from the outside?"

Target insight (leave open if no one lands it yet): the amount stays constant *because* two opposite processes are happening at equal rates, not because everything has stopped. We will name that condition formally in Phase 3.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–15 min · ABCs Activity — cup-transfer simulation, before the formal definition

**Before any formal vocabulary is introduced**, students build intuition by running a reversible "reaction" with counters and watching it reach a steady state on its own.

Set up: each pair gets two cups — one labeled **Reactants (R)**, one labeled **Products (P)** — and about 40 counters. Start with **all 40 counters in the Reactants cup, 0 in Products.**

**The transfer rule (write on the board):**

> Each round:
> 1. Move **half** of whatever is in the Reactants cup to the Products cup (round down). *(forward reaction)*
> 2. Move **one-tenth** of whatever is in the Products cup back to the Reactants cup (round down). *(reverse reaction)*
> 3. Count both cups. Record. Repeat.

Have students record R and P after each round in a table (provided on the worksheet). Run 6–8 rounds.

**Teacher facilitation language (circulate):**

> "Don't try to predict the final numbers — just follow the rule and count honestly each round. Watch what happens to the two counts as you go."

> "Are counters still moving in round 6? Yes. Are the *totals in each cup* still changing much by round 6? Look closely — they've nearly stopped changing. That's the interesting part."

**Anticipated student responses during ABCs:**

- "The numbers stopped changing but we're still moving counters every round!" — that is exactly the insight. Capture it loudly: the system is busy but the counts are steady.
- "Reactants ended around 7 and Products around 33 — they're not equal." — perfect; note that the steady state is *not* a 50/50 split. Equal *rates* of transfer, unequal *amounts*. Hold that thought for Phase 3.
- "Did we do it wrong? They never became equal." — no, you did it right; the two cups are not supposed to become equal. They become *steady*.

### 15–22 min · Initial Model — what is happening at the steady state?

**Prompt on the board:**

> *"By round 7, the count in each cup barely changes. But you are still moving counters every round. In your own words: how can the counts stay the same while counters keep moving? Draw or write your best explanation."*

Students work individually for 3 minutes, then compare with a partner.

Target idea (do not name it yet):

> The number of counters moving *forward* each round (R→P) has become equal to the number moving *back* each round (P→R). Forward out equals back in, so each cup's total holds steady — even though transfers never stop.

**Teacher facilitation language:**

> "Count it directly in your last round. How many counters went forward (R→P)? How many came back (P→R)? Are those two numbers close to equal? That equality is *why* the totals stopped changing."

**Anticipated student responses:**

- "The same number leaves and comes back, so it evens out." — exactly the model. Affirm and write the words "forward = back" on the board next to their language.
- "It's like the soda — gas leaving and coming back at the same speed." — beautiful transfer; connect explicitly to the phenomenon.
- "But the cups aren't equal — R is 7 and P is 33." — right, and that's the key distinction. The *rates* are equal; the *amounts* are not. We'll formalize this next.

### 22–30 min · Investigation — the rate graph and the CoCl₂ demo (optional)

Project `figures/equilibrium_rates.png` and have students examine it alongside their cup data.

![Line graph titled 'Forward and Reverse Rates Approaching Equilibrium': the purple forward-reaction-rate curve starts high and falls over time; the blue reverse-reaction-rate curve starts at zero and rises; the two curves converge to the same constant value, marked by a dashed orange vertical line labeled 'equilibrium reached' and a gray horizontal line labeled 'rates equal'; the x-axis is labeled 'time' and the y-axis is labeled 'reaction rate'.](figures/equilibrium_rates.png)

Pose, for partners to discuss and record:

> "Find the moment the purple (forward) and blue (reverse) curves meet. Before that moment, which rate is faster? After that moment, what are the two rates doing? And what is happening to the *concentrations* once the rates are equal?"

Target reading:

- **Early on:** forward rate is high (lots of reactant) and reverse rate is near zero (almost no product yet).
- **As time goes on:** forward rate falls (reactant is being used up) while the reverse rate rises (product is building up).
- **At equilibrium (the dashed line):** the two rates become equal and stay equal. From that moment on, the concentrations of reactants and products stop changing — they hold constant.

**Optional CoCl₂ demo (teacher only, sealed tube):** Show the cobalt(II) chloride solution sitting at a steady purple-ish intermediate color when undisturbed. The point to make today: *the color is holding constant* — that's the macroscopic sign of constant concentrations at equilibrium. (Save the pink↔blue *shifting* for the Le Châtelier lesson.)

**Teacher facilitation language:**

> "Notice the forward and reverse curves never cross zero and never stop — they level off at the same height. That 'same height' is the equilibrium rate. The reaction is still going both ways; it has just balanced."

**Anticipated student responses:**

- "After they meet, both lines are flat and on top of each other." — exactly; equal and constant. That's equilibrium.
- "So the reaction stopped at the dashed line?" — no — the rates are equal but not zero. Both reactions keep going; they just cancel out.
- "Concentrations stop changing but the reactions don't stop." — that is the whole lesson in one sentence. Capture it.

### 28–30 min · Reconnect + surface the pattern

Bring pairs back together. Ask one pair to report their final cup counts and how many counters moved each way in the last round. Then ask the class:

> "Across the cup simulation, the rate graph, and the soda: what is the *common pattern*? What two things are true once a system reaches this steady state?"

Surface the two characteristics (without yet giving the vocabulary term): (1) the forward and reverse processes are happening at **equal rates**, and (2) the **amounts/concentrations stay constant**. And the system is **never stopped** — it is busy in both directions.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Your cup simulation ended with about 7 counters in Reactants and 33 in Products — not equal. Turn to your partner: the word 'equilibrium' contains 'equal.' But the two cups were *not* equal. So what *was* equal at the steady state?"

Target consensus: at the steady state, the **rates** were equal (the number moving forward each round equaled the number moving back each round), even though the **amounts** in the two cups were very different. "Equilibrium" refers to equal *rates*, not equal *amounts*.

> "Second question: in the sealed soda, was the fizz reaction stopped, or running? How do you know?"

Target: it was running in both directions at once — escaping and re-dissolving at equal rates — so the dissolved amount stayed constant. Constant amount does *not* mean stopped.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name what we've been watching all period. A reaction that can run in both directions — forward and reverse — is a **reversible reaction**, and we write it with a double arrow: ⇌. The fizz in the soda, the counters between the cups, the cobalt solution — all reversible. When a reversible reaction reaches the steady state we kept finding — where the forward and reverse reactions run at *equal rates*, so the concentrations of everything stay constant — that condition is called **equilibrium**. And because the reactions never actually stop — they just balance — we call it a **dynamic equilibrium**: 'dynamic' meaning active, busy, still moving."

> "Here is the Hochman appositive move that locks in the definition. An appositive is a phrase set off by dashes that renames or explains the noun next to it. Say this with me:

> *Dynamic equilibrium — the condition where the forward and reverse reactions occur at equal rates so concentrations stay constant — is not a stopped reaction.*

> The phrase between the dashes is the appositive: it defines 'dynamic equilibrium' inside the sentence. You'll use this structure on the Exit Ticket and in your notes."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "If a reaction is at equilibrium, are the concentrations of reactants and products equal?" — *Expected response:* No — not necessarily, and usually not. What's equal is the forward and reverse *rates*. The concentrations are *constant* (unchanging), but they can be very different from each other — like the 7-vs-33 cups.
- "What does the double arrow ⇌ tell you that a single arrow → does not?" — *Expected response:* that the reaction runs in both directions at once and can reach a balance, rather than going only one way to completion.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the model + Appositive + Because/But/So expansion

Students return to their Initial Model (their cup steady-state explanation). They annotate it with vocabulary: label the steady state "dynamic equilibrium," label the equal forward/back transfers "equal rates," and label the steady cup counts "constant concentrations." Then they write an appositive sentence defining the result.

**Appositive sentence (model on board):**

> *"Dynamic equilibrium — the condition where the forward and reverse reactions occur at equal rates so concentrations stay constant — is not a stopped reaction."*

Ask students to write a parallel appositive for the soda:

> *"The fizz in a sealed soda — ___________________ — stays constant because ___________________."*

Then run a **Because / But / So** sentence about the phenomenon. Starter on the board:

> *"A sealed bottle of soda keeps its fizz, but an open bottle goes flat."*

Model one aloud:

> "A sealed bottle keeps its fizz **because** the CO₂ leaving the liquid and the CO₂ re-dissolving into it happen at equal rates, so the dissolved amount stays constant at dynamic equilibrium — **but** opening the bottle lets the escaping CO₂ leave the system permanently, removing the reverse process — **so** the forward (escaping) process no longer has an equal-and-opposite reverse process to balance it, the system can never reach equilibrium, and the soda keeps losing gas until it goes flat."

Then have students write their own B/B/S using one of these starters:

- *"In the cup simulation, the counts in each cup stopped changing after several rounds…"* (hint: forward transfers became equal to reverse transfers)
- *"A reaction at equilibrium is not a stopped reaction…"*

**Anticipated student responses:**

- "Because the same number of counters went each way." — good start; push for the frame: "because the number of counters moving forward each round became equal to the number moving back, so neither cup's total could keep changing."
- "Because the reactions are still going, just balanced." — excellent; push for the So: "so the concentrations stay constant even though the reaction never stops — that's why it's *dynamic* equilibrium, not a finished reaction."

### 39–40 min · Return to the phenomenon

> "Return to the two soda bottles. Using today's words — reversible reaction, equilibrium, dynamic — explain in one sentence why the sealed one keeps its fizz and the open one goes flat."

Target: "In the sealed bottle the reversible process CO₂(aq) ⇌ CO₂(g) reaches dynamic equilibrium — CO₂ escapes and re-dissolves at equal rates, so the dissolved amount stays constant — but opening the bottle removes the escaped gas so the reverse step can't keep up, equilibrium is impossible, and the soda goes flat."

> "The fizz isn't 'locked in' by the cap doing nothing. It's held steady by two opposite processes running at the same speed. Stability you can see, built from change you can't."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud:

> *A sealed flask is half-filled with liquid water and left to sit. After a while, the water level and the humidity in the flask stop changing. The process is H₂O(l) ⇌ H₂O(g).*
> *(a) State the TWO characteristics that tell you this system has reached equilibrium.*
> *(b) A classmate says, "The water level stopped changing, so evaporation must have stopped." Explain why this is wrong.*
> *(c) Write ONE appositive sentence (using dashes) that defines dynamic equilibrium.*

Expected answers are in `Answer_Key.docx`.

**Closing Reflection (SEL, 30 seconds):**

> "Today we found that something can look perfectly still on the outside while being busy on the inside. In one sentence: what is one thing that surprised you today about how 'staying the same' and 'still changing' can both be true at once — and who helped you see it?"

Collect worksheets; note which students wrote that equilibrium means "equal concentrations" (the most common error) versus "equal rates." Flag the equal-concentrations error for a brief one-on-one at the start of the next lesson, because Le Châtelier reasoning depends on getting this distinction right.

---

## Common Misconceptions

- **Misconception:** "Equilibrium means the reaction has stopped." → **Correction:** Equilibrium is *dynamic*. The forward and reverse reactions both continue at the particle scale — they just run at equal rates, so the net concentrations stop changing. In the cup simulation, counters keep moving every single round even after the totals hold steady. A stopped reaction would have *no* transfers; equilibrium has *equal* transfers.
- **Misconception:** "At equilibrium, the concentrations of reactants and products are equal." → **Correction:** What is equal at equilibrium is the forward and reverse *rates*, not the *amounts*. The cup simulation settled at roughly 7 reactant and 33 product — very unequal amounts, equal transfer rates. The concentrations are *constant*, but they are usually not equal to each other.
- **Misconception:** "The single arrow → and the double arrow ⇌ mean the same thing." → **Correction:** A single arrow means the reaction goes essentially one way to completion. A double arrow ⇌ means the reaction is reversible — it runs in both directions and can settle at a dynamic balance. The double arrow is the visual flag for an equilibrium system.
- **Misconception:** "The cap on the soda physically traps the gas, like a lid holding water in a cup." → **Correction:** The sealed system reaches equilibrium because the escaped CO₂ has nowhere to go but back into the liquid — so it re-dissolves as fast as it escapes. It is not that gas can't move; it is that gas moving out is exactly balanced by gas moving in. Open the system and you remove the return path, breaking the balance.
- **Misconception:** "Once a reaction reaches equilibrium, nothing further can change it." → **Correction:** Equilibrium is *condition-dependent* (the 'C' in HS-PS1-B). Changing conditions — adding or removing a substance, changing temperature — disturbs the balance and shifts it. (That shifting is the subject of the next lesson on Le Châtelier's principle; today's job is only to establish what an undisturbed equilibrium is.)

---

## Access & Differentiation

- **ELL/ENL supports:** Sentence frames for the steady-state explanation and Exit Ticket: *"At equilibrium, the ___ rate equals the ___ rate, so the ___ stay constant."* and *"This is not a stopped reaction because ___."* Word-choice box displayed on the board throughout: {reversible reaction, equilibrium, dynamic, forward rate, reverse rate, constant, concentration}. Pair the term "dynamic" with a gesture (hands circling) and "constant" with a flat, level hand. Pre-print the cup-transfer data table with the round numbers already filled in so students record only the counts. The double arrow ⇌ is labeled "both directions" everywhere it appears.
- **IEP/SPED supports:** Provide a partially-filled cup-transfer table where the first two rounds are worked as a model, so the student continues an established pattern rather than starting cold. Assign clear partner roles: one student transfers counters, one records. Offer a two-choice version of the Exit Ticket (b): provide two sentences and have the student select and explain the correct one. Pre-highlight the dashed "equilibrium reached" line on the rate graph so the key feature is unambiguous. Calculator not required; counts are small whole numbers.
- **Extensions:** (1) Predict the cup simulation's steady state from the rule: if you move ½ forward and 1/10 back each round, what ratio of P to R makes the forward transfer equal the reverse transfer? (Set ½·R = 1/10·P → P/R = 5, i.e. about 33⅓ to 6⅔ out of 40 — close to the observed 33/7.) (2) Sketch what `figures/equilibrium_rates.png` would look like if the reaction started with *pure product* instead of pure reactant. (3) Research a biological equilibrium — e.g., oxygen binding to hemoglobin, or CO₂/bicarbonate buffering in blood — and write one sentence about why "dynamic" matters for keeping you alive.

---

## Strategy Spotlight

**HOCHMAN — Appositive sentence.** The Hochman Writing Method (Judith Hochman and the Writing Revolution) treats sentence-level writing as a thinking tool. For this lesson the featured technique is the **appositive**, a noun phrase set off by dashes (or commas) that renames or defines the noun it follows. The appositive is ideal for a counterintuitive concept like dynamic equilibrium because it forces the student to pack the full, careful definition into one subject-verb sentence — and the careful definition is exactly where the common misconceptions hide.

**The target appositive for this lesson:**

> *Dynamic equilibrium — the condition where the forward and reverse reactions occur at equal rates so concentrations stay constant — is not a stopped reaction.*

This sentence structure does three things simultaneously: (1) names the term, (2) defines it precisely in the phrase between the dashes (equal *rates*, constant *concentrations*), and (3) heads off the central misconception in the main clause ("is not a stopped reaction"). A student who can write and say this sentence — not just recite "equilibrium is when rates are equal" in isolation — has integrated both the definition *and* the correction of the dominant error.

**How to run it in this lesson (Phase 3 → Phase 4):**

1. Post and read aloud the model appositive sentence together (Phase 3 vocabulary).
2. Ask students to write a parallel appositive for the soda phenomenon: *"The fizz in a sealed soda — ___ — stays constant because ___."* This requires them to substitute the equilibrium idea into a concrete context, confirming the abstract definition connects to the phenomenon.
3. In Phase 4, students write their own appositive defining dynamic equilibrium. Cold-call two or three students; ask: does the appositive phrase name *equal rates* AND *constant concentrations*? Does the main clause guard against the "stopped reaction" error? Both checks must pass for the sentence to be complete.

**Why the appositive fits dynamic equilibrium:** The single biggest barrier in this topic is that "equilibrium" *sounds* like "stopped" or "equal amounts," and both readings are wrong. A loose, one-clause definition lets those wrong readings survive. The appositive's tight, dash-bounded phrase forces students to state the two precise conditions in one breath, and the main clause gives them a built-in place to put the correction. Students who master this sentence are far less likely to mis-apply equilibrium in the Le Châtelier lesson that follows.

**CRSE connection:** The opening circle prompt (a crowded room where people keep entering and leaving but the count stays steady; a recirculating fountain) invites students to bring their own everyday systems into the conversation before any chemistry vocabulary appears. The anchoring phenomenon — a soda bottle — is a substance present in nearly every student's kitchen and corner store, making an abstract, particle-scale idea continuous with lived experience rather than confined to the lab. Honoring the everyday "steady but busy" systems students already know primes them to accept that an invisible chemical system can behave the same way.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — sealed vs. open soda bottle (fizz that stays vs. goes flat); rate graph `equilibrium_rates.png`; return in Phase 4 with the two-bottle explanation |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — does "doesn't change" mean nothing is happening?); Phase 3 (TT#2 — the cups weren't equal, so what *was* equal?) |
| 3 | Students develop questions/models/procedures | Phase 2 cup-transfer simulation (run the rule, record R and P each round); Initial Model (explain the steady state); rate-graph reading |
| 4 | CCC defined and used | Lesson Overview · *Stability and Change*, explicit in Phase 3 (vocabulary: stable concentrations from balanced change) and Phase 4 (B/B/S sealed vs. open soda) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: reversible reaction / equilibrium / dynamic (equilibrium) |
| 6 | Revisit phenomenon with evidence | Phase 4 — students return to the two soda bottles armed with cup-simulation data and the rate graph to explain why sealed stays fizzy and open goes flat |
| 7 | ENL/SPED supports | Access & Differentiation block: sentence frames, word-choice box, pre-filled/partially-worked cup table, partner roles, two-choice Exit Ticket option, highlighted equilibrium line |
| 8 | Assessment check | Phase 5 — Exit Ticket (two characteristics of equilibrium in a closed water flask; why "stopped" is wrong; appositive definition) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked cup-simulation example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **reversible reaction** — a reaction that can proceed in both the forward and reverse directions, written with a double arrow (⇌); both directions occur at the same time, allowing the system to reach a balance
- **equilibrium** — the condition in a reversible reaction at which the forward and reverse reactions occur at equal rates, so the concentrations of all reactants and products stay constant; equal *rates*, not equal *amounts*
- **dynamic equilibrium** — equilibrium understood at the particle scale: the forward and reverse reactions never stop — they continue at equal rates — so the system is constantly changing underneath while appearing macroscopically unchanged (constant concentrations, color, and pressure)
