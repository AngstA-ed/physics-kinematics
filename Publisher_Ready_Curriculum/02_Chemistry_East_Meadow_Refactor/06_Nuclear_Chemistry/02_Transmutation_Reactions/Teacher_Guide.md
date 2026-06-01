# Transmutation Reactions — Teacher Guide

## Cover

**Unit: Nuclear Chemistry — Lesson 02: Transmutation Reactions**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: HOCHMAN

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

**HS-PS1-8** — *"Develop models to illustrate the changes in the composition of the nucleus of the atom and the energy released during the processes of fission, fusion, and radioactive decay."* This lesson is the modeling-heavy core of the Nuclear Chemistry unit. Students build five distinct nuclear-process models — **fission, fusion, alpha (α) decay, beta (β) decay, and gamma (γ) emission** — and represent each as a balanced nuclear equation. The performance expectation is explicitly a *multiple-model* expectation: the East Meadow Scope & Sequence asks students to demonstrate that (1) total nucleons are conserved in every nuclear process; (2) the energy released in nuclear reactions is enormously larger than in chemical reactions (on the order of 10⁵–10⁶ times); (3) fusion merges two nuclei into one larger nucleus; (4) fission splits one nucleus into smaller fragments; and (5) the decay models show the energy and particle type for α, β, and γ. A subtle but assessed point: **alpha emission is itself a type of fission** (a small fragment, the alpha particle, breaks off), whereas beta and gamma emission are *not* fission — beta converts a neutron into a proton, and gamma releases energy only, with no change in the count of protons or neutrons.

The Cross-Cutting Concept of **Energy and Matter** is the explicit lens: in every transmutation, matter (nucleons and charge) is conserved while energy is transferred out of the nucleus. The accounting rule students carry through the whole lesson is conservation: **the sum of mass numbers and the sum of atomic numbers must each balance on both sides of a nuclear equation.** That single rule generates every balanced equation in the five-model portfolio.

### Phenomenon

The Sun has been pouring out light and heat for about 4.6 billion years and will keep going for billions more — no fuel truck ever pulls up to refill it. Down here on Earth, a nuclear power plant generates enough electricity for a whole city, and a fuel pellet the size of a fingertip holds as much energy as about a ton of coal. Yet the Sun and the power plant are doing *opposite* things in their nuclear cores: the Sun **fuses** small hydrogen nuclei into larger helium nuclei, while the power plant **splits** large uranium nuclei into smaller fragments. Same family of process (transmutation — one element becoming another), enormous energy release in both, but the nuclei move in opposite directions on the size scale. The driving puzzle: how can building nuclei up (fusion) and breaking nuclei down (fission) *both* release staggering amounts of energy?

### Javalab / Labs

- **Fission vs. fusion model construction:** Using paper nucleon tokens (small circles for protons in one color, neutrons in another) or magnetic manipulatives, students physically build the U-235 fission reaction and the H-2 + H-3 fusion reaction, then count nucleons on each side to confirm conservation. The schematic in `figures/fission_vs_fusion.png` is the reference model; students reproduce and extend it. No external URL required; a digital alternative is the PhET "Nuclear Fission" simulation or a Javalab nuclear-decay walkthrough for the decay models.
- **Balancing nuclear equations practice:** Students complete a structured set of nuclear equations (α decay of U-238, β decay of C-14, the U-235 fission equation, the D–T fusion equation) by solving for the missing particle using the two conservation rules (mass number balances; atomic number balances). Each equation is checked in a mass-number / atomic-number ledger.
- **Energy-scale reading:** Students interpret `figures/energy_scale_chemical_vs_nuclear.png` (a log-scale bar chart) to articulate *how much* larger nuclear energy release is than chemical — roughly a million-fold — and connect that to why a fingertip-sized fuel pellet rivals a ton of coal.

### Assessments

