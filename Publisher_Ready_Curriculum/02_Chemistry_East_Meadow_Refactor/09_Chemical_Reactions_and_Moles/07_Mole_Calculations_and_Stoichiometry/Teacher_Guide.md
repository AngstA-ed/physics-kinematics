# Mole Calculations & Stoichiometry — Teacher Guide

## Cover

**Unit: Chemical Reactions & Moles — Lesson 07: Mole Calculations & Stoichiometry**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: ACTIVE LEARNING

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

**HS-PS1-7** — *"Use mathematical representations to support the claim that atoms, and therefore mass, are conserved during a chemical reaction."* This lesson operationalizes the standard through three East Meadow assessment objectives. **1.a.iii** — students *use balanced chemical equations* as the source of the mole ratios that drive every calculation. **2.b.i** — given a chemical reaction, students *use mathematical representations to predict the relative number of atoms (and moles) in reactants vs. products* at the atomic-molecular scale; the coefficients in a balanced equation are that mathematical representation. **2.b.ii** — given a chemical reaction, students *calculate the mass of any component given any other component*, moving fluently along the mass → mole → mole → mass pathway.

The Cross-Cutting Concept of **Energy and Matter (conservation, flows, transfers)** is the explicit lens: in a closed reaction every atom present in the reactants reappears in the products, so the *count* of each kind of atom is conserved even as the molecules regroup. The balanced equation's coefficients are the bookkeeping that makes this conservation quantitative — they fix the ratio in which substances must combine and the ratio in which products form. Stoichiometry is prerequisite to limiting-reactant work, percent yield, and solution stoichiometry later in the course; per East Meadow guidance, mole-ratio fluency is the single most leveraged skill in the quantitative half of Regents chemistry.

### Phenomenon

A campfire is burning steadily. There is still a large pile of dry wood next to it, and the fire is out in the open air — there is plenty of air around it. Yet the flames shrink, then die, leaving a bed of glowing coals and unburned wood. Why does a fire go out *even when fuel is left and air is all around it*? Bank the same coals tightly under a heap of ash, or crowd the logs so air cannot flow between them, and the fire starves: the combustion reaction needs **oxygen** delivered in a fixed ratio to the fuel it is burning, and the moment one reactant can no longer reach the reaction in that ratio, the reaction stops — no matter how much of the *other* reactant remains. The leftover wood is **excess reactant**; the oxygen that ran out at the flame front is the **limiting reactant**.

**Driving question:** Why does a campfire go out even when there is still wood and air left — and how does a balanced equation let us predict exactly how much product a reaction can make?

### Javalab / Labs

