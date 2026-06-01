# Le Châtelier's Principle — Teacher Guide

## Cover

**Unit: Kinetics & Equilibrium — Lesson 06: Le Châtelier's Principle**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: BTC

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

**HS-PS1-6** — *"Refine the design of a chemical system by specifying a change in conditions that would produce increased amounts of products at equilibrium."* The emphasis is on changes at the macroscopic and molecular level and on *refining designs* of chemical reactions. This lesson is the engineering-design heart of the equilibrium unit: students do not merely observe that a reaction reaches balance (Lesson 05, Chemical Equilibrium) — they now *manipulate* the conditions of a reversible reaction to push the balance toward the products they want. The anchoring case is the **Haber process** for ammonia synthesis, the single chemical process that feeds roughly half the world's population through synthetic fertilizer. Students specify a change in concentration, pressure, or temperature and predict, then justify, the direction the equilibrium will shift.

The Cross-Cutting Concept of **Stability and Change** is the explicit lens: a system at equilibrium is *stable* (forward and reverse rates equal, concentrations constant) until a stress disturbs it; the system then *changes* — shifts — to partially counteract that stress and settle into a new equilibrium. Le Châtelier's principle is the predictive rule that tells you which way the change will go.

### Phenomenon

Industrial chemists at an ammonia plant face a paradox. Nitrogen gas is free — it is 78% of the air around them. Hydrogen is cheap. Yet for decades no one could make ammonia (NH₃) profitably, because the reaction N₂(g) + 3H₂(g) ⇌ 2NH₃(g) is reversible: as fast as ammonia forms, it breaks back apart, and the reaction stalls at a low yield. Fritz Haber's breakthrough was not a new reaction — it was a recipe of *conditions*. Crank the pressure to 200 atmospheres. Hold the temperature at a carefully chosen 450 °C. Add an iron catalyst. Continuously pull the ammonia out as it forms. Each of those choices nudges the same reversible reaction toward more product. Project `figures/ammonia_yield_pressure.png`: at 400 °C the ammonia yield climbs from 27% at 25 atm to 78% at 400 atm — same reaction, same gases, but a different balance point at every pressure. The driving question for students is the engineer's question: **how do you tilt a reversible reaction's balance toward the product you want?**

### Javalab / Labs

- **Le Châtelier color-change investigation (CoCl₂ equilibrium):** The cobalt(II) chloride equilibrium [Co(H₂O)₆]²⁺ (pink) + 4Cl⁻ ⇌ [CoCl₄]²⁻ (blue) + 6H₂O is a vivid, reversible color demonstration. Adding concentrated HCl (raises Cl⁻) shifts the equilibrium right → blue. Adding water (dilutes Cl⁻) shifts it left → pink. Warming the tube shifts it toward blue (forward reaction is endothermic); cooling shifts it toward pink. Students *see* the equilibrium move and reverse on demand. (Teacher demo — concentrated HCl is corrosive; goggles, gloves, fume hood.)
- **FeSCN²⁺ equilibrium (student-safe color change):** Fe³⁺(aq) + SCN⁻(aq) ⇌ FeSCN²⁺(aq, deep red). Adding more Fe³⁺ or more SCN⁻ deepens the red (shift right); adding a precipitating agent that removes Fe³⁺ fades it (shift left). This is the standard student-run Le Châtelier lab and is the basis for the Investigation below.
- **Javalab equilibrium simulator:** the Javalab "chemical equilibrium / Le Châtelier" interactive lets students add or remove reactant/product and change temperature, watching the bar of concentrations re-balance. No login required; use it as a virtual alternative or a pre-lab.
- **Haber process case study:** students read the pressure/temperature yield chart (`figures/ammonia_yield_pressure.png`) and argue for the conditions a real plant should use, weighing yield against cost and rate.

### Assessments

