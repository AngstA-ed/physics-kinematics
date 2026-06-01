# Writing Formulas from Names — Teacher Guide

## Cover

**Unit: Chemical Bonding — Lesson 03: Writing Formulas from Names**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: BTC

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

No standalone content performance expectation is tagged for this lesson — it is a skill-building bridge inside the Chemical Bonding unit. It operationalizes **HS-PS1-2** (constructing explanations for chemical outcomes from the periodic table and patterns of chemical properties) by giving students the procedural tool that turns an ionic *name* into the exact *formula* — the lowest whole-number ratio of ions that makes a compound electrically neutral. The Cross-Cutting Concept in focus is **Scale, Proportion, and Quantity**: a chemical formula is not a label, it is a *ratio statement*. The subscripts encode the precise proportion of atoms required for the positive and negative charges to cancel. Per East Meadow guidance, formula-writing fluency is prerequisite to every later quantitative unit — gram formula mass, mole ratios, balancing equations, and stoichiometry all assume the student can write a correct formula from a name.

### Phenomenon

Hold up two index cards. One reads **"aluminum oxide"** and the other reads **"Al₂O₃."** Tell students these are the *same substance* — the white grit in sandpaper and the protective coat on an aluminum window frame. Then ask the hook question: how did chemists know it had to be exactly **two** aluminums and **three** oxygens — not Al₃O₂, not AlO, not Al₅O₇? The name doesn't say "two" or "three" anywhere. Yet every chemist on Earth writes the identical subscripts. There is a hidden rule that converts the *name* into an *exact ratio of atoms*. The same move works for table salt (NaCl, ratio 1:1) and for the calcium chloride that melts ice on the roads (CaCl₂, ratio 1:2). One procedure, every ionic compound. The phenomenon is the surprising determinism: the formula is not a guess or a convention to memorize — it is forced by the charges on the ions.

### Javalab / Labs

- **Formula-writing dominoes:** Print a deck of cation cards (Na⁺, Ca²⁺, Al³⁺, NH₄⁺, K⁺, Mg²⁺, Fe³⁺) and anion cards (Cl⁻, O²⁻, S²⁻, OH⁻, NO₃⁻, SO₄²⁻, PO₄³⁻). Each "domino" is a cation matched to an anion; the group writes the neutral formula on a vertical surface and only "plays" the next domino once the formula is verified by another group. This is the core BTC task — see Phase 2.
- **Polyatomic ion practice:** Students keep the 2025 NYS Reference Tables open to the polyatomic-ion table (Table E). They build formulas that require parentheses — Ca(NO₃)₂, Al₂(SO₄)₃, (NH₄)₃PO₄ — and articulate *why* the parentheses are needed (the subscript multiplies the whole ion, not one atom).
- **Crossing-charges reference:** `figures/crossing_charges.png` projected on the screen as the worked anchor for the cross-and-reduce procedure.

### Assessments

- **Formula-writing quiz** (district checkpoint, following lesson; see `Assessments/` folder once created): students write formulas from names spanning 1:1, 1:2, 2:3 ratios and at least two polyatomic cases, showing the crossed charges.
- **Exit Ticket** (Phase 5): three items — write the formula for magnesium chloride, write the formula for aluminum sulfate (polyatomic, requires parentheses), and a one-sentence explanation of why the subscripts in a formula are not arbitrary. The Exit Ticket names are deliberately *different* from the worksheet practice. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | HS-PS1-2 (formula as the ratio of ions that produces a neutral compound) — skill bridge; no standalone content PE |
| **CCC focus** | Scale, Proportion, and Quantity — a formula's subscripts state the exact ratio of ions needed to make total positive charge equal total negative charge; the ratio, not the count of element types, is what the name encodes |
| **Strategy chips** | BTC — Building Thinking Classrooms (visibly random groups, vertical non-permanent surfaces, thin-slice task launched with minimal instructions) |
| **Materials** | 2025 NYS Chemistry Reference Tables (Table E — polyatomic ions; Periodic Table for common charges), vertical whiteboards/windows + markers, formula-writing domino deck (cation/anion cards), `figures/crossing_charges.png` projected, two index cards ("aluminum oxide" / "Al₂O₃") |
| **Safety** | No chemicals handled. Standard classroom routines. If marker fumes are a concern in a small room, ensure ventilation. |
| **Prior knowledge** | Lesson 01 (Naming Compounds) — students can read an ionic name and identify the cation and anion. Lesson 02 (Identifying Bond Type) — students can predict ionic vs. covalent. Students must know how to read an ion's charge (from the Periodic Table group for main-group ions; from Table E for polyatomic ions). |

