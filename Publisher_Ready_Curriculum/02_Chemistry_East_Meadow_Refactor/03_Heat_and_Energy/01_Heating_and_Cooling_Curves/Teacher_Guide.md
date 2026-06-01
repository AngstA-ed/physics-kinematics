# Heating & Cooling Curves — Teacher Guide

## Cover

**Unit: Heat and Energy — Lesson 01: Heating & Cooling Curves**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: ACTIVE LEARNING · RESTORATIVE CIRCLE

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

**PS3-1** — *"Create a computational model to calculate the change in the energy of one component in a system when the change in energy of the other component(s) and energy flows in and out of the system are known."* The initial energies of the system's components — energy in fields, thermal energy, kinetic energy, energy stored in springs — are expressed in Joules in each component, with an algebraic description used to calculate total initial energy. In this lesson students read a temperature-vs-time graph as a record of where energy goes as it flows *into* a sample at a constant rate. They build the conceptual model that distinguishes two destinations for that energy: the **kinetic energy** of the particles (which raises temperature) and the **potential energy** stored in the arrangement of particles (which changes phase without raising temperature). Students identify the limitation of the simple "heat in → temperature up" model: during a phase change, heat flows in but the temperature does not rise, because the energy is doing work against the attractions between particles rather than speeding them up.

The Cross-Cutting Concept of **Energy and Matter** is the explicit lens: energy that flows into a sample is conserved — it is always accounted for, either as a temperature increase (kinetic) or as a phase change (potential). A flat plateau on the graph is not "missing" energy; it is energy being stored as potential energy in the new arrangement of particles.

### Phenomenon

Put a pot of water on a hot plate, drop a thermometer in, and turn the heat to maximum. As the water warms from room temperature, the thermometer climbs steadily — 40 °C, 60 °C, 80 °C, 100 °C. Then the water begins to boil vigorously and the thermometer *stops climbing*. The burner is still on full power. Steam is pouring off the surface. Energy is clearly still flowing into the pot — you can feel the heat, you can see the rolling boil — and yet for the entire time the water is boiling, the thermometer reads a stubborn 100 °C and refuses to move. Where is all that energy going if it is not making the water hotter?

**Driving question:** Why does the temperature of boiling water stay at 100 °C no matter how much heat you add?

### Javalab / Labs

- **Heating curve of water lab (ice → steam):** Students start with crushed ice in a beaker, place a thermometer in it, and heat at a steady rate while recording temperature every 30 seconds. They graph temperature vs. time and discover two plateaus: one at 0 °C (melting) and one at 100 °C (boiling). The Javalab "States of Matter / Heating Curve" simulation (`javalab.org` → Physics/Chemistry → *Change of State*) is an excellent no-spill digital version: students drag the heat slider and watch the particle animation and the temperature graph build in real time. Either the wet-lab or the simulation produces the temperature-vs-time graph that anchors the whole lesson — compare class data to `figures/heating_curve_water.png`.
- **Graph-interpretation practice:** Using `figures/heating_curve_water.png`, students label the five segments (A–E), identify which two are phase changes, and mark where kinetic energy is rising (sloped segments) versus where potential energy is rising (flat plateaus).

### Assessments

