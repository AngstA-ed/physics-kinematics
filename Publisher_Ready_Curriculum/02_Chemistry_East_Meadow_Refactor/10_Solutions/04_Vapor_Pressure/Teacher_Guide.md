# Vapor Pressure — Teacher Guide

## Cover

**Unit: Solutions — Lesson 04: Vapor Pressure**
East Meadow Schools × Valley Stream Central High School District
Strategy chips: ACTIVE LEARNING

---

## Curated Resources (from East Meadow Scope & Sequence)

### NYSSLS Standards

**HS-PS1-3** — *"Plan and conduct an investigation to gather evidence to compare the structure of substances at the bulk scale to infer the strength of electrical forces between particles."* In this lesson the bulk-scale evidence is **equilibrium vapor pressure** and **boiling point**: a liquid whose particles are held together by strong intermolecular forces (IMF) evaporates slowly, so it has a low vapor pressure at a given temperature and a high boiling point; a liquid with weak IMF evaporates readily, so it has a high vapor pressure and a low boiling point. Students read these relationships directly off **Reference Table H** (Vapor Pressure of Four Liquids) in the 2025 NYS Chemistry Reference Tables, using it as the quantitative bridge between particle-scale forces and measurable, macroscopic behavior.

The Cross-Cutting Concept of **Cause and Effect** is the explicit lens: stronger IMF (cause) → fewer particles escape into the vapor at a given temperature → lower vapor pressure and a higher temperature required for boiling (effect). External air pressure is the other cause in the chain — a liquid boils at the temperature where its vapor pressure equals the surrounding pressure, so lowering the external pressure lowers the boiling point.

### Phenomenon

A camp stove takes far longer to cook rice on a 14,000-foot Colorado peak than at sea level — not because the flame is weaker, but because the water boils at a lower temperature up there (about 86–90 °C instead of 100 °C). Boiling water that is "only" 86 °C cooks food more slowly. Now flip the scene to the deep ocean floor: at a hydrothermal vent two miles down, water gushes out at 350–400 °C and stays *liquid*, never boiling, even though that is far above its sea-level boiling point. Same substance — water — boiling at 90 °C in one place and refusing to boil at 400 °C in another. The variable that changed is not the water and not the heat; it is the **pressure pressing down on the liquid's surface**.

**Driving question:** Why does the same liquid boil at different temperatures in different places — low on a mountaintop, and not at all (until extreme temperatures) at the bottom of the ocean?

### Javalab / Labs

- **Pressure-cooker / vacuum-flask demonstration (teacher-led):** A sealed pressure cooker raises the internal pressure above 101.3 kPa, so water inside must reach a higher temperature (≈120 °C) before its vapor pressure equals the surrounding pressure and it boils — that is why a pressure cooker cooks faster. The reverse demo, if a vacuum flask or syringe is available: pull a partial vacuum over warm (≈45 °C) water in a sealed syringe and students watch it boil at room temperature as the external pressure drops below the water's vapor pressure. No external URL required; a Javalab "vapor pressure / boiling" simulation can substitute if glassware is unavailable. Pair the demo with `figures/vapor_pressure_curves.png`.
- **Reference Table H curve interpretation:** Using Reference Table H (or the figure below), students find the temperature at which each liquid's vapor pressure equals 101.3 kPa (its normal boiling point), compare the four liquids' curves, and rank the liquids by IMF strength. This is the core data-reading skill for the HS-PS1-3 standard.

### Assessments

- **Vapor pressure & boiling point quiz** (district checkpoint, following lesson; see `Assessments/` folder once created): students read a normal boiling point off a vapor-pressure curve, predict the direction a boiling point shifts when external pressure changes, and rank liquids by IMF strength from their vapor pressures.
- **Exit Ticket** (Phase 5): three items — read propanone's normal boiling point off Reference Table H; predict whether water boils above or below 100 °C in a sealed pressure cooker and explain why; one Cause-and-Effect sentence linking IMF strength to vapor pressure. The Exit-Ticket liquids and pressures are deliberately distinct from the worksheet practice. See `Answer_Key.docx`.

---

## Lesson Overview

