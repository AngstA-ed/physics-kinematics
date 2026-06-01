# Titration — Teacher Guide

## Cover

**Unit: Acids and Bases — Lesson 03: Titration**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: BTC

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

**HS-PS1-11 (Acids and Bases)** — *"Plan and conduct an investigation to compare properties and behaviors of acids and bases."* Titration is the quantitative culmination of this standard: students plan and carry out a procedure (SEP-3, Planning & Carrying Out Investigations) in which a base of known concentration is added drop by drop to an acid of unknown concentration until the acid is exactly neutralized. The color change of an indicator signals when the moles of added base equal the moles of acid present — the **equivalence point** — and that single observation, paired with the volumes and the known concentration, lets students calculate the unknown concentration using M_a V_a = M_b V_b. Per East Meadow guidance, students should already know what acids and bases are (Lesson 01) and how the pH scale works (Lesson 02); this lesson makes those qualitative ideas measurable.

The Cross-Cutting Concept of **Scale, Proportion, and Quantity** is the explicit lens: neutralization is a proportional relationship. At the equivalence point the quantity of H⁺ delivered by the acid is exactly balanced by the quantity of OH⁻ delivered by the base, so for a strong monoprotic acid and a strong base the relationship reduces to M_a V_a = M_b V_b. Concentration and volume trade off proportionally — a more concentrated acid requires more base to neutralize, a more dilute acid requires less.

### Phenomenon

A chemist is handed an unlabeled bottle of hydrochloric acid recovered from a stockroom. There is no concentration printed anywhere — it could be a weak rinse or a dangerously strong reagent, and you cannot tell by looking, because both are clear and colorless. Tasting it is out of the question; a pH meter would give the pH but not directly the molarity for every situation, and the chemist needs the *exact* concentration. So instead the chemist measures out 25.0 mL of the mystery acid, adds two drops of phenolphthalein (which stays colorless in acid), and slowly drips in sodium hydroxide of *known* concentration from a burette. Drop after drop, nothing. Then one single drop turns the entire flask a flash of pink that does not fade. The chemist stops, reads the burette, and — using nothing but two volumes and one known concentration — calculates the exact molarity of the unknown acid. No guessing, no labels, just a controlled reaction and a number that drops out of the arithmetic.

**Driving question:** How can a chemist determine the exact concentration of an unknown acid or base using only a known solution, a burette, and a color change?

### Javalab / Labs

- **Acid–base titration lab (core activity):** Students titrate 25.0 mL of an "unknown" HCl with standardized 0.10 M NaOH, using two drops of phenolphthalein. They add base from a burette in 1 mL increments, then drop by drop near the end, until a single drop produces a permanent faint-pink color (the endpoint). They record the volume of NaOH delivered at the endpoint and calculate the acid's molarity with M_a V_a = M_b V_b. A class set of "unknowns" can be pre-made at 0.10 M so the expected equivalence volume is 25.0 mL; groups will get values clustered around it, which is itself a teachable point about experimental precision. Connect the data to the titration curve in `figures/titration_curve_naoh_into_hcl.png`.
- **Titration calculation practice:** A structured problem set on M_a V_a = M_b V_b — solving for any one of the four variables (M_a, V_a, M_b, V_b) given the other three. Each problem requires the student to label which quantity is the acid and which is the base before substituting. This is the core skill for the NYSSLS acid–base quantitative expectation.
- **Curve-reading (Javalab option):** A virtual strong-acid/strong-base titration simulation (Javalab "Acid-Base Titration" module) lets students drip base into acid and watch pH climb on a live curve, locating the steep jump that marks the equivalence point. Use it to preview or reinforce the shape of `figures/titration_curve_naoh_into_hcl.png` before the wet lab.

### Assessments