**Lesson objectives — students can:**

- Determine the charge of a cation and an anion from the Periodic Table (main-group ions) or the polyatomic-ion reference table.
- Write the correct neutral formula for an ionic compound by crossing the charges to set subscripts, then reducing to the lowest whole-number ratio.
- Use parentheses correctly when a polyatomic ion takes a subscript greater than one.
- Explain, using Scale, Proportion, and Quantity, why a chemical formula states an exact ratio of atoms and why the subscripts are not arbitrary.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers: *"Name one thing in your life that has to be in an exact ratio or it doesn't work — a recipe, a music beat, a game's odds. What goes wrong if the ratio is off?"* One round, one sentence each, pass allowed. This surfaces the everyday intuition that ratios are not decorative — they are load-bearing. A formula's subscripts are exactly that kind of ratio.

Then post the **Do Now**:

> *"Aluminum oxide is the same substance as Al₂O₃ — it's in sandpaper and in the coating on aluminum. Nowhere in the name 'aluminum oxide' does it say 'two' or 'three.' Write one sentence: how do you think chemists decided it had to be exactly 2 aluminums and 3 oxygens?"*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "Maybe they just measured it in a lab." — affirm; that is one historical route. Probe: but every chemist writes the *same* subscripts without re-measuring. Is there a rule that forces it?
- "It has something to do with the charges." — excellent; capture it. We will turn that hunch into a procedure today.
- "I think you just memorize it." — validate the honesty; then push: there are millions of ionic compounds — memorizing each formula is impossible. There must be a *method* that generates the right answer every time.

### 3–8 min · Phenomenon hook — same substance, two index cards

**Teacher actions.** Hold up the two index cards: "aluminum oxide" and "Al₂O₃." State plainly: same stuff, two ways of writing it. Then put a third card on the board with three *wrong* formulas — AlO, Al₃O₂, Al₅O₇ — and ask why none of these is the one chemists use.

**Sample teacher language:**

> "Here's the puzzle. The name 'aluminum oxide' gives you two ingredients — aluminum and oxygen — but it never tells you the recipe proportions. So why is it always Al₂O₃ and never AlO or Al₃O₂? Somewhere, hidden inside the ions, is a rule that *forces* the ratio. By the end of class you'll be able to take any ionic name and produce the exact formula — and prove why it has to be that one."

**Anticipated student responses:**

- "Because the charges have to cancel out?" — capture this; it is the heart of the rule. We will name it precisely in Phase 3.
- "Aluminum is 3-something and oxygen is 2-something, so they switch?" — that student has reinvented crossing charges. Affirm, hold it, and let the group discover it formally in Phase 2.
- "Why can't it just be AlO with one of each?" — great question; AlO would leave +3 and −2 unbalanced (net +1). It would not be a neutral compound. Hold that for the Explore.

**Driving question** (post on the board and leave it there):

> *How does a chemical formula tell us the exact ratio of atoms?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the cards or the wrong formulas. Then:

> "Turn to your partner: salt is NaCl — one sodium, one chlorine, a 1-to-1 ratio. But aluminum oxide is 2-to-3. What might be different about the *ions* in these two compounds that changes the ratio?"

Target insight (leave open if no one lands it): the *charges* differ. Na is +1 and Cl is −1, so one of each balances. Al is +3 and O is −2, so it takes a different count of each to make the charges cancel. The ratio is set by the charges — and we'll formalize that as **crossing charges** in Phase 3.

---

## Phase 2 · Explore *(10 – 30 min)*

This is the BTC core. Activity comes **before** the vocabulary: students discover the cross-and-reduce procedure on vertical surfaces before any term is named. See Strategy Spotlight for setup.

### 10–13 min · Form visibly random groups + launch the thin-slice task

Form **visibly random groups of three** in front of the class (deal cards or run the on-screen randomizer). Each group gets one marker and one **vertical non-permanent surface** (whiteboard, window, or chart paper).

**Launch the task in one sentence — resist defining the method first:**