- **Le Châtelier shift-prediction assessment** (district checkpoint, following lesson): students are given a balanced reversible equation with a stated ΔH, then for each of several stresses (add reactant, remove product, increase pressure, raise temperature, add catalyst) they state the shift direction (left / right / no shift) and justify it with Le Châtelier reasoning.
- **Exit Ticket** (Phase 5): a *different* reversible reaction from the worksheet — the contact-process equilibrium 2SO₂(g) + O₂(g) ⇌ 2SO₃(g), ΔH = −198 kJ — for which students predict three shifts and explain the catalyst's (non)effect. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | HS-PS1-6 (refine reaction conditions to increase product at equilibrium; macroscopic and molecular level) |
| **CCC focus** | Stability and Change — a system at equilibrium is stable until stressed; it then shifts to partially counteract the stress and reach a new equilibrium. Le Châtelier's principle predicts the direction of that change. |
| **Strategy chips** | BTC (Building Thinking Classrooms — random groups + vertical surfaces + thin-slice shift-prediction prompts in Phase 2) |
| **Materials** | FeSCN²⁺ stock solutions (0.002 M Fe(NO₃)₃ and 0.002 M KSCN), extra 0.1 M Fe(NO₃)₃ and 0.1 M KSCN for "add reactant," solid Na₂HPO₄ or NaF to remove Fe³⁺, small test tubes and droppers, hot-water and ice-water baths; CoCl₂ demo set-up for the teacher (concentrated HCl, water, hot plate, fume hood); whiteboards / vertical surfaces and markers for BTC; `figures/ammonia_yield_pressure.png` projected; the 2025 NYS Chemistry Reference Tables. |
| **Safety** | FeSCN²⁺ solutions are dilute and student-safe with goggles and gloves; SCN⁻ waste goes in the labeled container, not the drain. The CoCl₂ / concentrated-HCl portion is a **teacher demonstration only** — performed in the fume hood with goggles, gloves, and apron. No student handles concentrated HCl. |
| **Prior knowledge** | Lesson 05 (Chemical Equilibrium) — dynamic equilibrium, equal forward/reverse rates, the ⇌ symbol, reversible reactions; Lesson 01–03 (collision theory, reaction energy, potential-energy diagrams) — what a catalyst does to activation energy; reading a balanced equation and identifying moles of gas. |

**Lesson objectives — students can:**

- State Le Châtelier's principle: a system at equilibrium responds to an applied stress by shifting in the direction that partially relieves the stress.
- Predict the direction an equilibrium shifts (toward reactants or products) when concentration, pressure, or temperature is changed, and justify the prediction.
- Explain why a catalyst speeds the approach to equilibrium but does **not** shift the equilibrium position or change the yield.
- Refine the conditions of the Haber process to specify changes that increase the equilibrium yield of ammonia, using Stability and Change reasoning.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers: *"Think of a tug-of-war or a balanced seesaw. What happens the instant one side suddenly pulls harder or adds weight?"* One round, one sentence each, no judgment. This surfaces the everyday intuition the whole lesson rests on: a balanced system *responds* to a disturbance, and it responds in a *predictable direction* — away from the new push.

Then post the **Do Now**:

> *"A reversible reaction has reached equilibrium — the forward and reverse rates are equal and the amounts of reactant and product stop changing. Now you suddenly add a big scoop of one of the reactants. In one sentence, predict what you think the reaction will do, and why."*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "It would make more product, because there's more reactant to react." — affirm; this is exactly the right instinct. We will give this a name and a rule today.
- "Nothing changes — it's already at equilibrium." — validate the reasoning that equilibrium means "balanced," then create the tension: *if you dump in more reactant, are the rates still equal? Which rate just sped up?*
- "It would go back to where it started." — close; probe: it does settle into a *new* balance, but is the new balance identical to the old one, or shifted? That is the question of the day.

### 3–8 min · Phenomenon hook — the ammonia paradox

**Teacher actions.** Tell the Haber-process story. Nitrogen is free — 78% of the air. Hydrogen is cheap. The reaction N₂(g) + 3H₂(g) ⇌ 2NH₃(g) makes ammonia, the basis of synthetic fertilizer that feeds about half the world. So why was ammonia impossible to make profitably for so long? Because the reaction is *reversible*: as fast as NH₃ forms, it falls apart, and the reaction stalls at a low yield. Haber's fix was not a new reaction — it was a *recipe of conditions*: high pressure, a chosen temperature, a catalyst, and continuously removing the product. Project `figures/ammonia_yield_pressure.png`.

