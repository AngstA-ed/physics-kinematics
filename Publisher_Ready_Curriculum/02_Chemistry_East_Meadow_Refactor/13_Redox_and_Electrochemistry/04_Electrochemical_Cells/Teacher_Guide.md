# Electrochemical Cells — Teacher Guide

## Cover

**Unit: Redox & Electrochemistry — Lesson 04: Electrochemical Cells**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: ACTIVE LEARNING

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

**PS1-12 (Transfer of Electrons)** — *"Use evidence to illustrate that some chemical reactions involve the transfer of electrons as an energy conversion occurs within a system."* An electrochemical cell is the clearest physical demonstration of this idea: a spontaneous redox reaction is split into two half-reactions in separate containers so that the electrons it transfers are *forced to travel through an external wire* before they can complete the reaction. Per East Meadow guidance, oxidation–reduction is "the prevailing source of power for many of today's modern conveniences" — every battery, fuel cell, and rechargeable device is an electrochemical cell, so this lesson is where the abstract bookkeeping of oxidation numbers and half-reactions (Lessons 01–03) becomes a working power source students can hold in their hand.

This lesson also draws on **HS-PS2-6** — *"Communicate scientific and technical information about why the molecular-level structure is important in the functioning of designed materials."* A battery is a *designed material*: which metals are chosen for the electrodes is not arbitrary. The cell works because zinc gives up electrons more readily than copper does — a molecular-level property of the metals — and engineers choose electrode pairs precisely to set the voltage and direction of electron flow.

The Cross-Cutting Concept of **Energy and Matter** is the explicit lens: in a voltaic cell, chemical potential energy stored in the reactants is converted into electrical energy as electrons transfer from the substance oxidized to the substance reduced. The battery "dies" when the reactants are used up — matter is conserved, but the chemical energy that drove the electron transfer has been spent.

### Phenomenon

Hold up a fresh AA battery and a dead one — identical on the outside, but one runs a small motor or LED and the other does nothing. Then build the chemistry version live: stick a strip of copper and a strip of zinc into a lemon (or a potato), connect them to a small voltmeter, and watch the needle jump to roughly 0.9–1.0 V. No plug, no outlet — a piece of fruit is producing electricity. Push further: connect the lemon cell to a tiny LED or a low-voltage buzzer. Then ask the question that drives the whole lesson — *where is that electricity coming from, and why will it eventually stop?*

**Driving question:** How does a battery actually produce electricity, and why do batteries eventually die?

### Javalab / Labs

- **Lemon / potato battery (Engage demo + Explore station):** Insert a copper strip (or penny) and a zinc strip (or galvanized nail) into a lemon or potato; connect with alligator clips to a voltmeter. The zinc is the anode (oxidized), the copper is the cathode, and the citric/phosphoric acid in the fruit is the electrolyte. A single cell gives ~0.9 V; wiring 3–4 in series lights a small LED. This is the hook *and* a hands-on station.
- **Cu/Zn voltaic cell construction (core Explore):** Students build a true Daniell-style cell — a zinc strip in ZnSO₄(aq) and a copper strip in CuSO₄(aq), joined by a salt bridge (filter paper soaked in KNO₃, or a U-tube), with the metals wired through a voltmeter. They observe the voltage (~1.1 V), identify which electrode loses mass (Zn anode) and which gains a copper coating (Cu cathode), and trace the electron path. Diagram in `figures/voltaic_cell.png`.
- **Electroplating demonstration (Elaborate):** A short teacher demo of an *electrolytic* cell — a battery driving a non-spontaneous reaction to plate copper onto a key or a steel washer. This contrasts the voltaic cell (makes electricity) with the electrolytic cell (uses electricity), establishing both cell types named in the Scope & Sequence.

### Assessments

