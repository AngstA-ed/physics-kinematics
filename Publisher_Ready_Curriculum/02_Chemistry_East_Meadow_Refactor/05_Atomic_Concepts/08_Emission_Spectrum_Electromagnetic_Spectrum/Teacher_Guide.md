# Emission Spectrum & the Electromagnetic Spectrum — Teacher Guide

## Cover

**Unit: Atomic Concepts — Lesson 08: Emission Spectrum & the Electromagnetic Spectrum**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: HOCHMAN

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

**HS-PS4-4** — *"Evaluate the validity and reliability of claims in published materials of the effects that different frequencies of electromagnetic radiation have when absorbed by matter."* In this lesson students build the conceptual machinery needed to evaluate those claims: the electromagnetic (EM) spectrum is a single continuous family of waves that differ in wavelength, frequency, and energy, and the energy a wave carries is what determines whether it can damage matter. Radio waves and ultraviolet light are *the same kind of thing* — both are electromagnetic radiation — but they sit at opposite ends of the energy scale. That single fact is the key to evaluating a published claim such as "5G radio towers cause cell damage" versus "UV light causes skin cancer."

The Cross-Cutting Concept of **Energy and Matter** is the explicit lens: energy carried by radiation is transferred to matter when it is absorbed, and the *amount* of energy per wave determines what that transfer can do. Low-energy radiation (radio, microwave) cannot break the chemical bonds in a cell; high-energy radiation (UV, X-ray, gamma) can. The relationship is fixed and quantitative: higher frequency means shorter wavelength means higher energy (E = hf; c = fλ). Students do not need to compute with Planck's constant for this lesson, but they must master the *direction* of the relationship.

This lesson also closes the loop on the Atomic Concepts unit: the **emission spectrum** — the discrete bright lines an excited element gives off — is direct evidence that electrons occupy fixed energy levels. When an electron falls from a higher level to a lower one, the atom emits a single photon of a specific energy, and therefore a specific color. The hydrogen spectrum students see is the experimental fingerprint that confirmed the Bohr energy-level model from earlier in the unit.

### Phenomenon

You can stand in front of a radio transmitter all day and feel nothing — radio waves pass through you constantly (your phone is receiving them right now). But fifteen minutes of unprotected midday sun gives you a sunburn, and a few seconds of direct gamma radiation would be lethal. All three — radio, ultraviolet, gamma — are *the same kind of thing*: electromagnetic radiation, waves of energy traveling at the speed of light. So why is one harmless and the others dangerous? The visceral contrast is the hook: *same family of waves, wildly different effect on your body.* Pair this with a neon sign or a hydrogen discharge tube glowing a specific pink-red — that exact color is not a coincidence; it is the fingerprint of which atom is inside and how its electrons are arranged. Same underlying physics (light is energy emitted and absorbed by matter), two everyday encounters: the sunburn and the glowing sign.

**Driving question:** All electromagnetic waves are the same kind of thing — so why is UV light dangerous to your skin while radio waves pass through you harmlessly?

### Javalab / Labs

- **Light Emission Spectra Simulator (Javalab — "Emission/Atomic Spectra"):** Students select different elements (hydrogen, helium, neon, mercury) and observe that each produces its own unique set of discrete bright lines, not a continuous rainbow. They connect the discrete lines back to the energy-level (Bohr) model from earlier in the unit: each line is a specific electron "drop" between levels. Use `figures/hydrogen_emission_lines.png` as the printed reference for the hydrogen case so students can read exact wavelengths. (PhET "Models of the Hydrogen Atom" or a classroom hydrogen/neon discharge tube with handheld diffraction-grating glasses are equivalent live options.)
- **EM spectrum sorting activity:** Students receive a shuffled set of cards — each naming a region (radio, microwave, infrared, visible, ultraviolet, X-ray, gamma) along with a real-world example (FM radio, microwave oven, TV remote, sunlight color, sunburn, dental X-ray, radiation therapy). Their task is to sort the cards from lowest energy to highest energy and predict which examples are most likely to damage living tissue. They then check their ordering against `figures/em_spectrum_band.png`. This is the core sense-making activity for the wavelength–frequency–energy relationship.