![Line graph titled 'Haber process: NH₃ yield vs. pressure' with pressure in atmospheres on the x-axis (0 to 400 atm) and ammonia at equilibrium as a percentage on the y-axis (0 to 80%). Two concave-up-then-leveling curves rise as pressure increases: the upper purple curve labeled 400 °C climbs from about 27% at 25 atm to about 78% at 400 atm; the lower blue curve labeled 500 °C climbs from about 9% at 25 atm to about 48% at 400 atm. The lower-temperature curve sits above the higher-temperature curve at every pressure.](figures/ammonia_yield_pressure.png)

**Sample teacher language:**

> "Look at this chart. The reaction is identical at every point — same nitrogen, same hydrogen, same ammonia. But the *balance point* is different at every pressure. At 25 atmospheres and 400 degrees, only about a quarter of the gas ends up as ammonia. Crank the pressure to 400 atmospheres and suddenly almost 80% is ammonia. Same reaction — the engineers just changed the conditions and the equilibrium moved. And notice the two curves: the cooler 400-degree line sits *above* the hotter 500-degree line everywhere. So lowering the temperature also raised the yield. Today's question is the engineer's question: how do you tilt a reversible reaction toward the product you want?"

**Anticipated student responses:**

- "So more pressure means more ammonia?" — yes, in this reaction — and by the end of the period you will be able to explain *why* pressure helps this particular reaction. (Hint to bank: count the gas molecules on each side.)
- "Why does cooler give more ammonia? Usually heat speeds reactions up." — sharp observation; hold it. Cooler gives more *yield* (more product at equilibrium) but a *slower* rate. That trade-off is the heart of the Haber compromise — we'll return to it in Phase 4.
- "Can't they just get 100%?" — no reversible reaction goes to 100%, but you can push the balance a long way. That pushing is Le Châtelier's principle.

**Driving question** (post on the board and leave it there):

> *How do you tilt a reversible reaction's balance toward the product you want?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the yield chart. Then:

> "Turn to your partner: the chart shows that raising the pressure raised the ammonia yield. Make a guess — what is it about the *molecules* on the two sides of N₂ + 3H₂ ⇌ 2NH₃ that might make squeezing them help the product side? Count something."

Target insight (leave open if no one lands it yet): the left side has **4** gas molecules (1 N₂ + 3 H₂) and the right side has only **2** (2 NH₃). Squeezing the system — raising pressure — favors the side with fewer gas molecules, because that side takes up less room. We will name this in Phase 3.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–14 min · BTC launch — random groups, vertical surfaces, thin-slice prompt

**Before any vocabulary is introduced**, students build the shift-prediction intuition at vertical surfaces (see Strategy Spotlight). Form **random groups of three**. Each group claims a whiteboard / window panel with one marker that passes between members.

**Thin-slice prompt #1 (post it; do not pre-explain):**

> *"A reversible reaction sits at equilibrium: A + B ⇌ C. Picture the forward and reverse rates as exactly equal. Now you suddenly ADD more A. On your board: which rate speeds up first — forward or reverse? Which way does the amount of C go: up or down? Draw it."*

Circulate and ask only questions: *"If you add A, which reaction has more A to work with?" "If the forward rate jumps above the reverse rate, what happens to the amount of C while the system re-balances?"* Withhold the rule. Most groups will reason their way to: adding A speeds the forward reaction, so C goes up until the rates equalize again at a new balance.

### 14–22 min · Investigation — FeSCN²⁺ color-change equilibrium

Hand out the worksheet. Groups run the iron–thiocyanate equilibrium, a reversible reaction whose color *is* the position of the equilibrium:

> **Fe³⁺(aq, pale yellow) + SCN⁻(aq, colorless) ⇌ FeSCN²⁺(aq, deep red)**

Each group starts with a tube of the equilibrium mixture (orange-red). They split it across four tubes and apply one stress per tube, recording the color change and inferring the shift direction:

| Tube | Stress applied | What you observe | Shift direction (record) |
|---|---|---|---|
| 1 | Add a few drops of 0.1 M Fe(NO₃)₃ (more Fe³⁺) | red deepens | toward products (right) |
| 2 | Add a few drops of 0.1 M KSCN (more SCN⁻) | red deepens | toward products (right) |
| 3 | Add a pinch of Na₂HPO₄ or NaF (removes Fe³⁺ as a complex/precipitate) | red fades toward yellow | toward reactants (left) |
| 4 | Control — add a few drops of water only | color barely changes | little/no shift (just dilution) |