| | |
|---|---|
| **Duration** | 42 minutes (1 period) |
| **NYSSLS link** | HS-PS1-3 (infer IMF strength from bulk-scale evidence — vapor pressure and boiling point; read Reference Table H) |
| **CCC focus** | Cause and Effect — stronger IMF → fewer particles escape to vapor → lower vapor pressure and higher boiling point; a liquid boils when its vapor pressure equals the external pressure, so changing the external pressure changes the boiling temperature |
| **Strategy chips** | ACTIVE LEARNING — students generate and test predictions on Reference Table H before any term is defined; whole-class "stand and rank" of the four liquids by IMF |
| **Materials** | 2025 NYS Chemistry Reference Tables (Reference Table H), pressure cooker (or vacuum syringe / Javalab sim), hot plate, water, thermometer, `figures/vapor_pressure_curves.png` projected, student worksheet |
| **Safety** | The pressure-cooker demo involves steam and a hot surface — keep students at a distance, never open a pressurized cooker, release pressure fully before opening. Goggles and apron for anyone near the hot plate. The vacuum-boiling demo uses warm (not boiling) water and is low-risk. |
| **Prior knowledge** | Intermolecular forces (hydrogen bonding, dipole-dipole, dispersion) from the Bonding unit; the particle model of evaporation; reading a curve and a value off the NYS Reference Tables. Students should recognize that water molecules hydrogen-bond before this lesson. |

**Lesson objectives — students can:**

- Read the equilibrium vapor pressure of a liquid at a given temperature, and the normal boiling point (vapor pressure = 101.3 kPa), off Reference Table H.
- Explain that a liquid boils when its vapor pressure equals the external (atmospheric) pressure, and predict the direction a boiling point shifts when external pressure rises or falls.
- Compare two liquids' vapor-pressure curves and infer which has stronger intermolecular forces.
- Explain, using Cause and Effect, why water boils below 100 °C on a mountaintop and stays liquid above 100 °C under high pressure.

---

## Phase 1 · Engage *(0 – 10 min)*

### 0–3 min · Opening Circle + Do Now

Begin with a brief **community-building opening circle** (2–3 min). Everyone — teacher included — answers: *"Tell us about a time something behaved differently in a different place — food that cooked differently somewhere, ears that popped on a drive or flight, a recipe that 'didn't work' on a trip. What was different about the place?"* One round, one sentence each, no judgment. This surfaces the lived intuition that **altitude and pressure change how things behave** — which is exactly the variable at the heart of today's phenomenon.

Then post the **Do Now**:

> *"Boxes of cake mix and pots of pasta often have a separate 'high-altitude' instruction: cook longer, or add more water. Why would the same food need different cooking instructions on a mountain than at sea level? Write your best guess in one sentence."*

Give students 2 minutes to write silently, then take two or three responses.

**Anticipated student responses to Do Now:**

- "Because it's colder up high, so it takes longer." — capture; gently probe: the *stove* is just as hot. What if the issue isn't the air temperature but the boiling water itself?
- "The air is thinner up there." — excellent; that is the key variable. Press: thinner air means *less pressure*. Hold that thought.
- "I don't know — water always boils at 100, doesn't it?" — perfect tension to name; validate: "Most people think 100 °C is fixed. Today we find out it isn't."

### 3–8 min · Phenomenon hook — same water, two extremes

**Teacher actions.** Tell the story in two acts. Act 1, the mountaintop: on a 14,000-foot peak, water boils at about 86–90 °C, not 100 °C, so rice and pasta take much longer to cook — boiling water there is genuinely cooler. Act 2, the deep ocean: at a hydrothermal vent two miles down, water pours out at 350–400 °C and stays *liquid* — it never boils, even hundreds of degrees above its sea-level boiling point. Same substance, opposite behavior.

> "Nothing about the water molecules changed between the mountaintop and the ocean floor. So what *did* change? On the mountain, there's less air pressing down on the water. At the bottom of the ocean, there's enormous pressure pressing down. The pressure on the surface is the variable — and it controls the boiling point."

Project the `figures/vapor_pressure_curves.png` figure:

![Line graph titled 'Vapor Pressure vs. Temperature (Reference Table H)' plotting equilibrium vapor pressure in kPa against temperature in degrees Celsius for two liquids. The water curve (purple, labeled 'strong H-bonding') rises gradually and crosses 101.3 kPa at 100 °C, marked with a dot labeled '100 °C'. The ethanol curve (blue, labeled 'weaker IMF') sits above and to the left of the water curve, crossing 101.3 kPa near 78 °C. A dashed horizontal line marks 101.3 kPa, labeled 'sea-level air pressure'. A red dotted horizontal line marks about 70 kPa, labeled 'mountaintop air pressure', and the water curve crosses it near 90 °C, marked with a red dot labeled '90 °C'.](figures/vapor_pressure_curves.png)

**Sample teacher language:**

> "Look at the purple water curve. Find where it crosses the dashed line at 101.3 kPa — that's normal air pressure at sea level. It crosses at 100 °C. That is why water boils at 100 °C at sea level: that's the temperature where the water's own escaping-vapor pressure finally equals the air pushing down. Now look at the red dotted line lower down — that's the thinner air on a mountaintop, about 70 kPa. The water curve reaches that pressure at only about 90 °C. So on the mountain, the water 'wins' against the lighter air sooner, and boils cooler."

**Anticipated student responses:**

- "So boiling happens when the two pressures are equal?" — exactly the idea; we'll name it formally in Phase 3.
- "Why is the ethanol curve higher than water's?" — great noticing; ethanol's particles escape more easily, so at any temperature more of them are in the vapor. We'll connect that to intermolecular forces during the activity.
- "So in the ocean, the pressure line would be way up off the top of the chart?" — yes; the deep-ocean pressure is so high the water can't reach it until extreme temperatures, so it stays liquid far past 100 °C.

**Driving question** (post on the board and leave it there):

> *Why does the same liquid boil at different temperatures in different places — low on a mountaintop, and not at all (until extreme temperatures) at the bottom of the ocean?*

### 8–10 min · Notice & Wonder + Turn-and-Talk #1

Two columns on the board: **I notice… / I wonder…**

Collect 3–4 responses about the two curves and the pressure lines. Then:

> "Turn to your partner: the water curve and the ethanol curve are different heights at the same temperature. At 60 °C, ethanol's vapor pressure is much higher than water's. What might that difference tell us about the two liquids' particles — which liquid's particles are 'holding on' to each other more tightly?"

Target insight (leave open if no one lands it yet): the liquid that escapes *less* into the vapor (lower curve = water) has particles that hold together more strongly. That is the link between vapor pressure and **intermolecular forces** — we will name it in Phase 3.

---

## Phase 2 · Explore *(10 – 30 min)*

### 10–16 min · ABCs Activity — read and rank Reference Table H before any definition

**Before any formal vocabulary is introduced**, students build intuition by reading Reference Table H (or the projected figure) and ranking the liquids — generating and testing predictions, the heart of ACTIVE LEARNING.

Hand out (or open) Reference Table H. The four liquids on the table are **propanone, ethanol, water,** and **ethanoic acid**. Each student works the prediction first, then checks against the data.

**Part 1 — Predict before reading:**

> "Without reading any numbers yet — just from the shape of the curves — which liquid do you predict escapes into the vapor most easily? Which liquid do you predict needs the highest temperature to boil? Write your prediction and your reasoning."

**Part 2 — Read the table and rank:**

Have students fill in this table from Reference Table H (or the figure for water and ethanol):

| Liquid | Vapor pressure at 50 °C (read from table) | Normal boiling point (temp where VP = 101.3 kPa) |
|---|---|---|
| propanone |  |  |
| ethanol |  |  |
| water |  |  |
| ethanoic acid |  |  |

> "The normal boiling point is the temperature where each liquid's curve crosses the 101.3 kPa line. Trace each curve up to 101.3 kPa, then drop straight down to the temperature axis and read it."

**Teacher facilitation language (circulate):**

> "Trace with your finger — start at 101.3 on the pressure axis, slide right until you hit the curve, then drop straight down. What temperature do you land on? That's the normal boiling point."

> "Propanone's curve is the steepest and farthest to the left. What does that tell you about how easily its particles escape compared to water's?"

**Anticipated student responses during ABCs:**