### Assessments

- **EM spectrum & wavelength–energy quiz** (district checkpoint, following lesson; see `Assessments/` folder once created): students order EM regions by energy, state the wavelength–frequency–energy relationship, and explain why one region damages tissue while another does not.
- **Exit Ticket** (Phase 5): three items — order two EM regions by energy with reasoning; given a wavelength comparison, identify which wave has higher frequency and energy; and write one sentence explaining, in terms of energy, why UV causes sunburn but radio does not. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | HS-PS4-4 (evaluate claims about effects of different EM frequencies absorbed by matter) |
| **CCC focus** | Energy and Matter — radiation carries energy; when absorbed, that energy is transferred to matter; the energy *per wave* (set by its frequency) determines whether the transfer can break bonds and damage cells |
| **Strategy chips** | HOCHMAN — appositive sentence to define the electromagnetic spectrum crisply; B/B/S sentence in Phase 4 |
| **Materials** | EM-spectrum sorting cards (one set per group), `figures/em_spectrum_band.png` and `figures/hydrogen_emission_lines.png` projected, Javalab Emission Spectra simulator (or hydrogen/neon discharge tubes + diffraction-grating glasses), the energy-level (Bohr) diagram from Lesson 01 for reference, 2025 NYS Chemistry Reference Tables |
| **Safety** | If using live discharge tubes, they run on high voltage — only the teacher handles the power supply; students observe from a safe distance. Never look directly at a UV lamp. No hazardous chemicals. |
| **Prior knowledge** | Atomic Concepts Lesson 01 (energy levels / Bohr model — electrons occupy fixed energy levels) and the idea that electrons can absorb energy to move to a higher level. Students should recall "ground state" and "excited state" loosely; this lesson formalizes what happens when the electron falls back. |

**Lesson objectives — students can:**

- Order the regions of the electromagnetic spectrum (radio → gamma) by wavelength, frequency, and energy.
- State the relationship between wavelength, frequency, and energy: as wavelength decreases, frequency and energy increase.
- Explain, using Energy and Matter, why high-energy radiation (UV, X-ray, gamma) can damage living tissue while low-energy radiation (radio, microwave) cannot.
- Interpret an emission spectrum as evidence that electrons occupy fixed energy levels: each bright line is a photon emitted when an electron falls between two levels.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers: *"Name one type of 'invisible signal' that travels through the air around us right now — Wi-Fi, a phone signal, sunlight, heat from a heater. How do you know it's there if you can't see it?"* One round, one sentence each, no judgment. This surfaces the intuition that the air is full of electromagnetic radiation we cannot see but can detect by its effects — exactly the lens for today.

Then post the **Do Now**:

> *"You can stand next to a radio antenna all day and feel nothing. But fifteen minutes in strong midday sun gives you a sunburn. Both radio waves and the ultraviolet light in sunlight are the same kind of thing — electromagnetic radiation. Write one sentence: why might one be harmless and the other harmful, if they're the same kind of wave?"*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "Because the sun is way more powerful / brighter than a radio." — partial; affirm, then probe: a tiny UV lamp can still burn you and a giant radio tower still won't. It's not just *how much* — it's *what kind*. Hold that thought.
- "Because UV is stronger than radio waves." — close; push on the word *stronger*. What does "stronger" mean for a wave — louder, faster, higher energy? Today we'll define it precisely.
- "I don't get how they're the same kind of thing." — exactly the right tension to notice; validate: they really are the same family of waves, just at very different energies. That difference is what today is about.

### 3–8 min · Phenomenon hook — same family, different effect

**Teacher actions.** Project `figures/em_spectrum_band.png`. Walk the band left to right.