> "Each card pair gives you a positive ion and a negative ion. Your job: write a formula where the total positive charge exactly cancels the total negative charge — and use the *fewest* atoms that works. Start with the easy ones."

Hand each group the first three domino pairs (thin-slice — start easy, charges already labeled):

1. **Na⁺ and Cl⁻** (1:1)
2. **Mg²⁺ and Cl⁻** (1:2)
3. **Ca²⁺ and O²⁻** (reduces to 1:1)

### 13–22 min · Investigation Part 1 — discover cross-and-reduce on the boards

Groups work the pairs on their vertical surface. The teacher circulates and **asks, never tells.**

**Teacher facilitation language (circulate):**

> "Na⁺ and Cl⁻ — how many of each makes the charges cancel? Show me the running total: +1 and −1. Net zero. So the formula is…?"

> "Mg²⁺ and Cl⁻ — one chlorine only cancels +1 of magnesium's +2. How many chlorines do you need to cancel all of the +2? What does that do to the formula?"

> "Ca²⁺ and O²⁻ — try one of each: +2 and −2, that cancels. But notice you *could* have written Ca₂O₂ by crossing the charges. Which is fewer atoms? Which one do chemists use?"

**Anticipated student responses during Part 1:**

- "For MgCl₂ I need two chlorines because each Cl is only −1." — exactly the target reasoning; have them write the subscript and check the charge total (+2 and 2×−1 = −2).
- "Ca₂O₂ balances too — is that wrong?" — it balances, but it is not the *lowest* ratio. CaO already balances with fewer atoms. This is the **reduce** step — name it for them later; for now ask "can you make it smaller and still cancel?"
- "How do I know Mg is +2?" — redirect to the Periodic Table: Group 2 main-group metals form +2 ions. Group 1 → +1, Group 13 → +3; the common nonmetal anions: Group 17 → −1, Group 16 → −2.

### 22–30 min · Investigation Part 2 — harder dominoes + polyatomic ions

Once a group has the first three correct (verified by a neighboring group), release the next set. These force the *crossing* move and introduce polyatomic ions with parentheses.

4. **Al³⁺ and O²⁻** → cross to Al₂O₃ (2:3, already lowest)
5. **Na⁺ and SO₄²⁻** → Na₂SO₄ (the polyatomic ion stays intact)
6. **Ca²⁺ and NO₃⁻** → Ca(NO₃)₂ (**parentheses** — subscript multiplies the whole ion)
7. **Al³⁺ and SO₄²⁻** → Al₂(SO₄)₃ (cross *and* parentheses)

Project `figures/crossing_charges.png` now as a shared reference once at least one group has reached pair 4:

![Two-panel brand-styled diagram. Left panel 'Step 1 - Cross the charges' shows an Al box labeled 3+ and an O box labeled 2 minus, with dashed crossing arrows carrying the 3 down to become oxygen's subscript and the 2 down to become aluminum's subscript, producing Al2O3 with the ratio 2 Al to 3 O. Right panel 'Step 2 - Reduce the subscripts' shows a Ca box labeled 2+ and an O box labeled 2 minus crossing to Ca2O2, then dividing by 2 to give the reduced formula CaO at the lowest whole-number ratio 1 to 1.](figures/crossing_charges.png)

**Teacher facilitation language (circulate):**

> "Al³⁺ and O²⁻ — try crossing: the 3 becomes oxygen's subscript, the 2 becomes aluminum's subscript. You get Al₂O₃. Now check: total positive is 2 × (+3) = +6; total negative is 3 × (−2) = −6. They cancel. Can you reduce 2 and 3 to anything smaller? No — they share no common factor. So Al₂O₃ is final."

> "Ca and NO₃ — the nitrate ion is one *unit* with a −1 charge. You need two of them to cancel calcium's +2. But if you write CaNO₃₂ that's wrong — it looks like 32 oxygens. How do you show 'two whole nitrate ions'? Wrap it in parentheses: Ca(NO₃)₂."

**Anticipated student responses during Part 2:**

- "Al₂(SO₄)₃ — why three sulfates?" — cross the charges: Al is +3, sulfate is −2; crossing gives 2 Al and 3 sulfate. Check: 2 × (+3) = +6 and 3 × (−2) = −6. Balanced.
- "Do I reduce Al₂(SO₄)₃? 2 and 3 don't reduce." — correct, they share no common factor, so it stays.
- "Why parentheses for nitrate but not for sulfate in Na₂SO₄?" — because in Na₂SO₄ the sulfate has a subscript of 1 (only one sulfate). You only need parentheses when a polyatomic ion takes a subscript *greater than 1*.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