- "Propanone hits 101.3 first, at the lowest temperature." — affirm; so propanone boils at the lowest temperature of the four (≈56 °C). What does an easy-to-boil liquid suggest about its particle forces?
- "Water and ethanoic acid need the highest temperatures." — yes; both have strong intermolecular forces, so their particles escape least easily.
- "How do I read between the gridlines?" — estimate to the nearest few degrees; the curve interpretation is the skill, not perfect precision.

### 16–24 min · Initial Model — explain the mountaintop with the curve

**Prompt on the board:**

> *"Before we name the rule: use the water curve to explain the mountaintop. At sea level the air pushes down at 101.3 kPa and water boils at 100 °C. On a mountain the air pushes down at only about 70 kPa. Using the curve, find the temperature where water's vapor pressure equals 70 kPa. Does water boil hotter or cooler on the mountain? Write your reasoning."*

Students work individually for 3 minutes, then compare with a partner.

Target answer:

> At 70 kPa the water curve sits at about 90 °C. Because boiling happens when the liquid's vapor pressure equals the surrounding air pressure, and the mountain air pressure (70 kPa) is reached at a *lower* temperature (≈90 °C), water boils **cooler** on the mountain — which is why food cooks more slowly.

**Teacher facilitation language:**

> "Find 70 on the pressure axis. Slide right to the water curve. Drop down. What temperature? About 90 °C. So the boiling point dropped from 100 to 90 just because the air pushed down less hard."

**Anticipated student responses:**

- "So less pressure means a lower boiling point?" — exactly; you've found the rule before I've stated it.
- "Does that mean in the pressure cooker it's the opposite?" — great prediction; hold it for the demo — more pressure should raise the boiling point.

### 24–30 min · Investigation — pressure-cooker / vacuum demonstration

Run the demonstration (or the Javalab simulation). Two parts:

**Part A — Pressure cooker (higher external pressure):** A sealed pressure cooker traps steam and raises the internal pressure to roughly 200 kPa. Ask: *using the curve, what temperature must the water reach before its vapor pressure equals 200 kPa?* (Off the top of the chart — well above 100 °C, about 120 °C.) That is why a pressure cooker cooks faster: the water gets hotter than 100 °C before it boils.

**Part B — Vacuum boiling (lower external pressure):** Pull a partial vacuum over warm (~45 °C) water in a sealed syringe (or show the Javalab clip). The water boils at room temperature. Ask: *why?* The external pressure dropped below the water's vapor pressure at that temperature, so the liquid boils without any added heat.

**Teacher facilitation language:**

> "In the cooker, we raised the pressure pushing down. So the water has to climb to a higher temperature — and a higher vapor pressure — before it can boil. In the vacuum, we lowered the pressure pushing down, so the water boils at a temperature where it normally just sits quietly. Same water. We only changed the pressure on its surface."

**Anticipated student responses:**

- "So boiling isn't really about a fixed temperature at all?" — right; boiling is about the *match* between vapor pressure and external pressure. 100 °C is only special at sea level.
- "Could you boil water with ice still in your hand?" — at a low enough pressure, yes — water boils at room temperature in a strong vacuum. That surprises everyone.
- "Is the pressure cooker dangerous?" — yes if mishandled; that's why we never open a pressurized cooker. The high pressure is exactly what makes it cook fast.

---

## Phase 3 · Explain *(30 – 36 min)*

### 30–33 min · Turn-and-Talk #2 + class consensus

> "Look at your ranked table and the demonstrations. Turn to your partner: what is the *pattern*? What does a liquid's vapor pressure tell you about the forces between its particles, and what does it tell you about its boiling point?"

Target consensus:

> A liquid with a **high** vapor pressure (its curve is high/left, like propanone) has **weak** intermolecular forces — its particles escape easily — so it boils at a **low** temperature. A liquid with a **low** vapor pressure (its curve is low/right, like water and ethanoic acid) has **strong** intermolecular forces — its particles escape with difficulty — so it boils at a **high** temperature. And any liquid boils at the temperature where its vapor pressure equals the surrounding pressure.

> "If I gave you a brand-new liquid and told you it has a very low vapor pressure at room temperature, what would you predict about its intermolecular forces and its boiling point?"

Target: strong IMF, high boiling point.

### 33–36 min · Vocabulary introduction (exactly 3 terms)

**Sample teacher language:**