- **Five-model nuclear-process portfolio** (unit checkpoint): students produce one labeled model + one balanced nuclear equation for each of fission, fusion, α decay, β decay, and γ emission, with a one-sentence note on each that states what is conserved and whether the process counts as a type of fission. See `Assessments/` folder once created.
- **Exit Ticket** (Phase 5): three items — balance an α-decay equation for Po-210; identify which of two equations is fusion vs. fission and justify by nucleus size; explain in one Hochman appositive sentence why nuclear energy release dwarfs chemical energy release. Values are deliberately distinct from the worksheet practice. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | HS-PS1-8 (models of fission, fusion, and radioactive decay; nucleon and charge conservation; nuclear energy scale 10⁵–10⁶× chemical) |
| **CCC focus** | Energy and Matter — in every transmutation, mass number and atomic number (matter) are conserved while a large quantity of energy is transferred out of the nucleus; fusion and fission move nuclei in opposite size directions yet both release energy |
| **Strategy chips** | HOCHMAN — appositive sentence to define *transmutation* crisply; Because/But/So sentence in Phase 4 for fusion-vs-fission energy reasoning |
| **Materials** | 2025 NYS Chemistry Reference Tables (Periodic Table for atomic numbers; Table O — Symbols Used in Nuclear Chemistry; Table N — Selected Radioisotopes), nucleon tokens or magnetic manipulatives, calculators, `figures/fission_vs_fusion.png` and `figures/energy_scale_chemical_vs_nuclear.png` projected |
| **Safety** | No hazardous materials. This is a modeling and equation-balancing lesson; tokens/manipulatives only. Standard classroom procedures apply. |
| **Prior knowledge** | Lesson 01 (Radioactivity) — atoms have a nucleus of protons and neutrons; the notation ⁴₂He (mass number on top, atomic number on bottom); the existence of alpha, beta, and gamma radiation. Students should recognize that the atomic number determines the element's identity before this lesson. |

**Lesson objectives — students can:**

- Define **transmutation** and distinguish natural transmutation (spontaneous radioactive decay) from artificial transmutation (bombardment in a reactor or accelerator).
- Balance a nuclear equation by conserving the total mass number and the total atomic number on both sides.
- Build and compare models of **fission** (one nucleus splits) and **fusion** (two nuclei merge), and explain why both release energy.
- Explain, using Energy and Matter, why nuclear processes release roughly 10⁵–10⁶ times more energy than chemical reactions, and identify alpha emission as a type of fission while beta and gamma emission are not.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers: *"Name something that gives off a huge amount of energy from a tiny source — the Sun, a battery, a hot pepper, a small engine. What came to mind?"* One round, one sentence each, no judgment. This surfaces the intuition that the *amount* of stuff and the *amount* of energy are not the same thing — a tiny source can release enormous energy, which is exactly the nuclear story.

Then post the **Do Now**:

> *"The Sun has been shining for about 4.6 billion years with no fuel deliveries. A nuclear power plant lights up a whole city from fuel pellets the size of a fingertip. Both get their energy from the nucleus of atoms. Write one sentence: where do you think all that energy comes from, if the Sun and the power plant never seem to run low?"*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "The Sun is just burning, like a fire." — capture, then create tension: a fire burns through its fuel and goes out; the Sun has lasted billions of years. What if it is *not* burning the way wood burns? Set that up as the puzzle.
- "It comes from the atoms splitting apart." — close, and exactly right for the power plant; probe: does the Sun split atoms too, or does it do something different? Hold the question.
- "I don't really know — that's a lot of energy from a tiny pellet." — validate: that gap between tiny size and huge energy is precisely what today explains.

### 3–8 min · Phenomenon hook — same energy, opposite directions

**Teacher actions.** Tell the two-part story. Part 1: the Sun. Deep in its core, hydrogen nuclei are smashed together so hard they *merge* into larger helium nuclei. Building nuclei up releases energy — and the Sun has enough hydrogen to keep doing this for billions of years. Part 2: the power plant. A uranium-235 nucleus absorbs a neutron and *splits* into two smaller fragments plus a few neutrons. Breaking a nucleus down also releases energy. Two opposite directions — merging versus splitting — and both pour out energy.

Project `figures/fission_vs_fusion.png`:

![Two-panel schematic. Left panel labeled 'Fission: one large nucleus splits' shows a green neutron striking a large purple U-235 nucleus, an orange arrow, and the products: two smaller blue nuclei labeled Ba and Kr plus three released neutrons and the note '+ neutrons + energy.' Right panel labeled 'Fusion: two small nuclei merge' shows two small blue nuclei labeled H-2 and H-3, arrows converging, and the product: one larger purple He-4 nucleus plus a released neutron and the note '+ neutron + energy.'](figures/fission_vs_fusion.png)

**Sample teacher language:**

> "Look at the two panels. On the left, fission: one big uranium nucleus is hit by a neutron and splits into two smaller pieces. On the right, fusion: two tiny hydrogen nuclei merge into one bigger helium nucleus. These are *opposite* moves — splitting versus merging — but notice the last line under each: '+ energy,' both times. The Sun fuses. The power plant splits. Today we figure out how both directions release energy, and how to keep track of every proton and neutron while it happens."

**Anticipated student responses:**

- "Wait — the left side makes more pieces and the right side makes fewer. How can both give off energy?" — that is the central puzzle; affirm and post it as the driving question.
- "Where do the extra neutrons come from in fission?" — they were already inside the uranium nucleus; splitting frees a few of them. We will count them and confirm none appear from nowhere.
- "Is the Sun running out of hydrogen?" — slowly, over billions of years; the point is the energy-per-reaction is so large that a tiny amount of fuel lasts an astronomically long time.

**Driving question** (post on the board and leave it there):

> *How can building nuclei up (fusion) and breaking nuclei down (fission) both release enormous amounts of energy — and how do we keep track of every particle while a nucleus changes?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the two-panel figure. Then:

> "Turn to your partner: in the fission panel, count the nuclei before and after. In the fusion panel, count them too. Something is changing — the *number* of nuclei and their *size*. But is anything staying the *same* across the arrow? Try to name something that does not change."

Target insight (leave open if no one lands it yet): the *total number of protons and neutrons* (nucleons) is conserved — particles are rearranged, not created or destroyed. That conservation rule is what we will name and use in Phase 3.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–15 min · ABCs Activity — build the models before naming the rules

**Before any formal vocabulary is introduced**, students build the nuclear processes with tokens and discover the conservation pattern themselves.

Each group receives nucleon tokens (one color = proton, a second color = neutron) or examines the projected schematic. The task:

**Part 1 — Build fission:**

> "Start with a U-235 nucleus and a single incoming neutron. Using the figure as a guide, model the split into Ba-141 and Kr-92. Lay out your tokens for the 'before' side and the 'after' side. Count the total protons and the total neutrons on each side. Do they match?"

**Part 2 — Build fusion:**

> "Now model fusion: combine an H-2 nucleus and an H-3 nucleus. The product is He-4 plus one leftover neutron. Lay out 'before' and 'after.' Count protons and neutrons on each side. Do they match?"

Have students record what they find in this table:

| Process | Protons before | Protons after | Neutrons before | Neutrons after | Conserved? |
|---|---|---|---|---|---|
| Fission (U-235 + n) | | | | | |
| Fusion (H-2 + H-3) | | | | | |

**Teacher facilitation language (circulate):**

> "Before I give you any rule, just count. Don't assume — physically count the proton tokens before the arrow and after the arrow. Then do the same for neutrons. Tell me what you notice about the totals."

> "In fission, you ended up with more separate nuclei than you started with, but did you end up with more *protons* total? More *neutrons* total? Or did the same particles just get rearranged?"

**Anticipated student responses during ABCs:**

- "The number of protons is the same on both sides!" — affirm; that is conservation of atomic number. We'll name it formally soon.
- "The neutrons are the same too, if I count the loose ones." — exactly; the loose neutrons aren't new, they came out of the nucleus.
- "Fission has two nuclei after and fusion has one nucleus after, but the proton totals still match." — perfect; the *number of nuclei* changes but the *number of nucleons* does not.

### 15–22 min · Initial Model — first balanced nuclear equation

**Prompt on the board:**

> *"Before we name the process: here is the fission of uranium written as an equation, with one piece missing. Use your token counts to fill in the blank. Remember each symbol is written as (mass number on top, atomic number on bottom)."*

