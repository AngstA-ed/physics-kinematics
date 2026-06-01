# Half-Life — Teacher Guide

## Cover

**Unit: Nuclear Chemistry — Lesson 03: Half-Life**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: BTC

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

This lesson supports **HS-PS1-8** — *"Develop models to illustrate the changes in the composition of the nucleus of the atom and the energy released during the processes of fission, fusion, and radioactive decay."* Half-life is the quantitative description of radioactive decay: it is the fixed time required for half of a radioactive sample to decay. For the 2025 NYSSLS-aligned Regents, students are expected to use the half-life relationship to calculate the fraction of a sample remaining, the number of half-lives elapsed, and the total time elapsed, drawing the half-life value for each isotope from **Reference Table N (Selected Radioisotopes)**. Per East Meadow guidance, half-life fluency is the prerequisite for radiometric (radioactive) dating and for interpreting decay data later in the unit.

The Cross-Cutting Concept of **Patterns** is the explicit lens: radioactive decay is not random in the aggregate — it follows a fixed, predictable pattern. No matter how large the starting sample, exactly half is gone after one half-life, half of that after the next, and so on. Because the half-life of a given isotope never changes — it is unaffected by temperature, pressure, or chemical state — the pattern can be read backward in time, which is what makes radioactive isotopes a reliable natural clock.

### Phenomenon

Place a photograph or replica of an ancient artifact on the demonstration table — a 5,000-year-old wooden tool, a scrap of linen from a tomb, or a piece of charcoal from an old campfire. Tell students: there is no date written on it, no receipt, no witness. Yet a laboratory can state its age to within a century. How? Every living thing absorbs a small, steady amount of radioactive carbon-14 while alive. The instant it dies, the intake stops and the carbon-14 begins to decay at a fixed rate — its half-life is 5,730 years. By measuring how much carbon-14 is *left* compared to a fresh sample, a scientist counts backward through the half-lives to the moment the organism died.

For a vivid in-class version: hold up a jar of 100 pennies, all heads-up, representing 100 "undecayed" carbon-14 atoms. Shake the jar, remove every penny that landed tails (the "decayed" atoms), and announce: "One half-life just passed." About half the pennies are gone. Shake again — half of the rest are gone. The artifact's age is hidden in *how many shakes* it took to reach the amount we measure today.

**Driving question:** How can we use radioactive isotopes to date a 5,000-year-old artifact?

### Javalab / Labs

- **Penny (or M&M) half-life simulation:** Each group starts with 100 pennies (or M&Ms) representing radioactive atoms. Shake and pour them out; every penny showing tails (or every M&M showing the printed "m") has "decayed" and is removed. Record the number remaining after each toss. Each toss is one half-life. Groups plot remaining-count vs. number of tosses and compare their curve to `figures/half_life_decay_curve.png`. The simulation makes the fixed-fraction pattern tangible: roughly half disappear every round, regardless of how many you started with.
- **Carbon-14 dating problems:** Using the half-life of C-14 (5,730 years) from Reference Table N, students solve for the age of artifacts given the fraction of C-14 remaining (1/2, 1/4, 1/8). This is the direct application of the simulation to the anchoring phenomenon.
- **Decay-curve reading:** Students read and interpret `figures/half_life_decay_curve.png` to answer: what percent remains after 3 half-lives? After how many half-lives is less than 10% left? Connect the smooth curve to the discrete penny data.

### Assessments

- **Half-life problem set** (district checkpoint, following lesson; see `Assessments/` folder once created): students calculate fraction remaining, number of half-lives, and total time elapsed for several isotopes drawn from Reference Table N.
- **Exit Ticket** (Phase 5): three items — number of half-lives and time elapsed for a P-32 sample; fraction of K-37 remaining after a stated time; one sentence explaining why the same fraction is lost in every half-life regardless of starting amount. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | HS-PS1-8 (radioactive decay; half-life used to relate fraction remaining, number of half-lives, and time elapsed using Reference Table N) |
| **CCC focus** | Patterns — radioactive decay follows a fixed, repeating pattern: exactly one half of the remaining sample decays in each half-life, so the fraction remaining is (1/2)ⁿ after n half-lives, independent of the starting amount |
| **Strategy chips** | BTC — random groups at vertical non-permanent surfaces invent the half-life pattern from penny data before the term is named |
| **Materials** | 2025 NYS Chemistry Reference Tables (Table N especially), ~100 pennies or one fun-size bag of M&Ms per group, a cup or jar per group, calculators, whiteboards/windows + dry-erase markers (one per group), `figures/half_life_decay_curve.png` projected |
| **Safety** | Pennies/M&Ms are choking hazards only if mishandled — instruct students not to eat lab M&Ms (they have been handled). Pick up any that hit the floor immediately to prevent slips. Standard classroom conduct applies. No chemicals or open flame. |
| **Prior knowledge** | Lesson 01–02 (Nuclear Chemistry) — atoms have unstable (radioactive) nuclei that decay over time, emitting radiation; students should recognize that decay is a nuclear, not chemical, process. Students should be able to read a value from a reference table and use fractions and exponents of 1/2. |