- **S'mores stoichiometry (ABCs opener):** Treat the recipe `1 chocolate + 2 graham-halves + 1 marshmallow → 1 s'more` as a balanced equation. Give each group a bag with a deliberately mismatched count (e.g., 8 chocolate, 10 graham-halves, 12 marshmallows). Students assemble as many complete s'mores as possible, record what runs out first and what is left over, then connect "ran out first" to **limiting reactant** and "left over" to **excess**. Connect to the bar chart in `figures/limiting_reactant_smores.png`.
- **Limiting-reactant micro-lab (Mg + HCl):** Drop a measured ribbon of magnesium into excess hydrochloric acid in a test tube. The reaction `Mg + 2 HCl → MgCl₂ + H₂` fizzes vigorously and then stops — the Mg disappears entirely while acid remains, so Mg is the limiting reactant. Students measure the mass of Mg, then *calculate* the mass of H₂ gas predicted to be released (mass → mole → mole → mass). Qualitative observation: bubbling stops when the metal is gone, not when the acid is gone.
- **Particle-diagram reading:** Students interpret `figures/conservation_of_atoms.png` to verify that the number of each kind of atom is identical on both sides of `2 H₂ + O₂ → 2 H₂O` — the visual proof that mass is conserved and that coefficients (not subscripts alone) set the reacting ratio.

### Assessments

- **Stoichiometry problem set** (district checkpoint, following lesson; see `Assessments/` folder once created): mole-mole, mass-mole, and mass-mass conversions from balanced equations, plus one qualitative limiting-reactant item.
- **Lab calculation report** (Mg + HCl micro-lab): students report the mass of Mg used, the predicted mass of H₂, the full dimensional-analysis setup, and a sentence naming the limiting reactant with justification.
- **Exit Ticket** (Phase 5): three items on the combustion of methane `CH₄ + 2 O₂ → CO₂ + 2 H₂O` — a mole-mole conversion, a mass-mole conversion, and a one-sentence explanation of why a fire stops when one reactant runs out. See `Answer_Key.docx`. (Distinct reaction and distinct values from the worksheet practice.)

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | HS-PS1-7 (1.a.iii balanced equations; 2.b.i predict relative atom/mole counts; 2.b.ii calculate mass of any component from any other) |
| **CCC focus** | Energy and Matter — atoms (and therefore mass) are conserved in a reaction; the coefficients of a balanced equation are the mathematical representation of the fixed ratio in which substances react and form |
| **Strategy chips** | ACTIVE LEARNING — hands-on s'mores build and Mg + HCl micro-lab generate the mole-ratio concept *before* the term is named; students compute, predict, and verify rather than copy |
| **Materials** | 2025 NYS Chemistry Reference Tables (Periodic Table for molar masses), calculators, s'mores manipulatives or counters (chocolate/graham/marshmallow tokens), Mg ribbon + dilute HCl + test tubes (teacher demo or micro-lab), `figures/limiting_reactant_smores.png` and `figures/conservation_of_atoms.png` projected |
| **Safety** | Mg + HCl micro-lab: wear goggles and apron; HCl is corrosive — use dilute (≈1 M) acid, small volumes, and a test-tube rack. Hydrogen gas is flammable — no open flame near the reaction. S'mores tokens are non-edible manipulatives (do not eat lab materials). |
| **Prior knowledge** | Lesson 01 (Writing & Balancing Equations) — students can balance an equation and read coefficients; Lesson 02 (Conservation of Matter) — atoms are conserved; Lesson 05 (Defining the Mole) and Lesson 06 of Unit 1 (Gram Formula Mass) — the mole as a count, molar mass as the g ↔ mol bridge. |

**Lesson objectives — students can:**

- Read the mole ratio between any two substances directly from the coefficients of a balanced chemical equation.
- Carry out a mole-mole conversion using a balanced equation (predict moles of a product or second reactant from moles of a given substance).
- Carry out mass-mole and mass-mass conversions by chaining molar mass with the mole ratio (mass → mole → mole → mass).
- Explain, using the campfire phenomenon and the term *limiting reactant*, why a reaction stops when one reactant is used up even though the other reactant remains.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers in one sentence: *"Think of a time you were making or building something and ran out of one ingredient or part while you still had plenty of everything else. What were you making, and what ran out?"* One round, one sentence each, pass allowed. This surfaces the everyday intuition behind limiting reactants — that the thing you run out of *first* caps what you can make, no matter how much of the rest you have.

Then post the **Do Now**:

> *"You are making sandwiches. Each sandwich needs 2 slices of bread and 1 slice of cheese. You have 10 slices of bread and 8 slices of cheese. How many complete sandwiches can you make? What is left over, and how much?"*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "5 sandwiches, and 3 cheese left over." — correct; ask *what ran out first* (bread) and confirm that the bread, not the cheese, set the limit.
- "8 sandwiches." — probe: each sandwich needs *2* breads. With 10 breads you can only build 5. The 2:1 ratio is the constraint.
- "10 sandwiches because I have 10 bread." — redirect to the ratio: 2 slices *per* sandwich, so 10 ÷ 2 = 5. The recipe ratio is doing the work.

### 3–8 min · Phenomenon hook — the campfire that goes out

**Teacher actions.** Tell the campfire story vividly. A fire is roaring; a tall pile of dry wood sits right beside it; the air in the clearing is open. Then the fire shrinks and dies to glowing coals — with unburned wood still stacked next to it. Ask: *how can a fire go out when there is still fuel and still air?*

> "Wood doesn't burn by itself — it burns by reacting with oxygen. Combustion is a chemical reaction: fuel **plus oxygen** turns into carbon dioxide and water vapor. And like every reaction, it happens in a fixed ratio. At the flame front, if oxygen can't reach the wood fast enough — because the logs are packed too tight, or the coals are buried in ash — then oxygen becomes the thing that runs out *first*. The reaction stops. The leftover wood is exactly like your leftover cheese: there's plenty of it, but it has nothing to react with."

**Anticipated student responses:**

- "So the fire ran out of air even though air was around it?" — yes; *available in the room* is not the same as *delivered to the reaction in the right ratio*. Buried coals can't pull in oxygen fast enough.
- "The wood is the leftover, like the extra cheese." — exactly the connection we want; the wood is the **excess reactant**.
- "If you spread the logs out it burns again." — great observation; spreading the logs restores oxygen flow, so oxygen is no longer the one that runs out.

**Driving question** (post on the board and leave it there):

> *Why does a campfire go out even when there is still wood and air left — and how does a balanced equation let us predict exactly how much product a reaction can make?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the campfire and the sandwich Do Now. Then:

> "Turn to your partner: in the sandwich problem, why couldn't you use all 8 cheese slices? Connect that to the campfire — what is the campfire's version of 'running out of bread'?"

Target insight: a fixed recipe ratio means one ingredient runs out before the others. For the campfire, oxygen at the flame front is the ingredient that runs out, so it caps how much wood can actually burn. Leave the formal term unnamed for now.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–16 min · ABCs Activity — S'mores stoichiometry before any formal term

**Before any vocabulary is introduced**, students build mole-ratio intuition with their hands. Give each group a recipe written like an equation and a bag of mismatched ingredients.

> **Recipe (treat it like a balanced equation):**
> `1 chocolate + 2 graham-halves + 1 marshmallow → 1 s'more`
> **Your bag holds:** 8 chocolate, 10 graham-halves, 12 marshmallows.

