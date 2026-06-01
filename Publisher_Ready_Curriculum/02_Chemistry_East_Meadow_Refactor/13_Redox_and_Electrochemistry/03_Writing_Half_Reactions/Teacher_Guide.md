# Writing Half-Reactions — Teacher Guide

## Cover

**Unit: Redox & Electrochemistry — Lesson 03: Writing Half-Reactions**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: BTC

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

**HS-PS1-2 / PS1-12 (electron-transfer evidence)** — *"Evidence could include half-reactions, net ionic equations, and electrochemical cells to illustrate the mechanism of electron transfer."* In the previous two lessons students assigned oxidation numbers (Lesson 01) and used the change in oxidation number to label which species was oxidized and which was reduced (Lesson 02). This lesson turns that labeling into a written record: students split a single redox reaction into two **half-reactions** — one showing the species that loses electrons, one showing the species that gains them — and balance the electrons between them so that *every electron lost is accounted for as an electron gained*. The half-reaction is the unit of evidence the standard names: it is how a chemist writes down, in symbols, exactly how many electrons move and in which direction.

The Cross-Cutting Concept of **Energy and Matter — flows, cycles, and conservation** is the explicit lens: electrons are matter, and they are conserved. They are not created or destroyed in a redox reaction; they are *transferred* from one species to another. Half-reaction bookkeeping is conservation of charge made visible — the electrons that leave the oxidation half-reaction are the same electrons that arrive in the reduction half-reaction.

### Phenomenon

You cannot see an electron. So how does a chemist *prove* electrons are moving during a reaction? Drop a strip of zinc metal into a clear blue copper(II) sulfate solution and nothing dramatic seems to happen at first — but leave it a few minutes and the zinc darkens with a fuzzy reddish coating of copper metal, and the blue color of the solution fades. Something was transferred. Now build the same reaction as a cell: put the zinc in one beaker, a copper strip in another, connect them with a wire and a salt bridge, and clip a voltmeter into the wire. The needle jumps. The reaction is now pushing a measurable current through the wire — a current that *is* the electron flow, made visible by the meter. Same chemistry, two setups: one hides the electrons inside the beaker, the other routes them through a wire where an instrument can read them. The driving question of the lesson is how we write down — on paper, in two tidy equations — exactly what that needle is detecting.

### Javalab / Labs

- **Single-replacement "electron transfer" observation:** Place a clean strip of zinc (or an iron nail) into copper(II) sulfate solution; students observe the copper coating form and the blue color fade over 5–10 minutes. No external URL required; this is a standard stockroom demo. Students record before/after observations and connect them to the two half-reactions.
- **Electrochemical-cell build (optional, if cell hardware is available):** Zn|Zn²⁺ ‖ Cu²⁺|Cu cell with a salt bridge and a voltmeter, matching `figures/electrochemical_cell.png`. Students watch the voltmeter respond and label the anode (oxidation) and cathode (reduction). For a digital option, a Javalab "voltaic cell" or PhET-style electrochemistry simulation can stand in when wet-lab hardware is unavailable.
- **Half-reaction balancing practice (the core skill):** Students split a set of single-replacement reactions into oxidation and reduction half-reactions and balance the electrons using the structured board work in Phase 2.

### Assessments