![A horizontal band of the electromagnetic spectrum divided into seven labeled regions from left to right: Radio, Microwave, Infrared, Visible (shown as a rainbow gradient red through violet), Ultraviolet, X-ray, and Gamma. A blue arrow beneath the left half points left and is labeled 'longer wavelength (λ)'; an orange arrow beneath the right half points right and is labeled 'higher frequency (f) and energy (E)'. A purple arrow above the band runs left to right, labeled 'radio waves: harmless to cells' on the left end and 'UV / X-ray / gamma: can damage cells' on the right end.](figures/em_spectrum_band.png)

> "Every region on this band is electromagnetic radiation — the same fundamental thing, all traveling at the speed of light. The ONLY thing that changes as you move across the band is the wavelength, the frequency, and the energy. On the left — radio, microwave — the waves are long and low-energy. On the right — UV, X-ray, gamma — the waves are short and high-energy. Notice the purple arrow on top: harmless on the left, dangerous on the right. The danger tracks the energy."

Then show a glowing discharge tube (or `figures/hydrogen_emission_lines.png`):

> "And here's the second half of the phenomenon. When you energize hydrogen gas, it glows — and if you spread that light out, you don't get a rainbow. You get these four specific bright lines. Each element gives a different set. That's not decoration — it's a fingerprint of how the atom's electrons are arranged. We'll connect that back to the energy levels you learned earlier in this unit."

**Anticipated student responses:**

- "So the danger depends on which part of the spectrum it's in?" — exactly; the energy of the wave is the deciding factor, and energy increases left to right.
- "Why does hydrogen make exactly those lines and not others?" — great question; that's the emission spectrum, and it's direct evidence of fixed electron energy levels. We'll get there in the simulator.
- "Is visible light dangerous?" — visible light sits in the middle; it can warm you but generally doesn't break the bonds in your skin cells the way UV does. The line between "safe" and "damaging" falls right around the UV boundary.

**Driving question** (post on the board and leave it there):

> *All electromagnetic waves are the same kind of thing — so why is UV light dangerous to your skin while radio waves pass through you harmlessly?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the spectrum band or the emission lines. Then:

> "Turn to your partner: on the band, radio is on the far left and gamma is on the far right. Microwaves cook food; gamma rays are used to kill cancer cells. Both transfer energy to matter. What does the *position* on the band tell you about how much energy each wave carries — and why that matters for what it can do to your body?"

Target insight (leave open if no one lands it yet): position on the band = energy level of the wave. Moving right means higher frequency, shorter wavelength, and more energy per wave — and more energy per wave means more ability to break the chemical bonds that hold cells together. That is the **Energy and Matter** CCC, which we'll name formally in Phase 3.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–15 min · ABCs Activity — EM spectrum sorting before the formal definition

**Before any formal vocabulary is introduced**, students build intuition by sorting the EM spectrum from low energy to high energy using real-world examples.

Each group receives a shuffled set of sorting cards. Each card names a region and a familiar example:

| Region | Everyday example on the card |
|---|---|
| Radio | FM radio station / Wi-Fi |
| Microwave | microwave oven / phone signal |
| Infrared | TV remote / heat from a fire |
| Visible | the colors your eyes see |
| Ultraviolet | sunburn / tanning bed |
| X-ray | dental or bone X-ray |
| Gamma | cancer radiation therapy |

**Part 1 — Sort by energy (prediction, no reference yet):**

> "Without looking at the spectrum band, arrange these seven cards in order from the *lowest-energy* wave to the *highest-energy* wave. Use what you already know: which of these could hurt you, and which feel harmless? Write down your order and one sentence of reasoning."

**Part 2 — Predict the danger zone:**

> "Now draw a line in your ordering: on one side, the waves you think are safe to be around; on the other, the waves you'd want shielding from. Where does the line fall?"

**Teacher facilitation language (circulate):**