The task:

> "Build as many *complete* s'mores as you can. Then answer: How many s'mores did you make? Which ingredient ran out first? Which ingredients are left over, and how many of each?"

Have students record results, then project `figures/limiting_reactant_smores.png`:

![Bar chart titled 'Limiting reactant: the smallest bar sets the yield' with three purple bars showing how many complete s'mores each ingredient could make on its own: Chocolate (8 available) reaches 8, Graham pairs (10 available) reaches 5, and Marshmallows (12 available) reaches 12; the y-axis is labeled 'S'mores this ingredient can make'; the graham-pairs bar is clearly the shortest, marking it as the limiting ingredient.](figures/limiting_reactant_smores.png)

**Teacher facilitation language (circulate):**

> "Don't divide every number the same way. The recipe says *2* graham-halves per s'more but only *1* chocolate per s'more. So how many s'mores can the grahams alone make? How many can the chocolate alone make? The smallest of those numbers is your answer."

> "Look at the bar chart. Each bar is *how many s'mores that one ingredient could make if nothing else ran out.* Which bar is shortest? That ingredient is the bottleneck."

**Anticipated student responses during ABCs:**

- "I made 8 s'mores because I had 8 chocolate." — probe: do you have enough grahams for 8 s'mores? You'd need 16 graham-halves but only have 10. The grahams stop you at 5.
- "Grahams ran out first — I made 5 and have 3 chocolate and 7 marshmallows left." — exactly right; that is the limiting/excess pattern, named formally in Phase 3.
- "Why does the 2 in front of grahams matter so much?" — because it doubles how fast grahams get used. The coefficient is the ratio, and ratios decide who runs out first.

### 16–22 min · Initial Model — read a mole ratio and do a first mole-mole conversion

**Prompt on the board** (before naming the process):

> *"Here is a real balanced equation:* `Mg + 2 HCl → MgCl₂ + H₂`. *The coefficients are the recipe. If you fully react* **0.50 mol of Mg**, *how many moles of H₂ gas should you make? Use the coefficients the same way you used the s'mores recipe."*

Students work individually for 3 minutes, then compare with a partner.

Target answer:

> Mole ratio from the equation: 1 mol Mg → 1 mol H₂.
> 0.50 mol Mg × (1 mol H₂ / 1 mol Mg) = **0.50 mol H₂**.

**Teacher facilitation language:**

> "Where do the numbers 1 and 1 come from? Not the subscripts — the *coefficients* in front of Mg and H₂. The coefficient on Mg is 1 (invisible), the coefficient on H₂ is 1. That 1:1 is the mole ratio."

> "Now ask your partner: how many moles of HCl would you need for that 0.50 mol Mg? Look at the coefficient on HCl."

**Anticipated student responses:**