- **Voltaic cell diagram & explanation assessment** (district checkpoint, following lesson): students label a blank voltaic-cell diagram (anode, cathode, salt bridge, direction of electron flow, site of oxidation vs. reduction) and write half-reactions and the overall cell reaction for a given metal pair. See `Assessments/` folder once created.
- **Exit Ticket** (Phase 5): a *different* metal pair (Mg/Ag) than the worksheet practice (Zn/Cu) — students identify anode and cathode, the direction of electron flow, and write one sentence explaining why a battery dies. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | PS1-12 (electron transfer as energy conversion in a system); HS-PS2-6 (designed materials — electrode choice sets cell behavior) |
| **CCC focus** | Energy and Matter — chemical potential energy in the reactants is converted to electrical energy as electrons transfer from the oxidized substance to the reduced substance; the cell stops when the reactant matter is consumed |
| **Strategy chips** | ACTIVE LEARNING — students build and measure a working cell, then trace the electron path with their own hands before any term is defined |
| **Materials** | Lemons or potatoes, copper strips/pennies, zinc strips/galvanized nails, alligator-clip leads, low-voltage voltmeters or multimeters, a small LED or buzzer; for the core build: ZnSO₄(aq) and CuSO₄(aq), Zn and Cu electrodes, filter paper + KNO₃ for salt bridges, beakers; `figures/voltaic_cell.png` projected. Electroplating demo: copper electrode, a steel object, CuSO₄(aq), a 1.5–6 V DC source. |
| **Safety** | Goggles and aprons throughout. CuSO₄ and ZnSO₄ solutions are irritants and toxic if ingested — no food in the lab even though lemons/potatoes are used (these are designated lab materials, not snacks). KNO₃ salt bridge: avoid skin contact. The DC source for electroplating is low-voltage but keep leads dry and away from solutions except the cell itself. Dispose of metal-salt solutions per district hazardous-waste protocol. |
| **Prior knowledge** | Lesson 01 (assigning oxidation numbers), Lesson 02 (identifying which species is oxidized and which is reduced), Lesson 03 (writing balanced half-reactions). Students should be able to write a half-reaction such as Zn → Zn²⁺ + 2e⁻ before this lesson; this lesson puts those half-reactions into two physical containers. |

**Lesson objectives — students can:**

- Build a working voltaic cell from two metals and measure the voltage it produces.
- Identify the anode (oxidation, electrons leave) and the cathode (reduction, electrons arrive) and state the direction of electron flow (anode → cathode through the external wire).
- Explain the function of the salt bridge in completing the circuit and keeping each solution electrically neutral.
- Distinguish a voltaic cell (spontaneous; makes electricity) from an electrolytic cell (non-spontaneous; uses electricity), and explain — using Energy and Matter — why a battery eventually dies.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers: *"Name something you use every day that runs on a battery, and tell us about a time the battery died on you at a bad moment."* One round, one sentence each, no judgment. This grounds the lesson in lived experience and surfaces the shared frustration of a dead battery — exactly the phenomenon we will explain.

Then post the **Do Now**:

> *"A fresh AA battery and a dead AA battery look identical. The fresh one runs a small motor; the dead one does nothing. In one sentence: what do you think is physically different inside the two batteries?"*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "The fresh one has more power/charge stored in it." — affirm; push: power stored as *what*? Is it electricity sitting inside, or something else? Hold that question.
- "The dead one ran out of chemicals." — excellent; that's very close to today's answer. Validate and keep it visible.
- "Electricity leaked out of the dead one." — common idea; gently probe: a battery isn't a tank of electricity. Today we'll find out what's really inside.

### 3–8 min · Phenomenon hook — the lemon battery

**Teacher actions.** Hold up a fresh and a dead AA side by side. Then build the lemon cell live: push a copper strip and a zinc strip into a lemon, connect both to a voltmeter, and let the class watch the needle climb to ~0.9 V. Then swap the voltmeter for a small LED (or wire 3–4 lemon cells in series) so the class sees light.

> "There's no outlet. No charger. Just a piece of fruit and two different metals — and the meter reads almost a full volt. Something inside this lemon is pushing electrons through that wire. Where is that energy coming from? And here's the question that matters most: if I leave this hooked up long enough, the voltage will fade and the light will die. Why?"

**Sample teacher language:**

> "You already know how to write a half-reaction. Zinc can give up electrons: Zn → Zn²⁺ + 2e⁻. Copper ions can take electrons. In Lessons 1 through 3 we did that on paper. Today the lemon does it for real — but the two halves are happening on two *different* metals, so the electrons can't just jump across. They have to travel through this wire to get from the zinc to the copper. That moving stream of electrons through the wire *is* the electricity."