> "Think about your own experience. You use Wi-Fi and a microwave every day and you're fine. You wear sunscreen for UV. The dentist puts a lead apron on you for X-rays. What does the level of caution tell you about the energy?"

> "Don't just guess randomly — use the clue in the danger. The more protection something needs, the higher its energy. Order them by how careful you have to be."

**Anticipated student responses during ABCs:**

- "I put X-ray as the most dangerous because of the lead apron." — good reasoning; and gamma is even higher — that's why radiation therapy is so tightly controlled. The danger is tracking the energy.
- "Where does visible light go? It doesn't seem dangerous OR totally harmless." — exactly the right instinct; visible sits in the middle, between infrared and UV. It's the boundary region.
- "Radio and microwave both seem safe — which is lower?" — radio waves are the longest wavelength and lowest energy of all; microwaves are next. Both are below the danger line.

### 15–22 min · Initial Model — order the band and locate the danger line

**Prompt on the board:**

> *"Before we name the relationship: using your sorted cards, fill in the order of the seven EM regions from longest wavelength to shortest. Then, next to each, write 'low,' 'medium,' or 'high' energy. Finally, circle the boundary where waves start to become dangerous to living tissue."*

Students work individually for 3 minutes, then compare with a partner. Project `figures/em_spectrum_band.png` only *after* they commit to an order, so they can self-check.

Target ordering (longest wavelength / lowest energy → shortest wavelength / highest energy):

> Radio → Microwave → Infrared → Visible → Ultraviolet → X-ray → Gamma
> low … low … low … medium … **high** … high … high
> Danger line falls between Visible and Ultraviolet.

**Teacher facilitation language:**

> "Look at the band. Where did your sorted order match, and where did it slip? Most groups get radio and gamma at the two ends — the tricky one is where the danger line falls. It's right at ultraviolet: that's the first region energetic enough to damage the molecules in your skin."

> "Notice the two arrows under the band point in opposite directions. Wavelength gets *longer* to the left; frequency and energy get *higher* to the right. So as wavelength goes down, energy goes up. They move in opposite directions."

**Anticipated student responses:**

- "I put UV before visible." — check the band: visible light (the rainbow) is lower energy than UV. UV is *beyond* violet — that's literally what 'ultra-violet' means. So UV comes after visible.
- "Why is the danger line at UV and not at visible?" — UV is the first region carrying enough energy per wave to break the chemical bonds in DNA and skin proteins. Visible light usually can't. That bond-breaking is the actual mechanism of a sunburn.
- "So longer wavelength always means lower energy?" — yes, for electromagnetic waves that relationship is fixed: longer wavelength ↔ lower frequency ↔ lower energy.

### 22–30 min · Investigation — Emission Spectra simulator

Groups of three or four use the **Light Emission Spectra Simulator** (Javalab) or observe discharge tubes through diffraction-grating glasses. Each student records what they see for each element.

**Task — observe and record:**

| Element | What you see (continuous rainbow OR discrete lines?) | How many distinct bright lines? |
|---|---|---|
| Hydrogen | | |
| Helium | | |
| Neon | | |
| Mercury | | |

Then have students focus on hydrogen and compare to the printed reference:

![A black horizontal band representing the hydrogen emission spectrum in the visible region, with four discrete colored vertical lines: a red line at 656 nm, a blue line at 486 nm, a blue-violet line at 434 nm, and a violet line at 410 nm. Each line is labeled with its wavelength in nanometers. A blue arrow beneath the band points right, labeled 'wavelength (nm) — longer wavelength = lower energy.' Text above the band notes 'higher energy (violet)' on the left and 'lower energy (red)' on the right.](figures/hydrogen_emission_lines.png)

**Teacher facilitation prompts (circulate):**

> "Is hydrogen giving you a smooth rainbow, or separate lines with black gaps between them? Why might it be lines and not a continuous rainbow?"

> "Does neon look the same as hydrogen? Why would two different elements give two different sets of lines, if light is just light?"