- **Titration lab report** (district checkpoint, following lesson): students report their endpoint volume, show the M_a V_a = M_b V_b setup, calculate the unknown acid's molarity, and write one sentence explaining how the indicator told them when to stop.
- **Calculation quiz** (Phase 5 and a follow-up checkpoint): students solve M_a V_a = M_b V_b for a missing variable and define the equivalence point. The Exit Ticket below is the formative version — it uses values distinct from the worksheet practice so it checks transfer, not recall. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | HS-PS1-11 (plan/conduct an investigation comparing acids and bases; quantify neutralization with M_a V_a = M_b V_b) |
| **CCC focus** | Scale, Proportion, and Quantity — at the equivalence point the quantity of acid exactly balances the quantity of base; concentration and volume trade off proportionally (M_a V_a = M_b V_b) |
| **Strategy chips** | BTC — random groups at vertical non-permanent surfaces derive the neutralization relationship from titration data before the formula is named |
| **Materials** | Burettes (or graduated droppers), 25.0 mL volumetric pipettes or graduated cylinders, Erlenmeyer flasks, standardized 0.10 M NaOH, "unknown" HCl samples, phenolphthalein indicator, white background card, calculators, the 2025 NYS Chemistry Reference Tables, `figures/titration_curve_naoh_into_hcl.png` projected, vertical whiteboards/windows with dry-erase markers |
| **Safety** | NaOH and HCl are corrosive. Goggles and aprons required for all students at all times. Add acid to a flask first, then titrate base in; never the reverse for the stock. Rinse any skin contact immediately at the eyewash/sink and notify the teacher. Phenolphthalein is in an ethanol base — keep away from flames. Review the SDS routine from Unit 1 Lesson 01. |
| **Prior knowledge** | Lesson 01 (Properties of Acids and Bases) — acids release H⁺, bases release OH⁻, neutralization produces water and a salt; Lesson 02 (pH Scale) — pH 7 is neutral, < 7 acidic, > 7 basic; molarity (mol/L) from the solutions unit. |

**Lesson objectives — students can:**

- Describe the titration procedure: deliver a base of known concentration from a burette into a measured volume of acid until an indicator signals neutralization.
- Define the **equivalence point** as the moment when the moles of added base exactly equal the moles of acid present, and identify it on a titration curve as the steep vertical jump through pH 7.
- Calculate an unknown concentration using **M_a V_a = M_b V_b**, solving for any one of the four variables given the other three.
- Explain, using Scale, Proportion, and Quantity, why a more concentrated acid requires a larger volume of the same base to reach the equivalence point.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers: *"Think of a time you had to figure out exactly how much of something there was when you couldn't just read it off a label — how much sugar is really in a drink, how much gas is left in the tank, how strong a cleaning product is. What did you do to find out?"* One round, one sentence each, pass allowed. This surfaces the everyday intuition that you can measure an unknown amount indirectly, by reacting or comparing it against something you *do* know.

Then post the **Do Now**:

> *"A chemist has a bottle of acid with no concentration on the label. It is clear and colorless. They cannot taste it and cannot tell its strength by looking. Write one sentence: how might you measure exactly how strong (concentrated) the acid is without a label?"*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "Use a pH meter or pH paper." — affirm; pH tells you how acidic it is, but probe: does pH alone give you the *molarity* (mol/L)? Two acids can share a pH region yet differ; pH is a clue, not the full answer. We want the exact concentration.
- "React it with something and see how much it takes." — excellent; that is exactly the idea behind today's method. Capture it on the board.
- "I don't think you can without the label." — validate the instinct, then promise: by the end of today you'll have a method that needs no label at all.

### 3–8 min · Phenomenon hook — the unlabeled acid

**Teacher actions.** Tell the story. A bottle of HCl comes out of the stockroom with no concentration printed on it. Both a harmless rinse and a dangerous reagent look identical — clear and colorless. The chemist measures 25.0 mL of the mystery acid into a flask, adds two drops of phenolphthalein (still colorless), and slowly drips in NaOH of *known* concentration from a burette. Drop after drop: nothing. Then one single drop flashes the whole flask pink — and it stays. The chemist reads the burette and calculates the acid's exact molarity from two volumes and one known concentration.

**Sample teacher language:**

> "Nothing about the acid was labeled. The chemist never tasted it, never guessed. They reacted it — carefully, drop by drop — against a base whose concentration they *did* know, and watched for one color change. That single pink drop carried enough information to pin down the exact concentration of the unknown. How? That is what we are going to figure out today — and you are going to derive the rule yourselves before I ever write it on the board."

**Anticipated student responses:**