**Lesson objectives — students can:**

- Define half-life as the fixed time required for one half of a radioactive sample to decay.
- Determine the fraction of a sample remaining after a whole number of half-lives using (1/2)ⁿ.
- Calculate the number of half-lives elapsed and the total time elapsed, using the half-life value from Reference Table N.
- Explain, using the Patterns CCC, why the same fraction of a sample decays in each half-life regardless of how much sample is present, and why this makes radioactive isotopes a reliable clock for dating artifacts.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min) to open the unit's investigation. Everyone — teacher included — answers: *"Think of something that disappears or fades a little bit at a time, at a steady rate — a melting ice pop, a phone battery, a fading marker. What came to mind?"* One round, one sentence each, no judgment. This surfaces the everyday intuition of a steady, predictable decrease, which the half-life pattern will sharpen into something exact.

Then post the **Do Now**:

> *"An old wooden tool is dug up from a tomb. There is no date on it anywhere. Yet a laboratory says it is about 5,000 years old, give or take a century. Write one sentence: how could a scientist possibly know the age of an object that nobody recorded?"*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "Maybe they look at how worn out or rotted it is." — affirm; and ask: would two pieces of wood rot at exactly the same rate? Rotting depends on the environment. What if there were a clock inside the wood itself that always ticks at the same rate?
- "They could test the chemicals in it." — close; that is the right neighborhood. Probe: what kind of "chemical" inside the wood might change in a measurable, predictable way over thousands of years?
- "I don't think you can know for sure." — validate the skepticism: it sounds impossible, and yet it works. Today we'll find the clock that makes it possible — and it is hiding in the nucleus of an atom.

### 3–8 min · Phenomenon hook — the artifact and the penny jar

**Teacher actions.** Hold up the artifact (or its image). Then hold up a jar of 100 pennies, all heads-up.

> "Every living thing — this tree while it grew, you right now — takes in a tiny, steady amount of radioactive carbon-14. The moment it dies, the intake stops, and the carbon-14 it already has starts to disappear. Not all at once. At a fixed, steady rate. These 100 heads-up pennies are 100 carbon-14 atoms in the wood the day the tree was cut. Watch what happens to them."

Shake the jar and pour the pennies out. Remove every penny showing tails — these have "decayed."

> "About half of them flipped to tails. Those atoms decayed. I'll take them out. That one pour represents one half-life — for carbon-14, that's 5,730 years. Look how many are left. Now I shake again."

Repeat once or twice so students see the count roughly halve each time.

Project the `figures/half_life_decay_curve.png` figure:

![Line graph titled 'Radioactive decay: each half-life halves the amount.' The x-axis is labeled 'time (half-lives)' and runs from 0 to 6; the y-axis is labeled 'amount remaining (%)' and runs from 0 to 100. A single smooth purple curve starts at 100% at 0 half-lives and falls steeply, passing through 50% at 1 half-life, 25% at 2 half-lives, 12.5% at 3 half-lives, and approaching but never reaching zero by 6 half-lives.](figures/half_life_decay_curve.png)

**Sample teacher language:**

> "This curve is the pennies, smoothed out. Start at 100%. After one half-life, 50% is left. After two, 25%. After three, 12.5%. The amount keeps getting cut in half — and it never quite reaches zero. Here is the powerful part: the number of times the sample has been cut in half tells you how much time has gone by. If a lab measures that the artifact has one-quarter of the carbon-14 a fresh sample has, that's two half-lives — two times 5,730 — about 11,460 years. The amount that is *left* is the clock."

**Anticipated student responses:**