- "0.50 mol H₂ — same number because the ratio is 1 to 1." — exactly; the equal coefficients make this one easy, which is why we started here.
- "Do I need 0.50 mol HCl too?" — check the coefficient: HCl has a 2 in front. 0.50 mol Mg × (2 mol HCl / 1 mol Mg) = 1.0 mol HCl. The 2 doubles it.
- "Where do I look up the ratio?" — only in the balanced equation; the coefficients *are* the ratio. Nothing on the Periodic Table gives you the ratio.

### 22–30 min · Investigation — group mass-mass and mass-mole practice

Groups of three or four work through a structured practice set built on the same reaction `Mg + 2 HCl → MgCl₂ + H₂`. Each student writes the full dimensional-analysis chain individually, then compares with the group. Molar masses (from the Periodic Table): Mg = 24.3, HCl = 36.5, MgCl₂ = 95.3, H₂ = 2.0 g/mol.

**Practice set (distributed as a half-sheet or on the board):**

**Problem A — mole-mole (warm-up):** Starting from **1.0 mol Mg**, how many mol H₂ form? How many mol HCl are required?

> 1.0 mol Mg × (1 mol H₂ / 1 mol Mg) = **1.0 mol H₂**
> 1.0 mol Mg × (2 mol HCl / 1 mol Mg) = **2.0 mol HCl**

**Problem B — mole-mass:** Starting from **1.0 mol Mg**, what mass of MgCl₂ forms?

> 1.0 mol Mg × (1 mol MgCl₂ / 1 mol Mg) × (95.3 g MgCl₂ / 1 mol MgCl₂) = **95.3 g MgCl₂**

**Problem C — mass-mass:** A ribbon of **4.86 g Mg** reacts completely. What mass of H₂ gas is produced?

> 4.86 g Mg × (1 mol Mg / 24.3 g) × (1 mol H₂ / 1 mol Mg) × (2.0 g H₂ / 1 mol H₂) = **0.40 g H₂**

(Check: 4.86 g ÷ 24.3 = 0.200 mol Mg → 0.200 mol H₂ → 0.200 × 2.0 = 0.40 g.)

**Teacher facilitation prompts (circulate):**

> "Every problem follows the same road map: **grams → moles → moles → grams.** Use molar mass to turn grams into moles, use the *coefficient ratio* to cross from one substance to the other, then use molar mass again to turn moles back into grams."

> "For Problem C, what is the *bridge* step that crosses from Mg to H₂? It is the mole ratio (1:1), and it can only come from the balanced equation."

> "Check your units. If a conversion factor is upside-down, your units won't cancel and you'll end up with g²/mol — a sign you flipped a factor."

**Anticipated student responses:**

- On Problem C: "I got 9.72 g — I multiplied 4.86 by 2." — redirect: you skipped the move into moles. You must divide by the molar mass of Mg first; you can't multiply grams of Mg by a mole ratio directly.
- On Problem B: "Why MgCl₂ and not MgCl?" — the balanced formula is MgCl₂ (Mg²⁺ with two Cl⁻); molar mass 24.3 + 2(35.5) = 95.3 g/mol.
- "The ratio is 1:1 again so the moles didn't change." — right for Mg → H₂ and Mg → MgCl₂; the *mass* still changes because the molar masses differ. Same moles, different grams.

### 28–30 min · Reconnect + surface the method

Bring groups back together. Ask one group to put the full Problem C chain on the board. Ask the class:

> "Point to the exact step where we crossed from magnesium to hydrogen. What numbers made that crossing possible?"

Surface the key idea: the **coefficients of the balanced equation** are the only thing that lets you cross from one substance to another. Molar mass converts grams ↔ moles *within* a substance; the coefficient ratio converts moles ↔ moles *between* substances. Every stoichiometry problem is the same three-step bridge.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look at the completed Problem C chain. Turn to your partner: which single number in that chain came from the *balanced equation* and nowhere else? And what would change in your answer if the equation had been `Mg + 2 HCl → MgCl₂ + 2 H₂` instead?"

Target consensus: the **mole ratio** (the coefficient ratio) comes only from the balanced equation. Molar masses come from the Periodic Table; the ratio comes from the coefficients. If the H₂ coefficient were 2, every mole of Mg would make 2 mol H₂, doubling the predicted mass of hydrogen.

