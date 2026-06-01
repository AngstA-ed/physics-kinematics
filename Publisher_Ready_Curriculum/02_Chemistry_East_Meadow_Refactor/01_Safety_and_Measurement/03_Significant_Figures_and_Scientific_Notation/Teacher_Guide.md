# Significant Figures & Scientific Notation — Teacher Guide

## Cover

**Unit: Safety and Measurement — Lesson 03: Significant Figures & Scientific Notation**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: BTC

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

Foundational quantitative skill supporting **HS-PS1-7** — *"Use mathematical representations to support the claim that atoms, and therefore mass, are conserved during a chemical reaction."* Before students can write and interpret balanced equation stoichiometry, they must communicate measured quantities honestly — recording only the digits the instrument can actually support, and no more. Per East Meadow guidance, there is no separate math operation tested for sig figs on the state assessment; students are expected to round sensibly (three significant figures as a working default) and to express very large or very small numbers in scientific notation when context requires it. The lesson treats significant figures as a claim-making practice: every digit you write is a claim about what you actually measured, and the Cross-Cutting Concept of Scale, Proportion, and Quantity demands that the claim be honest.

### Phenomenon

Three students each measure the same pencil with a centimeter ruler and report their results: one writes 15 cm, another writes 15.0 cm, and a third writes 15.00 cm. All three could be looking at the same pencil — and the answer could depend on the ruler. Then a calculator divides two lab measurements and displays 15.2837 cm. The question on the floor: Which of those digits is the instrument actually telling you, and which is the calculator inventing? The driving question follows naturally: *How precise are we actually allowed to claim our answer is?* This phenomenon makes the abstract rule-counting world of significant figures feel like an honest conversation between a scientist and their instrument — not an arbitrary bookkeeping exercise.

### Javalab / Labs

- **Sig-fig sorting cards:** Sets of 10–12 measured values (including tricky cases: leading zeros, trailing zeros with and without a decimal point, captive zeros) written on index cards or half-sheets. Groups sort them into categories: "easy to count," "tricky," "I'm not sure." Then they count sig figs for each, compare across groups, and surface the rules inductively.
- **Estimate-the-last-digit measuring:** Students use the graduated cylinder figure (or a real cylinder at a lab station) to practice reading the instrument one digit past the last marked scale division. The `figures/reading_precision.png` image (27.5 mL in a 50 mL cylinder) is used as a whole-class anchor.
- **Scientific notation conversion practice:** Students convert a set of values both ways — standard to scientific and scientific to standard. Values include Avogadro's number, atomic radii, and masses from the 2025 Reference Tables, giving the notation meaning before it is tested.

### Assessments

- **Sig-fig and scientific notation quiz** (district checkpoint, following lesson; see `Assessments/` folder once created).
- **Exit Ticket** (Phase 5): three items — count sig figs in 0.03080, express 6,420,000 in scientific notation, round 7.86342 to 3 significant figures. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | HS-PS1-7 (mathematical representations — foundational quantitative communication) |
| **CCC focus** | Scale, Proportion, and Quantity — the precision you record must honestly reflect the instrument; a number's digits carry a claim about certainty. A measurement of 15.00 cm claims something different from 15 cm, even though the calculator evaluates them identically. |
| **Strategy chips** | BTC (Building Thinking Classrooms) — random groups at vertical non-permanent surfaces, thin-slice sig-fig sequence |
| **Materials** | Centimeter rulers, 50 mL graduated cylinders, sig-fig sorting cards (one set per group), whiteboards or large chart paper and markers (vertical surfaces), 2025 NYS Chemistry Reference Tables, `figures/reading_precision.png` projected. |
| **Safety** | No hazardous chemicals. Water only at any wet-measurement station. |
| **Prior knowledge** | Lessons 01–02 — lab safety, SI units, reading a graduated cylinder to the correct decimal place. Students already know that the last digit of a graduated-cylinder reading is estimated; this lesson names that practice formally. |