> "Connect this to the energy-level model from earlier in this unit. When an electron is given energy, it jumps up to a higher level. It can't stay there — it falls back. When it falls, the atom gives off a photon of light. The size of the drop sets the energy of the photon, and the energy of the photon sets its color."

**Anticipated student responses during the simulator:**

- "Hydrogen has exactly four lines I can see, but neon has way more." — yes; more electrons and more possible energy-level drops means more lines. Each element's set is unique — that's the fingerprint.
- "Why aren't there lines everywhere — why the black gaps?" — because the electron can only occupy *fixed* energy levels, so only *certain* drops are allowed. Only those exact photon energies (colors) get emitted. The gaps are forbidden energies.
- "The red line is at 656 — is that nanometers?" — yes, 656 nm, in the red part of visible light. The violet line at 410 nm is higher energy because shorter wavelength means higher energy.

### 28–30 min · Reconnect + surface the relationship

Bring groups back together. Ask one group to report the hydrogen lines from longest to shortest wavelength (656 → 486 → 434 → 410 nm). Then ask the class:

> "Look at the hydrogen lines. The red line is at 656 nm; the violet line is at 410 nm. Violet has the *shorter* wavelength. Which one carries more energy — and how do you know from everything we've seen today?"

Surface the key idea: the violet line (410 nm) has the shorter wavelength, so it has the higher frequency and the higher energy — it came from a *bigger* electron drop. The red line (656 nm) has the longer wavelength and lower energy — a smaller drop. Shorter wavelength always means higher energy, whether we're talking about hydrogen's colors or the whole EM spectrum.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look at the EM spectrum band and the hydrogen lines together. Turn to your partner: in BOTH figures, the same rule keeps showing up — shorter wavelength goes with higher energy. State that rule in your own words, and then explain what it tells you about why UV is dangerous but radio is not."

Target consensus: across the whole electromagnetic spectrum, as wavelength gets shorter, frequency and energy get higher. UV light has a much shorter wavelength than radio, so it carries far more energy per wave — enough energy to break the chemical bonds in skin cells. Radio waves have long wavelengths and very low energy, not enough to break any bonds, so they pass through harmlessly.

> "Now a prediction: a microwave oven and a tanning bed both transfer energy to matter. Which one is more likely to cause the kind of bond-breaking damage that leads to skin cancer, and why?"

Target: the tanning bed (UV) — UV has a much shorter wavelength and higher energy per wave than microwaves, so it can break chemical bonds in DNA. Microwaves mainly make water molecules jiggle (heat), which cooks food but doesn't carry enough energy per wave to break the bonds in DNA.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name what we've been studying. The whole band — radio through gamma — is the **electromagnetic spectrum**: the full range of electromagnetic waves, ordered by wavelength, frequency, and energy. Here is the Hochman appositive move to lock that definition into a sentence. An appositive is a phrase set off by dashes that renames or defines the noun next to it. Say it with me:
>
> *The electromagnetic spectrum — the full range of electromagnetic waves ordered by wavelength, frequency, and energy — runs from low-energy radio waves to high-energy gamma rays.*
>
> The phrase between the dashes defines the term in the same sentence. You'll use this structure on the Exit Ticket."

> "Two of those words describe a single wave. **Wavelength** is the distance from one wave crest to the next — long for radio, short for gamma. **Frequency** is how many wave cycles pass a point each second — low for radio, high for gamma. And here's the relationship that ties everything together: wavelength and frequency move in *opposite* directions, and frequency and energy move *together*. So as wavelength gets shorter, frequency gets higher, and energy gets higher. That one chain explains the whole band: short wavelength → high frequency → high energy → able to damage matter."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "Where on the band is the wavelength longest, and where is the energy highest?" — *Expected response:* wavelength is longest at the radio (far left); energy is highest at gamma (far right). They are at opposite ends, which is the whole point of the opposite-direction relationship.
- "Back to the hydrogen emission spectrum — what makes the violet line (410 nm) higher in energy than the red line (656 nm)?" — *Expected response:* the violet line has the shorter wavelength, so higher frequency and higher energy; it came from a larger electron drop between energy levels.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the model + Appositive + Because/But/So expansion