Bring groups back facing their boards. Ask the class to look across all their formulas.

> "Turn to your partner: NaCl, MgCl₂, Al₂O₃, Ca(NO₃)₂. What is the *one rule* every single one of these obeys? What number do the positives and negatives always add up to?"

Target consensus:

> "Every formula is built so the total positive charge and total negative charge cancel to zero. The compound is electrically neutral. The subscripts are whatever it takes to make the charges balance — and we use the smallest whole numbers that do it."

Then sharpen:

> "Look at how you got those subscripts. For Al₂O₃ you took aluminum's 3 and made it oxygen's subscript, and oxygen's 2 and made it aluminum's subscript. You *crossed* the charges. Then for CaO you crossed to Ca₂O₂ and *reduced*. Those are the two moves of the whole method."

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name the three things you've been doing all period. First, the trick where you take each ion's charge number and write it as the *other* ion's subscript — that is **crossing charges**. The charge on the cation becomes the subscript on the anion, and the charge on the anion becomes the subscript on the cation. Second, when both subscripts share a common factor — like the 2 and 2 in Ca₂O₂ — you divide both down to the smallest whole numbers. That is **reducing subscripts**; the formula must always be the lowest whole-number ratio. Third, some ions are not single atoms — nitrate NO₃⁻, sulfate SO₄²⁻ — these are **polyatomic ions**: a group of atoms that carries one overall charge and stays together as a unit. When a polyatomic ion needs a subscript bigger than one, you wrap it in parentheses so the subscript multiplies the whole group."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "Why do we cross the charges instead of just adding them?" — *Expected response:* crossing makes the total positive charge (cation charge × its subscript) automatically equal the total negative charge (anion charge × its subscript), because each subscript came from the *other* ion's charge. The cross guarantees the magnitudes match.
- "When do you actually need parentheses?" — *Expected response:* only when a polyatomic ion takes a subscript greater than 1 — like Ca(NO₃)₂ or Al₂(SO₄)₃. If the polyatomic subscript is 1, no parentheses (Na₂SO₄).

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the boards + Because/But/So expansion

Groups return to their vertical surfaces and revise: (a) circle any formula that needed a **reduce** step and write the unreduced version next to it (CaO ← Ca₂O₂); (b) box every **polyatomic** ion and check the parentheses. Because the surfaces are non-permanent and public, this relabeling is a low-stakes edit, not a crossed-out mess.

Then run a **Because/But/So** sentence. Starter on the board:

> *"A student writes the formula for calcium chloride as CaCl instead of CaCl₂."*

Model one aloud:

> "Writing CaCl is wrong **because** calcium is +2 and one chloride is only −1, so the charges do not cancel — there is a leftover +1 — **but** adding a second chloride contributes another −1, bringing the negative total to −2 — **so** the neutral formula must be CaCl₂, the lowest ratio in which calcium's +2 is exactly balanced by 2 × (−1)."

Then have students write their own B/B/S for **aluminum oxide** (why Al₂O₃ and not AlO).

**Anticipated student responses:**

- "Because Al is +3 and O is −2, but one of each leaves +1 left over, so you need 2 Al and 3 O to reach +6 and −6." — exactly; that is the full reasoning chain.
- "Because the charges cross." — good start; push for the *why*: "because crossing makes the total positive (2 × +3) equal the total negative (3 × −2)."

### 39–40 min · Return to the phenomenon

> "Back to our two index cards. 'Aluminum oxide' and 'Al₂O₃.' You now know the hidden rule. In one sentence, using the word *charge*, explain why it has to be exactly two aluminums and three oxygens — not AlO, not Al₃O₂."

Target: "It must be Al₂O₃ because that is the lowest whole-number ratio in which the total positive charge (2 × +3 = +6) exactly cancels the total negative charge (3 × −2 = −6), making the compound neutral."

> "The name didn't tell you the numbers — but the *charges* did. The formula isn't a label you memorize; it's the only ratio the charges allow."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud (these compounds are **new** — not the worksheet practice):