> "Let's name what we've been measuring all period. When a liquid sits in a closed container, particles leave the surface to become vapor *and* vapor particles fall back into the liquid. When those two rates are equal, the pressure of the vapor stops changing — that steady pressure is the **equilibrium vapor pressure**. It's exactly what every curve on Reference Table H plots: the equilibrium vapor pressure at each temperature."

> "The temperature where a liquid's vapor pressure reaches the surrounding air pressure is when bubbles of vapor can form throughout the liquid — that's **boiling point**. The **normal boiling point** is the special case where the surrounding pressure is 101.3 kPa, which is where each Reference Table H curve crosses the 101.3 kPa line."

> "And the reason the curves differ from liquid to liquid is the third term: **intermolecular forces** — the attractions *between* particles. Strong intermolecular forces, like the hydrogen bonding in water, hold particles in the liquid, so few escape: low vapor pressure, high boiling point. Weak intermolecular forces let particles escape easily: high vapor pressure, low boiling point."

Post the three terms on the board. Students fill them in on their notes.

**Discussion prompts to deploy here:**

- "Ethanol's vapor pressure is higher than water's at every temperature. What does that say about ethanol's intermolecular forces compared with water's?" — *Expected response:* ethanol's IMF are weaker than water's, so its particles escape more easily; that's why ethanol boils at ≈78 °C and water at 100 °C.
- "A liquid boils when its vapor pressure equals 101.3 kPa — but only at sea level. On a mountain, what pressure does it need to reach?" — *Expected response:* only the lower mountain air pressure (≈70 kPa), so it boils at a lower temperature.

---

## Phase 4 · Elaborate *(36 – 40 min)*

### 36–39 min · Revise the model + Because/But/So expansion

Students return to their Initial Model (the mountaintop curve reading). They revise it by labeling: (a) the 101.3 kPa line as "sea-level boiling," (b) the 70 kPa line as "mountaintop boiling," and (c) writing one cause→effect statement linking the external pressure to the boiling temperature. Then run a **Because/But/So** sentence:

> *"Water boils at a lower temperature on a mountaintop than at sea level."*
> *"This happens **because** ______, **but** _______, **so** _______."*

Model one aloud:

> "Water boils at a lower temperature on a mountaintop **because** the air pressure pushing down on the surface is lower there (about 70 kPa instead of 101.3 kPa), **but** a liquid still boils only when its own vapor pressure equals the surrounding pressure, **so** the water reaches that match at a lower temperature (about 90 °C) and boils cooler — which is why food takes longer to cook."

Then have students write one for the **hydrothermal vent** (high external pressure → boiling point pushed far above 100 °C, so the water stays liquid at 400 °C).

### 39–40 min · Return to the phenomenon

> "Return to our two extremes. Using the words *vapor pressure* and *external pressure*, explain in one sentence why the same water boils at 90 °C on a mountain but refuses to boil at 400 °C at a deep-sea vent."

Target: "Water boils when its vapor pressure equals the external pressure; the mountain's low external pressure is matched at a low temperature (≈90 °C), while the deep ocean's enormous external pressure is not matched until an extreme temperature, so the vent water stays liquid far above 100 °C."

---

## Phase 5 · Evaluate *(40 – 42 min)*

### 40–42 min · Exit Ticket + Closing Reflection

Post or read aloud:

> *(a) Using Reference Table H, find the normal boiling point of propanone (the temperature where its vapor pressure equals 101.3 kPa).*
> *(b) A sealed pressure cooker raises the pressure on the water's surface to about 200 kPa. Will the water inside boil above or below 100 °C? Explain why in one sentence using vapor pressure.*
> *(c) In one sentence, explain why a liquid with strong intermolecular forces has a low vapor pressure and a high boiling point (use Cause and Effect).*

Expected answers are in `Answer_Key.docx`. (The Exit-Ticket liquid (propanone) and pressure (200 kPa, pressure cooker) are distinct from the worksheet practice, which centers on water and ethanol at 70 kPa / mountaintop.)

**Closing Reflection (SEL, 30 seconds):**

> "Today we found out that 100 °C isn't a magic number — it depends on where you are. In one sentence: what is one everyday thing (cooking, weather, travel) you now understand differently, and who or what helped you see it?"