Students return to their Initial Model (the ordered EM regions with the danger line). They annotate it with vocabulary: label the left end "long wavelength / low frequency / low energy" and the right end "short wavelength / high frequency / high energy," then write the appositive sentence.

**Appositive sentence (model on board):**

> *"The electromagnetic spectrum — the full range of electromagnetic waves ordered by wavelength, frequency, and energy — runs from low-energy radio waves to high-energy gamma rays."*

Ask students to write a parallel appositive for one region:

> *"Ultraviolet light — a high-energy region of the spectrum just beyond ___ — carries enough energy per wave to ___."*

Then run a **Because / But / So** sentence about the phenomenon. Starter on the board:

> *"Radio waves pass through your body harmlessly, but ultraviolet light from the sun can damage your skin."*

Model one aloud:

> "Radio waves pass through your body harmlessly **because** they have a very long wavelength and therefore a very low energy per wave — not enough to break any chemical bonds — **but** ultraviolet light has a much shorter wavelength and a much higher energy per wave — **so** when UV is absorbed by your skin it carries enough energy to break the bonds in DNA and skin proteins, which is what causes a sunburn and, over time, skin cancer."

Then have students write their own B/B/S using one of these starters:

- *"A dentist puts a lead apron on you for an X-ray but not when you listen to the radio…"* (hint: X-rays are far higher energy than radio waves)
- *"The hydrogen violet line (410 nm) carries more energy than the red line (656 nm)…"* (hint: shorter wavelength = higher energy = larger electron drop)

**Anticipated student responses:**

- "Because X-rays have high energy." — good start; push for the full Because frame: "because X-rays have a very short wavelength and very high energy per wave, enough to pass through soft tissue and potentially damage cells, but radio waves have low energy that the body shrugs off, so the dentist shields you from X-rays but not from radio."
- "Because the violet line has a shorter wavelength." — excellent; push for the So: "so it has a higher frequency and higher energy, which means the electron dropped a larger gap between energy levels to release it."

### 39–40 min · Return to the phenomenon

> "Return to our driving question. Radio waves and UV are the same kind of thing — electromagnetic radiation. Now you have the rule. In one sentence, using the words *wavelength* and *energy*, explain why UV burns your skin but radio doesn't."

Target: "UV light has a much shorter wavelength than radio waves, so it carries much higher energy per wave — enough energy to break the chemical bonds in skin cells, which radio waves cannot do."

> "And the glowing hydrogen tube? Those four lines are direct evidence that electrons live at fixed energy levels. Each color is one specific electron drop. The spectrum isn't decoration — it's a window into the structure of the atom."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud:

> *(a) Two regions of the EM spectrum: infrared and gamma. Which one carries more energy per wave? Explain your answer using wavelength.*
> *(b) Wave A has a wavelength of 700 nm. Wave B has a wavelength of 200 nm. Which wave has the higher frequency, and which carries more energy? How do you know?*
> *(c) In one sentence, explain — in terms of energy — why ultraviolet light can damage your skin but radio waves cannot, even though both are electromagnetic radiation.*

Expected answers are in `Answer_Key.docx`.

**Closing Reflection (SEL, 30 seconds):**

> "Today we learned that invisible waves all around us range from totally harmless to dangerous, depending on their energy. In one sentence: what is one thing you'll think about differently now — sunscreen, a microwave, Wi-Fi, an X-ray — and who or what in today's lesson helped you see it that way?"

Collect worksheets; note which students correctly connect *shorter wavelength → higher frequency → higher energy* versus students who reverse the relationship (a common error). Reversing the wavelength–energy direction is the main conceptual stumbling block — target those students for a brief one-on-one check at the start of the next lesson.