- "Why did it suddenly turn pink?" — great; the indicator changes color the instant the acid is used up and the next drop of base makes the solution basic. We'll name that moment in Phase 3.
- "How does knowing the base concentration tell you the acid concentration?" — that is the whole puzzle; you will build the connection at the whiteboards in a few minutes.
- "Why drop by drop at the end?" — because you want to catch the *exact* point where the acid is just neutralized — one drop too many overshoots it.

**Driving question** (post on the board and leave it there):

> *How can a chemist determine the exact concentration of an unknown acid or base using only a known solution, a burette, and a color change?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the demonstration story or the projected curve. Then:

> "Turn to your partner: the base that was added had a *known* concentration. The volumes of acid and base were measured. Why might knowing the concentration of one solution and the volumes of both let you find the concentration of the other? Take a guess — you don't need to be right yet."

Target insight (leave open if no one lands it): neutralization pairs up acid and base in a fixed proportion, so if you know how much base it took and how concentrated that base was, you know how much "acid power" was there to begin with. That proportion becomes M_a V_a = M_b V_b in Phase 3.

---

## Phase 2 · Explore *(10 – 30 min)*

This phase runs as a **Building Thinking Classrooms** block: random groups, vertical non-permanent surfaces, and a thin-slice task that pushes students to derive the neutralization relationship from data *before* any formula is named. See Strategy Spotlight for setup.

### 10–14 min · ABCs Activity — random groups + thin-slice launch at vertical surfaces

**Before any formal vocabulary or formula is introduced**, form random groups of three (card shuffle or digital randomizer) and send each group to a vertical surface (whiteboard, window, or chart paper). One marker per group; it passes between members.

Project this **thin-slice data table** — results from three titrations of *different* acid samples, each neutralized by the **same 0.10 M NaOH**:

| Trial | Acid sample volume (mL) | NaOH (0.10 M) used to neutralize (mL) |
|---|---|---|
| 1 | 25.0 | 25.0 |
| 2 | 25.0 | 50.0 |
| 3 | 25.0 | 12.5 |

**The thin-slice prompt (post it, then step back):**

> "Every trial used the same 0.10 M base and the same 25.0 mL of acid. But the amount of base it took to neutralize was different each time. At your board: (1) Rank the three acid samples from *least concentrated* to *most concentrated*. (2) Explain your ranking. (3) If Trial 1's acid turned out to be 0.10 M, can you figure out the concentration of the Trial 2 and Trial 3 acids? Try."

**Teacher facilitation language (circulate; ask, never tell):**

> "Which acid 'fought back' the longest — needed the most base to neutralize? What does needing more base tell you about how much acid was in there?"

> "Trial 3 only needed half the base of Trial 1. So how does its acid concentration compare to Trial 1's?"

**Anticipated student responses during ABCs:**

- "Trial 2 needed the most base, so it's the strongest acid." — affirm the reasoning; push on the word *strongest* vs. *most concentrated* — we mean more concentrated (more acid per liter). More base needed ⇒ more acid present.
- "Trial 3 took half the base, so it's half as concentrated — 0.05 M." — excellent; that is the proportional relationship emerging. Ask them to write *why* on the board.
- "Trial 2 took twice the base, so it's twice as concentrated — 0.20 M." — exactly the pattern. Have them generalize it.

### 14–24 min · Initial Model — derive the relationship + run the titration

**Part A — Build the rule (at the vertical surface, ~4 min).** Prompt:

> "You just reasoned that doubling the base needed means doubling the acid concentration. Write a single equation at your board that connects: acid concentration, acid volume, base concentration, base volume — so that it works for all three trials. Test your equation on Trial 1, 2, and 3."

Most groups land on a "concentration × volume of acid = concentration × volume of base" structure. Do not correct the symbols yet — let them check it against the table. Trial 2: M_a × 25.0 = 0.10 × 50.0 → M_a = 0.20 M. Trial 3: M_a × 25.0 = 0.10 × 12.5 → M_a = 0.05 M. When the equation reproduces the table, the group has derived M_a V_a = M_b V_b on their own.

**Part B — Run the wet titration (~6 min).** Now move to benches for the hands-on titration. Each group titrates 25.0 mL of an "unknown" HCl with standardized 0.10 M NaOH and two drops of phenolphthalein.