**Teacher facilitation language (circulate):**

> "The color *is* your data. Deeper red means more FeSCN²⁺ — more product. Fading red means the system is consuming FeSCN²⁺ — it shifted back toward reactants. Don't tell me 'it changed color' — tell me which way the *equilibrium moved* and what you did to move it."

**Anticipated student responses during the Investigation:**

- "Adding Fe³⁺ made it darker — so more product formed." — exactly; you added a reactant and the system responded by making more product. Bank that pattern.
- "Tube 3 went yellow — did we destroy the product?" — not destroyed; the system *shifted back*. By yanking Fe³⁺ out, you starved the forward reaction, so the reverse reaction got ahead and FeSCN²⁺ broke down. Removing a reactant shifts toward reactants.
- "The water tube didn't really change." — good control. Adding a little water dilutes everything roughly equally, so there's no strong directional stress. That's why we test against a control.

### 22–26 min · Teacher demo — temperature as a stress (CoCl₂)

Run the cobalt(II) chloride demo in the fume hood (teacher only). Present it as the equilibrium:

> **[Co(H₂O)₆]²⁺(pink) + 4 Cl⁻ ⇌ [CoCl₄]²⁻(blue) + 6 H₂O    (forward reaction is endothermic)**

Heat a blue-ish tube in a hot-water bath → it turns **bluer** (shifts toward products). Cool it in an ice bath → it turns **pinker** (shifts back toward reactants). Tell students you also have a *concentration* lever: adding concentrated HCl (more Cl⁻) drives it blue; adding water drives it pink — same direction logic as their FeSCN²⁺ tubes.

> "Temperature is a stress too — but it behaves differently from concentration. Treat heat like a substance: this forward reaction *absorbs* heat, so heat is effectively a reactant. Add heat (warm it) and the system shifts toward products — blue. Remove heat (cool it) and it shifts back — pink. Watch."

### 26–30 min · BTC thin-slice #2 + reconnect

Back to the vertical surfaces. Post **thin-slice prompt #2:**

> *"Here is the gas reaction from the Haber chart: N₂(g) + 3H₂(g) ⇌ 2NH₃(g). Count the gas molecules on each side. Now predict: if you SQUEEZE the system into a smaller volume (raise the pressure), which way should it shift — toward the 4-molecule side or the 2-molecule side — to relieve the squeeze? Justify on your board."*

Groups should reason: the system relieves a pressure increase by shifting toward the side with *fewer* gas molecules — the 2-molecule product side — which matches the rising-yield curve they saw in Phase 1. Reconnect the whole class: every stress they have tested (add reactant, remove reactant, heat, squeeze) produced a shift in the direction that *partially undoes the stress*. That single pattern is what we name next.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look at everything on your boards and in your data table. Adding a reactant pushed toward products. Removing a reactant pushed toward reactants. Heating the endothermic reaction pushed toward products. Squeezing pushed toward fewer gas molecules. Turn to your partner: what is the *one pattern* that fits every single case? Complete this: 'When you stress an equilibrium, it shifts in the direction that ______.'"

Target consensus:

> "When you stress an equilibrium, it shifts in the direction that *partially relieves* or *counteracts* the stress — using up what you added, replacing what you removed, moving away from a squeeze, or absorbing added heat."

> "Quick check before we name it: does adding a catalyst belong on this list? You learned in the energy unit that a catalyst lowers activation energy for *both* the forward and reverse reaction equally. So does it stress the balance?"

Target: no — a catalyst speeds *both* directions equally, so the equilibrium gets there *faster* but lands at the *same* position. A catalyst changes the rate, not the yield.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name the pattern you discovered. It's called **Le Châtelier's principle**: when a system at equilibrium is disturbed by a stress — a change in concentration, pressure, or temperature — the system shifts in the direction that partially relieves that stress. That is the rule behind every color change and every yield number you saw today."

> "The thing the system does in response is an **equilibrium shift** — a change in the relative amounts of reactants and products as the reaction re-balances. A shift toward products (right) makes more product; a shift toward reactants (left) makes more reactant. The shift continues only until the forward and reverse rates are equal again, at a *new* equilibrium position."