- "So you just count how many times it got cut in half?" — exactly that; each cut-in-half is one half-life, and one half-life is a fixed number of years for each isotope. We'll build the counting in Phase 2.
- "Does carbon-14 ever fully disappear?" — great question; in theory it keeps halving forever, but after about 10 half-lives there's so little left that it's no longer measurable. That sets a practical limit on how old something carbon-14 can date.
- "Why is it always exactly half?" — that is the pattern we are here to discover. Hold that question — we'll answer it with the penny data.

**Driving question** (post on the board and leave it there):

> *How can we use radioactive isotopes to date a 5,000-year-old artifact?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the penny pour or the decay curve. Then:

> "Turn to your partner: I started with 100 pennies and about half decayed each shake. What if I had started with 400 pennies, or just 8 pennies? Would the *fraction* that decays each shake be different? Make a prediction."

Target insight: the fraction is always about one half, regardless of the starting count. Whether you start with 400, 100, or 8, roughly half are gone each round. The pattern is in the *fraction*, not the *amount* — which is exactly why the size of the original sample doesn't need to be known to read the clock.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–15 min · BTC launch — random groups, vertical surfaces, the penny simulation

**Before any formal vocabulary is introduced**, students generate the half-life pattern themselves using the penny (or M&M) simulation at vertical non-permanent surfaces. See the Strategy Spotlight for full BTC setup.

1. **Random groups:** Use a card randomizer or digital spinner to form groups of three. Announce: "These are your groups for the next 18 minutes. Find your vertical surface and send one person for a cup of 100 pennies."
2. **Vertical surfaces:** Each group claims a whiteboard panel, a window with a dry-erase marker, or chart paper at standing height. One marker per group, passed between members.
3. **The task (thin-slice, posted, not explained):**

> *"You have 100 pennies. Pour them out. Every penny showing TAILS has decayed — set those aside and count how many pennies REMAIN. Record the remaining count. Then pour only the remaining pennies again, remove tails again, and record again. Repeat until 3 or fewer pennies remain. Make a table: Toss # vs. Pennies Remaining. Then answer on your board: about what fraction disappears each toss? What pattern do you see in the numbers?"*