![Brand-styled titration curve titled 'Titration Curve: NaOH added to 25.0 mL HCl'. The x-axis is volume of NaOH added in milliliters from 0 to 50; the y-axis is pH from 0 to 14. A thick purple S-shaped curve starts near pH 1 in the acidic region, stays low until about 20 mL, then rises almost vertically through pH 7 at 25 mL of base, and levels off near pH 13 in the basic region. A horizontal grey line marks pH 7 (neutral). A dashed orange vertical line at 25.0 mL and an orange dot mark the equivalence point, labeled '(25.0 mL, pH 7)'. A light green horizontal band between pH 8.2 and 10 is labeled 'phenolphthalein turns pink', showing where the indicator changes color just past the equivalence point.](figures/titration_curve_naoh_into_hcl.png)

**Teacher facilitation language:**

> "Add base a full milliliter at a time at first. As you near 20 mL, slow down — go drop by drop, swirling after each one. You are hunting for the single drop that makes the pink color stay. The instant one drop tints the whole flask faint pink and it does not fade back, stop and read your burette."

**Anticipated student responses:**

- "It flashed pink then went clear again — did I overshoot?" — no, that is the signal you are *close*; the local pink fades when you swirl because there's still acid left. Keep going drop by drop until it stays. Good catch.
- "We needed about 25 mL — same as Trial 1." — yes; so what does that say about your unknown's concentration? (≈ 0.10 M.) Confirm with M_a V_a = M_b V_b.
- "Our group got 24.6 mL and another got 25.4 mL." — perfect chance to talk precision; both are close to 25.0, both give roughly 0.10 M; small differences come from reading the burette and catching the exact drop.

### 24–30 min · Investigation — calculation practice with M_a V_a = M_b V_b

Back at boards (or seated), groups work a structured practice set. Each student writes the setup individually, then the group compares.

> "For each problem, first label which numbers are the acid (M_a, V_a) and which are the base (M_b, V_b). Then substitute into M_a V_a = M_b V_b and solve for the missing one. Show the substitution."

**Problem 1 (solve for M_a):** 25.0 mL of HCl is neutralized by 25.0 mL of 0.10 M NaOH. Find the acid's molarity.
→ M_a (25.0) = (0.10)(25.0) → M_a = 0.10 M.

**Problem 2 (solve for M_a):** 25.0 mL of HCl is neutralized by 50.0 mL of 0.10 M NaOH. Find the acid's molarity.
→ M_a (25.0) = (0.10)(50.0) → M_a = 0.20 M.

**Problem 3 (solve for V_b):** How many mL of 0.10 M NaOH are needed to neutralize 25.0 mL of 0.05 M HCl?
→ (0.05)(25.0) = (0.10) V_b → V_b = 12.5 mL.

**Teacher facilitation prompts (circulate):**

> "Before you plug in, tell me: in Problem 1, which letter is the unknown? You're solving for M_a, so isolate it — divide both sides by V_a (25.0 mL)."

> "In Problem 3 the unknown is a *volume*, not a concentration. Same equation, just a different letter missing. Set it up the same way and solve for V_b."

**Anticipated student responses:**

- "I got 0.20 M for Problem 2 — that's twice Problem 1." — exactly; twice the base needed means twice the acid concentration. The proportional relationship from the BTC table holds.
- "I divided wrong and got 250 M." — check units and the divide: M_a = (0.10 × 25.0) / 25.0; the volumes cancel to leave 0.10 M, not hundreds.
- "Do the volumes have to be in liters?" — for M_a V_a = M_b V_b the volume units just have to *match* on both sides; mL works as long as both are mL, because the units cancel. (Contrast with mol = M × L, where liters are required.)

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look at the curve and your three calculations. Turn to a partner: there's one special moment in every titration — the instant the acid is *exactly* used up, neither acid nor base in excess. Where is that moment on the curve, and how did the indicator tell you that you'd reached it in the lab?"

Target consensus:

> "It's the steep vertical jump where the pH shoots up through 7. In the lab, the phenolphthalein flips from colorless to permanent pink right at that jump, because the very next drop of base after the acid is gone makes the solution basic. That moment — moles of base equal moles of acid — is what M_a V_a = M_b V_b captures: the two quantities are equal."

> "If your acid needed exactly 25.0 mL of 0.10 M base, what was the acid's concentration — and how do you know without measuring it directly?"