> "And the thing that pushes — the change you impose — is the **stress**: adding or removing a reactant or product, changing the volume or pressure of a gas system, or changing the temperature. Catalysts are the famous exception: a catalyst is not a stress, because it speeds the forward and reverse reactions equally. It changes how *fast* you reach equilibrium, not *where* the equilibrium sits."

Post the three terms. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "Why does raising the temperature of the Haber reaction *lower* the ammonia yield, when the chart's cooler curve is on top?" — *Expected response:* the forward reaction (making NH₃) is exothermic, so it *releases* heat — heat behaves like a product. Adding heat (raising temperature) stresses the product side, so the system shifts *back* toward reactants, lowering the yield. (Lower temperature → higher yield, as the chart shows.)
- "If a catalyst doesn't raise the yield, why does the Haber plant use an iron catalyst at all?" — *Expected response:* to reach the equilibrium *faster*. Without it, the reaction is far too slow to be practical even at high pressure. The catalyst buys speed, not yield.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Refine the Haber conditions + Because/But/So

Students return to the yield chart and now act as the plant engineer (the HS-PS1-6 "refine the design" move). On their worksheet they specify, for N₂(g) + 3H₂(g) ⇌ 2NH₃(g), ΔH = −92 kJ, a change in each lever that would *increase* the ammonia yield, and justify it with Le Châtelier reasoning:

| Lever | Change that increases NH₃ yield | Why (Le Châtelier) |
|---|---|---|
| Pressure | increase pressure | shifts toward the 2-molecule product side (fewer gas molecules) |
| Temperature | decrease temperature | forward reaction is exothermic; removing heat shifts toward products |
| Concentration | remove NH₃ as it forms (and/or feed in more N₂/H₂) | removing product shifts the system to replace it → more product |
| Catalyst | add iron catalyst | does **not** shift the equilibrium — only speeds the approach to it |

Then model a **Because / But / So** sentence on the board capturing the central trade-off:

> "Lowering the temperature should raise the ammonia yield **because** the forward reaction is exothermic, so removing heat shifts the equilibrium toward the products — **but** a lower temperature also makes the reaction much *slower*, so the plant would wait far too long for any ammonia — **so** real engineers choose a *compromise* temperature near 450 °C and add an iron catalyst, accepting a slightly lower equilibrium yield in exchange for a usable reaction rate."

Have students write their own B/B/S for the **pressure** lever, using the starter: *"Industrial plants run the Haber process at very high pressure because… but… so…"* (Anticipated: *because* high pressure shifts the equilibrium toward the fewer-molecule product side, raising yield; *but* very high pressure requires expensive, heavy reinforced equipment and lots of energy to compress the gas; *so* plants settle near 200 atm as a cost-versus-yield compromise.)

### 39–40 min · Return to the phenomenon

> "Return to the opening paradox. Nitrogen was free, hydrogen was cheap, and the reaction was known — yet ammonia was impossible to make profitably until Haber. In one sentence using the words *stress* and *shift*, explain what Haber actually changed."

Target: "Haber didn't change the reaction; he changed the *conditions* — applying stresses (high pressure, controlled temperature, constant removal of ammonia) that each shift the equilibrium toward the product side, plus a catalyst to reach that shifted equilibrium fast enough to be practical."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud the **contact-process** equilibrium — a *different* reaction from the FeSCN²⁺ and Haber work, so students must transfer the reasoning, not recall an answer:

> *Consider:* **2 SO₂(g) + O₂(g) ⇌ 2 SO₃(g),   ΔH = −198 kJ** *(forward reaction is exothermic).*
> *(a) Predict the shift if you increase the pressure. Justify by counting gas molecules.*
> *(b) Predict the shift if you raise the temperature. Justify using the sign of ΔH.*
> *(c) A factory adds a vanadium(V) oxide catalyst. What happens to the equilibrium position, and why?*

Expected answers are in `Answer_Key.docx`.

**Closing Reflection (SEL, 30 seconds):**

> "Today you learned that you can *steer* a reaction's balance instead of just watching it. In one sentence: what is one moment today — a color change, a yield curve, a classmate's argument at the board — that made an equilibrium shift finally click for you, and who or what helped?"