Collect worksheets; note which students correctly read the *crossing point with 101.3 kPa* as the boiling point versus students who read a vapor pressure value off the y-axis instead. Misreading the axes is the main stumbling block — target those students for a brief one-on-one check next lesson.

---

## Common Misconceptions

- **Misconception:** "Water always boils at 100 °C." → **Correction:** 100 °C is the boiling point of water *only* at 101.3 kPa (sea-level pressure). Boiling occurs when a liquid's vapor pressure equals the surrounding pressure, so the boiling temperature rises with external pressure (pressure cooker, ocean depth) and falls with reduced pressure (mountaintop, vacuum). The Reference Table H curve makes this explicit: read off any external pressure and you get a different boiling temperature.
- **Misconception:** "Boiling means the liquid is being heated as hot as it can get." → **Correction:** Boiling is not a maximum temperature — it is the condition where vapor pressure equals external pressure. Under reduced pressure water can boil at room temperature without being hot at all; under high pressure it can reach 120 °C or more before boiling.
- **Misconception:** "A higher vapor pressure means stronger forces holding the liquid together." → **Correction:** It is the opposite. High vapor pressure means particles escape *easily*, which means the intermolecular forces are *weak*. The volatile liquid (propanone) has the highest vapor pressure and the weakest IMF; water and ethanoic acid have low vapor pressures and strong IMF.
- **Misconception:** "Vapor pressure depends on how much liquid you have." → **Correction:** Equilibrium vapor pressure depends only on the substance and the temperature, not on the amount of liquid or the size of the container's surface. A teaspoon and a swimming pool of water at the same temperature have the same equilibrium vapor pressure.
- **Misconception:** "The boiling point and the normal boiling point are the same thing." → **Correction:** The *normal* boiling point is the specific boiling temperature when the external pressure is exactly 101.3 kPa — that's the value Reference Table H gives at the 101.3 kPa line. The boiling point in general is whatever temperature matches the *actual* surrounding pressure, which changes with altitude and conditions.

---

## Access & Differentiation