> *(a) Write the correct formula for magnesium chloride. Show the crossed charges.*
> *(b) Write the correct formula for aluminum sulfate. (Hint: sulfate is a polyatomic ion, SO₄²⁻.) Show the crossed charges and use parentheses if needed.*
> *(c) In one sentence, explain why the subscripts in a chemical formula are not arbitrary — what do they guarantee?*

Expected answers are in `Answer_Key.docx`.

**Closing Reflection (SEL, 30 seconds):**

> "Today a name turned into an exact recipe of atoms by following one rule. In one sentence: what is one thing that finally clicked for you about formulas, and who — a partner or an idea on someone's board — helped it click?"

Collect worksheets; note which students cross the charges correctly but forget to **reduce** (e.g., leaving Ca₂O₂), and which forget **parentheses** on a polyatomic subscript > 1. These two are the dominant procedural errors — target those students at the start of the next lesson.

---

## Common Misconceptions

- **Misconception:** "The subscripts in a formula are just a convention you memorize." → **Correction:** Subscripts are forced by the ion charges. They are the lowest whole-number ratio in which total positive charge equals total negative charge. Al₂O₃ is not a memorized fact — it is the *only* neutral ratio of Al³⁺ and O²⁻. Change the charges and the ratio changes.
- **Misconception:** "Crossing charges always gives the final answer." → **Correction:** Crossing gives a balanced formula, but not always the *lowest* one. Ca²⁺ and O²⁻ cross to Ca₂O₂, which must be reduced to CaO. Always check whether both subscripts share a common factor and divide it out.
- **Misconception:** "A subscript after a polyatomic ion only multiplies the nearest atom." → **Correction:** Parentheses make the subscript multiply the *entire* ion. Ca(NO₃)₂ means two whole nitrate ions: 2 N and 6 O, plus 1 Ca. Writing CaNO₃₂ (no parentheses) would wrongly read as 32 oxygens.
- **Misconception:** "You write the subscript equal to the ion's own charge." → **Correction:** You cross the charges — each subscript comes from the *other* ion's charge. Al³⁺ gives oxygen the subscript 3; O²⁻ gives aluminum the subscript 2. Using an ion's own charge as its own subscript produces wrong formulas.
- **Misconception:** "Every compound needs parentheses around the negative part." → **Correction:** Parentheses are needed only when a polyatomic ion takes a subscript greater than 1. NaCl, MgCl₂, and Na₂SO₄ need none; Ca(NO₃)₂ and Al₂(SO₄)₃ do.

---

## Access & Differentiation

- **ELL/ENL supports:** Charge-and-cross template pre-printed with two labeled boxes (CATION + charge | ANION − charge) and a crossing arrow, plus the sentence frame: *"The formula for ___ is ___ because the charges ___ to make the compound ___ (neutral)."* Word-choice box displayed throughout: {cross, charge, subscript, reduce, polyatomic, neutral, ratio, parentheses}. Pair each move with a gesture: hands crossing for "cross the charges," palms pressing together for "reduce." Allow a bilingual dictionary for the circle and reflection prompts; ask students to record formulas in standard notation.
- **IEP/SPED supports:** Provide a reference card listing the common ion charges used in the lesson (Na⁺, K⁺, Mg²⁺, Ca²⁺, Al³⁺, Cl⁻, O²⁻, S²⁻ and polyatomics NO₃⁻, SO₄²⁻, OH⁻, NH₄⁺) so the charge lookup is removed as a barrier and the student focuses on the cross-and-reduce procedure. Use the vertical-surface BTC structure with assigned partner roles: one student reads charges, one writes the formula, one checks the charge total. Offer a graphic organizer that walks one formula per box, one step per row.
- **Extensions:** (1) Write formulas for compounds with a **transition metal** that has a Roman-numeral charge: iron(III) oxide, copper(II) nitrate — the charge is given in the name. (2) Build the formula for ammonium phosphate, (NH₄)₃PO₄, which needs parentheses on the *cation*, and explain why. (3) Given an unknown formula like X₂O₃, deduce the charge on element X and justify it from the crossing rule.

---

## Strategy Spotlight

**BTC — Building Thinking Classrooms (Peter Liljedahl).** BTC restructures the room so that *students*, not the teacher, do the thinking. Three core practices anchor this lesson: **visibly random groups** (formed in front of the class so students trust the process and mix with everyone), **vertical non-permanent surfaces** (whiteboards, windows, or chart paper — vertical and erasable, which lowers the stakes of being wrong and makes thinking public), and **a thin-slice task launched with minimal instructions** (the teacher poses the problem in one sentence, releases easy cases first, and asks questions instead of demonstrating the method).