- **Half-reaction balancing quiz** (district checkpoint, following lesson): students are given several single-replacement and ion-transfer reactions and must write the two balanced half-reactions and confirm the electrons lost equal the electrons gained.
- **Exit Ticket** (Phase 5): two items — write the balanced oxidation and reduction half-reactions for Ca + 2Ag⁺ → Ca²⁺ + 2Ag (equal electrons, no scaling needed), then balance the electrons for the Al / Ni²⁺ reaction (least-common-multiple scaling required). See `Answer_Key.docx`. These reactions are deliberately different from the worksheet practice set.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | HS-PS1-2 / PS1-12 — half-reactions and net ionic equations as evidence of electron transfer |
| **CCC focus** | Energy and Matter (conservation) — electrons are conserved; the count lost in oxidation equals the count gained in reduction. Balancing half-reactions *is* conservation of charge. |
| **Strategy chips** | BTC — Building Thinking Classrooms: random groups at vertical surfaces split and balance half-reactions before the method is named |
| **Materials** | Zinc strip (or iron nail), copper(II) sulfate solution, copper strip; cell hardware + salt bridge + voltmeter (optional); whiteboards / vertical surfaces and markers (one per group); 2025 NYS Chemistry Reference Tables (Table J — activity series; Table E — common ions); `figures/electrochemical_cell.png` and `figures/splitting_half_reactions.png` projected |
| **Safety** | Copper(II) sulfate solution is an irritant — goggles and gloves; do not ingest; wash hands after. The metal strips have sharp edges. Standard lab safety applies. No open flame. |
| **Prior knowledge** | Lesson 01 (Assigning Oxidation Numbers) — students can assign oxidation numbers to elements and monatomic ions; Lesson 02 (Identifying Reduction and Oxidation) — students can use the change in oxidation number to label which species is oxidized (loses electrons, number increases) and which is reduced (gains electrons, number decreases). Students should recognize a single-replacement reaction and read the Table J activity series. |

**Lesson objectives — students can:**

- Split a single redox reaction into an oxidation half-reaction and a reduction half-reaction, each showing the electrons (e⁻) explicitly.
- Write each half-reaction so that atoms balance and charge balances, placing electrons on the correct side (products for oxidation, reactants for reduction).
- Balance the electrons between the two half-reactions by multiplying each by a whole number so the electrons lost equal the electrons gained (using the least common multiple when the numbers differ).
- Explain, using Energy and Matter / conservation, why the electrons lost in oxidation must equal the electrons gained in reduction, and connect that count to the current a voltmeter reads in a cell.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers: *"Name a time you knew something was happening even though you couldn't see it directly — and how you knew. (Wind moving leaves, a phone buzzing in another room, the smell of food cooking.)"* One round, one sentence each, no judgment. This primes the central idea: we detect invisible electron flow by its effects, not by seeing the electrons themselves.

Then post the **Do Now**:

> *"A clean strip of zinc metal is dropped into a clear blue copper(II) sulfate solution. After a few minutes, the zinc is coated with reddish copper metal and the blue color has faded. In one sentence: what do you think moved from one substance to the other, and how would you prove it?"*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "The copper came out of the solution and stuck to the zinc." — affirm the observation; ask *why* — what did the copper ion need in order to become copper metal?
- "Electrons moved from the zinc to the copper." — exactly the target idea; push: how could you *prove* electrons moved if you can't see them?
- "I'm not sure — the colors just changed." — validate the observation; the color change *is* the evidence, and today we'll learn to write down what it means.

### 3–8 min · Phenomenon hook — making electron flow visible

**Teacher actions.** Show (or recall) the zinc-in-copper-sulfate demo. Then introduce the cell version. Project `figures/electrochemical_cell.png`:

![Diagram of a zinc–copper electrochemical cell: a zinc electrode in a beaker of zinc(II)-ion solution on the left and a copper electrode in a beaker of copper(II)-ion solution on the right, connected by a salt bridge between the two solutions and by an external wire carrying a voltmeter; blue arrows along the wire show electron flow moving from the zinc anode to the copper cathode; the zinc side is labeled ANODE (oxidation) with the half-reaction Zn to Zn 2 plus plus 2 electrons, and the copper side is labeled CATHODE (reduction) with the half-reaction Cu 2 plus plus 2 electrons to Cu.](figures/electrochemical_cell.png)

**Sample teacher language:**

> "In the beaker, the electrons jumped straight from the zinc to the copper ions — invisible, hidden inside the liquid. But watch what happens when we separate the two metals into two beakers and force the electrons to travel through a wire to get from one to the other. The voltmeter needle moves. That moving needle is reading the electrons flowing through the wire. We just made the invisible visible. The electrons leave the zinc, travel through the wire, and arrive at the copper ions. Today our job is to write that down — in symbols — so anyone can see exactly how many electrons moved and which direction."

**Anticipated student responses:**