- **ELL/ENL supports:** Sentence frames for the curve reading and Exit Ticket: *"At ___ kPa, the liquid boils at ___ °C."* and *"___ has ___ (strong/weak) forces because its vapor pressure is ___ (low/high)."* Word-choice box displayed on the board throughout: {vapor pressure, boiling point, normal boiling point, intermolecular forces, external pressure, Reference Table H, 101.3 kPa}. Pair each term with a gesture: hands pushing down for external pressure, fingers flying apart for escaping vapor. Provide the curve-reading procedure as a numbered finger-trace card (start at the pressure axis → slide to the curve → drop to the temperature axis).
- **IEP/SPED supports:** Provide a pre-labeled copy of `figures/vapor_pressure_curves.png` with the 101.3 kPa and 70 kPa lines already drawn and the boiling-point dots circled, so the student's task is to *read* the marked crossing points rather than locate them unaided. Offer a partially completed ranking table (propanone and water pre-filled) so the student completes ethanol and ethanoic acid. Pre-highlight the 101.3 kPa row on Reference Table H. Sentence starters for the Exit Ticket.
- **Extensions:** (1) Estimate the boiling point of water on Mount Everest, where the air pressure is only about 34 kPa — read it off the curve and explain why climbers cannot make a proper cup of tea. (2) Ethanoic acid (vinegar's acid) and water both hydrogen-bond, but ethanoic acid has a *higher* normal boiling point than water on Reference Table H — propose a reason in terms of molecular size and total intermolecular attraction. (3) Research why autoclaves (steam sterilizers in hospitals) are pressurized to about 200 kPa and reach 121 °C, and connect it to the pressure-cooker demonstration.

---

## Strategy Spotlight

**ACTIVE LEARNING — predict-then-test with Reference Table H.** Active learning replaces "watch me read the table" with "make a prediction, then check it against the data yourself." For this lesson, students predict the relative volatility and boiling points of the four liquids *before* reading a single number, then test those predictions by tracing the curves. The cognitive commitment of a written prediction makes the subsequent data-reading stick: students are no longer copying a value, they are confirming or revising their own claim.

**How to run it in this lesson (Phase 2 → Phase 3):**

1. **Predict (Phase 2, Part 1):** Each student writes a prediction about which liquid escapes most easily and which boils hottest — from curve shape alone, no numbers. Commit it in writing.
2. **Test (Phase 2, Part 2):** Students trace each curve to the 101.3 kPa line, read the boiling point, and fill the ranking table. They immediately compare the data to their written prediction: confirmed or revised?
3. **Whole-class "stand and rank" (transition into Phase 3):** Call four students to the front, each holding a card for one liquid. The class physically directs them into order — lowest boiling point to highest — and states the IMF consequence aloud. The kinesthetic ordering cements the inverse relationship (high vapor pressure ↔ weak IMF ↔ low boiling point).

Research on active learning in STEM (Freeman et al., 2014; the East Meadow instructional framework) consistently finds that prediction-and-test cycles outperform demonstration-only instruction on conceptual post-tests. The two minutes spent committing a prediction are repaid in retention.

**Connection to Hochman literacy:** the predict-then-test cycle primes the Because/But/So writing in Phase 4, because students have just experienced a *cause* (external pressure / IMF strength), a *contrast* (but the prediction or the sea-level assumption), and a *consequence* (so the boiling point shifts). When they meet the B/B/S frame on paper, they are narrating an investigation they actually ran.

**CRSE connection:** the opening-circle prompt (food, ears popping, travel) and the high-altitude cooking phenomenon draw on experiences common to students whose families travel, cook traditional dishes, or have lived at different elevations. High-altitude cooking adjustments are everyday knowledge in many communities; naming that knowledge as legitimate chemistry honors students' home expertise and makes the abstract vapor-pressure curve feel continuous with their lived experience.

---

## NYSSLS Observation Checklist Crosswalk

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | Phase 1 — high-altitude cooking vs. deep-sea hydrothermal vent; `vapor_pressure_curves.png`; return in Phase 4 with both extremes |
| 2 | Turn and Talk (2–3×) | Phase 1 (TT#1 — which liquid's particles hold on more tightly?); Phase 3 (TT#2 — what does vapor pressure tell you about IMF and boiling point?) |
| 3 | Students develop questions/models/procedures | Phase 2 ABCs prediction-then-test on Reference Table H; Initial Model (explain the mountaintop from the curve); pressure-cooker/vacuum investigation |
| 4 | CCC defined and used | Lesson Overview · *Cause and Effect*, explicit in Phase 3 discussion prompt and Phase 4 B/B/S (pressure → boiling point; IMF → vapor pressure) |
| 5 | ENL — ≤ 3 vocab, second half | Phase 3 — vocabulary introduced at 33–36 min: equilibrium vapor pressure / boiling point (and normal boiling point) / intermolecular forces |
| 6 | Revisit phenomenon with evidence | Phase 4 — students return to the mountaintop and the vent armed with the curve and the demos to explain *why* the boiling point shifts |
| 7 | ENL/SPED supports | Access & Differentiation block: sentence frames, word-choice box, finger-trace card, pre-labeled curve, partially completed ranking table |
| 8 | Assessment check | Phase 5 — Exit Ticket (read propanone's normal boiling point; predict pressure-cooker boiling direction; one Cause-and-Effect IMF sentence) |

---

## Companion Materials

- `Student_Worksheet.docx` — the 5E student investigation (hand out at start of Phase 2)
- `Student_Notes.docx` — guided note-guide for vocabulary and the worked Reference Table H example
- `Answer_Key.docx` — answers to "Make It Make Sense" prompts and the Exit Ticket

---

## Key Vocabulary (max 3)

- **equilibrium vapor pressure** — the steady pressure of a vapor above its liquid in a closed container when the rate of evaporation equals the rate of condensation; it depends only on the substance and the temperature, and it is exactly what each curve on Reference Table H plots
- **boiling point** — the temperature at which a liquid's equilibrium vapor pressure equals the surrounding (external) pressure, so vapor bubbles form throughout the liquid; the *normal boiling point* is this temperature when the external pressure is 101.3 kPa
- **intermolecular forces (IMF)** — the attractions between particles in a liquid; strong IMF (e.g., hydrogen bonding in water) hold particles in the liquid, giving a low vapor pressure and a high boiling point, while weak IMF give a high vapor pressure and a low boiling point