> ²³⁵₉₂U + ¹₀n → ¹⁴¹₅₆Ba + ⁹²₃₆Kr + ___ ¹₀n

> *"How many neutrons go in the blank? Check using two rules you just discovered: the top numbers (mass numbers) must add up the same on both sides, and the bottom numbers (atomic numbers) must add up the same on both sides."*

Students work individually for 3 minutes, then compare with a partner.

Target answer:

> Mass numbers (top): left = 235 + 1 = 236. Right = 141 + 92 + (n × 1). To reach 236: 141 + 92 = 233, so 236 − 233 = **3 neutrons**.
> Atomic numbers (bottom): left = 92 + 0 = 92. Right = 56 + 36 + (n × 0) = 92. ✓ Balanced.
> The blank is **3**.

**Teacher facilitation language:**

> "Look at your token count from the ABCs activity. How many loose neutrons did you have left over after the split? Does that match the 3 you just solved for with the equation? If it does, your model and your equation agree — that's the goal."

> "Check your partner's setup. Did they balance the *top* numbers (mass) and the *bottom* numbers (atomic number) separately? Both have to balance, independently."

**Anticipated student responses:**

- "I got 2 neutrons — I forgot to include the incoming neutron on the left." — redirect: the left side is 235 + 1 = 236, not just 235. The incoming neutron counts.
- "The bottom numbers already balanced without the neutrons — is that okay?" — yes; neutrons have atomic number 0, so they don't affect the bottom sum. They only affect the top (mass) sum. That's a great observation.
- "So I just need the top and bottom to match on both sides?" — exactly. That single rule balances every nuclear equation.

### 22–30 min · Investigation — balance the decay and fusion equations

Groups of three or four work through a structured practice set. Each student fills in the missing particle individually and then checks with the group using a mass-number / atomic-number ledger.

**Practice set (written on the board or distributed as a half-sheet):**

For each equation, find the missing particle. Use the Periodic Table for atomic numbers and Reference Table O for nuclear symbols. Confirm with the ledger: mass numbers balance (top); atomic numbers balance (bottom).

**Equation A — alpha decay of uranium-238 (natural transmutation):**

> ²³⁸₉₂U → ___ + ⁴₂He

| | Mass number (top) | Atomic number (bottom) |
|---|---|---|
| Left total | 238 | 92 |
| Known right (⁴₂He) | 4 | 2 |
| **Missing particle** | 238 − 4 = **234** | 92 − 2 = **90** |

Missing particle: **²³⁴₉₀Th** (thorium-234). Atomic number 90 = Th on the Periodic Table.

**Equation B — beta decay of carbon-14 (natural transmutation):**

> ¹⁴₆C → ___ + ⁰₋₁e

| | Mass number (top) | Atomic number (bottom) |
|---|---|---|
| Left total | 14 | 6 |
| Known right (⁰₋₁e, a beta particle) | 0 | −1 |
| **Missing particle** | 14 − 0 = **14** | 6 − (−1) = **7** |

Missing particle: **¹⁴₇N** (nitrogen-14). A neutron became a proton; the atomic number went *up* by 1.

**Equation C — fusion (the Sun / the D–T reaction):**

> ²₁H + ³₁H → ⁴₂He + ___

| | Mass number (top) | Atomic number (bottom) |
|---|---|---|
| Left total | 2 + 3 = 5 | 1 + 1 = 2 |
| Known right (⁴₂He) | 4 | 2 |
| **Missing particle** | 5 − 4 = **1** | 2 − 2 = **0** |

Missing particle: **¹₀n** (one neutron).

**Teacher facilitation prompts (circulate):**

> "For alpha decay, the alpha particle is ⁴₂He — it takes away 4 mass and 2 protons. So the leftover nucleus has 4 less on top and 2 less on the bottom. What element has atomic number 90?"

> "For beta decay, the beta particle is ⁰₋₁e. Its bottom number is *negative* one. Watch the subtraction: 6 − (−1) = 7. The atomic number goes UP. A neutron turned into a proton inside the nucleus."

> "For fusion, you've already balanced the top to 4 with helium — what's left over on top? One mass unit with zero charge. That's a neutron."

**Anticipated student responses:**