Collect worksheets; note which students correctly treat **heat as a reactant or product** (the most common temperature pitfall) and which still think a **catalyst changes the yield**. Target those two ideas in a brief opener next lesson.

---

## Common Misconceptions

- **Misconception:** "A catalyst shifts the equilibrium toward products and increases the yield." → **Correction:** A catalyst lowers the activation energy of the forward *and* reverse reactions by the *same* amount, so it speeds both directions equally. The system reaches equilibrium faster, but at the *same* position — the yield is unchanged. The Haber plant uses iron for speed, not yield.
- **Misconception:** "When the equilibrium shifts right, the reverse reaction stops." → **Correction:** Both reactions continue the whole time. A "shift right" means the forward rate temporarily exceeds the reverse rate, so product builds up, until the rates become equal again at a new equilibrium. Equilibrium is dynamic, not static, before and after the shift.
- **Misconception:** "Adding heat is just like adding a reactant — it always shifts toward products." → **Correction:** Heat behaves like a reactant only for an *endothermic* forward reaction. For an *exothermic* forward reaction, heat is effectively a *product*, so adding heat shifts the system *back toward reactants*. You must check the sign of ΔH first. (This is why cooler temperatures raise the Haber yield.)
- **Misconception:** "Increasing pressure always shifts the equilibrium toward products." → **Correction:** Increasing pressure (by decreasing volume) shifts toward the side with *fewer moles of gas*. It only favors products if the product side has fewer gas molecules. If both sides have equal moles of gas, a pressure change causes no shift at all.
- **Misconception:** "Diluting a solution with water has no effect on an aqueous equilibrium." → **Correction:** Adding water can shift an aqueous equilibrium toward the side with *more* dissolved particles (it lowers all concentrations, and the system responds to restore them). In the FeSCN²⁺ control, the dilution effect is small and roughly symmetric, which is why the control tube barely changes — but dilution is not always neutral.

---

## Access & Differentiation

- **ELL/ENL supports:** Shift-direction sentence frame displayed all period: *"I added/removed ___, so the equilibrium shifted toward the ___ to ___ the stress."* Word-choice box on the board: {equilibrium, shift, stress, reactant, product, left, right, catalyst, pressure, temperature}. Color-code the directions consistently — a left-pointing arrow for "toward reactants," a right-pointing arrow for "toward products" — and pair each with a gesture. Provide the FeSCN²⁺ equation pre-printed with the colors labeled under each species so the language load is on the *reasoning*, not the vocabulary.
- **IEP/SPED supports:** Provide a pre-filled stress-and-shift table where the "stress applied" column is already written and the student fills only the observed color and the shift direction (a left/right choice, not free recall). Give a "heat as a substance" reference card: *endothermic forward → heat is a reactant; exothermic forward → heat is a product.* Assign clear BTC group roles (marker-holder, equation-counter, recorder). Calculator is not needed — the work is directional reasoning, not arithmetic.
- **Extensions:** (1) For N₂(g) + 3H₂(g) ⇌ 2NH₃(g), explain why adding an *inert* gas (e.g., argon) at constant volume does **not** shift the equilibrium, even though the total pressure rises. (2) Research why ammonia is continuously *condensed out* of the Haber reactor and recycled — connect "removing product" to a higher overall conversion than any single pass. (3) Predict and explain the shift for the endothermic reaction of the CoCl₂ demo when (a) silver nitrate is added (Ag⁺ removes Cl⁻ as AgCl) and (b) the tube is plunged into ice.

---

## Strategy Spotlight

**BTC — Building Thinking Classrooms.** The Building Thinking Classrooms framework (Peter Liljedahl, *Building Thinking Classrooms in Mathematics*, 2021) centers three core practices that consistently raise the level of student thinking: (1) **random grouping** removes status hierarchies and friend-group comfort zones; (2) **vertical non-permanent surfaces** (whiteboards, windows, chart paper) make thinking visible, erasable, and shared; and (3) **thin-slice prompts** launch students into reasoning *before* any direct instruction, so the thinking happens before the consolidation.

**How BTC runs in this lesson (Phase 2, minutes 10–30):**