Target: 0.10 M, because M_a (25.0) = (0.10)(25.0) gives M_a = 0.10 M. The equality of moles at that special point is the whole basis of the calculation.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Now let's name what you have already been doing. The whole procedure — slowly adding a solution of *known* concentration from a burette into a measured volume of a solution of *unknown* concentration until a reaction is just complete — is called a **titration**. You ran one in the lab; that is its name."

> "The exact moment you were hunting for — when the moles of added base equal the moles of acid present, so neither is in excess — is the **equivalence point**. On the curve it is the steep vertical jump through pH 7; in your flask it is the single drop that turned the pink permanent. Your indicator's job was to make that invisible moment visible."

> "And the rule you derived at your boards — acid concentration times acid volume equals base concentration times base volume — is the **neutralization equation**, written **M_a V_a = M_b V_b**. It works because at the equivalence point the quantity of H⁺ from the acid exactly equals the quantity of OH⁻ from the base. Notice you derived this from data before I named it — that is the point of working at the boards first."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "Is the equivalence point always at pH 7?" — *Expected response:* For a strong acid neutralized by a strong base, yes — pH 7. (For other combinations it can differ; students don't need that nuance yet. Accept "pH 7 for strong acid + strong base" as full understanding for this lesson.)
- "Why does M_a V_a = M_b V_b let mL stay as mL, when molarity usually needs liters?" — *Expected response:* because the same volume unit appears on both sides and cancels; only the ratio of volumes matters, not their absolute size in liters.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the model + Because/But/So expansion

Students return to their Initial Model (the equation and ranking they wrote at the board). They revise it by labeling each variable with its proper symbol (M_a, V_a, M_b, V_b), marking the equivalence point on the projected curve, and writing one cause→effect statement: *more concentrated acid → more base required to reach the equivalence point.*

Then run a **Because / But / So** sentence. Starter on the board:

> *"Trial 2's acid needed twice as much NaOH as Trial 1's acid to reach the equivalence point, even though both acid samples were 25.0 mL."*

Model one aloud:

> "Trial 2's acid needed twice as much base **because** it contained twice as many moles of H⁺ in the same 25.0 mL — it was more concentrated — **but** the NaOH delivering the OH⁻ was the same 0.10 M in both trials — **so** it took twice the *volume* of that base to supply enough OH⁻ to reach the equivalence point, which is why M_a V_a = M_b V_b gives Trial 2 a concentration of 0.20 M, double Trial 1's 0.10 M."

Then have students write their own B/B/S using one of these starters:

- *"At the equivalence point the phenolphthalein turns permanently pink…"* (hint: moles of base now equal moles of acid)
- *"A more dilute acid reaches its equivalence point after only a small volume of base…"*

**Anticipated student responses:**

- "Because there's less acid, so it doesn't take much base." — good start; push for the So: "so the equivalence point arrives early — at a small V_b — and M_a comes out small when you solve M_a V_a = M_b V_b."
- "Because the moles finally matched." — strong; push for the But/So: "but one more drop would make the base the excess, so you stop exactly there to keep the moles equal."

### 39–40 min · Return to the phenomenon

> "Return to our unlabeled bottle from the start of class. The chemist measured 25.0 mL of the mystery acid and it took 25.0 mL of 0.10 M NaOH to flip the phenolphthalein permanently pink. Using the rule you derived — M_a V_a = M_b V_b — can you now tell me the exact concentration of that mystery acid in one sentence?"

Target: M_a (25.0) = (0.10)(25.0) → M_a = 0.10 M. The unlabeled acid was 0.10 M.

> "No label, no taste, no guess — just a burette, a known base, and one pink drop. That is the power of titration: it turns a color change into an exact number."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud:

> *(a) A 20.0 mL sample of HCl is exactly neutralized by 40.0 mL of 0.25 M NaOH. Set up M_a V_a = M_b V_b and calculate the molarity of the HCl.*
> *(b) Define the equivalence point in one sentence.*
> *(c) In one sentence, explain why a more concentrated acid requires a larger volume of the same base to reach the equivalence point.*

Expected answers are in `Answer_Key.docx`.

**Closing Reflection (SEL, 30 seconds):**

> "Today you derived a chemistry rule from data before anyone told it to you. In one sentence: what is one thing that clicked for you at the whiteboard today, and who — a groupmate or an idea — helped you get there?"

Collect worksheets; note which students correctly isolated the unknown variable versus students who substituted but could not solve algebraically. The "solve for the missing letter" step is the main procedural stumbling block — target those students for a brief one-on-one at the start of the next lesson.

---

## Common Misconceptions

- **Misconception:** "The equivalence point is the same as the moment the indicator changes color." → **Correction:** They are very close but not identical. The *equivalence point* is where moles of base exactly equal moles of acid; the *endpoint* is where the indicator changes color. A well-chosen indicator (phenolphthalein for strong acid + strong base) makes the endpoint arrive within one drop of the equivalence point, which is why we treat them as the same in this lesson — but the distinction is real, and the endpoint is what you actually observe.
- **Misconception:** "You have to convert all volumes to liters before using M_a V_a = M_b V_b." → **Correction:** Because the same volume unit appears on both sides of the equation, the units cancel — mL works fine as long as both volumes are in mL. (Liters *are* required for mol = M × L, which is a different relationship.)
- **Misconception:** "The acid is always the unknown and the base is always known." → **Correction:** Either solution can be the unknown. You titrate an unknown of either kind against a *standard* (known-concentration) solution of the other. M_a V_a = M_b V_b can be solved for whichever variable is missing — acid concentration, base concentration, or either volume.
- **Misconception:** "More color change = more acid; if it turns dark pink, the acid was strong." → **Correction:** The depth of the final color does not measure concentration. The *volume of base required* to reach the endpoint is what measures the acid's concentration. A faint permanent pink and a darker pink both signal you have passed the endpoint; you stop at the first permanent faint pink to avoid overshooting.
- **Misconception:** "pH 7 means the titration is done for every acid and base." → **Correction:** The equivalence point sits at pH 7 only for a strong acid neutralized by a strong base. The *idea* — equal moles of acid and base — is general, but the pH at that point depends on the specific acid and base. For this lesson's HCl + NaOH, pH 7 is correct.

---

## Access & Differentiation

- **ELL/ENL supports:** Sentence frames for the investigation and Exit Ticket: *"The equivalence point is when the moles of ___ equal the moles of ___."* and *"More base was needed because the acid was more ___."* Word-choice box displayed on the board throughout: {titration, burette, indicator, equivalence point, neutralize, phenolphthalein, M_a V_a = M_b V_b}. Pair vocabulary with gestures: two hands meeting palm-to-palm for "equivalence," a slow drip motion for "titrate." Pre-label a copy of the titration curve with the words *acidic*, *neutral*, *basic*, and *equivalence point* so students map language onto the graph.
- **IEP/SPED supports:** Provide a pre-formatted M_a V_a = M_b V_b solving template with the four boxes (M_a, V_a, M_b, V_b) labeled and one box circled as "the one to find," so the algebra step is scaffolded. Assign clear lab roles: one student adds base, one swirls, one reads/records the burette. For the calculation set, pre-fill the known three values so the student practices isolating and solving for the fourth. Calculator use expected for all arithmetic; the conceptual work (labeling acid vs. base, identifying the unknown) is the skill target.
- **Extensions:** (1) Solve for a base concentration: 30.0 mL of an unknown NaOH is neutralized by 24.0 mL of 0.50 M HCl — find M_b. (2) Sketch how the titration curve would shift if the starting acid were *twice* as concentrated (steep jump moves to a larger V_b). (3) Research why phenolphthalein is the right indicator for a strong-acid/strong-base titration but a poor choice for a weak-acid/strong-base titration — connect the indicator's color-change range to where the equivalence point falls on the curve.

---

## Strategy Spotlight

**BTC — Building Thinking Classrooms.** The Building Thinking Classrooms framework (Peter Liljedahl, *Building Thinking Classrooms in Mathematics*, 2021) centers three practices that raise student thinking: (1) **random grouping** removes status hierarchies and friend-group comfort zones; (2) **vertical non-permanent surfaces** (whiteboards, windows, chart paper) make thinking visible, erasable, and collaborative; and (3) **thin-slice problems** launch students into work immediately — before direct instruction — so thinking happens before consolidation.

**How BTC runs in this lesson (Phase 2, minutes 10–30):**

1. **Random groups:** Use a card randomizer, a digital spinner, or the shuffled roster to assign groups of three. Announce: "These are your working groups for the next 18 minutes. Find your vertical surface."
2. **Vertical surfaces:** Each group claims one whiteboard panel, a window section with a dry-erase marker, or chart paper taped at standing height. One marker per group — it passes between members so all three contribute writing and thinking.
3. **Thin-slice prompt:** The three-trial titration table (same base, same acid volume, different volumes required) is designed to be *just* beyond what a student can reason out alone but reachable as a group. Students are *not* given M_a V_a = M_b V_b — they rank the acids by concentration, notice the proportional pattern (twice the base ⇒ twice the concentration), and build the equation themselves. The task forces them to invent the relationship before Phase 3 names it.
4. **Teacher as knowledge-withholder:** While groups work, circulate and ask only questions — never give the formula. Ask: "Which acid needed the most base?" "If Trial 3 took half the base, how does its concentration compare?" "Write one equation that reproduces all three rows." The goal is for students to arrive at M_a V_a = M_b V_b themselves before you formalize it in Phase 3.
5. **Gallery glance (built in):** During the Initial Model step, groups take a quick look at one neighboring board to compare equations before the wet lab — exposing them to a second derivation of the same relationship.

**Why BTC fits titration:** The neutralization relationship is a single proportional pattern that emerges directly from titration data, which makes the three-trial table an ideal thin-slice. Once students build "concentration × volume = concentration × volume" at the board — before seeing M_a V_a = M_b V_b written anywhere — the vocabulary and formula in Phase 3 name something they already understand from the data. Research on BTC (Liljedahl, 2021) shows that students who derive a relationship before seeing it stated retain it more reliably than students who copy it from the board.

**CRSE connection:** The unlabeled-bottle phenomenon connects to real work students may have seen — water-quality testing, pool chemistry, food and beverage labeling, pharmacy compounding — fields where knowing an exact concentration protects health and safety in their own communities. The random grouping is itself a CRSE move: it disrupts the social sorting that concentrates academic authority in a few students, signaling that every student's thinking belongs on the board.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — unlabeled acid bottle; projected titration curve `titration_curve_naoh_into_hcl.png`; return in Phase 4 to solve the mystery acid's concentration |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — why do known concentration + two volumes give the unknown?); Phase 3 (TT#2 — where is the equivalence point on the curve and how did the indicator show it?) |
| 3 | Students develop questions/models/procedures | Phase 2 BTC thin-slice (rank acids by concentration, derive the equation at vertical surfaces); run the wet titration; calculation practice solving for any variable |
| 4 | CCC defined and used | Lesson Overview · *Scale, Proportion, and Quantity*; explicit in Phase 3 consensus (equal moles at equivalence) and Phase 4 B/B/S (more concentrated acid ⇒ more base) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: titration / equivalence point / neutralization equation (M_a V_a = M_b V_b) |
| 6 | Revisit phenomenon with evidence | Phase 4 — students return to the unlabeled-bottle story and calculate its 0.10 M concentration using the rule they derived and their lab data |
| 7 | ENL/SPED supports | Access & Differentiation block: sentence frames, word-choice box, gestures, pre-labeled curve, solving template, pre-filled-three-values practice, lab roles, calculator |
| 8 | Assessment check | Phase 5 — Exit Ticket (solve M_a V_a = M_b V_b for HCl molarity with distinct values; define equivalence point; explain concentration–volume proportionality) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked titration calculation
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **titration** — a laboratory procedure in which a solution of known concentration is added in measured amounts (usually from a burette) to a measured volume of a solution of unknown concentration until the reaction between them is just complete, allowing the unknown concentration to be calculated
- **equivalence point** — the point in a titration at which the moles of added base exactly equal the moles of acid present, so neither is in excess; on a strong-acid/strong-base titration curve it is the steep vertical jump through pH 7, made visible in the lab by the indicator's color change
- **neutralization equation (M_a V_a = M_b V_b)** — the relationship used to find an unknown concentration in an acid–base titration; because the moles of acid equal the moles of base at the equivalence point, the product of acid molarity and acid volume equals the product of base molarity and base volume (valid for a strong monoprotic acid and a strong base, with volumes in matching units)