> "Now back to the campfire. In `fuel + O₂ → CO₂ + H₂O`, if the oxygen at the flame front runs out, what happens to the leftover fuel? Use the s'mores language."

Target: the fuel becomes the leftover (excess), and no more product forms because the reactant that ran out first (oxygen) is gone. The ratio in the equation decides which one runs out.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name what we've been doing all period. **Stoichiometry** is the math of using a balanced equation to calculate how much reactant is needed or how much product forms. Every stoichiometry problem rests on one tool: the **mole ratio** — the ratio of coefficients between any two substances in the balanced equation. The mole ratio is the bridge that lets you cross from moles of one substance to moles of another. In `Mg + 2 HCl → MgCl₂ + H₂`, the mole ratio of HCl to Mg is 2:1, and the mole ratio of Mg to H₂ is 1:1."

> "And here is the campfire word. When two reactants are mixed, one usually runs out before the other. The reactant that runs out first — the one that *limits* how much product can form — is the **limiting reactant**. The one left over is the *excess* reactant. In your s'mores bag, the graham-halves were the limiting reactant; the marshmallows were in excess. At the campfire, oxygen at the flame front is the limiting reactant, and the unburned wood is the excess."

> "These three ideas lock together: you read the **mole ratio** from a balanced equation, you use it to do **stoichiometry** calculations, and when reactants are mismatched, the ratio tells you which one is the **limiting reactant** that caps the product."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "In `Mg + 2 HCl → MgCl₂ + H₂`, what is the mole ratio of HCl to H₂?" — *Expected response:* 2 mol HCl : 1 mol H₂, read straight from the coefficients (2 and 1).
- "If you keep adding wood to a fire but never improve airflow, will the fire get bigger forever?" — *Expected response:* No — oxygen is the limiting reactant; adding more of the excess reactant (wood) does not make more product once the limiting reactant is the bottleneck.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the model + Because/But/So expansion

Students return to their Initial Model (the `Mg + 2 HCl → MgCl₂ + H₂` mole-mole work). They annotate it with vocabulary: label the coefficient ratio as the *"mole ratio,"* label the full chain as *"stoichiometry,"* and add a one-line note identifying which reactant would be limiting if only a small amount of Mg were dropped into a large excess of acid (answer: Mg is limiting).

Then run a **Because / But / So** sentence about the campfire phenomenon. Starter on the board:

> *"A campfire goes out even though a pile of dry wood is still sitting right next to it."*

Model one aloud:

> "A campfire goes out even with wood left **because** combustion needs oxygen delivered to the fuel in a fixed ratio, and once the oxygen reaching the flame front runs out, oxygen becomes the limiting reactant — **but** the leftover wood is the excess reactant and has nothing left to react with — **so** the reaction stops and the fire dies, even though plenty of fuel remains, because product can only form while *both* reactants are available in the ratio the balanced equation requires."

Then have students write their own B/B/S using one of these starters:

- *"A student drops a small ribbon of Mg into a large beaker of HCl, and the bubbling stops while acid is still left in the beaker…"* (hint: which reactant ran out?)
- *"In the s'mores activity I had marshmallows and chocolate left over but could not make any more s'mores…"*

**Anticipated student responses:**

- "Because the Mg all dissolved, but there was still acid, so Mg was the limiting reactant." — strong; push for the *so*: "so no more H₂ could form once the magnesium was gone, even with acid remaining."
- "Because I ran out of graham-halves." — good start; add the ratio: "because the recipe needs 2 graham-halves per s'more, so the grahams ran out twice as fast and limited the yield."

### 39–40 min · Return to the phenomenon

> "Return to the campfire. We started by asking how a fire can die with wood and air still around. Now you have the words. Quickly: in `fuel + O₂ → products`, if oxygen is the limiting reactant, what is the wood? And could you, in principle, calculate how much CO₂ a given mass of wood *would* make if it burned completely?"

Target: the wood is the excess reactant; and yes — given a balanced combustion equation and the molar masses, the same grams → moles → moles → grams chain predicts the CO₂ produced. The chemistry isn't magic: the balanced equation is the recipe, and stoichiometry reads the recipe quantitatively.

> "That bridge — coefficients to grams — is what lets a chemist scale a reaction up from a test tube to a factory and know exactly how much to load in and how much will come out."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud (uses the combustion of methane, `CH₄ + 2 O₂ → CO₂ + 2 H₂O` — molar masses CH₄ = 16.0, O₂ = 32.0, CO₂ = 44.0 g/mol):