- On Equation A: "I got atomic number 88 — I added instead of subtracted." — redirect: the alpha particle *leaves* the nucleus, so subtract. 92 − 2 = 90 = thorium.
- On Equation B: "How can the atomic number go up if nothing was added?" — affirm the puzzle: inside the nucleus a neutron converts to a proton and emits the electron (beta particle). The mass number stays 14 because a neutron and a proton have nearly the same mass; only the charge balance shifts.
- On Equation C: "Helium already balances the charge, so the last particle has no charge?" — exactly; bottom is 2 = 2 already, so the missing particle has atomic number 0 — a neutron.

### 28–30 min · Reconnect + surface the pattern

Bring groups back together. Ask one group to put the alpha-decay ledger on the board. Ask the class:

> "Look at every equation we balanced. What two quantities always matched on both sides of the arrow? (Total mass number; total atomic number.) Did any proton or neutron ever appear from nowhere or vanish?"

Surface the key idea: every nuclear equation balances *two* totals — mass number (top) and atomic number (bottom). Nothing is created or destroyed; particles are rearranged and energy is released. That conservation rule is the backbone of the whole five-model portfolio.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look back at your alpha-decay equation and your fission equation. In alpha decay, a small piece (the ⁴₂He) breaks off a big nucleus. In fission, a big nucleus splits into pieces. Turn to your partner: how are alpha decay and fission *similar*? And how is beta decay *different* from both of them?"

Target consensus: in both alpha decay and fission, a nucleus breaks into smaller pieces — so **alpha emission is actually a type of fission** (a tiny fragment splits off). Beta decay is different: nothing splits off the outside; instead, a neutron *inside* converts into a proton, changing the element's identity without breaking the nucleus into fragments. Gamma emission is different again — it releases only energy, with no change in the count of protons or neutrons at all.

> "If gamma emission changes neither the mass number nor the atomic number, what does change? Why would a nucleus emit gamma rays at all?"

Target: gamma is pure energy leaving the nucleus as it settles from a high-energy (excited) state to a lower-energy state. The nucleus is the same element with the same nucleons — it just released excess energy.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name what we've been modeling. Any process that changes one element into another by changing the nucleus is called **transmutation**. Every equation we balanced today was a transmutation: uranium became barium and krypton; carbon became nitrogen; hydrogen became helium. The element's *identity* changed because the *atomic number* changed."

> "Here is the Hochman appositive move that locks the definition in. An appositive is a phrase set off by dashes that renames or explains the noun beside it. Say this with me:

> *Transmutation — the change of one element into another by altering the nucleus — always conserves the total mass number and the total atomic number.*

> The phrase between the dashes defines 'transmutation' inside the same sentence. You'll use this structure on the Exit Ticket and in your notes."

> "Transmutation comes in two kinds. **Natural transmutation** happens on its own — spontaneous radioactive decay, like the carbon-14 beta decay or the uranium-238 alpha decay. No one has to start it; the unstable nucleus changes by itself. **Artificial transmutation** is forced — a nucleus is bombarded with a particle, like the neutron striking U-235 in a reactor or particles fired in an accelerator. Natural = the nucleus changes spontaneously; artificial = we make it change by hitting it."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "Is the fission of U-235 in a power plant natural or artificial transmutation?" — *Expected response:* artificial — it's started by bombarding the nucleus with a neutron. The uranium would not split by itself the same way at the same rate.
- "Why is alpha emission considered a type of fission but beta emission is not?" — *Expected response:* alpha emission breaks a fragment (⁴₂He) off the nucleus — that's a split, like fission. Beta emission doesn't break off a fragment; a neutron converts to a proton inside the nucleus, so nothing splits.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the model + Appositive + Because/But/So expansion

Students return to their Initial Model (the U-235 fission equation). They annotate it with vocabulary: label it *artificial transmutation*, draw a box around the conserved totals (mass number 236 = 236; atomic number 92 = 92), and then write an appositive sentence defining the process.

**Appositive sentence (model on board):**

> *"Transmutation — the change of one element into another by altering the nucleus — always conserves the total mass number and the total atomic number."*

Ask students to write a parallel appositive sentence for alpha decay:

> *"Alpha decay — the loss of a ___ particle (⁴₂He) from a nucleus — is a type of ___ because a fragment splits off."*

Then run a **Because / But / So** sentence about the phenomenon. Starter on the board:

> *"A fingertip-sized nuclear fuel pellet releases about as much energy as a ton of coal."*

Project `figures/energy_scale_chemical_vs_nuclear.png`:

![Bar chart on a logarithmic y-axis comparing energy released per gram of fuel. The left blue bar, labeled 'Chemical reaction (burning H2),' reaches about 1.4 times 10 squared kilojoules per gram. The right purple bar, labeled 'Nuclear reaction (fusion of H2),' reaches about 3.4 times 10 to the eighth kilojoules per gram — roughly a million times taller. The title reads 'Nuclear reactions release ~10^5 to 10^6 times more energy.'](figures/energy_scale_chemical_vs_nuclear.png)

Model one aloud:

> "A nuclear fuel pellet releases vastly more energy than the same mass of coal **because** nuclear reactions rearrange the strong forces *inside the nucleus*, which store roughly 10⁵–10⁶ times more energy per gram than the chemical bonds *between atoms* that burning rearranges — **but** both reactions still obey conservation (the nucleons and charge are all accounted for, nothing is created from nothing) — **so** a tiny amount of nuclear fuel can release the energy of a whole ton of chemical fuel, which is exactly why the Sun lasts billions of years and a fingertip pellet lights a city."

Then have students write their own B/B/S using one of these starters:

- *"The Sun fuses hydrogen for billions of years without running out…"* (hint: tiny fuel, enormous energy per reaction)
- *"A power plant gets more energy from one uranium pellet than from a truckload of coal…"*

**Anticipated student responses:**

- "Because the energy comes from inside the nucleus, not from the bonds between atoms." — good start; push for the So: "so a much smaller amount of fuel releases the same energy, which is why the pellet rivals a ton of coal."
- "Because fusion combines nuclei and that releases a lot of energy." — affirm; push for the But: "but the protons and neutrons are still all conserved — fusion doesn't make matter disappear, it converts a tiny bit of mass into a huge amount of energy."

### 39–40 min · Return to the phenomenon

> "Return to our opening puzzle. The Sun fuses small nuclei into bigger ones; the power plant splits big nuclei into smaller ones. Now you have the tools. Using the words *transmutation*, *fusion*, and *fission*, explain in one sentence how the Sun and the power plant can do opposite things yet both release enormous energy."

Target: "Both the Sun (fusion) and the power plant (fission) carry out transmutation — changing one element into another — and although fusion builds nuclei up while fission breaks them down, both rearrange the nucleus into a more stable arrangement and release the huge energy stored inside it, all while conserving every proton and neutron."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud:

> *(a) Balance this alpha-decay equation for polonium-210. Find the missing nucleus and name the element:*
> ²¹⁰₈₄Po → ___ + ⁴₂He
> *(b) Here are two equations. One is fusion and one is fission. Label each and justify your choice by what happens to the size of the nuclei:*
> Equation 1: ⁶₃Li + ²₁H → 2 ⁴₂He
> Equation 2: ²³⁹₉₄Pu + ¹₀n → ¹³⁴₅₄Xe + ¹⁰³₄₀Zr + 3 ¹₀n
> *(c) In one Hochman appositive sentence, explain why a nuclear reaction releases far more energy than a chemical reaction.*