**Lesson objectives — students can:**

- Count the significant figures in a measured value, including tricky cases involving leading zeros, captive zeros, and trailing zeros (with and without a decimal point).
- Read any measuring instrument to one digit past the smallest scale division, recognizing that the last digit is estimated.
- Express a measured value in scientific notation and convert back to standard form.
- Explain, using Scale, Proportion, and Quantity, why the number of significant figures a result carries must be limited by the least-precise measurement used to calculate it.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers: *"Name something in your life where you've had to be really precise — and something where 'close enough' was fine. What made the difference?"* One round, one sentence each, no judgment. This surfaces the intuition that precision is not always maximized but always chosen deliberately — and that choosing wrong has consequences. Keep it to a sentence each.

Then post the **Do Now**:

> *"Three students measure the same pencil and write: 15 cm, 15.0 cm, 15.00 cm. Are these the same number? If a calculator says the answer is 15.2837 cm, is that an honest answer? Write one sentence about what you think."*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "They're all the same — 15 equals 15.0." — affirm the math; ask whether they carry the *same message* about how careful the measurement was. They do not.
- "The calculator is just giving you all the digits." — exactly right; ask: "Does the instrument that produced the original measurements actually know those extra digits?" That question drives the lesson.
- "I don't know what 15.00 means different from 15." — validate: "That is the exact question we are going to answer today."

### 3–8 min · Phenomenon hook — the pencil + the calculator

**Teacher actions.** Hold up (or project) three strips of paper labeled 15 cm / 15.0 cm / 15.00 cm. Tell the story:

> "Student A used a ruler with only 1-cm marks — the smallest mark on the ruler was 1 cm, so the best they could honestly report was the nearest centimeter. Student B had a ruler marked to millimeters — they could read to 0.1 cm and estimate one digit further to get 15.0. Student C had a precision instrument marked to 0.1 mm — they could honestly claim four significant figures: 15.00 cm."

Then pull out a calculator and type 15.2837.

**Sample teacher language:**

> "A calculator has no idea what instrument you used. It will happily tell you an answer to six decimal places for data that can only support two digits of certainty. That's not the calculator's fault — it doesn't know how you measured. *You* have to know. Every digit you write down is a claim you are making. Today we learn which claims are honest."

**Anticipated student responses:**

- "So you just cut off the extra digits?" — almost; you round, and you round to the right place. How do you know the right place? That's what significant figures tell you.
- "Does this matter for chemistry tests?" — yes, but more importantly it matters any time your data supports a decision. A medicine dose rounded too precisely (or imprecisely) can have real consequences.
- "What's the rule for the zeros?" — great question; hold it for Phase 2. That's where the confusion lives.

**Driving question** (post on the board and leave it there):

> *How precise are we actually allowed to claim our answer is?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses. Then:

> "Turn to your partner: Student A's ruler can't see the difference between 14.7 cm and 15 cm — they both round to 15 cm on that instrument. Does that mean those two pencils are the same length? What does Student A's measurement actually *tell* you, and what does it *not* tell you?"

Target insight: a measurement of 15 cm means the pencil is somewhere between 14.5 and 15.5 cm. A measurement of 15.00 cm means it is between 14.995 and 15.005 cm. Same number, very different claim.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–15 min · Initial Model — estimate the last digit

**Prompt on the board:**

> *"Before we name any rules: look at the figure your teacher is projecting. What is the reading? And which digit did the instrument tell you for certain, and which digit did you have to estimate?"*

Project `figures/reading_precision.png`:

![A 50 mL graduated cylinder filled to 27.5 mL, showing a concave meniscus between the 25 and 30 mL marks; tick marks represent every 1 mL; the liquid surface sits halfway between the 27 and 28 mL marks, with the meniscus bottom landing at 27.5 mL — illustrating that the last digit (5) is the estimated digit.](figures/reading_precision.png)