- "So the wire is like a path for the electrons?" — yes; the salt bridge and wire together let us route the electrons where we can measure them.
- "Why does the zinc lose the electrons and not the copper?" — great question; that's the Table J activity series at work — we labeled it in Lesson 02, and today we'll record it as two half-reactions.
- "What is the voltmeter actually measuring?" — the push behind the electron flow; the needle moving is your proof that electrons are on the move.

**Driving question** (post on the board and leave it there):

> *How can we "see" the invisible flow of electrons — and write it down — in a chemical reaction?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the cell diagram or the demo. Then:

> "Turn to your partner: in the diagram, the zinc strip is slowly disappearing and the copper strip is slowly growing. Where are the electrons coming from, and where are they going? Try to name the *direction* of the flow."

Target insight (leave open if no one lands it yet): electrons leave the zinc (it loses them) and arrive at the copper ions (they gain them). One species gives; one species takes. That giving and taking is what we will write as two separate half-reactions in Phase 3.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–14 min · BTC launch — random groups to vertical surfaces

**Form random groups of three** (card randomizer or digital spinner — see Strategy Spotlight). Send each group to a **vertical non-permanent surface** (whiteboard, window, or chart paper at standing height) with **one marker** that passes between members. Announce: *"These are your thinking groups for the next 16 minutes. No method has been given yet — you're going to invent the bookkeeping yourselves."*

Project `figures/splitting_half_reactions.png` as the only scaffold:

![Flow diagram showing one full net ionic equation, Zn(s) plus Cu 2 plus (aq) yields Zn 2 plus (aq) plus Cu(s), at the top, with two arrows branching down to two boxes: a purple OXIDATION box reading Zn yields Zn 2 plus plus 2 electrons (lose electrons) and an orange REDUCTION box reading Cu 2 plus plus 2 electrons yields Cu (gain electrons); below both, a green bar states that electrons must balance, 2 electrons lost equals 2 electrons gained.](figures/splitting_half_reactions.png)

### 14–24 min · Thin-slice board work — split and balance (before the method is named)

Write the **thin-slice prompt** on the board and let groups work. Withhold all method — circulate and ask questions only.

> *"Each reaction below shows a metal trading places with an ion. Using your oxidation-number skills from Lesson 02, split each reaction into TWO equations: one for the species that LOSES electrons and one for the species that GAINS electrons. Show the electrons (e⁻) in each equation. Then check: do the electrons lost equal the electrons gained?"*

**Reaction set (post one at a time as groups finish):**