1. **Random groups:** Use a card randomizer or a roster shuffle to form groups of three. Announce: "These are your working groups for the next 20 minutes — find your vertical surface."
2. **Vertical surfaces:** Each group claims a whiteboard panel, a window with a dry-erase marker, or standing-height chart paper. *One marker per group*, passed between members so all three write and argue.
3. **Thin-slice prompts:** The two prompts ("add reactant A → which way does C go?" and "squeeze N₂ + 3H₂ ⇌ 2NH₃ → which side?") are calibrated to be *just* beyond solo reach but reachable as a group. Students predict the shift direction *before* the term "Le Châtelier" exists for them — they build the rule from the FeSCN²⁺ data and the molecule count, then Phase 3 simply *names* what they already did.
4. **Teacher as knowledge-withholder:** While groups work, circulate and ask only questions — never state the rule. "Which rate just sped up?" "Which side has fewer gas molecules?" "Is the new balance the same as the old one?" The goal is for students to arrive at "shifts to relieve the stress" themselves.
5. **Built-in consensus:** The reconnect at minute 30 turns the boards into a gallery — groups see that *every* stress produced a shift in the same logical direction, which is the consolidation moment.

**Why BTC fits Le Châtelier:** Shift prediction is a single, transferable rule that *emerges* cleanly from a handful of cases — the perfect thin-slice. Because students generate the rule from their own FeSCN²⁺ color data and molecule-counting before it is named, the Phase 3 vocabulary labels a pattern they already own, and the Phase 5 transfer to a brand-new reaction (the contact process) is far more reliable than it would be after a lecture-first sequence.

**CRSE connection:** The anchoring phenomenon — the Haber process — is a powerful equity story: synthetic ammonia fertilizer is estimated to sustain roughly half the world's population, making this lesson's chemistry directly relevant to global food security and to students whose families farm or come from agricultural regions. Inviting students to name a food or crop important in their family and asking where its fertilizer comes from grounds an abstract gas-phase equilibrium in lived, global experience. The random-grouping practice is itself a CRSE move: it disrupts the social sorting that concentrates academic authority in a few students and signals that every student's reasoning belongs on the board.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — Haber ammonia paradox and `ammonia_yield_pressure.png` yield curves; return in Phase 4 with the "what did Haber actually change?" prompt |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — count molecules on each side of N₂ + 3H₂ ⇌ 2NH₃); Phase 3 (TT#2 — the one pattern that fits every stress; the catalyst check) |
| 3 | Students develop questions/models/procedures | Phase 2 BTC thin-slice predictions at vertical surfaces; FeSCN²⁺ four-tube investigation; Phase 4 engineer's refine-the-conditions table |
| 4 | CCC defined and used | Lesson Overview · *Stability and Change*; explicit in Phase 3 consensus ("stable until stressed, then shifts") and Phase 4 Haber-conditions refinement |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: Le Châtelier's principle / equilibrium shift / stress |
| 6 | Revisit phenomenon with evidence | Phase 4 — students use the yield curves and their FeSCN²⁺ data to specify the conditions that raise NH₃ yield and explain the opening paradox |
| 7 | ENL/SPED supports | Access & Differentiation block: shift-direction sentence frame, word-choice box, color-coded arrows, pre-filled stress table, "heat as a substance" card, BTC group roles |
| 8 | Assessment check | Phase 5 — Exit Ticket on the contact process (2SO₂ + O₂ ⇌ 2SO₃): pressure shift, temperature shift, catalyst effect |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked shift-prediction example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **Le Châtelier's principle** — the rule that when a system at equilibrium is disturbed by a stress (a change in concentration, pressure, or temperature), the system shifts in the direction that partially relieves the stress and reaches a new equilibrium
- **equilibrium shift** — a change in the relative amounts of reactants and products as a stressed system re-balances; a shift "right" (toward products) makes more product, a shift "left" (toward reactants) makes more reactant; the shift continues only until the forward and reverse rates are equal again
- **stress** — a change imposed on a system at equilibrium — adding or removing a reactant or product, changing the pressure/volume of a gas system, or changing the temperature; a catalyst is *not* a stress, because it speeds the forward and reverse reactions equally and does not shift the equilibrium position