Give students 2 minutes silently. Target response: the cylinder shows 27.5 mL. The 27 is certain (the bottom of the meniscus falls between the 27 and 28 marks). The 5 is estimated — the observer judges that the liquid is about halfway between the two marks.

**Teacher facilitation language:**

> "How many significant figures does 27.5 mL have? Three. And two of those digits the instrument *told* you; one digit *you* contributed by estimating. That's always the deal. Every measurement has certain digits plus one estimated digit. Together those are the significant figures."

### 15–25 min · BTC Sorting Activity — sig-fig thin-slice sequence

*See Strategy Spotlight for full BTC mechanics.* Assign random groups. Students go to vertical surfaces (whiteboards, flipchart paper). Each group receives a set of sorting cards. The sequence is thin-sliced — start with easy cases, then advance:

**Round 1 — "How many sig figs?" (certain rules first):**

Post these values on the board one at a time. Groups write their count and brief reasoning on the vertical surface.

| Value | Sig figs | Key idea |
|---|---|---|
| 34.7 | 3 | all non-zero digits count |
| 0.0040 | 2 | leading zeros don't count; trailing zero after decimal does |
| 1500 | ambiguous (2 or 4) | trailing zeros without a decimal — the ambiguous case |
| 1500. | 4 | the decimal point signals all four digits are significant |
| 0.03080 | 4 | leading zeros don't count; captive zero counts; trailing zero after decimal counts |
| 102.0 | 4 | captive zero counts; trailing zero after decimal counts |

**Teacher facilitation prompts (circulate):**

> "Point to the digit you're unsure about. What rule would resolve it? Is there a decimal point? Does a zero sit between two non-zero digits?"

> "1500 — is there a way to write this number that removes the ambiguity?" (Scientific notation: 1.5 × 10³ is clearly two sig figs; 1.500 × 10³ is clearly four.)

**Anticipated student responses:**

- On 0.0040: "I said 4 because I counted all the digits." — prompt: "Which zeros can you actually see on the ruler? The leading zeros just tell you where the decimal is. They don't represent measurements."
- On 1500: "How are we supposed to know?" — validate: this is a genuine ambiguity in standard notation. Scientific notation solves it.
- On 1500.: "Oh — the dot changes everything?" — exactly. The decimal point is a signal that the trailing zeros are intentional, not just placeholders.

**Round 2 — Scientific notation (10 minutes):**