Expected answers are in `Answer_Key.docx`. (Note: these values — Po-210 alpha decay, the Li-6 + H-2 fusion, and the Pu-239 fission — are intentionally different from the worksheet's U-238 alpha decay, C-14 beta decay, U-235 fission, and D–T fusion practice.)

**Closing Reflection (SEL, 30 seconds):**

> "Today we found out that the Sun and a power plant run on opposite nuclear processes that both release staggering energy. In one sentence: what is one thing that surprised you about how much energy is locked inside a nucleus, and who — a person or a moment in class — helped you figure something out?"

Collect worksheets; note which students balanced both the mass number AND the atomic number versus students who balanced only one. The two-totals check is the main procedural stumbling block — target the single-balance students for a brief one-on-one check at the start of the next lesson.

---

## Common Misconceptions

- **Misconception:** "Fission and fusion are opposites, so one releases energy and the other absorbs it." → **Correction:** Both release energy, even though they move nuclei in opposite size directions. Splitting a very large nucleus (fission) and merging very small nuclei (fusion) both move toward more stable, lower-energy arrangements, and the released energy is what's left over. The phenomenon (Sun vs. power plant) is built precisely to confront this.
- **Misconception:** "In fission, the extra neutrons are created out of nothing." → **Correction:** The released neutrons were already inside the uranium nucleus. Splitting frees a few of them. Counting tokens in the ABCs activity makes this concrete — the total neutron count is conserved, never increased from nothing.
- **Misconception:** "Balancing a nuclear equation is just like balancing a chemical equation — match the atoms." → **Correction:** In a *chemical* equation you conserve atoms of each element. In a *nuclear* equation the elements themselves change (transmutation), so you instead conserve two running totals: mass number (top) and atomic number (bottom). Students who try to "match elements" will be stuck because carbon legitimately becomes nitrogen.
- **Misconception:** "Beta decay adds a proton from outside the atom." → **Correction:** No proton enters from outside. Inside the nucleus, a neutron converts into a proton (and emits the beta particle, ⁰₋₁e). The mass number stays the same; the atomic number rises by 1 because the proton count went up by one. Nothing was added externally.
- **Misconception:** "Gamma emission changes the element, like alpha and beta." → **Correction:** Gamma emission releases only energy. The mass number and atomic number are both unchanged, so the element is the same before and after — the nucleus simply drops from an excited (high-energy) state to a lower-energy state. This is why gamma is *not* a type of fission: nothing splits off and no nucleons are lost.
- **Misconception:** "Nuclear and chemical reactions release similar amounts of energy." → **Correction:** Nuclear reactions release roughly 10⁵–10⁶ times more energy per gram. The log-scale bar chart makes the gap visible — the nuclear bar is about a million times taller. This is why a fingertip pellet rivals a ton of coal, and why the energy comes from the strong forces inside the nucleus rather than from the chemical bonds between atoms.

---

## Access & Differentiation

- **ELL/ENL supports:** Nuclear-equation balancing template pre-printed with the two-row ledger (Mass number (top) | Atomic number (bottom)) and the sentence frame: *"In ___ , one element becomes ___ because the ___ number changes."* Word-choice box displayed on the board throughout: {transmutation, natural, artificial, fission, fusion, nucleus, conserved, mass number, atomic number}. Pair vocabulary with gestures: two fists coming together for fusion, two hands pulling apart for fission. Provide the nuclear notation read-aloud: "uranium-235" for ²³⁵₉₂U so students decode the symbol verbally before writing.
- **IEP/SPED supports:** Pre-fill the atomic numbers for the elements used in practice (U = 92, Ba = 56, Kr = 36, C = 6, N = 7, He = 2, Th = 90, H = 1) on a reference card so the Periodic Table lookup is removed as a barrier. Offer the two-totals ledger as a fill-in grid where the student completes the mass-number row fully before starting the atomic-number row. Provide physical nucleon tokens for every step so the abstract symbols are anchored to countable objects. Calculator use expected; the conceptual work (which total to balance, add vs. subtract for emitted particles) is the skill target.
- **Extensions:** (1) Write the full natural-decay chain from U-238 to a stable lead isotope by repeating alpha and beta steps — how many of each are needed to reach Pb-206? (2) Research and explain why fusion is so much harder to sustain on Earth than fission (the temperature and pressure of the Sun's core vs. a reactor). (3) Using Reference Table N (Selected Radioisotopes), pick a radioisotope used in medicine (e.g., I-131, Co-60) and write its decay equation, then explain in two sentences why its particular decay mode makes it useful for that medical purpose.

---

## Strategy Spotlight

**HOCHMAN — Appositive sentence.** The Hochman Writing Method (Judith Hochman and the Writing Revolution) treats sentence-level writing as a thinking tool. For this lesson the featured technique is the **appositive**, a noun phrase set off by dashes (or commas) that renames or defines the noun it follows. The appositive is ideal for vocabulary-heavy nuclear content because it forces students to embed a definition into a complete subject-verb sentence rather than reciting it in isolation.

**The target appositive for this lesson:**

> *Transmutation — the change of one element into another by altering the nucleus — always conserves the total mass number and the total atomic number.*

This sentence structure does three things at once: (1) names the term, (2) defines it in a concise phrase between the dashes, and (3) states the governing rule (conservation) in the main clause. Students who can write and say this sentence — not just recite the definition separately — are integrating the term into their active vocabulary and binding it to the conservation rule they used all period.

**How to run it in this lesson (Phase 3 → Phase 4):**

1. Post and read aloud the model appositive sentence together (Phase 3 vocabulary).
2. Ask students to write a parallel appositive for a specific process: *"Alpha decay — the loss of a ⁴₂He particle from a nucleus — is a type of fission because…"* This requires them to substitute the concrete process they balanced in Phase 2, confirming that the abstract definition connects to their hands-on modeling.
3. In Phase 4, students write their own appositive for fusion or fission and use the Because/But/So frame to reason about the energy scale. Cold-call two or three students; ask: does the appositive phrase correctly define the term? Does the main clause state what is conserved or why energy is released?

**Why the appositive fits transmutation:** The term "transmutation" sounds like alchemy, but it translates directly — *trans* (across, change) + *mutation* (change of form): a change across elements. The appositive makes that meaning visible and ties it to the conservation rule, so students don't walk away thinking transmutation means matter appears from nowhere. Students who internalize the three-part logic (name → definition → rule) are far less likely to confuse nuclear-equation balancing with chemical-equation balancing in future work.

**CRSE connection:** The opening circle prompt (a tiny source giving off huge energy — the Sun, a battery, a hot pepper) invites students to bring their own examples and cultural reference points into the lesson. The anchoring phenomenon — the Sun — is shared by every human culture and is the subject of creation stories, agricultural calendars, and seasonal celebrations worldwide. Grounding an abstract nuclear concept in the Sun, a phenomenon every student has a personal and cultural relationship with, honors students' lived experience and makes the science feel continuous with the sky they see every day rather than confined to a reactor.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — Sun vs. nuclear power plant (fusion vs. fission); `fission_vs_fusion.png`; return in Phase 4 with the energy-scale chart and in Phase 4 close |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — what stays the same across the arrow?); Phase 3 (TT#2 — how are alpha decay and fission similar, and how is beta decay different?) |
| 3 | Students develop questions/models/procedures | Phase 2 ABCs token build (fission and fusion models, count conservation); Initial Model (solve for missing neutrons); group investigation (balance α, β, fusion equations) |
| 4 | CCC defined and used | Lesson Overview · *Energy and Matter*, explicit in Phase 2 conservation ledger, Phase 3 vocabulary, and Phase 4 Because/But/So energy reasoning |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: transmutation / natural transmutation / artificial transmutation |
| 6 | Revisit phenomenon with evidence | Phase 4 — students use the balanced equations and energy-scale chart to explain how the Sun (fusion) and power plant (fission) both release enormous energy |
| 7 | ENL/SPED supports | Access & Differentiation block: two-totals ledger template, sentence frame, word-choice box, pre-filled atomic numbers, physical nucleon tokens, calculator |
| 8 | Assessment check | Phase 5 — Exit Ticket (balance Po-210 alpha decay; classify fusion vs. fission with justification; appositive sentence on nuclear vs. chemical energy) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked balancing example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **transmutation** — the change of one element into another caused by a change in the nucleus (a change in the atomic number); every nuclear equation in this lesson is a transmutation, and all conserve total mass number and total atomic number
- **natural transmutation** — a transmutation that occurs spontaneously through radioactive decay, with no outside particle needed (e.g., the alpha decay of U-238 or the beta decay of C-14); the unstable nucleus changes on its own
- **artificial transmutation** — a transmutation forced by bombarding a nucleus with a particle, such as the neutron that triggers U-235 fission in a reactor or particles fired in an accelerator; the change is induced, not spontaneous