> *(a) Mole-mole: If 3.0 mol of CH₄ burns completely, how many moles of O₂ are required? Show the mole ratio you used.*
> *(b) Mass-mole: If 8.0 g of CH₄ burns completely, how many moles of CO₂ form? Show the grams → moles → moles chain.*
> *(c) In one sentence, explain why a flame goes out when the oxygen around it is used up, even if unburned fuel remains — use the term* **limiting reactant**.

Expected answers are in `Answer_Key.docx`.

**Closing Reflection (SEL, 30 seconds):**

> "Today we learned to read a balanced equation as a recipe and predict exactly how much a reaction can make. In one sentence: what is one thing that clicked for you about why reactions stop, and who in your group helped you see it?"

Collect worksheets; note which students correctly inserted the *mole ratio* step versus students who tried to cross from one substance to another without it (multiplying grams by grams, or skipping the coefficient). The missing-mole-ratio error is the central procedural stumbling block — target those students for a brief one-on-one check at the start of the next lesson.

---

## Common Misconceptions

- **Misconception:** "The mole ratio comes from the subscripts in the formulas." → **Correction:** The mole ratio comes from the **coefficients** in front of each formula in the *balanced* equation, not from the subscripts inside a formula. In `Mg + 2 HCl → MgCl₂ + H₂`, the 2 in front of HCl is the coefficient that sets the 2:1 ratio of HCl to Mg; the subscript inside H₂ tells you a molecule contains 2 H atoms but does not set the reacting ratio.
- **Misconception:** "I can convert grams of one substance directly to grams of another by using the mole ratio." → **Correction:** The mole ratio relates **moles to moles**, never grams to grams. You must first convert grams to moles (divide by molar mass), then apply the mole ratio, then convert moles back to grams (multiply by the other molar mass). Skipping the move into moles is the most common stoichiometry error.
- **Misconception:** "The reactant you have *more* of (by mass or by count) is the one in excess." → **Correction:** The limiting reactant is decided by the *ratio*, not the raw amount. In the s'mores bag there were more graham-halves (10) than chocolate (8), yet grahams were limiting because the recipe needs 2 grahams per s'more. You must compare amounts *against the coefficient ratio*, not against each other directly.
- **Misconception:** "Adding more of the excess reactant makes more product." → **Correction:** Once the limiting reactant is gone, the reaction stops. Adding more wood to a fire whose oxygen has run out makes no more product — the limiting reactant caps the yield. More excess reactant just means more left over.
- **Misconception:** "Mass is not conserved because the product weighs a different amount than the reactant I started with." → **Correction:** *Total* mass is conserved — every atom in the reactants reappears in the products (see `conservation_of_atoms.png`). The mass of one *named* component (e.g., just the H₂) differs from the mass of the Mg because they are different substances with different molar masses; the conserved quantity is the sum of all reactants equaling the sum of all products.

---

## Access & Differentiation

- **ELL/ENL supports:** Stoichiometry road-map strip displayed on every desk: `grams (given) → ÷ molar mass → moles → × mole ratio → moles → × molar mass → grams (wanted)`. Sentence frame: *"The mole ratio of ___ to ___ is ___ : ___ because the coefficients in the balanced equation are ___ and ___."* Word-choice box on the board throughout: {stoichiometry, mole ratio, limiting reactant, excess, coefficient, molar mass}. Pair every calculation with the s'mores bar chart so the abstract ratio has a concrete visual anchor.
- **IEP/SPED supports:** Pre-fill the molar masses for the substances used in practice (Mg = 24.3, HCl = 36.5, MgCl₂ = 95.3, H₂ = 2.0, CH₄ = 16.0, O₂ = 32.0, CO₂ = 44.0 g/mol) on a reference card so the Periodic Table lookup is removed as a barrier. Provide a pre-drawn three-box conversion template (grams → moles → moles → grams) where the student writes one number per box in sequence. Calculator use expected for all arithmetic; the conceptual targets are identifying the mole ratio and ordering the steps.
- **Extensions:** (1) **Limiting-reactant calculation (quantitative):** 6.0 g of Mg is added to 0.10 mol of HCl. Which is the limiting reactant, and what mass of H₂ forms? (Compute moles of each, compare to the 1:2 ratio.) (2) **Percent yield primer:** the Mg + HCl micro-lab predicted 0.40 g of H₂ from 4.86 g Mg, but the measured H₂ was 0.36 g — what fraction of the predicted product was actually collected, and name two reasons real yield falls short. (3) **Scale-up:** a factory must produce 1.00 kg of MgCl₂ by this reaction — what mass of Mg must it load in? Carry the full grams → moles → moles → grams chain at industrial scale.