Each group converts two values from their set: one from standard notation to scientific notation, one from scientific to standard. Then they convert a value from the Reference Table (e.g., Avogadro's number: 6.02 × 10²³, or atomic radii in pm).

**Teacher facilitation language:**

> "Scientific notation isn't just for very large or very small numbers. It's the clearest way to show exactly how many sig figs you mean. When you write 1.5 × 10³, everyone knows you have two sig figs. The ambiguity disappears."

### 25–30 min · Reconnect + Surface the rules

Bring groups back. Ask each group to contribute one rule they built from the sorting. Synthesize on the board:

> "Let me try to turn everything your groups found into a short list."

**Sig-fig rules (build from student input):**

1. All non-zero digits are significant.
2. Zeros between non-zero digits (captive zeros) are significant.
3. Leading zeros (zeros before the first non-zero digit) are never significant — they are place-holders, not measurements.
4. Trailing zeros to the right of the decimal point are significant — they represent a deliberate measurement claim.
5. Trailing zeros in a whole number without a decimal point are ambiguous — use scientific notation to clarify.

Do not lecture this list — build it collaboratively. Students who contributed the insight should hear their reasoning echoed.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look at 0.03080 on the board. Turn to a partner: walk me through every digit, one at a time. Which ones count, and why? Be specific — 'it's a zero' is not a complete answer."

Target consensus: 0 (leading — no), 0 (leading — no), 3 (non-zero — yes), 0 (captive between 3 and 8 — yes), 8 (non-zero — yes), 0 (trailing after decimal — yes). Four significant figures.

> "Now: the number 1500 versus the number 1500. — what is the one-symbol difference, and what is the enormous difference in meaning?"

Target: 1500 could be 2, 3, or 4 sig figs; 1500. is unambiguously 4 because the decimal point signals that all four digits are intentional.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name what we've been doing all period. The digits in a measurement that carry meaning — all the certain digits plus the one estimated digit — those are the **significant figures**. Not 'significant' as in important; significant as in *they carry information about the measurement*. When you write 27.5 mL, all three digits are significant because they all came from reading the instrument."

> "The second idea: when a number is very large or very small — Avogadro's number, the mass of an electron, distances between atoms — writing it in standard notation is clumsy and hides the sig-fig count. We write it instead as a coefficient between 1 and 10, multiplied by a power of 10. That's **scientific notation**. 6,420,000 becomes 6.42 × 10⁶. The coefficient shows you exactly three significant figures; the exponent carries the scale."

> "And the third term brings us back to Lesson 02. **Precision** is the level of detail a measurement claims. A reading of 27.5 mL is more precise than a reading of 28 mL because it claims a tenth-of-a-milliliter level of certainty. More significant figures means a more precise claim — but only if your instrument can support it. Writing 27.500 mL when your cylinder is only marked to 1 mL is a false precision claim."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "If significant figures communicate precision, what does a calculator result of 15.2837 cm tell you about precision?" — *Expected response:* nothing useful — the calculator doesn't know what instrument was used. The sig-fig count in the answer must come from the data, not the display.
- "In 0.03080, how many sig figs are there — and why do leading zeros not count?" — *Expected response:* four. The leading zeros are place-holders that locate the decimal; they don't represent anything the instrument measured. Remove them in scientific notation: 3.080 × 10⁻².

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the model + Because/But/So expansion

Students return to their Do Now response (their first crack at the pencil phenomenon). They revise it: add the vocabulary, count the sig figs for each pencil reading (15 cm = 2; 15.0 cm = 3; 15.00 cm = 4), and explain what each measurement claims about the instrument.

Then run a **Because / But / So** sentence. Starter on the board:

> *"A calculator divides two measured values and displays 8.473921 cm."*

Model one aloud:

> "This six-decimal-place answer is misleading **because** the measured values that were divided each had only three significant figures — meaning the instruments could only support three digits of certainty — **but** the calculator treats all inputs as if they have infinite precision, **so** you must round the result to three significant figures: 8.47 cm."

Then have students write their own B/B/S using one of these starters:
- *"A student writes 1500 instead of 1.5 × 10³ on their lab report…"*
- *"The graduated cylinder is marked to 1 mL intervals, but a student records 27.53 mL…"*

### 39–40 min · Return to the phenomenon

> "Return to our three-student pencil story. Student C's measurement was 15.00 cm. What does that tell you about their ruler? And if you multiplied 15.00 cm × 2.0 cm to get an area, how many significant figures should the answer have, and why?"

Target: Student C's ruler has millimeter markings and one estimated digit — their instrument is precise to ±0.005 cm. Multiplying 15.00 × 2.0: the result is limited to 2 sig figs (the less precise measurement) → 30 cm². The calculator would say 30.00 — that's a false precision claim.

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud:

> *(a) How many significant figures are in 0.03080?*
> *(b) Write 6,420,000 in scientific notation.*
> *(c) Round 7.86342 to 3 significant figures.*

Expected answers are in `Answer_Key.docx`.

**Closing Reflection (SEL, 30 seconds):**

> "Today we said that every digit you write is a claim. In one sentence: where else in your life — outside of chemistry — does the number of digits you use make a difference? Who helped you figure something out today?"

Collect worksheets; note which groups' vertical-surface work showed the strongest reasoning on 1500 vs. 1500. — that tells you who has internalized trailing-zero ambiguity and who needs more practice before the quiz.

---

## Common Misconceptions

- **Misconception:** "15, 15.0, and 15.00 are the same number — they're equal." → **Correction:** As calculator values, yes. As scientific measurements, no. Each claims a different level of precision: 15 claims two significant figures (certainty to ±0.5 cm), 15.0 claims three (certainty to ±0.05 cm), 15.00 claims four (certainty to ±0.005 cm). Writing extra zeros does not improve your measurement; it misrepresents it.
- **Misconception:** "All zeros are insignificant." → **Correction:** Zeros come in three kinds. Captive zeros (between non-zero digits) are always significant: 102 has three sig figs. Trailing zeros after a decimal point are significant: 1.500 has four sig figs. Only leading zeros — those before the first non-zero digit — are not significant, because they are place-holders, not measurements.
- **Misconception:** "Rounding to 3 sig figs means 3 decimal places." → **Correction:** Significant figures and decimal places are different counts. 7.86342 rounded to 3 sig figs is 7.86 (the third sig fig is the second decimal place). But 1500 rounded to 3 sig figs is 1500 or, more clearly, 1.50 × 10³ — there are no decimal places in the standard-notation answer, but there are three sig figs.
- **Misconception:** "Scientific notation is just for very big numbers like Avogadro's number." → **Correction:** Scientific notation is useful at any scale when you want to make the sig-fig count explicit. 1.5 × 10³ clearly has two sig figs; 1500 is ambiguous. Chemists use scientific notation for clarity, not just for large numbers.
- **Misconception:** "The calculator answer is the most precise because it has the most digits." → **Correction:** The calculator has no knowledge of the instruments used. It propagates the floating-point representation of the input, which carries far more digits than the instruments can support. The scientist — not the calculator — is responsible for reporting the answer to the correct number of significant figures.

---

## Access & Differentiation

- **ELL/ENL supports:** Sig-fig rule poster with a visual example for each rule and the rule printed in plain language (no jargon). Sentence frame for the sorting activity: *"This value has ___ sig fig(s) because ___."* Word-choice box displayed on the board throughout: {significant figures, scientific notation, precision, estimated digit, leading zero, captive zero, trailing zero}. Pair the sorting-card activity with a color-coding convention: non-zero digits in black, captive zeros in blue, trailing-after-decimal zeros in green, leading zeros in gray. Color carries the rule visually before language does.
- **IEP/SPED supports:** Color-coded sig-fig rules card (laminated; matches the color convention above) for reference throughout. Pre-sorted subset of cards — present the six values that follow clear rules first; introduce trailing-zero-without-decimal ambiguity only after those six are solid. Calculator use permitted for all arithmetic. Enlarged `figures/reading_precision.png` printed at the station. Offer sentence starters for the B/B/S: *"This is a false precision claim because…"*
- **Extensions:** (1) Research why "1500" is ambiguous: write a paragraph explaining why scientific notation solves the problem and what conventions (like the "decimal point" signal) exist in standard notation. (2) Look up the rules for addition and subtraction with significant figures (different from multiplication/division) and solve two problems from the Reference Table. (3) Express Avogadro's number (6.02 × 10²³) and the approximate mass of an electron (9.11 × 10⁻³¹ kg) in standard notation — and explain why scientific notation is clearly better for both.

---

## Strategy Spotlight

**BTC (Building Thinking Classrooms) — thin-slice sig-fig sequence.** Building Thinking Classrooms (Peter Liljedahl, 2021) is a research-based framework for keeping all students in a state of productive cognitive engagement during mathematics and quantitative reasoning tasks. The two core mechanics for this lesson are **random grouping** and **vertical non-permanent surfaces**.

**How to run it in this lesson:**

1. **Random groups.** Before Phase 2, shuffle a deck of cards and deal one to each student — the suit determines the group (four groups of ~7, or use number-cards to make more groups). Randomness removes social stratification from group formation and signals that the class norm is *thinking together*, not performing for the teacher.
2. **Vertical surfaces.** Groups work standing up at whiteboards or large chart paper posted to the wall. Vertical non-permanent surfaces have two crucial properties: the work is visible to other groups (creating low-stakes cross-pollination) and it can be erased (lowering the perceived risk of being wrong). Research shows vertical surfaces produce 1.5× more "thinking time" than seated paper work, because students can't hide behind a notebook.
3. **Thin-slice sequence.** Post one value at a time (not the whole list). Each group writes their count on the board. You see all groups simultaneously. If a group is stuck, give only a *thinking prompt*, not the answer: "Which zeros are between non-zero digits? Is there a decimal point?" The sequence starts easy (34.7) to build confidence, then introduces ambiguity (1500) at the point where groups are ready to wrestle.
4. **Gallery walk moment.** After Round 1, give groups 90 seconds to look at each other's boards. The prompt: "Find one thing you want to borrow and one thing you want to argue with." This is not a presentation — it is a fast, low-stakes idea exchange.

**Why this strategy fits significant figures:** Sig figs are rule-bound but not obvious — students need to apply rules to new cases they have never seen before, not recall a memorized list. BTC keeps students in the zone where they are "thinking about the rules" rather than "waiting to be told the rules." When the vocabulary arrives in Phase 3, it names patterns the students have already discovered.

**Connection to Hochman literacy:** The Because/But/So sentence in Phase 4 asks students to articulate the chain: the instrument limits precision (*because*), but the calculator ignores that limit (*but*), so the scientist must round (*so*). Students who construct that sentence have understood significant figures as a claim about measurement — not a counting exercise.

**CRSE connection:** Precision and rounding are embedded in everyday reasoning across many cultural contexts (cooking, carpentry, textile work, financial planning). The opening circle prompt invites students to locate this skill in their own lived experience before it becomes a chemistry convention. That grounding honors the knowledge students bring and makes the chemistry formalism feel like a clarification of something already known, not an arbitrary rule imposed from outside.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — three-student pencil measurement + calculator over-precision story; return in Phase 4 with pencil area calculation |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — what does 15 cm *tell* you vs. *not tell* you?); Phase 3 (TT#2 — walk through 0.03080 digit by digit; 1500 vs. 1500.) |
| 3 | Students develop questions/models/procedures | Phase 2 estimate-the-last-digit (Initial Model); BTC sorting-card investigation builds the rules inductively; Phase 4 model revision with vocab |
| 4 | CCC defined and used | Lesson Overview · *Scale, Proportion, and Quantity*, explicit in Phase 3 vocabulary introduction and Phase 4 B/B/S expansion |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: significant figures / scientific notation / precision |
| 6 | Revisit phenomenon with evidence | Phase 4 — students classify each pencil reading's sig-fig count and explain what instrument each reading implies; Phase 5 Exit Ticket applies counting to new values |
| 7 | ENL/SPED supports | Access & Differentiation block: sentence frame, word-choice box, color-coded sig-fig card, pre-sorted card subset, sentence starters |
| 8 | Assessment check | Phase 5 — Exit Ticket (count sig figs in 0.03080; scientific notation; rounding to 3 sig figs) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked sig-fig example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **significant figures** — the digits in a measurement that carry meaning: all the digits the instrument reported with certainty, plus one estimated digit; when you write 27.5 mL, all three digits are significant because they all came from reading the instrument
- **scientific notation** — a way of expressing a number as a coefficient between 1 and 10, multiplied by a power of ten (e.g., 6,420,000 = 6.42 × 10⁶); scientific notation makes the sig-fig count explicit and handles very large and very small quantities without strings of placeholder zeros
- **precision** — the level of detail a measurement claims; a reading of 27.5 mL is more precise than 28 mL because it claims a tenth-of-a-milliliter level of certainty; precision is communicated by the number of significant figures recorded, and it must honestly reflect what the instrument can support