**How to run it in this lesson (Phase 2):**

1. Form visibly random groups of three (deal cards / randomizer on screen). Each group gets one marker and one vertical surface.
2. Launch the dominoes task verbally in one sentence: *"Write a formula where the positive and negative charges exactly cancel, using the fewest atoms."* Resist defining "crossing charges" first — the whole point is that students build the procedure from the balancing requirement.
3. Release the cards in **thin slices**: easy 1:1 and 1:2 pairs first, then the crossing cases (Al₂O₃), then the polyatomic cases that force parentheses. A group only gets the next slice once a *neighboring* group verifies their current formulas.
4. Circulate and ask, never tell: *"What's the charge total?" "Can you make it smaller and still cancel?" "How do you show two whole nitrate ions?"* When a group is stuck, give a hint that keeps the thinking with them.
5. Use the vertical surfaces as the class's shared thinking record in Phase 3 — groups literally point to the crossing arrows and reduce steps they wrote as the formal terms emerge.

Because the surfaces are non-permanent and public, students revise freely in Phase 4 — adding the unreduced Ca₂O₂ next to CaO, or boxing a polyatomic ion, is a low-stakes edit on a board rather than a crossed-out mess on private paper. Research on BTC (Liljedahl, *Building Thinking Classrooms in Mathematics*, and its cross-disciplinary extensions) finds that random groups + vertical surfaces sharply increase the proportion of students actively reasoning rather than copying.

**Connection to Hochman literacy:** the Because/But/So sentence in Phase 4 captures the exact reasoning students just made visible on the board — a *cause* (calcium is +2 and one chloride is only −1), a *contrast* (but a second chloride adds another −1), and a *consequence* (so the neutral formula is CaCl₂). The vertical-surface argument becomes the sentence.

**RESTORATIVE CIRCLE (unit-window opener).** The opening circle prompt — *a thing in your life that has to be in an exact ratio or it breaks* — primes the proportion intuition at the heart of formula-writing, while giving every student a voice in the first three minutes. It is not graded; one sentence each, pass allowed.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — "aluminum oxide" vs. "Al₂O₃" index cards (sandpaper / window coating); return in Phase 4 to explain why exactly 2 Al : 3 O |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — why is NaCl 1:1 but aluminum oxide 2:3?); Phase 3 (TT#2 — what one rule does every formula obey?) |
| 3 | Students develop questions/models/procedures | Phase 2 BTC dominoes on vertical surfaces — students discover cross-and-reduce before it is named; Phase 4 board revision (mark reduce steps and polyatomic parentheses) |
| 4 | CCC defined and used | Lesson Overview · *Scale, Proportion, and Quantity*; explicit in Phase 3 (subscripts = ratio that neutralizes charge) and Phase 4 (B/B/S CaCl₂ / Al₂O₃) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: crossing charges / reducing subscripts / polyatomic ion |
| 6 | Revisit phenomenon with evidence | Phase 4 — students return to the index cards and explain Al₂O₃ using the charge totals (+6 / −6) they verified on their boards |
| 7 | ENL/SPED supports | Access & Differentiation block: charge-and-cross template, sentence frame, word-choice box, ion-charge reference card, partner roles, one-step-per-row organizer |
| 8 | Assessment check | Phase 5 — Exit Ticket (magnesium chloride; aluminum sulfate with parentheses; sentence on why subscripts are not arbitrary) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked crossing-charges example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **crossing charges** — the procedure for writing an ionic formula in which each ion's charge number becomes the subscript of the *other* ion; this makes the total positive charge equal the total negative charge so the compound is neutral (e.g., Al³⁺ + O²⁻ → Al₂O₃)
- **reducing subscripts** — dividing both subscripts in a formula by their greatest common factor to express the compound as the lowest whole-number ratio of ions (e.g., Ca₂O₂ reduces to CaO)
- **polyatomic ion** — a group of atoms bonded together that carries a single overall electric charge and acts as one unit in a formula (e.g., nitrate NO₃⁻, sulfate SO₄²⁻); when its subscript is greater than 1 it is enclosed in parentheses, as in Ca(NO₃)₂