**Anticipated student responses:**

- "So the zinc is losing electrons and they go through the wire?" — yes — that's exactly the path; we'll confirm the direction during the build.
- "Why does it have to be two different metals?" — outstanding question; if both were the same metal there'd be no push. We'll discover why during the Explore.
- "Why will it die?" — when the zinc is used up — when there's no more reactant to be oxidized — the electron stream stops. We'll come back to this with evidence.

**Driving question** (post on the board and leave it there):

> *How does a battery actually produce electricity, and why do batteries eventually die?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the lemon cell. Then:

> "Turn to your partner: the electrons have to travel from the zinc to the copper through the wire. In which direction are they moving — *from* the zinc *to* the copper, or the other way? And what is your reasoning?"

Target insight (leave open if no one lands it yet): the zinc is the metal being oxidized — it gives up electrons — so electrons must leave the zinc and travel through the wire to the copper. We will confirm this physically during the build and name the electrodes in Phase 3.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–15 min · ACTIVE LEARNING — build and measure the Cu/Zn cell (before any formal definition)

**Before any formal vocabulary is introduced**, students build a real voltaic cell and gather evidence with their own hands. Distribute the worksheet and materials. Each group sets up: a zinc strip standing in a beaker of ZnSO₄(aq), a copper strip standing in a beaker of CuSO₄(aq), the two metals wired through a voltmeter, and a salt-bridge (KNO₃-soaked filter paper) connecting the two solutions.

**The task (students record on the worksheet):**

- Read and record the **voltage** before the salt bridge is connected, then again after. (Before: ~0 V. After: ~1.1 V.)
- Note which terminal of the voltmeter reads positive — that wire leads to the **copper**.

**Teacher facilitation language (circulate):**

> "Connect everything *except* the salt bridge first. What does the voltmeter read? Now lay the salt bridge across. What happens to the reading? That jump from nothing to over a volt is your evidence that the salt bridge completes the circuit."

> "Look at the sign on your voltmeter. The red lead is reading positive — which metal is it clipped to? That tells you which way the electrons are flowing through the wire."

**Anticipated student responses during the build:**

- "It read zero until we added the salt bridge, then it jumped." — that is the key observation; the circuit was open without the salt bridge. We'll explain why in Phase 3.
- "The copper side is positive." — good; so electrons are arriving at the copper. Where are they leaving from? The zinc.
- "Nothing's bubbling — how do I know it's working?" — the voltmeter is your evidence; the reaction is slow and quiet, but the needle proves electrons are moving.

### 15–22 min · Initial Model — trace the electron path and the half-reactions

**Prompt on the board:**

> *"Before we name the parts: on your diagram, draw an arrow showing which way electrons move through the wire. Then write the half-reaction happening at each metal. Use what you measured (which side is positive) as your evidence."*

Students work individually for 3–4 minutes, then compare with a partner.

Target model:

> Electrons leave the **zinc** (Zn → Zn²⁺ + 2e⁻), travel through the wire, and arrive at the **copper**, where copper ions in solution pick them up (Cu²⁺ + 2e⁻ → Cu). The arrow points from zinc to copper through the wire.

**Teacher facilitation language:**

> "The zinc strip is slowly dissolving — Zn atoms are turning into Zn²⁺ ions and leaving their electrons behind on the metal. Those stranded electrons push through the wire. At the copper, Cu²⁺ ions from the blue solution grab those electrons and plate out as solid copper. Check your arrow: does it point from the zinc to the copper?"

**Anticipated student responses:**

- "I drew the arrow from copper to zinc." — redirect to their evidence: which side read positive? Electrons flow *toward* the positive terminal externally? Have them re-reason from the oxidation half-reaction: zinc loses electrons, so electrons *leave* zinc.
- "Why does copper come out of the solution?" — the blue CuSO₄ solution is full of Cu²⁺ ions; when electrons arrive, those ions are reduced to copper metal and coat the electrode. The solution slowly fades in color — evidence of Cu²⁺ being used up.
- "Both half-reactions need 2 electrons — is that a coincidence?" — no; the electrons lost by zinc are exactly the electrons gained by copper. That balance is why the overall reaction is Zn + Cu²⁺ → Zn²⁺ + Cu.