1. **Zn + Cu²⁺ → Zn²⁺ + Cu** *(warm-up — matches the figure; electrons already equal)*
2. **Mg + 2H⁺ → Mg²⁺ + H₂** *(the gained-electron side now forms a diatomic molecule)*
3. **Al + Cu²⁺ → Al³⁺ + Cu** *(the electron counts DON'T match — groups must figure out how to fix it)*

**Target board work (your reference — do not hand this out):**

Reaction 1:
> Oxidation: Zn → Zn²⁺ + 2e⁻
> Reduction: Cu²⁺ + 2e⁻ → Cu
> Electrons: 2 lost = 2 gained ✓ — net ionic equation: Zn + Cu²⁺ → Zn²⁺ + Cu

Reaction 2:
> Oxidation: Mg → Mg²⁺ + 2e⁻
> Reduction: 2H⁺ + 2e⁻ → H₂
> Electrons: 2 lost = 2 gained ✓ — net ionic equation: Mg + 2H⁺ → Mg²⁺ + H₂

Reaction 3 (the productive struggle):
> Oxidation: Al → Al³⁺ + 3e⁻ (each Al gives up 3)
> Reduction: Cu²⁺ + 2e⁻ → Cu (each Cu²⁺ takes 2)
> 3 ≠ 2 — not balanced. Least common multiple of 3 and 2 is **6**.
> Multiply oxidation by 2: 2Al → 2Al³⁺ + 6e⁻
> Multiply reduction by 3: 3Cu²⁺ + 6e⁻ → 3Cu
> Electrons: 6 lost = 6 gained ✓ — net ionic equation: 2Al + 3Cu²⁺ → 2Al³⁺ + 3Cu

**Teacher facilitation language (circulate — ask, never tell):**

> "Which species' oxidation number went *up*? That one lost electrons — where do the electrons go, on the left or the right of its arrow?"

> "Count the electrons in your oxidation equation, then count them in your reduction equation. Are they the same number? If not, the electrons aren't conserved yet — what could you do to make the counts match?"

> "What's the smallest number that both 3 and 2 divide into evenly? Once you find it, how many times do you have to copy each half-reaction?"

**Anticipated student responses during BTC:**

- "We put the electrons on the same side as the metal for both." — probe: a species that *loses* electrons should show them as a product (they left); a species that *gains* them should show them as a reactant (they arrived). Which side for each?
- "Reaction 3 doesn't work — we get 3 on one side and 2 on the other." — exactly the right struggle; affirm it. "Electrons can't just disappear — what do you do with 3 and 2 to make them equal?"
- "Do we multiply the whole equation or just the electrons?" — the whole half-reaction, including the atoms and the ion charges, so everything scales together.

### 24–30 min · Gallery walk + reconnect

Groups take 90 seconds to glance at one neighboring board, comparing how others handled Reaction 3. Then bring the class together. Ask one group to present their Reaction 3 board.

> "Look at every board. The hard one was Reaction 3 — the electron counts didn't match. Tell me what you did to fix it, and *why* you were allowed to multiply the whole half-reaction by a number."

Surface the key idea (do not name vocabulary yet): the electrons that leave one species are the *same* electrons that arrive at the other — so the counts must be equal. When they aren't, we scale each half up to the least common multiple. We are not inventing electrons; we are making sure none are lost or created.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look at your three boards. Turn to your partner: what is the *rule* — in your own words — for where the electrons go in each of the two equations? And why must the two equations always end with the same number of electrons?"

Target consensus:

> "The species that loses electrons shows e⁻ on the product side (the electrons left it). The species that gains electrons shows e⁻ on the reactant side (the electrons arrived). The two equations must end with equal electrons because every electron lost by one species is gained by the other — electrons are conserved."

> "If I told you a reaction's oxidation half gives off 3 electrons and its reduction half takes in 2, would the reaction be balanced as written? What would you do?"

Target: no — scale to the least common multiple (6), multiplying the oxidation half by 2 and the reduction half by 3, so both show 6 electrons.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name what you've been writing all period. Each of those two equations — the one for the species losing electrons and the one for the species gaining electrons — is called a **half-reaction**. It's called *half* because it shows only one side of the electron transfer; you need both halves to describe the whole reaction. The half showing electrons leaving is the **oxidation half-reaction** (oxidation = loss of electrons, so e⁻ appears as a *product*). The half showing electrons arriving is the **reduction half-reaction** (reduction = gain of electrons, so e⁻ appears as a *reactant*)."

> "And the third term names what you get when you add the two balanced halves back together and cancel the electrons: a **net ionic equation** — an equation that shows only the species that actually change, with the electrons cancelled out because they were transferred, not consumed. The net ionic equation for our cell is Zn + Cu²⁺ → Zn²⁺ + Cu. The electrons don't appear in it because they moved from one species to the other and balanced out perfectly."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "In the oxidation half-reaction Zn → Zn²⁺ + 2e⁻, why are the electrons on the *right*?" — *Expected response:* because zinc *loses* them; they leave the atom, so they are a product.
- "When we add the two balanced halves and the electrons cancel, what does that cancellation prove about the electrons?" — *Expected response:* the number lost exactly equals the number gained — the electrons are conserved, which is why they cancel completely in the net ionic equation.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the model + Because/But/So expansion

Students return to their board work (or Initial Model on the worksheet) and annotate it with the new vocabulary: label the e⁻-on-the-right equation "oxidation half-reaction," the e⁻-on-the-left equation "reduction half-reaction," and the combined cancelled form "net ionic equation."

Then run a **Because / But / So** sentence about the Reaction 3 scaling. Starter on the board:

> *"In the reaction Al + Cu²⁺, aluminum gives up 3 electrons per atom but each copper ion takes only 2."*

Model one aloud:

> "Aluminum's oxidation half-reaction releases 3 electrons per atom **because** Al becomes Al³⁺ (it loses three), **but** copper's reduction half-reaction takes in only 2 electrons per ion (Cu²⁺ becomes Cu), **so** we must scale the halves to the least common multiple of 6 — multiplying aluminum's half by 2 and copper's by 3 — so that 6 electrons lost equal 6 electrons gained and none are created or destroyed."

Then have students write their own B/B/S using one of these starters:

- *"In Zn + Cu²⁺, the electrons did not need to be scaled…"* (hint: 2 lost already equals 2 gained)
- *"A student wrote the reduction half-reaction as Cu²⁺ → Cu + 2e⁻ instead of Cu²⁺ + 2e⁻ → Cu…"* (hint: putting electrons on the wrong side reverses gain and loss)

**Anticipated student responses:**

- "Because Zn already loses 2 and Cu already gains 2, so they're equal." — good; push for the So: "so no scaling was needed and the electrons cancel directly in the net ionic equation."
- "Because the student put the electrons as a product, it looks like copper is losing them." — excellent; push for the So: "so the equation now shows oxidation instead of reduction, which is backwards — Cu²⁺ gains electrons, so e⁻ must be a reactant."

### 39–40 min · Return to the phenomenon

> "Return to the voltmeter. The needle moved because electrons were flowing through the wire from the zinc to the copper. Now you can write exactly what that needle was reading: two half-reactions. Quickly — what are the two halves the cell was performing, and how many electrons crossed the wire per zinc atom?"

Target: oxidation Zn → Zn²⁺ + 2e⁻ at the anode; reduction Cu²⁺ + 2e⁻ → Cu at the cathode; 2 electrons per zinc atom traveled through the wire — which is exactly the current the voltmeter detected.

> "The half-reactions aren't just symbols on paper — they are the bookkeeping of the actual electrons that pushed that needle. That is how a chemist 'sees' the invisible."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud:

> *(a) For the reaction Ca + 2Ag⁺ → Ca²⁺ + 2Ag, write the balanced oxidation half-reaction and the balanced reduction half-reaction. Show the electrons in each.*
> *(b) For the reaction of aluminum with nickel(II) ions, the half-reactions are Al → Al³⁺ + 3e⁻ and Ni²⁺ + 2e⁻ → Ni. Balance the electrons by multiplying each half-reaction by the correct whole number, then state how many electrons are transferred.*

Expected answers are in `Answer_Key.docx`. These reactions are deliberately different from the worksheet practice set (Zn/Cu²⁺, Mg/H⁺, Al/Cu²⁺).

**Closing Reflection (SEL, 30 seconds):**

> "Today we wrote down something nobody can see — the movement of electrons. In one sentence: what is one thing that finally clicked for you about how the two halves connect, and who — a partner or an idea — helped it click?"

Collect worksheets; note which students placed electrons on the correct side of each half-reaction versus students who reversed oxidation and reduction, and which students correctly scaled to the least common multiple. The side-of-the-arrow error and the failure to scale are the two main procedural stumbling blocks — target those students for a brief one-on-one check at the start of the next lesson.

---

## Common Misconceptions

- **Misconception:** "The electrons go on whichever side makes the equation look balanced." → **Correction:** Electron placement is determined by what the species *does*, not by appearance. A species that is oxidized *loses* electrons, so e⁻ appears as a **product** (Zn → Zn²⁺ + 2e⁻). A species that is reduced *gains* electrons, so e⁻ appears as a **reactant** (Cu²⁺ + 2e⁻ → Cu). Use the oxidation-number change from Lesson 02 to decide: number goes up → electrons lost → product side; number goes down → electrons gained → reactant side.
- **Misconception:** "If the two half-reactions have different numbers of electrons, the reaction just doesn't work." → **Correction:** It works — you scale. Multiply each half-reaction by the smallest whole number that makes the electron counts equal (the least common multiple). For Al (3 e⁻) and Cu²⁺ (2 e⁻), the LCM is 6: double the aluminum half, triple the copper half. Scaling does not change the chemistry; it just expresses both halves in the same electron count.
- **Misconception:** "You only multiply the electrons when you balance, not the atoms or ions." → **Correction:** When you multiply a half-reaction by a whole number, you multiply *everything* — atoms, ions, and electrons — so the half-reaction stays internally balanced. 2 × (Al → Al³⁺ + 3e⁻) gives 2Al → 2Al³⁺ + 6e⁻, not Al → Al³⁺ + 6e⁻.
- **Misconception:** "The net ionic equation should still show the electrons." → **Correction:** In the net ionic equation the electrons cancel out, because the number lost in oxidation exactly equals the number gained in reduction. The cancellation is the proof of conservation — if electrons remained, you would not have balanced the halves correctly.
- **Misconception:** "Oxidation and reduction are separate reactions that happen on their own." → **Correction:** They always occur together — you cannot have one without the other, because the electrons one species loses must be the electrons another species gains. That is why we call the pair a redox reaction and write *both* halves. The cell makes this literal: the anode (oxidation) and cathode (reduction) are connected by the wire that carries the shared electrons.

---

## Access & Differentiation

- **ELL/ENL supports:** Half-reaction template pre-printed with two blank arrows and a labeled "e⁻ goes here" prompt under each, plus sentence frames: *"In the oxidation half-reaction, ___ loses ___ electrons, so e⁻ is a product."* and *"In the reduction half-reaction, ___ gains ___ electrons, so e⁻ is a reactant."* Word-choice box displayed throughout: {half-reaction, oxidation, reduction, electron (e⁻), net ionic equation, lose, gain, least common multiple}. Pair each term with a gesture: open hand pushing away for "lose / oxidation," open hand pulling toward the body for "gain / reduction."
- **IEP/SPED supports:** Provide a pre-split scaffold for the harder reactions — the oxidation and reduction arrows already drawn with the species filled in, so the student's task is only to place the electrons and count them (not to identify the split). Pre-fill the oxidation-number changes from Lesson 02 on a reference card (Zn: 0→+2, Cu: +2→0, Al: 0→+3, Mg: 0→+2, H: +1→0) so the lookup is removed as a barrier. Offer a least-common-multiple table (e.g., 2 & 3 → 6; 2 & 2 → 2) for the scaling step. Assign clear group roles at the vertical surface: one writes, one counts electrons, one checks the activity series.
- **Extensions:** (1) Write the two half-reactions for a reaction with a polyatomic spectator (e.g., Zn + CuSO₄ → ZnSO₄ + Cu) and identify the sulfate as a spectator ion that does not appear in the net ionic equation. (2) For Fe → Fe³⁺ + 3e⁻ paired with Ag⁺ + e⁻ → Ag, balance the electrons (LCM = 3) and write the net ionic equation: Fe + 3Ag⁺ → Fe³⁺ + 3Ag. (3) Predict, using Table J (activity series), whether copper metal placed in zinc(II) sulfate solution would react — write the half-reactions you would expect and explain why the reaction does *not* proceed spontaneously.

---

## Strategy Spotlight

**BTC — Building Thinking Classrooms.** The Building Thinking Classrooms framework (Peter Liljedahl, *Building Thinking Classrooms in Mathematics*, 2021) centers on three core practices that consistently raise student thinking: (1) **random grouping** removes status hierarchies and prevents friend-group comfort zones; (2) **vertical non-permanent surfaces** (whiteboards, windows, chart paper) make thinking visible, erasable, and collaborative; and (3) **thin-slice problems** launch students into work immediately — before any direct instruction — so thinking happens before consolidation.

**How BTC runs in this lesson (Phase 2, minutes 10–30):**

1. **Random groups:** Use a card randomizer, a digital spinner, or the class roster shuffled to assign groups of three. Announce: "These are your working groups for the next 16 minutes. Find your vertical surface."
2. **Vertical surfaces:** Each group claims one whiteboard panel, a section of window with a dry-erase marker, or a sheet of chart paper taped at standing height. One marker per group — the marker passes between members so all three contribute writing and thinking.
3. **Thin-slice prompt:** The three reactions are sequenced to increase in difficulty by one variable at a time: Reaction 1 has equal electrons (warm-up), Reaction 2 introduces a diatomic product, and Reaction 3 forces the least-common-multiple scaling. Students are *not* told the balancing rule — they generate the split, place the electrons, and discover the need to scale when the counts don't match in Reaction 3. The task forces them to invent the bookkeeping before Phase 3 names it.
4. **Teacher as knowledge-withholder:** While groups work, circulate and ask only questions — never give the rule. Ask: "Which oxidation number went up?" "Are your electron counts equal?" "What's the smallest number both counts divide into?" The goal is for students to arrive at *electrons lost = electrons gained* and the least-common-multiple fix themselves before you formalize half-reactions in Phase 3.
5. **Gallery walk (built in):** During the reconnect step, groups glance at one neighboring board to compare how others scaled Reaction 3 — exposing them to a second route to the same balanced result.

**Why BTC fits writing half-reactions:** Splitting and balancing half-reactions is a procedural pattern that *emerges* naturally from the conservation idea — every electron lost is gained — which makes the three-reaction sequence an ideal thin-slice. Once students hit the wall on Reaction 3 at the whiteboard and invent the least-common-multiple fix themselves, the vocabulary in Phase 3 names something they already understand from their own struggle. Research on BTC (Liljedahl, 2021) shows that students who derive a procedure before seeing it stated retain it more reliably than students who copy it from the board.

**CRSE connection:** The phenomenon — detecting something invisible by its effects — connects to many ways of knowing the world through indirect evidence, a practice common across cultures and central to all of science. The random grouping practice is itself a CRSE move: it disrupts the social sorting that often concentrates academic authority in a few students, signaling that every student's thinking belongs on the board. The electrochemical cell also opens a door to everyday technology students rely on — every battery in a phone or game controller runs on exactly the half-reactions written in this lesson.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — zinc-in-copper-sulfate color change and the voltmeter cell (`electrochemical_cell.png`); return in Phase 4 to write what the needle was reading |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — where do the electrons come from and go?); Phase 3 (TT#2 — what is the rule for electron placement and why must counts be equal?) |
| 3 | Students develop questions/models/procedures | Phase 2 BTC board work — groups invent the split-and-balance procedure at vertical surfaces before any method is given; gallery walk compares approaches |
| 4 | CCC defined and used | Lesson Overview · *Energy and Matter / conservation*, explicit in Phase 3 (electrons cancel = conserved) and Phase 4 B/B/S (least-common-multiple scaling) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: half-reaction / oxidation & reduction half-reaction / net ionic equation |
| 6 | Revisit phenomenon with evidence | Phase 4 — students return to the voltmeter and write the two half-reactions the cell was performing, connecting 2 e⁻ per Zn atom to the measured current |
| 7 | ENL/SPED supports | Access & Differentiation block: half-reaction template, sentence frames, word-choice box, pre-split scaffold, oxidation-number reference card, LCM table, group roles |
| 8 | Assessment check | Phase 5 — Exit Ticket (Ca/Ag⁺ half-reactions with equal electrons; Al/Ni²⁺ electron balancing by least common multiple) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked half-reaction example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **half-reaction** — one of the two equations that together describe a redox reaction; the **oxidation half-reaction** shows the species that loses electrons (e⁻ written as a *product*, e.g., Zn → Zn²⁺ + 2e⁻) and the **reduction half-reaction** shows the species that gains electrons (e⁻ written as a *reactant*, e.g., Cu²⁺ + 2e⁻ → Cu)
- **balancing electrons** — multiplying each half-reaction by the smallest whole number (the least common multiple of the electron counts) so that the electrons lost in oxidation equal the electrons gained in reduction; this enforces conservation of charge
- **net ionic equation** — the equation obtained by adding the two balanced half-reactions and cancelling the electrons (and any spectator ions); it shows only the species that actually change, e.g., Zn + Cu²⁺ → Zn²⁺ + Cu