- **Heating-curve interpretation quiz** (district checkpoint, following lesson; see `Assessments/` folder once created): students label segments of an unlabeled heating curve, identify the phase(s) present in each region, and explain in writing why temperature is constant during a phase change in terms of kinetic and potential energy.
- **Exit Ticket** (Phase 5): three items built on a *cooling* curve of a different substance (so the values and direction differ from the worksheet's water heating curve) — identify the freezing plateau, state what happens to kinetic vs. potential energy along a sloped segment, and explain why temperature holds constant during condensation. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | PS3-1 (energy flowing into a sample is accounted for as kinetic energy → temperature change, or potential energy → phase change; identify the limit of the simple "heat → temperature" model) |
| **CCC focus** | Energy and Matter — energy that flows in is conserved and tracked: a rising temperature signals rising kinetic energy; a flat plateau signals rising potential energy as a phase change proceeds |
| **Strategy chips** | ACTIVE LEARNING — students generate and graph data (or drive the simulation), then physically annotate the graph to locate energy; RESTORATIVE CIRCLE — unit-opening circle to launch the Heat & Energy unit |
| **Materials** | Hot plate or Javalab *Change of State* simulation, beaker with crushed ice, thermometer or temperature probe, stopwatch, graph paper or projected grid, calculators optional, `figures/heating_curve_water.png` projected on screen |
| **Safety** | Hot plate and boiling water present a burn and scald hazard. Goggles on. Keep cords away from water. If using the wet-lab, the teacher controls the hot plate; students record. The Javalab simulation removes the burn hazard entirely and is recommended for a single-period lesson. |
| **Prior knowledge** | States of matter (solid, liquid, gas) and the particle model from the Matter unit; the idea that temperature is related to particle motion. Students should know the three phases and the names of the phase changes (melting, freezing, boiling/vaporization, condensation) before this lesson, though the lesson re-grounds them. |

**Lesson objectives — students can:**

- Read a temperature-vs-time (heating or cooling) graph and identify the sloped segments and the flat plateaus.
- Identify each plateau as a phase change and name which two phases are present during that plateau.
- Explain that along a sloped segment the particles' **kinetic energy** is rising (temperature increases), and along a plateau the **potential energy** is rising (temperature is constant) as energy goes into rearranging particles.
- Explain, using Energy and Matter, why the temperature of boiling water stays constant even though heat continues to flow in.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **Restorative Circle** to open the new Heat & Energy unit (see Strategy Spotlight). Everyone — teacher included — answers in one sentence: *"Tell us about a time you were waiting for something to heat up or cool down — a shower, a cup of cocoa, snow melting on the sidewalk. Did it change as fast as you expected?"* One round, every voice, pass allowed. This grounds the abstract idea of energy flow in something everyone has felt with their own hands, and it launches the unit with the message that everyone's experience belongs in this room.

Then post the **Do Now**:

> *"A pot of water is boiling hard on a stove turned up to maximum. A thermometer in the water reads 100 °C. You leave it boiling for five more minutes — burner still on full power. Predict: what does the thermometer read after those five minutes? Write your prediction and one sentence of reasoning."*

Give students 2 minutes to write silently, then take two or three predictions.

**Anticipated student responses to Do Now:**

- "It goes up — like 120 or 150 °C, because you keep adding heat." — capture this; it is the intuitive (and incorrect) prediction the phenomenon will challenge. Do not correct yet; write it on the board to revisit.
- "It stays at 100 because that's as hot as water gets." — close; affirm the observation, then probe: *why* is that as hot as it gets? Where does the extra heat go?
- "It goes down because some water turned to steam." — interesting; note it. The water level does drop, but the temperature of what remains is the question.

### 3–8 min · Phenomenon hook — the burner is on but the thermometer won't move

**Teacher actions.** Show the boiling-pot phenomenon (live on a hot plate, by short demo video, or by launching the Javalab *Change of State* simulation and dragging the heat slider to maximum). Narrate the contradiction: the burner is on full power, steam is pouring off, energy is obviously flowing into the pot — and the thermometer is frozen at 100 °C.

**Sample teacher language:**

> "Watch the thermometer. The burner has not changed — it is on maximum the whole time. Energy is flowing into this pot every single second; you can feel the heat coming off it. And yet the number on the thermometer is stuck. It will not move past 100. So here is the puzzle: if I am pouring energy into this water, and the water is not getting any hotter, then where is all that energy *going*?"

**Anticipated student responses:**

- "It's turning into steam." — excellent; capture it. That is the key. Push gently: so the energy is going into *making steam* rather than *raising the temperature* — hold that thought, we will name it in Phase 3.
- "The heat escapes into the air." — partly true (some always does), but the burner is adding far more than escapes; the real answer is the phase change. Validate and steer back.
- "Water can't get hotter than 100." — that is the rule, yes — but the question is *why*. The answer is the whole lesson.

**Driving question** (post on the board and leave it there):

> *Why does the temperature of boiling water stay at 100 °C no matter how much heat you add?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the boiling pot. Then:

> "Turn to your partner: the burner is still adding energy, but the temperature is not rising. Where could that energy be going if it is not making the water hotter? Try to name a specific destination — not just 'it disappears.'"

Target insight (leave open if no one lands it yet): the energy is being used to pull the water molecules *apart* — to turn liquid into gas — rather than to make them move faster. Energy that pulls particles apart is stored as **potential energy**; energy that makes them move faster shows up as temperature. We will name these in Phase 3.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–15 min · ACTIVE LEARNING — generate the heating curve (data before vocabulary)

**Before any formal vocabulary is introduced**, students generate the temperature-vs-time data themselves — either by running the ice → steam heating in the beaker (teacher operates the hot plate, students time and record) or by driving the Javalab *Change of State* simulation. Either way, the students produce the data; they are not handed a finished graph.

The recording task (students fill this in on the worksheet):

> *"Start with ice. Heat at a steady rate. Every 30 seconds, write down the temperature. Keep going until the sample is well past boiling. Do NOT stop recording when the temperature stops changing — those moments are the most important data points."*

**Teacher facilitation language (circulate):**

> "I see your temperature climbing — good. Now watch what happens as it gets near zero. Keep recording even if the number stops moving. A flat stretch in your data is not a mistake; it is the discovery."

> "You are the one collecting this data — own it. When you graph it in a minute, the shape will tell a story. Predict now: how many times do you think the line will go flat?"

**Anticipated student responses during data collection:**

- "The temperature stopped going up but the ice is still melting — should I keep writing the same number?" — yes, absolutely. That repeated number is the plateau. Write every reading.
- "My number jumped around at 100." — boiling is turbulent; record what you read and we will smooth it on the graph. The plateau is real even if individual readings wobble.
- "Why isn't it going up evenly?" — perfect observation to hold. The unevenness is the whole point of today.

### 15–22 min · Initial Model — graph the data and describe its shape

**Prompt on the board:**

> *"Plot your data: temperature (y-axis) vs. time (x-axis). Connect the points. Then, before we name anything, describe the shape in words: where does the line go up? Where does it go flat? How many flat parts are there?"*

Students plot individually for 3–4 minutes, then compare with a partner. Most class data will show the now-classic shape: a rise, a flat stretch near 0 °C, a rise, a longer flat stretch at 100 °C, and a final rise.

Project the reference figure so students can compare their hand-drawn graph to the idealized version:

![Temperature-vs-time heating curve for water heated at a constant rate from ice to steam. The purple line rises through five labeled segments A–E. Segment A: solid ice warming from −20 °C to 0 °C (sloped). Segment B: a flat plateau at 0 °C shaded blue, labeled 'melting (solid+liquid)'. Segment C: liquid water warming from 0 °C to 100 °C (sloped). Segment D: a longer flat plateau at 100 °C shaded orange, labeled 'boiling (liquid+gas)'. Segment E: gas/steam warming above 100 °C (sloped). Sloped segments are annotated 'KE rising (temperature up)' and the plateaus are annotated 'PE rising (temperature constant)'. The y-axis is temperature in degrees Celsius; the x-axis is time / heat added at a constant rate.](figures/heating_curve_water.png)

**Teacher facilitation language:**

> "Compare your graph to this one. Did your line go flat in the same two places? At what temperatures? Those two flat stretches are the heart of today's lesson."

> "Look at your partner's graph. Did they draw two flat parts or one? Where exactly did each flat part happen — at what temperature?"

**Anticipated student responses:**

- "I only got one flat part — I missed the one at zero because I started with cold water, not ice." — great diagnosis; that is exactly why we start with ice. The melting plateau only appears if you begin below 0 °C.
- "The flat part at 100 is way longer than the one at 0." — excellent observation; it takes much more energy to boil water than to melt the same amount of ice. Hold that — it connects to why boiling 'wastes' so much energy without heating.
- "Mine rises, goes flat, rises, goes flat, rises — five parts." — perfect. Five segments, two of them flat. Those two flat segments are where the puzzle lives.

### 22–30 min · Investigation — label the segments and locate the energy

Groups of three or four work through a structured analysis of the heating curve. Each student annotates their own graph (and the reference figure) and then compares with the group.

**Investigation tasks (on the worksheet):**

**Task 1 — Label the five segments.** For each segment A–E, name the phase(s) of water present:

| Segment | What is happening | Phase(s) present |
|---|---|---|
| A (rising, below 0 °C) | ice warming up | solid |
| B (flat, at 0 °C) | melting | solid + liquid |
| C (rising, 0–100 °C) | liquid warming up | liquid |
| D (flat, at 100 °C) | boiling | liquid + gas |
| E (rising, above 100 °C) | steam warming up | gas |

**Task 2 — Find the two phase changes.** Circle the two flat plateaus. Which phase change is each one? (B = melting; D = boiling/vaporization.)

**Task 3 — Sort the energy.** For each segment, decide: is the *temperature* changing? If temperature is changing, the particles are speeding up or slowing down (kinetic energy is changing). If temperature is constant, the energy is going somewhere else (potential energy — the particles are being pulled apart or together).

| Segment | Temperature changing? | Energy going to… |
|---|---|---|
| A | yes | kinetic (particles speed up) |
| B | no (flat) | potential (particles separating as solid → liquid) |
| C | yes | kinetic |
| D | no (flat) | potential (particles separating as liquid → gas) |
| E | yes | kinetic |

**Teacher facilitation prompts (circulate):**

> "On segment C the line is sloped — what is the temperature doing? Rising. So the particles are moving faster. Where is the energy going? Into making them move — that's kinetic energy."

> "On segment D the line is flat — the temperature is NOT changing even though heat is still flowing in. So the energy is NOT making particles move faster. Where is it going? Into pulling the liquid molecules apart to make a gas. That stored energy is potential energy."

> "Here is the connection to our phenomenon: segment D *is* the boiling pot. The thermometer stuck at 100 °C is this flat plateau. Now you can say where the energy is going."

**Anticipated student responses:**

- "On the flat parts the energy just disappears." — gently correct: energy is never lost. On a flat part, the energy is being *stored* as potential energy in the new arrangement of particles. It is not gone; it is hidden in the phase change.
- "Why does melting need energy at all if the temperature doesn't go up?" — because pulling solid particles loose from their fixed positions takes energy, even though that energy doesn't speed them up. That is the definition of a potential-energy change.
- "So kinetic = temperature and potential = phase change?" — that is exactly the pattern we are building. Sloped = kinetic = temperature change; flat = potential = phase change.

### 28–30 min · Reconnect + surface the pattern

Bring groups back together. Ask one group to put their segment table on the board. Ask the class:

> "Look at every segment. What do all the *sloped* segments have in common? What do both *flat* segments have in common?"

Surface the key pattern: every sloped segment is a temperature change with no phase change (energy → kinetic). Every flat segment is a phase change with no temperature change (energy → potential). The energy flowing in is always accounted for — it either speeds particles up or pulls them apart. That is the Energy and Matter CCC made visible on a graph.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look at your completed segment table. Turn to your partner: during the boiling plateau (segment D), the burner is adding energy the whole time. The temperature does not rise. So energy is flowing in but temperature is constant — is energy being conserved, or is some of it lost? Where exactly is it going?"

Target consensus: energy is fully conserved. During the plateau it flows into the *potential energy* of the system — the energy stored when liquid molecules are pulled apart into a gas. The molecules are not moving faster (so the temperature, which tracks average kinetic energy, holds steady), but the system stores more energy in the separated arrangement.

> "If I doubled the burner power, what would change about the boiling plateau — its height (temperature) or its length (time)?"

Target: the *height* stays the same (still 100 °C — that is fixed by the substance), but the plateau gets *shorter* in time because the water boils away faster. More power means faster phase change, not a higher temperature. This is a direct PS3-1 idea: energy flow rate changes how fast the component's energy changes, not the plateau temperature.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name what we've been tracking all period. The energy that makes particles move faster — the energy that shows up as a rising temperature on the sloped parts of the graph — is **kinetic energy**. Kinetic energy is the energy of motion; the faster the particles move, the higher the temperature. Every sloped segment on our curve is kinetic energy rising."

> "The energy that goes into pulling particles apart during a phase change — the energy that flows in on the flat plateaus without raising the temperature — is **potential energy**. Potential energy is stored energy, set by how far apart the particles are and how strongly they attract each other. Every flat plateau on our curve is potential energy rising while kinetic energy (and temperature) holds steady."

> "And the moment a substance switches from one state to another — solid to liquid, liquid to gas — is a **phase change**. A phase change happens at a constant temperature, and it is exactly where the energy goes into potential energy instead of kinetic energy. The two plateaus on our graph, melting and boiling, are the two phase changes."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "On a sloped segment, which kind of energy is rising — kinetic or potential?" — *Expected response:* kinetic; the temperature is rising, which means the particles are moving faster.
- "During boiling, the thermometer reads a constant 100 °C. What does that constant temperature tell you about the kinetic energy of the molecules?" — *Expected response:* the average kinetic energy is constant (temperature is not changing), so the added energy must be going into potential energy — the molecules separating into gas.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the model + Because/But/So expansion

Students return to their Initial Model graph. They annotate it with the new vocabulary: write "KE rising" along each sloped segment and "PE rising — phase change" along each plateau, and label the two plateaus *melting* and *boiling*.

Then run a **Because/But/So** sentence about the phenomenon. Starter on the board:

> *"While water boils, the burner keeps adding energy but the thermometer stays at 100 °C."*

Model one aloud:

> "While water boils, the temperature stays at 100 °C **because** the energy flowing in is being stored as potential energy — it is pulling the liquid molecules apart into gas rather than speeding them up — **but** temperature only measures the average *kinetic* energy of the particles, which is not changing during the phase change, **so** the thermometer reads a constant 100 °C even though energy is still flowing into the pot the entire time."

Then have students write their own B/B/S using one of these starters:

- *"When you put a pot of water on a hot stove, it heats up quickly at first but then seems to 'stall' at 100 °C…"* (hint: kinetic vs. potential energy)
- *"A heating curve has a flat plateau at the melting point even though heat is still being added…"*

**Anticipated student responses:**

- "Because the energy turns into steam instead of heat." — good start; sharpen the wording: "because the energy is stored as potential energy by separating the molecules into a gas, not added as kinetic energy."
- "But the temperature only measures how fast they move." — excellent; that is precisely the "but." Temperature tracks average kinetic energy only.

### 39–40 min · Return to the phenomenon

> "Return to our boiling pot. The burner was on full power and the thermometer was stuck at 100 °C. Now you have the language. In one sentence, using the words *potential energy* and *phase change*, explain where the burner's energy was going."

Target: "The burner's energy was going into the potential energy of the phase change — pulling liquid water molecules apart into steam — so it raised the potential energy of the system instead of the kinetic energy, which is why the temperature stayed at 100 °C."

> "That stuck thermometer is segment D on your graph. The 'missing' energy was never missing — it was stored as potential energy in steam. That is the Energy and Matter idea: every joule the burner adds is accounted for, either as a hotter sample or as a changed phase."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud (note: the Exit Ticket uses a **cooling** curve of a *different* substance so students transfer the idea rather than recall the worksheet's water heating curve):

> *A liquid substance is cooled at a constant rate. Its cooling curve shows the temperature dropping, then holding flat at 80 °C for a while, then dropping again.*
> *(a) What is happening to the substance during the flat plateau at 80 °C, and what is this temperature called?*
> *(b) Along the sloped part before the plateau (temperature dropping), is the particles' kinetic energy increasing or decreasing? Explain in one sentence.*
> *(c) During the flat plateau, energy is still flowing out of the substance, yet the temperature does not drop. In one sentence, explain why, using the words potential energy and phase change.*

Expected answers are in `Answer_Key.docx`.

**Closing Reflection (SEL, 30 seconds):**

> "Today an everyday thing — a pot that won't get hotter than boiling — turned out to hide an invisible energy story. In one sentence: what is one thing that surprised you about where energy goes, and who — a partner or a moment in the lab — helped you see it?"

Collect worksheets; note which students correctly distinguished sloped (kinetic) from flat (potential) regions versus students who still equate "heat added" with "temperature rises." That equivalence is the central misconception — target those students for a brief one-on-one check at the start of the next lesson.

---

## Common Misconceptions

- **Misconception:** "If you keep adding heat, the temperature always keeps rising." → **Correction:** During a phase change the temperature holds constant even though heat keeps flowing in. The energy is stored as potential energy (separating particles), not added as kinetic energy (speeding particles up). The flat plateaus on the heating curve are the direct evidence that "more heat" does not always mean "higher temperature."
- **Misconception:** "On the flat parts of the graph, no energy is being added / the energy disappears." → **Correction:** Energy is flowing in the entire time, at the same rate as everywhere else — that is why the plateau takes *time*. The energy is conserved and stored as potential energy in the new arrangement of particles. A long plateau means a lot of energy went into the phase change.
- **Misconception:** "Temperature and heat are the same thing." → **Correction:** Heat is energy flowing in or out; temperature measures only the *average kinetic energy* of the particles. During a phase change, heat flows but temperature is constant — proof that they are different quantities. Heat can change either kinetic energy (temperature) or potential energy (phase).
- **Misconception:** "Boiling water gets hotter the longer it boils / the higher you turn the burner." → **Correction:** Pure water boils at 100 °C and stays there. Turning up the burner makes it boil *faster* (shorter plateau, water disappears sooner), but the temperature of the remaining liquid stays at 100 °C. More power changes the *rate* of the phase change, not its temperature.
- **Misconception:** "Melting and boiling need energy, but the energy makes the substance hotter." → **Correction:** Melting and boiling absorb energy at constant temperature. The absorbed energy raises potential energy (breaking the attractions that hold particles in place), not kinetic energy, so the temperature does not change until the phase change is complete.

---

## Access & Differentiation

- **ELL/ENL supports:** Sentence frames for the segment analysis: *"On segment ___ the temperature is ___, so the ___ energy is rising."* and *"During a phase change the temperature is ___ because the energy goes into ___ energy."* Word-choice box displayed on the board throughout: {kinetic energy, potential energy, phase change, melting, boiling, plateau, slope}. Pair the abstract terms with gestures: hands moving fast for kinetic energy / rising temperature, hands pulling apart for potential energy / phase change. Allow students to label the graph segments with the gesture-paired word before writing full sentences.
- **IEP/SPED supports:** Provide a pre-labeled axis grid and a partially completed segment table (segments A, C, E already filled as "kinetic / temperature rising") so the student focuses on the two phase-change plateaus (B and D), which are the conceptual target. Assign clear partner roles during data collection: one student reads the thermometer aloud, one records, one watches the clock. Offer the heating-curve figure with the five segments pre-divided by vertical lines so the student matches each region to a phase rather than drawing the divisions. Provide sentence starters for the Exit Ticket.
- **Extensions:** (1) Why is the boiling plateau (segment D) so much longer than the melting plateau (segment B)? Research and explain in terms of the energy needed to separate liquid molecules into a gas versus loosening a solid into a liquid (heat of vaporization ≫ heat of fusion). (2) Draw the *cooling* curve for the same water sample (steam → ice) and label where energy is *released* as potential energy (condensation, freezing). How is it the mirror image of the heating curve? (3) Predict and sketch the heating curve for a substance with a melting point of −10 °C and a boiling point of 60 °C, heated from −40 °C to 80 °C — where are the plateaus?

---

## Strategy Spotlight

**ACTIVE LEARNING — students generate and annotate their own data.** The Active Learning strategy puts the cognitive work in the students' hands: instead of receiving a finished heating curve and being told what it means, students *produce* the temperature-vs-time data (live or in the Javalab simulation), *graph* it, and *discover* the two plateaus before any vocabulary is introduced. The flat stretches are not told to them — they emerge from data the students collected and graphed themselves. Then, in the annotation step, students physically mark the energy regions on their own graph, which converts a passive figure into an active analytical object.

**How to run it in this lesson (Phase 2):**

1. Students collect temperature readings every 30 seconds as ice is heated to steam (wet-lab or simulation). The crucial coaching move: *keep recording during the flat stretches.* Students who stop recording when the number stops changing miss the plateau entirely — and missing it is the most common reason students later believe "heat always raises temperature."
2. Students graph their own data and describe the shape in their own words before any term like "phase change" is spoken.
3. Students annotate the graph: "KE rising" on slopes, "PE rising" on plateaus, and circle the two phase changes. This annotation is the active-learning payoff — the graph becomes a record of *their* reasoning, not a textbook image.

**Why Active Learning fits heating curves:** the central misconception (more heat → always hotter) is intuitively sticky and resists being told. It only dislodges when a student watches their *own* data go flat while the heat keeps flowing. The plateau has to be experienced as a surprise in data the student trusts. That is precisely what Active Learning provides, and it is why the lesson withholds the finished figure until students have drawn their own.

**RESTORATIVE CIRCLE (unit-opening circle).** Because this is the first lesson of the Heat & Energy unit, open with a brief restorative circle (2–3 min). The prompt — *"a time you waited for something to heat up or cool down"* — surfaces everyday thermal experiences (waiting for a shower to warm, cocoa to cool, snow to melt) that the whole class shares, and it primes the Because/But/So writing in Phase 4 by getting students to articulate a *cause* (added or removed heat), a *contrast* (but it took longer than expected), and a *consequence* in their own words first.

**CRSE connection:** the circle and the phenomenon both use kitchen-and-home thermal experiences (boiling water, cocoa, melting snow) that every student has lived, regardless of background. Grounding an abstract energy concept in universally shared domestic experiences honors students' out-of-school knowledge and makes the science feel continuous with their lived experience rather than confined to the lab.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — boiling pot whose thermometer stays at 100 °C; opening-circle home thermal experiences; return in Phase 4 to explain the stuck thermometer |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — where does the burner's energy go if not to temperature?); Phase 3 (TT#2 — is energy conserved during the boiling plateau, and where does it go?) |
| 3 | Students develop questions/models/procedures | Phase 2 ACTIVE LEARNING data collection (ice → steam), Initial Model graph from their own data, group segment-and-energy analysis tables |
| 4 | CCC defined and used | Lesson Overview · *Energy and Matter*; explicit in Phase 2 reconnect (energy always accounted for), Phase 3 vocabulary, and Phase 4 B/B/S (energy stored as potential energy during boiling) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: kinetic energy / potential energy / phase change |
| 6 | Revisit phenomenon with evidence | Phase 4 — students return to the boiling pot armed with the labeled graph (segment D = boiling plateau) to explain the constant temperature in terms of potential energy |
| 7 | ENL/SPED supports | Access & Differentiation block: sentence frames, word-choice box, gesture pairing, pre-labeled axis grid, partially completed segment table, partner roles |
| 8 | Assessment check | Phase 5 — Exit Ticket on a *cooling* curve of a different substance (freezing plateau, KE direction on the slope, constant temperature during condensation) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked heating-curve example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **kinetic energy** — the energy of particle motion; the faster the particles move, the higher the temperature, so a rising temperature (a sloped segment on a heating curve) signals rising kinetic energy
- **potential energy** — energy stored in the arrangement and separation of particles; during a phase change (a flat plateau on a heating curve) the energy flowing in raises potential energy without changing the temperature
- **phase change** — a change from one state of matter to another (melting, freezing, boiling/vaporization, condensation) that occurs at a constant temperature; on a heating or cooling curve it appears as a flat plateau where potential energy changes while kinetic energy (temperature) holds steady