---

## Strategy Spotlight

**ACTIVE LEARNING — concept before vocabulary, hands before symbols.** Active learning means students generate the central idea through doing, then attach the formal name afterward. This lesson is built so that *every* abstract term in Phase 3 is the name for something students have already physically done or calculated in Phase 2. The mole-ratio concept is not lectured; it is discovered by building s'mores from a mismatched bag and noticing that one ingredient runs out first.

**How to run it in this lesson (Phase 2 → Phase 3):**

1. **Hands-on first (s'mores ABCs):** students assemble products from a deliberately mismatched recipe and record what runs out and what is left. They experience "limiting" and "excess" before the words exist.
2. **Symbolic transfer (Mg + HCl):** students immediately re-encounter the same logic in a real balanced equation, doing mole-mole then mass-mass conversions. The recipe ratio they just used by hand becomes the *coefficient ratio* on paper.
3. **Name it last (Phase 3):** only after students have computed correct answers does the teacher attach the words *stoichiometry, mole ratio, limiting reactant.* The vocabulary lands on top of lived experience, so it sticks.

**Why active learning fits stoichiometry:** Stoichiometry fails for students when it is taught as a memorized algorithm divorced from meaning — they plug numbers without knowing why the mole ratio belongs in the middle. By having students *run out of graham crackers* before they ever see a coefficient, the bottleneck becomes intuitive: of course the ratio decides who runs out first; they just watched it happen. The Mg + HCl micro-lab then closes the loop — they predict a mass of H₂ and can, in the lab report, compare it to what actually bubbles off.

**CRSE connection:** The opening circle prompt (running out of an ingredient while building something) and the s'mores and sandwich contexts draw on cooking and making, activities present in every student's home life regardless of background. Grounding an abstract quantitative skill in the universal experience of following a recipe — and running short of something — honors students' out-of-school knowledge and signals that the reasoning of chemistry is continuous with reasoning they already do at home.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — campfire that dies with wood and air left; sandwich Do Now; return in Phase 4 with the combustion equation |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — campfire's version of "running out of bread"); Phase 3 (TT#2 — which number comes only from the balanced equation?) |
| 3 | Students develop questions/models/procedures | Phase 2 ABCs s'mores build (run out / left over); Initial Model mole-mole conversion; group mass-mass investigation (Mg + HCl) |
| 4 | CCC defined and used | Lesson Overview · *Energy and Matter (conservation)*; explicit in Phase 3 (coefficients as the conserved-ratio representation) and Phase 4 (B/B/S campfire) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: stoichiometry / mole ratio / limiting reactant |
| 6 | Revisit phenomenon with evidence | Phase 4 — students return to the campfire armed with the mole-ratio concept; identify wood as excess and predict CO₂ from the balanced equation; `conservation_of_atoms.png` used to confirm atom counts |
| 7 | ENL/SPED supports | Access & Differentiation block: stoichiometry road-map strip, sentence frames, word-choice box, pre-filled molar masses, three-box conversion template |
| 8 | Assessment check | Phase 5 — Exit Ticket (mole-mole and mass-mole for CH₄ combustion; one limiting-reactant sentence) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked stoichiometry example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **stoichiometry** — the use of a balanced chemical equation to calculate how much of each reactant is needed and how much of each product forms; every stoichiometry problem follows the path grams → moles → (mole ratio) → moles → grams
- **mole ratio** — the ratio of the coefficients of any two substances in a balanced equation; it is the bridge that converts moles of one substance to moles of another (e.g., in `Mg + 2 HCl → MgCl₂ + H₂` the HCl : Mg mole ratio is 2 : 1)
- **limiting reactant** — the reactant that is completely used up first in a reaction, capping how much product can form; the other reactant, present in more than the ratio requires, is left over as the *excess* reactant