### 22–30 min · Investigation — what does each part do?

Groups now investigate the *role* of each part by reasoning from their observations. They complete a structured table on the worksheet.

**Investigation prompts (on the board or worksheet):**

1. **The two metals:** Why must the two electrodes be *different* metals? (Evidence: a cell with two identical metals reads 0 V.)
2. **The salt bridge:** What happened to the voltage when you removed or omitted the salt bridge? Why is it needed?
3. **Direction of electron flow:** Using the positive terminal you identified, state the direction electrons travel through the wire.

**Reference — the labeled cell (project for the whole investigation):**

![Brand-styled diagram of a Zn/Cu voltaic cell: a zinc electrode in zinc-sulfate solution on the left labeled anode, negative, oxidation, with the half-reaction Zn → Zn²⁺ + 2e⁻; a copper electrode in copper-sulfate solution on the right labeled cathode, positive, reduction, with the half-reaction Cu²⁺ + 2e⁻ → Cu; an external wire runs through a voltmeter at the top with purple arrows showing electron flow from anode to cathode; a salt bridge connects the two beakers at the bottom with a blue arrow showing anions moving toward the anode; the title notes a spontaneous cell with a cell potential of +1.10 V.](figures/voltaic_cell.png)

**Teacher facilitation prompts (circulate):**

> "When the salt bridge is removed, the voltage collapses. Think about charge: the zinc side is making positive Zn²⁺ ions, so it's building up positive charge; the copper side is removing positive Cu²⁺ ions, so it's building up negative charge. That charge imbalance would stop the electrons almost instantly. What does the salt bridge do to fix that?"

> "Two identical copper strips would have no reason to push electrons either way — there's no difference in how strongly they hold their electrons. You need one metal that gives up electrons more easily than the other."

**Anticipated student responses:**

- "The salt bridge lets charge balance out." — exactly; ions flow through it to keep each beaker neutral, so electrons can keep moving. (Anions drift toward the zinc side, cations toward the copper side.)
- "If both metals were the same, there'd be a tie — no winner." — nice intuition; the 'winner' is the metal more easily oxidized (zinc here). That difference *is* the voltage.
- "So the bigger the difference between the two metals, the bigger the voltage?" — yes; that's the basis for predicting cell potential, which we'll formalize next.

### 28–30 min · Reconnect + surface the method

Bring groups back together. Ask one group to put their electron-flow arrow and half-reactions on the board. Ask the class:

> "Every group measured about the same voltage — 1.1 V — for zinc and copper. That number isn't random. It comes from how strongly each metal holds its electrons. If I swapped copper for silver, would the voltage go up or down? What would I need to know to predict it?"

Surface the key idea: each metal has a measured tendency to gain electrons (a reduction potential). The **cell potential** is the difference between the two electrodes' tendencies. The metal more easily oxidized becomes the anode; the metal more easily reduced becomes the cathode. A positive cell potential means the reaction is spontaneous — it runs on its own and produces electricity.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look at your measured cell — zinc dissolving, copper plating out, electrons flowing zinc-to-copper, 1.1 volts on the meter. Turn to your partner: in one sentence, where did the electrical energy come from, and what will happen to the voltage as the zinc strip keeps dissolving?"

Target consensus: the electrical energy came from the *chemical* energy of the spontaneous reaction Zn + Cu²⁺ → Zn²⁺ + Cu. As the zinc dissolves and the Cu²⁺ runs out, the reactants are consumed; when they're gone, there are no more electrons to push, the voltage drops to zero, and the cell is "dead."

> "Now imagine I reverse it: I connect a power supply and *force* electrons backward through the cell. What would happen to the zinc and copper? Would that reaction happen on its own?"

Target: forcing current backward would re-deposit zinc and dissolve copper — a *non-spontaneous* reaction driven by an outside power source. That is the second kind of cell, which we'll name now.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name what you built and measured. The electrode where **oxidation** happens — where the zinc gives up electrons and dissolves — is the **anode**. The electrode where **reduction** happens — where copper ions gain electrons and plate out — is the **cathode**. One memory hook: *an ox* (anode = oxidation) and *red cat* (reduction = cathode). Electrons always travel from the anode to the cathode through the external wire. That direction is fixed by which metal is more easily oxidized."