---

## Common Misconceptions

- **Misconception:** "Longer wavelength means more energy because the wave is bigger." → **Correction:** It is the opposite. For electromagnetic radiation, *longer* wavelength means *lower* frequency and *lower* energy. Radio waves are the longest waves and the lowest energy; gamma rays are the shortest waves and the highest energy. "Bigger wave" (longer wavelength) does not mean "more powerful per wave."
- **Misconception:** "Radio waves and UV are completely different things." → **Correction:** They are the same kind of thing — electromagnetic radiation, all traveling at the speed of light. They differ only in wavelength, frequency, and energy. Their position on a single continuous spectrum is the only difference, and that difference is exactly what determines their effect on matter.
- **Misconception:** "UV is dangerous because the sun is so bright/intense." → **Correction:** Brightness (intensity) is about *how many* waves arrive, not the energy *per* wave. A small UV lamp can still cause damage, and an enormously powerful radio transmitter still cannot — because the *energy per wave* (set by frequency) is what determines whether a wave can break chemical bonds. UV is dangerous because of its high energy per wave, not its brightness.
- **Misconception:** "An emission spectrum is a continuous rainbow." → **Correction:** An emission spectrum is a set of *discrete* bright lines on a dark background, not a continuous rainbow. The discrete lines are direct evidence that electrons occupy fixed energy levels: only specific electron drops are allowed, so only specific photon energies (colors) are emitted. A continuous rainbow comes from a hot solid (like the sun's surface), not from an excited gas.
- **Misconception:** "Each element's emission lines are random / could be any element's." → **Correction:** Each element produces a unique, reproducible set of lines — a fingerprint — because each element has its own unique set of energy levels. Astronomers identify the elements in distant stars precisely by reading these fingerprints in starlight.

---

## Access & Differentiation

- **ELL/ENL supports:** Sentence frames for sorting and the Exit Ticket: *"___ has a ___ wavelength, so it has ___ energy."* and *"___ is dangerous to skin because ___."* Word-choice box displayed on the board throughout: {electromagnetic spectrum, wavelength, frequency, energy, radio, ultraviolet, gamma, absorb}. Pair vocabulary with gestures: hands far apart for "long wavelength / low energy," hands close together for "short wavelength / high energy." Provide the EM-region names on the sorting cards in English with a small icon (a radio, a sun, a bone X-ray) so the example is recognizable regardless of reading level.
- **IEP/SPED supports:** Provide a pre-printed EM-spectrum order strip (Radio → Gamma) with blanks only for the energy labels (low/medium/high), so the student's task is to mark the energy trend, not recall the order from scratch. Pre-highlight the danger line position on the strip. For the simulator, assign clear partner roles: one student selects the element, one records the number of lines. Offer the Exit Ticket with the answer choices for part (a) and (b) as a fill-in ("Wave ___ has higher energy because it has a ___ wavelength") rather than open response.
- **Extensions:** (1) Use c = fλ to show that as wavelength λ decreases, frequency f must increase (since c, the speed of light, is constant). Compute the frequency of the 656 nm and 410 nm hydrogen lines and confirm the violet line has the higher frequency. (2) Research one published claim about EM radiation and health (e.g., "5G causes harm," "blue light from screens damages eyes") and evaluate it using the energy argument from this lesson — does the radiation in question carry enough energy per wave to break chemical bonds? This is the HS-PS4-4 claim-evaluation skill applied directly. (3) Explain how astronomers use emission/absorption spectra to determine which elements are present in a distant star.

---

## Strategy Spotlight

**HOCHMAN — Appositive sentence.** The Hochman Writing Method (Judith Hochman and the Writing Revolution) treats sentence-level writing as a thinking tool. For this lesson the featured technique is the **appositive**, a noun phrase set off by dashes (or commas) that renames or defines the noun it follows. The appositive is ideal for the dense, term-heavy content of the EM spectrum because it forces the student to embed a definition inside a complete subject–verb sentence rather than parking the definition in isolation.

**The target appositive for this lesson:**

> *The electromagnetic spectrum — the full range of electromagnetic waves ordered by wavelength, frequency, and energy — runs from low-energy radio waves to high-energy gamma rays.*

This sentence structure does three things simultaneously: (1) names the term, (2) defines it in a concise phrase between the dashes, and (3) states the key fact (the ordering principle) in the main clause. Students who can write and say this sentence — not just recite the definition separately — are integrating the term into their active vocabulary.

**How to run it in this lesson (Phase 3 → Phase 4):**

1. Post and read aloud the model appositive sentence together (Phase 3 vocabulary).
2. Ask students to write a parallel appositive for a specific region: *"Ultraviolet light — a high-energy region just beyond visible light — carries enough energy to..."* This requires them to substitute in what they learned about that region's position and effect.
3. In Phase 4, students write their own appositive for the EM spectrum or a chosen region, then a Because/But/So sentence comparing two regions. Cold-call two or three students; ask: does the appositive phrase correctly define the term? Does the main clause state the right fact?

**Why the appositive fits the EM spectrum:** The term "electromagnetic spectrum" sounds intimidating, but the appositive unpacks it: *spectrum* (a full range), *electromagnetic* (waves of electric and magnetic energy), ordered by three measurable properties. Forcing the definition into the middle of a sentence makes students commit to *what* is being ordered and *by what*, which is exactly the conceptual core of HS-PS4-4.

**CRSE connection:** The opening circle prompt (invisible signals all around us — Wi-Fi, phone signals, sunlight) draws on technology students use constantly and on shared bodily experiences like sunburn that cross every cultural background. The claim-evaluation extension (evaluating a published health claim about 5G or blue light) invites students to bring the media messages they actually encounter into the science classroom and equips them to reason about those claims with evidence — a direct enactment of HS-PS4-4 and of culturally responsive, real-world-relevant instruction.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — sunburn vs. standing by a radio antenna; glowing discharge tube; return in Phase 4 with the UV-vs-radio explanation |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — what does band position tell you about energy and effect?); Phase 3 (TT#2 — state the wavelength–energy rule and apply it to UV vs. radio) |
| 3 | Students develop questions/models/procedures | Phase 2 ABCs sorting (order regions by energy before any reference); Initial Model (order the band, locate the danger line); emission-spectra simulator observation |
| 4 | CCC defined and used | Lesson Overview · *Energy and Matter*, explicit in Phase 3 vocabulary and Phase 4 B/B/S (energy per wave → bond-breaking → tissue damage) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: electromagnetic spectrum / wavelength / frequency |
| 6 | Revisit phenomenon with evidence | Phase 4 — students return to the UV-vs-radio driving question using the energy relationship and explain the hydrogen lines as electron-drop evidence |
| 7 | ENL/SPED supports | Access & Differentiation block: sentence frames, word-choice box, gestures, pre-printed order strip, partner roles, fill-in Exit Ticket option |
| 8 | Assessment check | Phase 5 — Exit Ticket (order IR vs. gamma by energy; compare 700 nm vs. 200 nm waves; one-sentence UV-vs-radio energy explanation) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked emission-spectrum example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **electromagnetic spectrum** — the full range of electromagnetic waves, ordered by wavelength, frequency, and energy; it runs from low-energy radio waves (long wavelength) through visible light to high-energy gamma rays (short wavelength); all of these waves travel at the speed of light and differ only in their wavelength, frequency, and energy
- **wavelength** — the distance from one wave crest to the next; long for low-energy radiation (radio) and short for high-energy radiation (gamma); as wavelength gets shorter, frequency and energy increase (they move in opposite directions to wavelength)
- **frequency** — the number of wave cycles that pass a point each second; high frequency means high energy and short wavelength; frequency and energy increase together, while wavelength decreases — this is the relationship that determines whether radiation can damage matter