**Teacher facilitation language (circulate — ask, don't tell):**

> "What fraction is gone after one toss? After two tosses, how does the count compare to the start? Is it a half, a quarter, an eighth?"

> "Group at the window — your numbers went 100, 53, 24, 11, 6. The textbook 'ideal' would be 100, 50, 25, 12.5. Why isn't yours perfectly exact? What would make it closer to perfect?"

**Anticipated student responses during the BTC launch:**

- "We got 100, 48, 27, 12, 5 — it's not exactly half each time." — affirm; ask: is it *close* to half each time? With only 100 pennies there's randomness, but the trend is unmistakable. What if you had a million pennies?
- "Each row is about half the row before it." — that is the pattern; capture it on the board. We will name it in Phase 3.
- "Toss 1 is half, toss 2 is a quarter, toss 3 is an eighth." — excellent; you've found that the fraction remaining is (1/2) multiplied by itself once per toss. Hold that — it's the key relationship.

### 15–22 min · Initial Model — build the fraction-remaining pattern

**Prompt on the board (each group, on their vertical surface):**

> *"Forget the messy real data for a second. If decay were PERFECT and exactly half decayed every toss, fill in this 'ideal' table starting from 100:*
> *Toss 0 → 100, Toss 1 → ___, Toss 2 → ___, Toss 3 → ___, Toss 4 → ___.*
> *Then, next to each, write the FRACTION of the original that remains as a fraction with a 2 in the denominator. What is the pattern that connects the toss number to the fraction?"*

Groups work for 3–4 minutes, then a quick gallery glance at one other board.

Target answer:

> Toss 0 → 100 → 1/1 = (1/2)⁰
> Toss 1 → 50 → 1/2 = (1/2)¹
> Toss 2 → 25 → 1/4 = (1/2)²
> Toss 3 → 12.5 → 1/8 = (1/2)³
> Toss 4 → 6.25 → 1/16 = (1/2)⁴
> **Pattern:** fraction remaining = (1/2) raised to the toss number.

**Teacher facilitation language:**

> "Compare your ideal table to the decay curve I projected. Does your 50, 25, 12.5 land on the curve at 1, 2, and 3 on the x-axis? It should — the curve is your table with the dots connected."

> "Look at the exponent next to each fraction. What number is it equal to in your table? The number of tosses. That is the whole secret: the number of tosses — the number of times the sample got cut in half — is the exponent."

**Anticipated student responses:**

- "After toss 3 we got 12.5 — you can't have half a penny." — true with real pennies; but the *math* of the ideal pattern keeps halving cleanly. Real samples have trillions of atoms, so the fractions stay smooth.
- "The bottom of the fraction doubles every row: 2, 4, 8, 16." — yes, and doubling the denominator is the same as multiplying by 1/2 each time, which is the same as raising 1/2 to a higher power.
- "So 4 tosses leaves one-sixteenth?" — exactly: (1/2)⁴ = 1/16. You've found the rule before we've named it.

### 22–30 min · Investigation — from tosses to TIME using a real isotope

Keep groups at their boards. Now connect "tosses" to real years using a half-life value. Post this structured set; each group works it on their vertical surface.

**Tell students:** "A 'toss' in our simulation is one *half-life*. For a real isotope, one half-life is a fixed number of years you look up on Reference Table N. We'll use carbon-14: half-life = 5,730 years."

**Problem A — fraction remaining → number of half-lives → time:**

> *"A lab measures that an artifact has 1/4 of the carbon-14 that a fresh sample has."*
> (i) How many half-lives have passed? (ii) How old is the artifact?

Target:
> (i) 1/4 = (1/2)², so **2 half-lives**.
> (ii) 2 × 5,730 yr = **11,460 years old**.

**Problem B — number of half-lives → fraction remaining:**

> *"A different sample has gone through 3 half-lives of carbon-14."*
> (i) What fraction of its carbon-14 remains? (ii) How much time has passed?

Target:
> (i) (1/2)³ = **1/8 remaining**.
> (ii) 3 × 5,730 yr = **17,190 years**.

**Problem C — time → number of half-lives → fraction remaining (uses a different isotope from Table N):**

> *"Iodine-131 has a half-life of about 8 days (Reference Table N). A hospital sample sits for 24 days."*
> (i) How many half-lives is that? (ii) What fraction of the original I-131 remains?

Target:
> (i) 24 days ÷ 8 days/half-life = **3 half-lives**.
> (ii) (1/2)³ = **1/8 remaining**.

**Teacher facilitation prompts (circulate):**

> "Which number do you divide to get the number of half-lives? Total time divided by the half-life. For I-131: 24 ÷ 8 = 3."

> "Once you know the number of half-lives is 3, where does the fraction come from? Raise 1/2 to that power: (1/2)³ = 1/8. The exponent is always the number of half-lives."

**Anticipated student responses:**

- On A: "1/4 — is that 4 half-lives?" — redirect: 1/4 means the sample was cut in half *twice* (100 → 50 → 25%), so 2 half-lives. The denominator (4) is 2 raised to the number of half-lives, not the number of half-lives itself.
- On C: "Why do we divide here instead of multiply?" — because we're given the *total time* and want the *count of half-lives*. Time ÷ (time per half-life) = number of half-lives. In Problem A we were given the count and multiplied to get time. They're inverse operations.
- "Do all isotopes have a 5,730-year half-life?" — no; each isotope has its own fixed half-life on Table N. I-131 is 8 days; C-14 is 5,730 years. The *method* is identical; only the half-life value changes.

### 28–30 min · Reconnect + surface the method

Bring groups together at the boards. Ask one group to read out their Problem A work and another to read Problem C. Then ask the class:

> "Across all three problems, what three quantities kept appearing, and how are they connected? (Fraction remaining, number of half-lives, and total time.) What links the fraction to the number of half-lives? What links the number of half-lives to the time?"

Surface the key relationships: fraction remaining = (1/2)^(number of half-lives); number of half-lives = total time ÷ half-life; total time = number of half-lives × half-life. The half-life value is the bridge between counting half-lives and measuring years.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look at your ideal table and the decay curve. Turn to your partner: a sample with 1,000,000 atoms and a sample with 100 atoms both go through one half-life. The big sample loses 500,000 atoms; the small one loses only 50. Those are very different *amounts*. So why do we say they followed the *same* pattern?"

Target consensus: the pattern is in the *fraction*, not the amount. Both samples lose exactly half of whatever they had. Because the fraction is fixed, you never need to know the original amount to read how many half-lives have passed — you only need the ratio of what's left to a fresh sample.

> "If an artifact has 1/8 of its original carbon-14, how many half-lives have passed, and how old is it?"

Target: 1/8 = (1/2)³ → 3 half-lives → 3 × 5,730 = 17,190 years. The same logic that built the penny table dates the artifact.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name what we've been doing all period. The fixed time it takes for exactly half of a radioactive sample to decay — one 'toss' in our simulation — is called the **half-life**. The half-life of carbon-14 is 5,730 years; the half-life of iodine-131 is 8 days. It is fixed for each isotope and never changes."

> "The process the pennies were modeling — an unstable nucleus breaking down and releasing radiation — is **radioactive decay**. Half-life is simply the *rate* at which radioactive decay happens, expressed as a time."

> "And the unstable atom doing the decaying is a **radioisotope** — a version of an element with an unstable nucleus. Carbon-14, iodine-131, and uranium-238 are all radioisotopes, each with its own half-life listed on Reference Table N."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "If the half-life of carbon-14 is 5,730 years, what exactly happens in 5,730 years?" — *Expected response:* exactly half of the carbon-14 atoms present at the start of that interval will have decayed; half remain.
- "Where do you find the half-life of a radioisotope you've never heard of?" — *Expected response:* Reference Table N (Selected Radioisotopes) in the 2025 NYS Chemistry Reference Tables; it lists each radioisotope's symbol and half-life.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the model + Because/But/So expansion

Groups return to their vertical surfaces and annotate their ideal table with vocabulary: label each toss as "one half-life," label the fraction column "fraction remaining = (1/2)^(half-lives)," and circle where the number of half-lives appears as the exponent.

Then run a **Because / But / So** sentence about the phenomenon. Starter on the board:

> *"A scientist can date a 5,000-year-old artifact even though no one wrote down when it was made."*

Model one aloud:

> "A scientist can date a 5,000-year-old artifact **because** the carbon-14 inside it decays at a fixed, known rate — one half-life every 5,730 years — so the fraction remaining acts like a built-in clock — **but** the scientist never sees how many carbon-14 atoms the wood started with, only the fraction that is left compared to a fresh sample — **so** by counting how many times the sample has been cut in half (1/2, then 1/4, then 1/8…) they can read the number of half-lives off the fraction and multiply by 5,730 years to find the age."

Then have students write their own B/B/S using one of these starters:

- *"A big sample and a tiny sample of the same radioisotope both lose the same fraction in one half-life…"* (hint: the pattern is in the fraction, not the amount)
- *"A student thinks 1/4 remaining means 4 half-lives have passed…"* (hint: 1/4 = (1/2)², so it's 2 half-lives)

**Anticipated student responses:**

- "Because the rate never changes." — good start; push for the full frame: "because the half-life is fixed at 5,730 years no matter the temperature or amount, *but* we only measure the fraction left, *so* the fraction tells us the number of half-lives and therefore the time."
- "Because they only see what's left, so they work backward." — excellent; sharpen the *so*: "so they match the measured fraction (1/4) to (1/2)², find 2 half-lives, and multiply 2 × 5,730 = 11,460 years."

### 39–40 min · Return to the phenomenon

> "Return to the artifact on the table. We started not knowing how anyone could date it. Now suppose the lab reports that it has 1/2 of the carbon-14 of a fresh sample. Quickly — how many half-lives is that, and how old is the artifact?"

Target: 1/2 = (1/2)¹ → 1 half-life → 1 × 5,730 = 5,730 years old. (Note for students: a measured fraction near 1/2 is why such an artifact reads close to "about 5,000 years.")

> "That age isn't a guess from how worn the wood looks. It's read directly from the fraction of carbon-14 left and the fixed half-life on Reference Table N. The decay pattern is the clock — and you just read it."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud:

> *(a) Phosphorus-32 has a half-life of about 14 days (Reference Table N). A sample sits for 42 days. How many half-lives have passed, and what fraction of the original P-32 remains? Show your work.*
> *(b) Potassium-37 has a half-life of about 1.2 seconds. After 6 seconds (about 5 half-lives), what fraction of the original K-37 remains? Show your work.*
> *(c) In one sentence, explain why the same fraction of a radioactive sample decays in each half-life, no matter how much sample you start with.*

Expected answers are in `Answer_Key.docx`.

**Closing Reflection (SEL, 30 seconds):**

> "Today we found a clock hidden inside the nucleus of an atom. In one sentence: what is one thing that surprised you about how scientists know the age of something nobody dated — and who in your group helped you see the pattern?"

Collect worksheets; note which students correctly raise 1/2 to the *number of half-lives* versus students who confuse the number of half-lives with the denominator of the fraction (e.g., reading 1/4 as 4 half-lives). The exponent-vs-denominator confusion is the main procedural stumbling block — target those students for a brief one-on-one check at the start of the next lesson.

---

## Common Misconceptions

- **Misconception:** "After two half-lives the sample is completely gone (half plus half equals all of it)." → **Correction:** Each half-life removes half of *what remains*, not half of the original. After one half-life, 1/2 remains; after two, half of that 1/2 is gone, leaving 1/4 — not zero. The amounts shrink by halves forever and never reach zero. The penny simulation shows this directly: you never empty the cup in two pours.
- **Misconception:** "A fraction of 1/4 remaining means 4 half-lives have passed." → **Correction:** The fraction remaining is (1/2)ⁿ, where n is the number of half-lives. 1/4 = (1/2)² → 2 half-lives; 1/8 = (1/2)³ → 3 half-lives. The number of half-lives is the *exponent*, not the denominator. Students who read the denominator as the count will consistently double the true age.
- **Misconception:** "Half-life depends on how much sample you have, or on temperature/pressure." → **Correction:** Half-life is a fixed property of each radioisotope and does not change with the amount of sample, temperature, pressure, or chemical bonding. A gram and a kilogram of carbon-14 both have a half-life of 5,730 years. This invariance is exactly why radioisotopes work as clocks.
- **Misconception:** "All radioisotopes have the same half-life." → **Correction:** Each radioisotope has its own half-life, listed on Reference Table N. Carbon-14 is 5,730 years; iodine-131 is about 8 days; uranium-238 is about 4.5 billion years. The calculation method is identical, but you must use the correct half-life value for the isotope in the problem.
- **Misconception:** "Half-life tells you when a specific atom will decay." → **Correction:** Half-life is a statistical property of a large sample, not a prediction about any one atom. Any individual nucleus might decay in the next second or last for many half-lives. Only across a huge number of atoms does the steady "half every interval" pattern emerge — which is why the penny data is only *approximately* half each toss with 100 pennies, but essentially exact for the trillions of atoms in a real sample.

---

## Access & Differentiation

- **ELL/ENL supports:** Half-life calculation template pre-printed with the three relationships labeled in plain language: *number of half-lives = total time ÷ half-life*; *fraction remaining = (1/2) raised to the number of half-lives*; *total time = number of half-lives × half-life*. Sentence frame: *"After ___ half-lives, ___ of the sample remains, and ___ years (or days) have passed."* Word-choice box displayed on the board throughout: {half-life, radioactive decay, radioisotope, fraction remaining, Reference Table N}. Pair each calculation with the decay curve (visual) so students self-check their fraction against the curve height.
- **IEP/SPED supports:** Pre-fill the half-life values used in practice (C-14 = 5,730 yr, I-131 = 8 days, P-32 = 14 days, K-37 = 1.2 s) on a reference card so the Table N lookup is removed as a barrier. Provide a pre-built "halving ladder" graphic organizer (100 → 50 → 25 → 12.5 → 6.25, with the matching fractions 1/2, 1/4, 1/8, 1/16 beside each step) so the student can count half-lives by stepping down the ladder rather than computing exponents. Calculator use expected for all arithmetic; the conceptual work (counting half-lives, choosing multiply vs. divide) is the skill target.
- **Extensions:** (1) Work backward: a sample has 1/16 of its original carbon-14 — how old is it? (Answer: (1/2)⁴ → 4 half-lives → 22,920 years.) (2) Carbon-14 dating becomes unreliable past about 10 half-lives because too little is left to measure. About how many years is that, and why does it set a ceiling on the method? (3) Compare uranium-238 (half-life ≈ 4.5 billion years) and carbon-14 (5,730 years): why would a geologist dating a rock use uranium rather than carbon-14? Connect the choice of isotope to the timescale being measured.

---

## Strategy Spotlight

**BTC — Building Thinking Classrooms.** The Building Thinking Classrooms framework (Peter Liljedahl, *Building Thinking Classrooms in Mathematics*, 2021) centers on three core practices that consistently raise student thinking: (1) **random grouping** removes status hierarchies and prevents friend-group comfort zones; (2) **vertical non-permanent surfaces** (whiteboards, windows, chart paper) make thinking visible, erasable, and collaborative; and (3) **thin-slice problems** launch students into work immediately — before any direct instruction — so thinking happens before consolidation.

**How BTC runs in this lesson (Phase 2, minutes 10–30):**

1. **Random groups:** Use a card randomizer, a digital spinner, or the class roster shuffled to assign groups of three. Announce: "These are your working groups for the next 18 minutes. Find your vertical surface."
2. **Vertical surfaces:** Each group claims one whiteboard panel, a section of window with a dry-erase marker, or a sheet of chart paper taped at standing height. One marker per group — the marker passes between members so all three contribute writing and thinking.
3. **Thin-slice prompt:** The penny (or M&M) simulation task is designed to be *just* beyond what students can reason out alone but reachable as a group. Students aren't told the half-life rule — they generate the table, notice the count roughly halves each toss, and build the ideal (1/2)ⁿ pattern themselves. The task forces them to invent the relationship before Phase 3 names it.
4. **Teacher as knowledge-withholder:** While groups work, circulate and ask only questions — never give the rule. Ask: "What fraction is gone each toss?" "How does each row compare to the one above it?" "What's the exponent equal to?" The goal is for students to arrive at fraction remaining = (1/2)ⁿ themselves before you formalize half-life in Phase 3.
5. **Gallery walk (built in):** During the Initial Model step, groups take a quick glance at one neighboring board to compare ideal tables before the class debrief — exposing them to a second representation of the same pattern.

**Why BTC fits half-life:** The half-life relationship is a single, repeatable pattern that emerges naturally from data, which makes the penny simulation an ideal thin-slice. Once students build the halving table at the whiteboard — before seeing (1/2)ⁿ written anywhere — the vocabulary in Phase 3 names something they already understand from their own data. Research on BTC (Liljedahl, 2021) shows that students who derive a pattern before seeing it stated retain it more reliably than students who copy it from the board.

**CRSE connection:** The artifact-dating phenomenon connects to archaeology, ancestry, and the deep histories of many cultures — students can be invited to name an object or site from their own heritage that scientists have dated (Indigenous tools, Egyptian linen, ancient ceramics), honoring the global reach of the science. The random grouping practice is itself a CRSE move: it disrupts the social sorting that often concentrates academic authority in a few students, signaling that every student's thinking belongs on the board.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — artifact dating + penny-jar decay demo; decay curve `half_life_decay_curve.png`; return in Phase 4 with the 1/2-remaining artifact calculation |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — does the *fraction* lost change if you start with 400 vs. 8 pennies?); Phase 3 (TT#2 — why is the big and small sample's pattern the "same"?) |
| 3 | Students develop questions/models/procedures | Phase 2 BTC penny simulation (generate decay table); Initial Model (build ideal (1/2)ⁿ pattern); Investigation (fraction ↔ half-lives ↔ time problems) |
| 4 | CCC defined and used | Lesson Overview · *Patterns*, explicit in Phase 3 (TT#2 + vocabulary) and Phase 4 (B/B/S on the fixed-fraction decay clock) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: half-life / radioactive decay / radioisotope |
| 6 | Revisit phenomenon with evidence | Phase 4 — students compute the artifact's age from its measured fraction of carbon-14; decay curve used to self-check fractions |
| 7 | ENL/SPED supports | Access & Differentiation block: calculation template, sentence frame, word-choice box, pre-filled half-life card, halving-ladder organizer, calculator |
| 8 | Assessment check | Phase 5 — Exit Ticket (half-lives and fraction for P-32 and K-37; sentence on the fixed-fraction pattern) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked half-life example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **half-life** — the fixed time required for exactly one half of a radioactive sample to decay; it is a constant for each radioisotope (listed on Reference Table N) and is unaffected by amount, temperature, or pressure; after n half-lives the fraction remaining is (1/2)ⁿ
- **radioactive decay** — the process by which an unstable nucleus breaks down over time and releases radiation; half-life is the rate of this process expressed as a time
- **radioisotope** — a version of an element with an unstable nucleus that undergoes radioactive decay; each radioisotope (e.g., carbon-14, iodine-131, uranium-238) has its own characteristic half-life listed on Reference Table N