> "The whole device you built — a setup that uses a *spontaneous* redox reaction to produce electricity — is a **voltaic cell** (also called a galvanic cell). Every battery is a voltaic cell. The energy comes from the chemical reaction, not from a wall outlet."

> "There is a second kind: an **electrolytic cell** — a setup that uses an outside power source to *drive a non-spontaneous* redox reaction. It's the reverse situation: instead of the reaction making electricity, electricity makes the reaction happen. Electroplating and recharging a battery are electrolytic processes. Same parts — anode, cathode, electrons from anode to cathode — but the energy flows the opposite way: electrical energy goes *in*."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "Which electrode lost mass in your cell, and is that the anode or the cathode?" — *Expected response:* the zinc strip lost mass; it's the anode, because oxidation (Zn → Zn²⁺ + 2e⁻) removes atoms from the metal.
- "In a voltaic cell the anode is the negative terminal. In an electrolytic cell, what's pushing the electrons?" — *Expected response:* an external power source (a battery or supply) pushes the electrons, so the reaction that wouldn't happen on its own is forced to occur. Energy goes in rather than coming out.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Predict a new cell + Because/But/So expansion

Students apply the method to a *new* metal pair they did not build. Project a short reduction-potential reference (or the values below) and pose:

> *"A cell is built from magnesium and copper. Magnesium is oxidized much more easily than zinc; copper still gains electrons. Predict: which metal is the anode? Which way do electrons flow? Will the voltage be larger or smaller than your zinc–copper cell?"*

Target reasoning:

> Magnesium is the anode (it's oxidized: Mg → Mg²⁺ + 2e⁻); copper is the cathode (Cu²⁺ + 2e⁻ → Cu). Electrons flow Mg → Cu through the wire. Because magnesium gives up electrons even more readily than zinc, the difference between the two electrodes is larger, so the voltage is *higher* than the 1.1 V zinc–copper cell.

Then run a **Because / But / So** sentence about the phenomenon. Starter on the board:

> *"A battery eventually dies even though no electricity 'leaked out' of it."*

Model one aloud:

> "A battery eventually dies **because** the spontaneous redox reaction inside it consumes its reactants — the metal at the anode dissolves away and the ions at the cathode get used up — **but** matter is conserved, so nothing leaked out; the reactants simply turned into products — **so** once the reactants are gone there are no more electrons to transfer, the chemical energy is spent, and the voltage drops to zero."

Then have students write their own B/B/S using one of these starters:

- *"A voltaic cell and an electrolytic cell have the same parts but do opposite things…"* (hint: one makes electricity, one uses it)
- *"The salt bridge doesn't carry electrons, yet without it the cell stops working…"*

**Anticipated student responses:**

- "Because the voltaic cell is spontaneous but the electrolytic cell needs a power source." — good start; push for the So: "so in one, chemical energy turns into electrical energy, and in the other, electrical energy is used to force a reaction that wouldn't happen on its own."
- "Because the salt bridge carries ions, not electrons." — excellent; push the So: "so it keeps each beaker electrically neutral, which lets the electrons keep flowing through the wire."

### 39–40 min · Return to the phenomenon

> "Return to the lemon cell and the dead AA from the start of class. You now have the vocabulary. Using the words *anode*, *cathode*, and one of *voltaic* or *electrolytic*, explain in one sentence how the lemon produced electricity. Then explain in one sentence why the dead AA does nothing."

Target: "The lemon is a voltaic cell — the zinc anode is oxidized and pushes electrons through the wire to the copper cathode, producing electricity; the dead AA does nothing because its reactants are used up, so there are no more electrons to transfer."

> "That voltage on the meter wasn't magic — it was a redox reaction you could write as two half-reactions, pulled apart into two containers so the electrons had to take the long way around. That's every battery you own."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud:

> *A voltaic cell is built from a magnesium strip in Mg(NO₃)₂(aq) and a silver strip in AgNO₃(aq), joined by a salt bridge. Magnesium is oxidized much more easily than silver.*
> *(a) Which metal is the anode and which is the cathode? Explain how you decided.*
> *(b) State the direction electrons flow through the external wire.*
> *(c) In one sentence, explain why this battery will eventually stop producing electricity.*

Expected answers are in `Answer_Key.docx`.

**Closing Reflection (SEL, 30 seconds):**

> "Today you built a battery out of metal and salt water and watched it make real electricity. In one sentence: what is one thing that surprised you about how a battery actually works, and who — a partner or a moment in the build — helped it click for you?"

Collect worksheets; note which students correctly placed the anode at the *more easily oxidized* metal (Mg) versus students who guessed based on position in the diagram. Anode/cathode assignment from the oxidation tendency — not from left/right placement — is the main conceptual stumbling block; target those students for a brief one-on-one check at the start of the next lesson.

---

## Common Misconceptions

- **Misconception:** "Electrons flow through the salt bridge." → **Correction:** Electrons travel only through the *external wire*, from anode to cathode. The salt bridge carries *ions*, not electrons, to keep each solution electrically neutral so the electron flow can continue. If electrons could cross the salt bridge, there would be no need for the external circuit — and no usable electricity.
- **Misconception:** "The anode is always negative" (or "always on the left"). → **Correction:** The anode is wherever *oxidation* happens — the electrode that loses electrons. In a voltaic cell the anode is the negative terminal; in an electrolytic cell the anode is the positive terminal. Anode/cathode are defined by oxidation/reduction, not by sign or by position in a drawing. The metal more easily oxidized is the anode regardless of which side it's drawn on.
- **Misconception:** "A battery stores electricity, and the electricity leaks out as it's used." → **Correction:** A battery stores *chemical* energy, not electricity. It produces electricity by running a redox reaction; it "dies" when the reactants are consumed. Nothing leaks out — the reactant matter is converted to product matter, and the chemical energy that drove electron transfer is spent.
- **Misconception:** "A voltaic cell and an electrolytic cell are completely different devices." → **Correction:** Both have an anode, a cathode, and electrons flowing from anode to cathode. The difference is the energy direction: a voltaic cell uses a *spontaneous* reaction to *produce* electrical energy; an electrolytic cell uses an *external power source* to *force* a non-spontaneous reaction. Recharging a battery runs the very same chemistry backward in electrolytic mode.
- **Misconception:** "Any two pieces of metal will make a battery." → **Correction:** The two electrodes must be *different* metals with different tendencies to lose electrons. Two identical electrodes produce 0 V because neither has a reason to give up electrons to the other. The voltage is the *difference* in their reduction potentials — bigger difference, bigger voltage.

---

## Access & Differentiation

- **ELL/ENL supports:** Sentence frames for the investigation and Exit Ticket: *"The ___ is the anode because ___."* and *"Electrons flow from the ___ to the ___."* Word-choice box displayed on the board throughout: {anode, cathode, oxidation, reduction, salt bridge, voltaic cell, electrolytic cell, electrons}. Pair vocabulary with gestures: open hand pushing away for oxidation/anode (giving up electrons), cupped hand pulling in for reduction/cathode (gaining electrons). Provide the "AN OX / RED CAT" memory hook as a printed card. Label the figure parts in both English and a home-language glossary card if available.
- **IEP/SPED supports:** Provide a pre-labeled cell diagram so the cognitive task is *explaining* the parts, not locating them from scratch. Assign clear roles for the build: one student handles the electrodes, one connects the meter, one records readings. Pre-write the two half-reactions on a card so the student matches each to the correct electrode rather than recalling them. Offer a partially completed investigation table (the "what does each part do?" column pre-filled for one row as a model). Calculator not needed; the conceptual identification is the skill target.
- **Extensions:** (1) Using a reduction-potential table, calculate the standard cell potential E°cell = E°cathode − E°anode for the Zn/Cu cell (≈ +0.34 − (−0.76) = +1.10 V) and for the Mg/Cu cell; confirm the prediction that Mg/Cu gives a higher voltage. (2) Explain how a *rechargeable* battery uses electrolytic-cell operation to reverse the reaction and restore the reactants. (3) Research a real designed cell (alkaline AA, lithium-ion, or hydrogen fuel cell) and write two sentences on which materials are chosen for the electrodes and why — connecting to HS-PS2-6.

---

## Strategy Spotlight

**ACTIVE LEARNING — build-then-name.** Active learning means students generate the evidence with their own hands *before* the teacher supplies the vocabulary. In this lesson the move is deliberate and sequenced: students assemble a real Cu/Zn cell, watch the voltmeter jump from 0 V to ~1.1 V when the salt bridge is added, see the copper electrode darken and the blue solution fade, and trace the electron path themselves — all before the words *anode*, *cathode*, *voltaic*, and *electrolytic* are ever spoken. By the time the terms arrive in Phase 3, every term names something the student has already physically observed.

**Why build-then-name fits electrochemistry:** electrochemistry is notoriously abstract — invisible electrons, ions in solution, signs and conventions that students memorize and confuse. The hands-on cell makes the abstractions concrete: "the electrode that lost mass" *becomes* the anode; "the side the positive lead clipped to" *becomes* the cathode; "the thing that made the voltage jump" *becomes* the salt bridge. Students who attach the vocabulary to a remembered observation are far less likely to flip anode and cathode on the assessment.

**How to run it in this lesson (Phase 2 → Phase 3):**

1. Students build the cell and record voltage *before* and *after* the salt bridge — the single most memorable data point of the lesson (Phase 2, 10–15 min).
2. Students draw the electron-flow arrow and write the half-reactions from their own evidence — committing to a model before any term exists (Phase 2, 15–22 min).
3. Only in Phase 3 (33–36 min) does the teacher name the parts, each time pointing back to what the students already saw: "the electrode that dissolved — that's the anode."
4. In Phase 4, students predict a *new* cell (Mg/Cu) they never built, proving the method transfers beyond the single hands-on case.

**CRSE connection:** The opening circle invites every student to share a dead-battery moment from their own life — a phone that died mid-text, a controller, a flashlight during a power outage. Batteries are universal across every student's lived experience regardless of background, which makes this an equitable entry point: no prior chemistry advantage is needed to have a strong opinion about a battery dying at the worst possible moment. Grounding an abstract redox concept in a device every student owns honors out-of-school knowledge and makes the chemistry feel like an explanation of *their* world.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — lemon battery + dead AA; return in Phase 4 to explain the lemon cell and dead AA with new vocabulary |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — which direction do electrons flow, and why?); Phase 3 (TT#2 — where did the electrical energy come from and what happens as the zinc dissolves?) |
| 3 | Students develop questions/models/procedures | Phase 2 — build the Cu/Zn cell, measure voltage before/after salt bridge, draw electron-flow arrow and write half-reactions, complete the "what does each part do?" investigation table |
| 4 | CCC defined and used | Lesson Overview · *Energy and Matter*, explicit in Phase 3 (energy source of the cell) and Phase 4 (B/B/S on why a battery dies — reactants consumed, energy spent) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: anode/cathode (paired term) / voltaic cell / electrolytic cell |
| 6 | Revisit phenomenon with evidence | Phase 4 — students return to the lemon cell and dead AA armed with measured voltage, the electron-flow arrow, and the half-reactions to explain how electricity is produced and why batteries die |
| 7 | ENL/SPED supports | Access & Differentiation block: sentence frames, word-choice box, gestures, AN OX/RED CAT card, pre-labeled diagram, partner roles, half-reaction matching cards, partially completed table |
| 8 | Assessment check | Phase 5 — Exit Ticket (Mg/Ag cell: identify anode and cathode, electron-flow direction, one sentence on why the battery dies) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked cell example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **anode / cathode** — the two electrodes of an electrochemical cell: the **anode** is where oxidation occurs (electrons leave the electrode; the electrode loses mass in a metal cell), and the **cathode** is where reduction occurs (electrons arrive; ions plate out). Electrons always travel from anode to cathode through the external wire. Memory hook: *AN OX* (anode–oxidation), *RED CAT* (reduction–cathode)
- **voltaic cell** — an electrochemical cell that uses a *spontaneous* redox reaction to convert chemical energy into electrical energy; every battery is a voltaic cell (also called a galvanic cell); the cell potential is positive and the reaction produces electricity until the reactants are consumed
- **electrolytic cell** — an electrochemical cell that uses an *external* power source to drive a *non-spontaneous* redox reaction; electrical energy is put *in* to force a reaction that would not occur on its own; electroplating and recharging a battery are electrolytic processes
