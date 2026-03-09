#!/usr/bin/env python3
"""Fill lesson gaps in daily configs so every unit matches its target day count."""

import json
import copy
import os

# Gap-filler lesson templates — specific content for each gap
GAP_FILLERS = {
    "chemistry": {
        6: [
            {
                "title": "Calorimetry Lab: Measuring Heat in Chemical Reactions",
                "learning_target": "At the end of 42 minutes I can design and conduct a calorimetry experiment to measure the heat released or absorbed during a chemical reaction.",
                "circle_prompt": "Share a time when you felt a big temperature change — like jumping into a cold pool or holding a hot cup.",
                "do_now": "A student dissolves ammonium nitrate in water and the beaker gets cold. Is this exothermic or endothermic? What is the sign of ΔH?",
                "standards": {
                    "pe": ["HS-PS1-4", "HS-PS3-1"],
                    "sep": ["Planning and Carrying Out Investigations"],
                    "ccc": ["Energy and Matter"],
                    "dci": ["PS3.A: Definitions of Energy", "PS1.B: Chemical Reactions"]
                },
                "materials": ["Calorimeters (nested foam cups)", "Thermometers", "Graduated cylinders", "HCl solution (1M)", "NaOH solution (1M)", "Magnesium ribbon", "Safety goggles", "Lab aprons"],
                "five_e": {
                    "engage": {"time": "5 min", "description": "Demonstrate dissolving ammonium nitrate (cold pack) vs calcium chloride (hot pack) in water. Ask: How can we measure exactly how much heat is exchanged?"},
                    "explore": {"time": "15 min", "description": "Students conduct calorimetry lab: measure temperature change when HCl reacts with NaOH. Record initial/final temps, calculate q=mCΔT."},
                    "explain": {"time": "7 min", "description": "Review calculations as a class. Connect measured heat to enthalpy of neutralization. Discuss sources of error in calorimetry."},
                    "elaborate": {"time": "5 min", "description": "Hochman activity: Because/But/So using 'calorimetry' and 'enthalpy.'"},
                    "evaluate": {"time": "3 min", "description": "Exit ticket: If 50 mL of water increases 12°C in a calorimeter, calculate the heat absorbed."}
                },
                "differentiation": {
                    "approaching": "Provide a step-by-step calculation template with q=mCΔT filled in; students plug in measured values.",
                    "on_level": "Students complete the full calorimetry calculation independently and analyze sources of error.",
                    "advanced": "Calculate percent error compared to accepted enthalpy of neutralization; explain major sources of heat loss.",
                    "ell": "Visual lab procedure cards with labeled diagrams of equipment; bilingual vocabulary sheet for calorimetry terms.",
                    "iep": "Pre-measured solutions provided; calculation steps broken into individual boxes on worksheet; extended time."
                },
                "crse_connection": "Percy Julian — African American chemist whose synthesis of physostigmine required precise temperature control and calorimetric measurements. His work made life-saving medicines affordable.",
                "hochman_activity": "Because/But/So using 'calorimetry': A calorimeter measures heat changes because___. The calculated enthalpy may differ from the accepted value, but___. We assume no heat is lost to the surroundings, so___.",
                "vocabulary": [
                    {"term": "Calorimeter", "definition": "An insulated device used to measure heat changes in chemical or physical processes"},
                    {"term": "Specific heat capacity", "definition": "The amount of heat needed to raise 1 gram of a substance by 1°C (water = 4.18 J/g°C)"}
                ],
                "guided_notes_outline": ["Calorimetry Setup and Procedure", "Calculating Heat with q=mCΔT", "Sources of Error in Calorimetry"],
                "cer": {
                    "topic": "Calorimetry Lab Analysis",
                    "phenomenon": "Two students perform the same neutralization reaction. Student A uses a foam cup calorimeter and measures ΔT = 8.5°C. Student B uses a metal can and measures ΔT = 6.2°C. Both used the same volumes and concentrations.",
                    "claim_starter": "The difference in temperature change between the two calorimeters is due to...",
                    "evidence_source": "Use your lab data and knowledge of heat transfer to compare the two setups.",
                    "reasoning_frame": "This evidence supports my claim because the foam cup... but the metal can..."
                }
            },
            {
                "title": "Energy Diagrams and Catalysts: Practice and Problem Solving",
                "learning_target": "At the end of 42 minutes I can interpret and draw potential energy diagrams for catalyzed and uncatalyzed reactions and calculate activation energy.",
                "circle_prompt": "What's something in your life that would be really hard to do without a shortcut or helper?",
                "do_now": "Sketch a potential energy diagram for an exothermic reaction. Label: reactants, products, activation energy, and ΔH.",
                "standards": {
                    "pe": ["HS-PS1-4", "HS-PS1-5"],
                    "sep": ["Developing and Using Models", "Using Mathematics and Computational Thinking"],
                    "ccc": ["Energy and Matter", "Stability and Change"],
                    "dci": ["PS1.B: Chemical Reactions"]
                },
                "materials": ["Potential energy diagram worksheets", "Colored pencils", "Reference table"],
                "five_e": {
                    "engage": {"time": "5 min", "description": "Show two potential energy diagrams side by side — one with catalyst, one without. Ask: What changed? What stayed the same?"},
                    "explore": {"time": "12 min", "description": "Students complete a set of 6 practice problems: drawing PE diagrams from descriptions, reading values from given diagrams, comparing catalyzed vs uncatalyzed pathways."},
                    "explain": {"time": "8 min", "description": "Review solutions as a class. Emphasize: catalysts lower activation energy but do NOT change ΔH or equilibrium position."},
                    "elaborate": {"time": "7 min", "description": "Application: Given reaction data, students draw complete PE diagrams and calculate activation energy for both forward and reverse reactions."},
                    "evaluate": {"time": "3 min", "description": "Exit ticket: Given a PE diagram, identify Ea forward, Ea reverse, ΔH, and whether a catalyst is present."}
                },
                "differentiation": {
                    "approaching": "Provide partially completed PE diagrams with labeled axes; students add missing labels and values.",
                    "on_level": "Students draw complete diagrams from verbal descriptions and calculate all energy values.",
                    "advanced": "Explain why catalysts speed up both forward and reverse reactions equally using collision theory.",
                    "ell": "Color-coded diagrams — red for activation energy, blue for ΔH; visual glossary of PE diagram components.",
                    "iep": "Enlarged diagram templates; step-by-step checklist for drawing PE diagrams; formula reference card."
                },
                "crse_connection": "Catalytic converters in cars — disproportionate impact of air pollution on communities of color near highways. Environmental justice connection to how catalysts reduce harmful emissions.",
                "hochman_activity": "Appositive sentence: 'A catalyst, ___(definition)___, affects a chemical reaction by ___.'",
                "vocabulary": [
                    {"term": "Catalyst", "definition": "A substance that speeds up a reaction by lowering activation energy without being consumed"},
                    {"term": "Activated complex", "definition": "The temporary, high-energy arrangement of atoms at the peak of a potential energy diagram"}
                ],
                "guided_notes_outline": ["Reading Potential Energy Diagrams", "Catalyzed vs Uncatalyzed Reactions", "Calculating Activation Energy"],
                "cer": None
            }
        ],
        8: [
            {
                "title": "Acid-Base Indicators Lab: Identifying Unknown Solutions",
                "learning_target": "At the end of 42 minutes I can use acid-base indicators to classify unknown solutions as acidic, basic, or neutral.",
                "circle_prompt": "What's your favorite food or drink that tastes sour? What about something that tastes bitter?",
                "do_now": "List three properties of acids and three properties of bases from memory.",
                "standards": {
                    "pe": ["HS-PS1-11"],
                    "sep": ["Planning and Carrying Out Investigations"],
                    "ccc": ["Patterns"],
                    "dci": ["PS1.B: Chemical Reactions"]
                },
                "materials": ["Unknown solutions (labeled A-F)", "pH paper", "Litmus paper (red and blue)", "Phenolphthalein", "Bromthymol blue", "Methyl orange", "Well plates", "Droppers", "Safety goggles"],
                "five_e": {
                    "engage": {"time": "4 min", "description": "Show red cabbage juice changing colors with different household substances. Ask: How do indicators help us identify acids and bases?"},
                    "explore": {"time": "18 min", "description": "Lab: Students test 6 unknown solutions with 4 different indicators. Record color changes in data table. Classify each as acidic, basic, or neutral."},
                    "explain": {"time": "5 min", "description": "Discuss results as a class. Review indicator color ranges. Connect to pH scale."},
                    "elaborate": {"time": "5 min", "description": "Students rank unknowns from most acidic to most basic based on indicator results."},
                    "evaluate": {"time": "3 min", "description": "Exit ticket: Given indicator results, classify a solution and estimate its pH range."}
                },
                "differentiation": {
                    "approaching": "Provide a color reference chart for each indicator; pre-organized data table with column headers.",
                    "on_level": "Students complete lab independently, classify unknowns, and estimate pH ranges.",
                    "advanced": "Predict the chemical identity of each unknown based on indicator patterns and properties.",
                    "ell": "Color-coded indicator reference cards with images; simplified lab directions with numbered steps.",
                    "iep": "Partner work with defined roles; larger well plates for easier handling; pre-printed data table."
                },
                "crse_connection": "Traditional pH indicators in cultures worldwide — turmeric used in South Asian cooking changes color with baking soda; hibiscus tea (Jamaica/agua de jamaica) changes color with acids and bases.",
                "hochman_activity": "Because/But/So using 'indicator': Phenolphthalein turns pink in a solution because___. Litmus paper and pH paper both test for acids, but___. The solution turned bromthymol blue yellow, so___.",
                "vocabulary": [
                    {"term": "Indicator", "definition": "A substance that changes color depending on the pH of a solution"},
                    {"term": "pH range", "definition": "The span of pH values over which an indicator changes color"}
                ],
                "guided_notes_outline": ["Types of Acid-Base Indicators", "Indicator Color Ranges", "Using Multiple Indicators to Narrow pH"],
                "cer": {
                    "topic": "Identifying Unknown Solutions",
                    "phenomenon": "A student tests an unknown solution with three indicators: litmus turns blue, phenolphthalein turns pink, and bromthymol blue turns blue. The student claims the solution is a strong base with pH > 10.",
                    "claim_starter": "Based on the indicator results, the unknown solution is...",
                    "evidence_source": "Use the indicator color change data from your lab and the reference table of indicator ranges.",
                    "reasoning_frame": "The indicator results support this classification because all three indicators show... so the pH must be..."
                }
            },
            {
                "title": "Titration Lab: Determining Acid Concentration",
                "learning_target": "At the end of 42 minutes I can perform an acid-base titration to determine the concentration of an unknown acid.",
                "circle_prompt": "Have you ever had to measure something very precisely? What tools did you use?",
                "do_now": "Write the balanced equation for the neutralization of HCl with NaOH. What is the mole ratio?",
                "standards": {
                    "pe": ["HS-PS1-11"],
                    "sep": ["Planning and Carrying Out Investigations", "Using Mathematics and Computational Thinking"],
                    "ccc": ["Scale, Proportion, and Quantity"],
                    "dci": ["PS1.B: Chemical Reactions"]
                },
                "materials": ["Burets", "Buret clamps and stands", "Erlenmeyer flasks", "NaOH standard solution (0.10 M)", "Unknown HCl solution", "Phenolphthalein indicator", "Wash bottles", "Safety goggles", "Lab aprons"],
                "five_e": {
                    "engage": {"time": "5 min", "description": "Demo: Add NaOH drop by drop to HCl with phenolphthalein. The dramatic color change at the endpoint captures attention. Ask: How can we use this to find concentration?"},
                    "explore": {"time": "18 min", "description": "Students perform titration: add NaOH from buret to unknown HCl in flask with indicator. Record volume at endpoint. Repeat for two trials."},
                    "explain": {"time": "7 min", "description": "Walk through MaVa = MbVb calculation using class data. Discuss what endpoint means vs equivalence point."},
                    "elaborate": {"time": "5 min", "description": "Students calculate the molarity of their unknown using both trial results and find average."},
                    "evaluate": {"time": "3 min", "description": "Exit ticket: Given titration data (volumes and one molarity), calculate the unknown concentration."}
                },
                "differentiation": {
                    "approaching": "Provide a calculation template with MaVa=MbVb set up; students substitute values step by step.",
                    "on_level": "Complete titration and all calculations independently; evaluate precision of two trials.",
                    "advanced": "Calculate percent error compared to actual concentration; explain sources of systematic error in titration.",
                    "ell": "Visual step-by-step titration procedure with photos; bilingual labels on equipment.",
                    "iep": "Partner performs buret reading; student records and calculates; calculation steps chunked with checkboxes."
                },
                "crse_connection": "Water quality testing in communities — titration is used to measure acid levels in drinking water. Connection to Flint, MI water crisis and environmental justice in water testing access.",
                "hochman_activity": "Kernel sentence expansion: Start with 'Titration determines concentration.' Add when, how, and why to create a detailed explanation sentence.",
                "vocabulary": [
                    {"term": "Titration", "definition": "A lab technique that uses a solution of known concentration to determine the concentration of an unknown solution"},
                    {"term": "Endpoint", "definition": "The point in a titration where the indicator changes color, signaling neutralization is complete"},
                    {"term": "Standard solution", "definition": "A solution with a precisely known concentration used in titration"}
                ],
                "guided_notes_outline": ["Titration Setup and Procedure", "Endpoint vs Equivalence Point", "Calculating Concentration with MaVa = MbVb"],
                "cer": None
            },
            {
                "title": "Acid-Base Stoichiometry and Problem Solving",
                "learning_target": "At the end of 42 minutes I can solve acid-base stoichiometry problems including neutralization calculations and buffer concepts.",
                "circle_prompt": "What's one thing about acids and bases that you feel confident about now that you didn't know before this unit?",
                "do_now": "How many moles of NaOH are needed to completely neutralize 0.5 moles of H₂SO₄? Write the balanced equation first.",
                "standards": {
                    "pe": ["HS-PS1-11", "HS-PS1-7"],
                    "sep": ["Using Mathematics and Computational Thinking"],
                    "ccc": ["Scale, Proportion, and Quantity", "Patterns"],
                    "dci": ["PS1.B: Chemical Reactions"]
                },
                "materials": ["Practice problem worksheets", "Calculators", "Reference tables", "Periodic table"],
                "five_e": {
                    "engage": {"time": "5 min", "description": "Present a real-world problem: A lake has become too acidic (pH 4.5) due to acid rain. How many kg of calcium carbonate (limestone) would be needed to neutralize it? Set up the problem framework."},
                    "explore": {"time": "12 min", "description": "Students work in pairs on a set of progressive acid-base stoichiometry problems: simple neutralization → excess reagent → dilution calculations."},
                    "explain": {"time": "8 min", "description": "Review solutions. Emphasize dimensional analysis approach. Introduce the concept of buffers briefly — solutions that resist pH change."},
                    "elaborate": {"time": "7 min", "description": "CER activity: Students analyze titration data to determine the identity of an unknown acid."},
                    "evaluate": {"time": "3 min", "description": "Exit ticket: Multi-step neutralization problem requiring balanced equation, mole ratio, and concentration calculation."}
                },
                "differentiation": {
                    "approaching": "Provide a dimensional analysis template showing conversion factor slots; first problem worked as example.",
                    "on_level": "Complete all practice problems independently; explain reasoning for each step.",
                    "advanced": "Solve the lake neutralization problem with realistic volumes and concentrations; research buffer systems in blood.",
                    "ell": "Word problem translator — key phrases highlighted with their mathematical meaning (e.g., 'completely neutralize' = stoichiometric equivalence).",
                    "iep": "Problems broken into single-step calculations with checkpoints; formula card provided; extended time."
                },
                "crse_connection": "Ocean acidification impacts on island nations and coastal communities of color — coral reef destruction affects food security and cultural practices in Pacific Island and Caribbean communities.",
                "hochman_activity": "Because/But/So using 'neutralization': The lake's pH increased after adding limestone because___. Adding a strong acid to a buffer solution changes the pH slightly, but___. Blood maintains a pH of 7.4 through buffer systems, so___.",
                "vocabulary": [
                    {"term": "Neutralization", "definition": "A reaction between an acid and base that produces water and a salt"},
                    {"term": "Buffer", "definition": "A solution that resists changes in pH when small amounts of acid or base are added"},
                    {"term": "Stoichiometric equivalence", "definition": "The point where moles of acid exactly equal moles of base according to the balanced equation"}
                ],
                "guided_notes_outline": ["Acid-Base Stoichiometry Steps", "Neutralization Calculations", "Introduction to Buffers"],
                "cer": {
                    "topic": "Acid Rain Remediation",
                    "phenomenon": "A factory near a lake emits sulfur dioxide, which forms sulfuric acid in rainwater. The lake's pH has dropped from 6.8 to 4.5 over 10 years. Local officials propose adding 500 kg of crushed limestone (CaCO₃) to restore the pH.",
                    "claim_starter": "Based on stoichiometric calculations, 500 kg of limestone is/is not sufficient to neutralize the acid in the lake because...",
                    "evidence_source": "Use the balanced neutralization equation for CaCO₃ + H₂SO₄ and the provided lake volume data to calculate.",
                    "reasoning_frame": "The stoichiometric calculation shows... because the mole ratio... so the proposed amount..."
                }
            }
        ]
    },
    "physics": {
        2: [
            {
                "title": "Kinematic Equations: Multi-Step Problem Solving",
                "learning_target": "At the end of 42 minutes I can select and apply the appropriate kinematic equation to solve multi-step motion problems.",
                "circle_prompt": "What's the most complicated math problem you've ever solved? How did it feel when you got the answer?",
                "do_now": "A car accelerates from 5 m/s to 25 m/s in 4 seconds. Find the acceleration and the distance traveled.",
                "standards": {
                    "pe": ["HS-PS2-1"],
                    "sep": ["Using Mathematics and Computational Thinking"],
                    "ccc": ["Patterns"],
                    "dci": ["PS2.A: Forces and Motion"]
                },
                "materials": ["Problem sets", "Calculators", "Kinematic equation reference cards", "Whiteboards and markers"],
                "five_e": {
                    "engage": {"time": "5 min", "description": "Challenge problem: A ball is thrown upward at 20 m/s. How high does it go? How long until it returns? Students predict before solving."},
                    "explore": {"time": "12 min", "description": "Whiteboard practice in groups: each group solves a different multi-step problem, then presents their solution strategy to the class."},
                    "explain": {"time": "8 min", "description": "Review common approaches: identifying knowns/unknowns, selecting the right equation, checking units and signs."},
                    "elaborate": {"time": "7 min", "description": "Independent practice on progressively harder problems involving two-object scenarios and combined horizontal/vertical analysis."},
                    "evaluate": {"time": "3 min", "description": "Exit ticket: Two-step kinematic problem requiring equation selection and algebraic manipulation."}
                },
                "differentiation": {
                    "approaching": "Provide a 'Which equation do I use?' flowchart based on known/unknown variables; first problem scaffolded with blanks.",
                    "on_level": "Solve all problems independently using systematic known/unknown identification.",
                    "advanced": "Create their own kinematics problem with a real-world context and solve it; present to partner.",
                    "ell": "Visual equation selector with color-coded variables; word problem key phrases translated.",
                    "iep": "Equation reference card always available; problems chunked into single-step parts; extended time."
                },
                "crse_connection": "Katherine Johnson — NASA mathematician who calculated flight trajectories for John Glenn's orbital mission using kinematics equations. Her work was essential despite racial and gender barriers.",
                "hochman_activity": "Because/But/So using 'acceleration': The ball's velocity decreases as it rises because___. Both a feather and a bowling ball have the same acceleration in a vacuum, but___. The car accelerates at 3 m/s², so after 5 seconds___.",
                "vocabulary": [
                    {"term": "Kinematic equations", "definition": "A set of four equations relating displacement, velocity, acceleration, and time for constant acceleration"},
                    {"term": "Known/Unknown", "definition": "Problem-solving strategy: identify given values (knowns) and what you need to find (unknowns) before selecting an equation"}
                ],
                "guided_notes_outline": ["Selecting the Right Kinematic Equation", "Multi-Step Problem Strategy", "Checking Your Answer"],
                "cer": None
            },
            {
                "title": "Motion Graphs: Position-Time and Velocity-Time Analysis",
                "learning_target": "At the end of 42 minutes I can translate between position-time graphs, velocity-time graphs, and verbal descriptions of motion.",
                "circle_prompt": "If your day today were a graph, what would it look like? Would it be smooth, bumpy, or have sudden changes?",
                "do_now": "Draw a velocity-time graph for this scenario: A car starts at rest, speeds up for 3 seconds, moves at constant speed for 4 seconds, then slows to a stop in 2 seconds.",
                "standards": {
                    "pe": ["HS-PS2-1"],
                    "sep": ["Analyzing and Interpreting Data", "Developing and Using Models"],
                    "ccc": ["Patterns"],
                    "dci": ["PS2.A: Forces and Motion"]
                },
                "materials": ["Graph paper", "Rulers", "Motion graph analysis worksheets", "Colored pencils"],
                "five_e": {
                    "engage": {"time": "5 min", "description": "Show a motion sensor graph of a student walking — forward, stop, backward. Class interprets what happened."},
                    "explore": {"time": "12 min", "description": "Station activity: Station 1 — convert verbal descriptions to d-t graphs. Station 2 — convert d-t to v-t graphs. Station 3 — calculate displacement from v-t graph area."},
                    "explain": {"time": "8 min", "description": "Connect concepts: slope of d-t = velocity, slope of v-t = acceleration, area under v-t = displacement."},
                    "elaborate": {"time": "7 min", "description": "Regents-style practice: match graphs to descriptions, calculate values from graph data."},
                    "evaluate": {"time": "3 min", "description": "Exit ticket: Given a v-t graph, find acceleration for each segment and total displacement."}
                },
                "differentiation": {
                    "approaching": "Provide graph templates with pre-labeled axes and scales; reference card showing slope/area relationships.",
                    "on_level": "Complete all station activities and translate fluently between graph types.",
                    "advanced": "Create acceleration-time graphs from v-t graphs; analyze non-uniform acceleration scenarios.",
                    "ell": "Color-coded graphs — position in blue, velocity in red; visual vocabulary showing what 'slope' and 'area' mean on each graph type.",
                    "iep": "Enlarged graph paper; one station at a time with checkpoint; graph interpretation reference card."
                },
                "crse_connection": "GPS technology and motion tracking — how motion graphs are used in sports analytics, helping athletes from all backgrounds optimize performance through physics-based data analysis.",
                "hochman_activity": "Appositive sentence: 'The slope of a position-time graph, ___(what it represents)___, tells us about an object's motion by ___.'",
                "vocabulary": [
                    {"term": "Slope (of d-t graph)", "definition": "Represents velocity — rise (change in position) over run (change in time)"},
                    {"term": "Area (under v-t graph)", "definition": "Represents displacement — calculated as the geometric area between the line and time axis"}
                ],
                "guided_notes_outline": ["Position-Time Graph Interpretation", "Velocity-Time Graph Interpretation", "Translating Between Graph Types"],
                "cer": {
                    "topic": "Interpreting Motion Graphs",
                    "phenomenon": "Two runners in a 100m race have different velocity-time graphs. Runner A reaches 10 m/s in 2 seconds and maintains that speed. Runner B reaches 12 m/s in 4 seconds and maintains that speed. Who wins?",
                    "claim_starter": "Based on the velocity-time graph analysis, the winner of the 100m race is...",
                    "evidence_source": "Calculate the displacement of each runner using the area under their v-t graph at different time intervals.",
                    "reasoning_frame": "Runner ___ wins because the area under their v-t curve reaches 100m first at t = ___, while Runner ___ reaches 100m at t = ___."
                }
            },
            {
                "title": "Kinematics Problem-Solving Workshop",
                "learning_target": "At the end of 42 minutes I can solve a variety of kinematics problems by integrating graphical analysis, kinematic equations, and free fall concepts.",
                "circle_prompt": "What study strategy has been most helpful for you in this class so far?",
                "do_now": "A stone is dropped from a bridge 45 m above a river. How long does it take to hit the water? What is its final velocity?",
                "standards": {
                    "pe": ["HS-PS2-1"],
                    "sep": ["Using Mathematics and Computational Thinking", "Constructing Explanations"],
                    "ccc": ["Patterns", "Cause and Effect"],
                    "dci": ["PS2.A: Forces and Motion"]
                },
                "materials": ["Mixed problem set worksheets", "Calculators", "Reference tables", "Whiteboards"],
                "five_e": {
                    "engage": {"time": "4 min", "description": "Quick challenge: Can you solve this problem in under 2 minutes? A car brakes from 30 m/s to rest in 50 m. Find the acceleration."},
                    "explore": {"time": "15 min", "description": "Problem-solving workshop: students rotate through problems of increasing difficulty. Each problem requires a different approach (graphs, equations, free fall, projectiles)."},
                    "explain": {"time": "6 min", "description": "Gallery walk — students post solutions and identify common strategies and mistakes."},
                    "elaborate": {"time": "7 min", "description": "CER activity: Analyze a real-world kinematics scenario using multiple approaches."},
                    "evaluate": {"time": "3 min", "description": "Self-assessment: Rate confidence on each kinematics subtopic; identify areas for review."}
                },
                "differentiation": {
                    "approaching": "Problem set starts with guided examples; equation selection hints provided; peer tutoring pairs.",
                    "on_level": "Complete all problems independently; explain strategy selection for each.",
                    "advanced": "Create a 'kinematics challenge' problem for classmates combining multiple concepts; solve a projectile problem at an angle.",
                    "ell": "Problem set with diagrams for each scenario; key physics terms highlighted with definitions in margin.",
                    "iep": "Reduced problem set focusing on core types; formula card and calculator always available; check-in after every 2 problems."
                },
                "crse_connection": "Physics of track and field — Usain Bolt's 100m sprint kinematics analysis. Discuss how athletes from Jamaica and across the African diaspora have dominated sprinting and what the physics reveals about human performance.",
                "hochman_activity": "Because/But/So using 'free fall': All objects in free fall accelerate at 9.81 m/s² because___. A feather and hammer fall at the same rate on the Moon, but___. The stone was dropped from rest, so its initial velocity___.",
                "vocabulary": [
                    {"term": "Problem-solving strategy", "definition": "A systematic approach: identify knowns/unknowns, draw a diagram, select equation, solve, check units"},
                    {"term": "Integration of concepts", "definition": "Using multiple physics ideas together to solve complex real-world problems"}
                ],
                "guided_notes_outline": ["Kinematics Problem Types Review", "Strategy Selection Guide", "Common Mistakes and How to Avoid Them"],
                "cer": {
                    "topic": "Analyzing Sprint Performance",
                    "phenomenon": "A sprinter's velocity data is recorded during a 100m race: 0s→0 m/s, 2s→8 m/s, 4s→11 m/s, 6s→11.5 m/s, 8s→11.5 m/s. The sprinter's coach claims they had constant acceleration throughout the race.",
                    "claim_starter": "The coach's claim that the sprinter had constant acceleration is...",
                    "evidence_source": "Calculate acceleration for each 2-second interval and compare. Create a v-t graph from the data.",
                    "reasoning_frame": "The data shows... because constant acceleration would mean... but the actual pattern shows..."
                }
            },
            {
                "title": "Projectile Motion: Practice and Real-World Applications",
                "learning_target": "At the end of 42 minutes I can solve projectile motion problems involving horizontal launch and connect projectile concepts to real-world scenarios.",
                "circle_prompt": "What's the farthest you've ever thrown something? What did you notice about its path?",
                "do_now": "A ball rolls off a table 1.2 m high with a horizontal velocity of 3 m/s. How far from the base of the table does it land?",
                "standards": {
                    "pe": ["HS-PS2-1"],
                    "sep": ["Using Mathematics and Computational Thinking", "Developing and Using Models"],
                    "ccc": ["Cause and Effect", "Systems and System Models"],
                    "dci": ["PS2.A: Forces and Motion"]
                },
                "materials": ["Projectile motion worksheets", "Calculators", "Projectile launcher (demo)", "Carbon paper", "Meter sticks"],
                "five_e": {
                    "engage": {"time": "5 min", "description": "Demo: Launch a projectile horizontally from different heights. Students predict landing spots before launch. Compare predictions to actual."},
                    "explore": {"time": "12 min", "description": "Problem-solving practice: series of horizontal projectile problems with increasing complexity. Include problems where students must find launch height, horizontal velocity, or time of flight."},
                    "explain": {"time": "8 min", "description": "Review key principle: horizontal and vertical motions are independent. Time in air depends ONLY on vertical distance. Horizontal distance depends on horizontal velocity × time."},
                    "elaborate": {"time": "7 min", "description": "Real-world application: Calculate where a rescue package dropped from a helicopter moving at 40 m/s at 200 m altitude will land."},
                    "evaluate": {"time": "3 min", "description": "Exit ticket: Two-step projectile problem requiring both time calculation and horizontal distance."}
                },
                "differentiation": {
                    "approaching": "Provide a two-column template separating horizontal and vertical calculations; first problem fully worked.",
                    "on_level": "Solve all problems independently; draw trajectory diagrams showing velocity components.",
                    "advanced": "Analyze angled projectile launch — decompose initial velocity into components and calculate range and max height.",
                    "ell": "Visual diagram showing independent horizontal/vertical motions with color coding; bilingual problem set.",
                    "iep": "Problems chunked into vertical-only and horizontal-only parts before combining; reference card with steps."
                },
                "crse_connection": "Physics of basketball — the science behind the perfect free throw arc. Discuss how players from diverse backgrounds use intuitive physics, and how sports science research has improved training.",
                "hochman_activity": "Because/But/So using 'projectile motion': A horizontally launched projectile hits the ground at the same time as a dropped object because___. The horizontal velocity of a projectile stays constant, but___. The ball was launched at 5 m/s horizontally from a 20 m cliff, so___.",
                "vocabulary": [
                    {"term": "Projectile", "definition": "An object moving through the air under the influence of gravity only (no propulsion)"},
                    {"term": "Independence of motion", "definition": "Horizontal and vertical components of projectile motion act independently and can be analyzed separately"}
                ],
                "guided_notes_outline": ["Horizontal Projectile Review", "Solving Multi-Step Projectile Problems", "Real-World Projectile Applications"],
                "cer": None
            },
            {
                "title": "Kinematics Unit Review and Assessment Preparation",
                "learning_target": "At the end of 42 minutes I can demonstrate mastery of kinematics concepts including motion graphs, kinematic equations, free fall, and projectile motion.",
                "circle_prompt": "What topic in this unit are you most proud of understanding? What still feels challenging?",
                "do_now": "Quick review — solve one problem from each category: (a) Find velocity from a d-t graph slope, (b) Use a kinematic equation to find distance, (c) Calculate free fall time.",
                "standards": {
                    "pe": ["HS-PS2-1"],
                    "sep": ["Using Mathematics and Computational Thinking", "Constructing Explanations"],
                    "ccc": ["Patterns", "Cause and Effect"],
                    "dci": ["PS2.A: Forces and Motion"]
                },
                "materials": ["Review packets", "Calculators", "Reference tables", "Index cards for concept maps"],
                "five_e": {
                    "engage": {"time": "5 min", "description": "Kinematics Jeopardy-style review game — quick-fire questions across all topics to identify strengths and gaps."},
                    "explore": {"time": "10 min", "description": "Self-directed review: students choose practice problems from their weakest areas identified in the game."},
                    "explain": {"time": "8 min", "description": "Address top 3 class-wide misconceptions identified during the game. Reteach using different approaches."},
                    "elaborate": {"time": "7 min", "description": "Regents-style cluster practice: students work through a 5-question cluster based on a real-world phenomenon."},
                    "evaluate": {"time": "5 min", "description": "Comprehensive exit ticket covering all kinematics subtopics — serves as self-assessment for study planning."}
                },
                "differentiation": {
                    "approaching": "Targeted review packet focusing on fundamental skills; formula reference card; worked examples for each problem type.",
                    "on_level": "Complete full review packet; create a one-page study guide summarizing key concepts and formulas.",
                    "advanced": "Complete challenge problems combining kinematics with prediction and experimental design.",
                    "ell": "Visual concept map template connecting all kinematics terms; review problems with diagrams for every scenario.",
                    "iep": "Reduced review set covering essential standards; quiet workspace option; extended time on practice."
                },
                "crse_connection": "Review of all CRSE connections from the unit — how kinematics applies across cultures and communities, from sports analytics to transportation equity to space exploration by diverse scientists.",
                "hochman_activity": "Kernel sentence expansion: Start with 'Motion can be described.' Expand by adding specific details about graphs, equations, and real-world examples studied this unit.",
                "vocabulary": [
                    {"term": "Review", "definition": "Comprehensive revisit of all unit concepts to consolidate understanding and prepare for assessment"}
                ],
                "guided_notes_outline": ["Key Concepts Summary", "Formula Review", "Common Problem Types and Strategies"],
                "cer": {
                    "topic": "Comprehensive Kinematics Analysis",
                    "phenomenon": "A stunt driver accelerates a car from rest at 4 m/s² for 5 seconds, then maintains constant speed for 10 seconds, then brakes to a stop in 8 seconds. A traffic engineer claims the total distance traveled is exactly 350 m.",
                    "claim_starter": "The traffic engineer's claim that the total distance is 350 m is...",
                    "evidence_source": "Calculate the distance for each phase of motion using kinematic equations and/or v-t graph area analysis.",
                    "reasoning_frame": "The total distance is ___ because during phase 1... during phase 2... during phase 3... so the engineer's claim is..."
                }
            }
        ],
        8: [
            {
                "title": "Wave Interference Lab: Constructive and Destructive Patterns",
                "learning_target": "At the end of 42 minutes I can observe and explain constructive and destructive interference patterns using wave simulations and ripple tanks.",
                "circle_prompt": "Have you ever been at a concert or event where the sound seemed louder in some spots and quieter in others? What was that like?",
                "do_now": "Draw two identical waves on the same axis. Now draw what happens when they overlap perfectly in phase. What about exactly out of phase?",
                "standards": {
                    "pe": ["HS-PS4-3"],
                    "sep": ["Planning and Carrying Out Investigations", "Developing and Using Models"],
                    "ccc": ["Patterns", "Cause and Effect"],
                    "dci": ["PS4.A: Wave Properties"]
                },
                "materials": ["Ripple tank (or simulation)", "Slinky springs", "Wave interference simulation (PhET)", "Colored pencils", "Rulers"],
                "five_e": {
                    "engage": {"time": "4 min", "description": "Demo with two slinkies: send pulses toward each other. Students observe what happens when they meet — sometimes bigger, sometimes they cancel. Why?"},
                    "explore": {"time": "15 min", "description": "Lab stations: Station 1 — Slinky interference (constructive/destructive). Station 2 — PhET wave simulation showing two-source interference patterns. Station 3 — Ripple tank creating nodal lines."},
                    "explain": {"time": "8 min", "description": "Connect observations to superposition principle. Define constructive (waves in phase, amplitudes add) and destructive (waves out of phase, amplitudes subtract) interference."},
                    "elaborate": {"time": "5 min", "description": "Students predict interference patterns for waves with different amplitudes and frequencies."},
                    "evaluate": {"time": "3 min", "description": "Exit ticket: Given two waves, draw the resultant wave showing interference."}
                },
                "differentiation": {
                    "approaching": "Pre-drawn wave diagrams where students mark constructive/destructive points; step-by-step superposition guide.",
                    "on_level": "Complete all stations; draw and explain interference patterns from observations.",
                    "advanced": "Calculate path length differences that produce constructive vs destructive interference; connect to thin film interference (oil slicks).",
                    "ell": "Visual vocabulary cards showing interference types with diagrams; bilingual station instructions.",
                    "iep": "Focus on two stations with partner support; enlarged wave diagrams; verbal explanation option instead of written."
                },
                "crse_connection": "Noise-canceling headphones — technology that uses destructive interference to protect hearing. Discuss noise pollution in urban communities and how physics-based solutions improve quality of life.",
                "hochman_activity": "Because/But/So using 'interference': Two waves meeting in phase produce a larger wave because___. Constructive and destructive interference both involve superposition, but___. The two speakers are equidistant from the listener, so___.",
                "vocabulary": [
                    {"term": "Constructive interference", "definition": "When two waves combine in phase, their amplitudes add to produce a larger wave"},
                    {"term": "Destructive interference", "definition": "When two waves combine out of phase, their amplitudes subtract, reducing or canceling the wave"},
                    {"term": "Superposition principle", "definition": "When two waves overlap, the resultant displacement is the sum of the individual displacements"}
                ],
                "guided_notes_outline": ["Superposition Principle", "Constructive vs Destructive Interference", "Interference Patterns from Two Sources"],
                "cer": None
            },
            {
                "title": "Sound Waves: Properties, Speed, and Applications",
                "learning_target": "At the end of 42 minutes I can describe how sound waves travel through different media and calculate the speed of sound using wave properties.",
                "circle_prompt": "What's your favorite sound? What is it about that sound that you enjoy?",
                "do_now": "Sound travels at 343 m/s in air and 1480 m/s in water. Why does sound travel faster in water? Think about what you know about molecular spacing.",
                "standards": {
                    "pe": ["HS-PS4-1"],
                    "sep": ["Constructing Explanations", "Using Mathematics and Computational Thinking"],
                    "ccc": ["Cause and Effect", "Structure and Function"],
                    "dci": ["PS4.A: Wave Properties"]
                },
                "materials": ["Tuning forks (various frequencies)", "Rulers", "Resonance tubes", "Calculators"],
                "five_e": {
                    "engage": {"time": "5 min", "description": "Strike a tuning fork and touch it to water — students observe the splash pattern. Touch it to the table — students hear it louder. Ask: What does this tell us about sound?"},
                    "explore": {"time": "12 min", "description": "Investigation: Use resonance tubes and tuning forks to determine the speed of sound in air. Measure the length of the air column at resonance, calculate wavelength, and use v = fλ."},
                    "explain": {"time": "8 min", "description": "Direct instruction: Sound as a longitudinal wave, compressions and rarefactions, factors affecting speed of sound (medium, temperature). Compare values from investigation to accepted value."},
                    "elaborate": {"time": "7 min", "description": "Application problems: calculate speed of sound at different temperatures; determine distance to a lightning strike from the time delay between light and thunder."},
                    "evaluate": {"time": "3 min", "description": "Exit ticket: Given frequency and wavelength, calculate speed of sound; explain why sound cannot travel in a vacuum."}
                },
                "differentiation": {
                    "approaching": "Provide v = fλ calculation template; step-by-step resonance tube procedure with checkpoints.",
                    "on_level": "Complete investigation and all calculations independently; explain why sound speed varies with medium.",
                    "advanced": "Calculate the speed of sound at various temperatures using the formula v = 331 + 0.6T; analyze ultrasound applications.",
                    "ell": "Visual diagram of longitudinal wave with labeled compressions/rarefactions; bilingual vocabulary sheet.",
                    "iep": "Partner for resonance tube measurements; calculation steps pre-structured; formula card provided."
                },
                "crse_connection": "Music across cultures — the physics of instruments from diverse traditions: West African talking drums use variable tension to change pitch, Aboriginal Australian didgeridoos use standing waves, and Caribbean steel drums were invented from recycled oil barrels in Trinidad.",
                "hochman_activity": "Appositive sentence: 'Sound, ___(type of wave)___, travels through air by ___.'",
                "vocabulary": [
                    {"term": "Longitudinal wave", "definition": "A wave where particle motion is parallel to the direction of wave travel (compressions and rarefactions)"},
                    {"term": "Compression", "definition": "A region in a longitudinal wave where particles are pushed close together"},
                    {"term": "Rarefaction", "definition": "A region in a longitudinal wave where particles are spread apart"}
                ],
                "guided_notes_outline": ["Sound as a Longitudinal Wave", "Speed of Sound in Different Media", "Factors Affecting Sound Speed"],
                "cer": {
                    "topic": "Speed of Sound Investigation",
                    "phenomenon": "During a thunderstorm, a student sees lightning and counts 4 seconds before hearing thunder. Their friend in a different location counts 7 seconds. Both claim they can determine how far away the lightning struck.",
                    "claim_starter": "The lightning struck approximately ___ m from the first student and ___ m from the second student because...",
                    "evidence_source": "Use the speed of sound in air (343 m/s) and the time delay between seeing lightning and hearing thunder.",
                    "reasoning_frame": "Since light travels almost instantaneously and sound travels at 343 m/s, the distance can be calculated because..."
                }
            },
            {
                "title": "Resonance and Standing Waves: Investigation",
                "learning_target": "At the end of 42 minutes I can explain how standing waves form and identify nodes, antinodes, and harmonic frequencies.",
                "circle_prompt": "Have you ever made music with something that wasn't an instrument? A water bottle, a desk, a rubber band?",
                "do_now": "When you pluck a guitar string, it vibrates. Draw what you think the string looks like when it vibrates at its fundamental frequency. What about twice that frequency?",
                "standards": {
                    "pe": ["HS-PS4-1", "HS-PS4-3"],
                    "sep": ["Developing and Using Models", "Analyzing and Interpreting Data"],
                    "ccc": ["Patterns", "Structure and Function"],
                    "dci": ["PS4.A: Wave Properties"]
                },
                "materials": ["Standing wave demonstrator or string/vibration generator", "Rulers", "Frequency generator", "Closed and open tubes", "Tuning forks"],
                "five_e": {
                    "engage": {"time": "5 min", "description": "Demo: Generate standing waves on a string. Increase frequency to show 1st, 2nd, 3rd harmonics. Students count nodes and antinodes at each."},
                    "explore": {"time": "12 min", "description": "Investigation: Students use vibration generators to create standing waves. Find the fundamental frequency. Then find 2nd and 3rd harmonics. Measure wavelengths and record the pattern."},
                    "explain": {"time": "8 min", "description": "Define standing waves, nodes, antinodes. Explain the mathematical relationship between harmonics (fn = nf1). Connect string length to wavelength for open and closed pipes."},
                    "elaborate": {"time": "7 min", "description": "Application: Calculate fundamental frequency and harmonics for a guitar string of known length and wave speed. Compare to open vs closed pipes."},
                    "evaluate": {"time": "3 min", "description": "Exit ticket: Draw the 3rd harmonic standing wave pattern; label nodes and antinodes; calculate its frequency."}
                },
                "differentiation": {
                    "approaching": "Provide standing wave diagrams with nodes/antinodes pre-labeled for 1st and 2nd harmonics; students complete 3rd and 4th.",
                    "on_level": "Complete investigation, draw all harmonic patterns, and calculate frequencies independently.",
                    "advanced": "Research and explain why different instruments playing the same note sound different (overtone series and timbre).",
                    "ell": "Visual diagrams showing each harmonic with bilingual labels; pattern chart showing node/antinode counts.",
                    "iep": "Hands-on focus with standing wave demonstrator; reduced calculations; visual pattern recognition emphasized."
                },
                "crse_connection": "The physics of the steel drum (steelpan) — invented in Trinidad and Tobago by communities of African descent. Each section of the pan is tuned to resonate at a specific frequency, creating standing waves that produce distinct musical notes.",
                "hochman_activity": "Because/But/So using 'resonance': A wine glass shatters when a singer hits the right note because___. A node and an antinode are both parts of a standing wave, but___. The string is fixed at both ends, so only certain wavelengths can form standing waves___.",
                "vocabulary": [
                    {"term": "Standing wave", "definition": "A wave pattern that appears stationary, formed by the interference of two identical waves traveling in opposite directions"},
                    {"term": "Node", "definition": "A point on a standing wave that remains stationary (zero displacement)"},
                    {"term": "Antinode", "definition": "A point on a standing wave with maximum displacement"},
                    {"term": "Harmonic", "definition": "A multiple of the fundamental frequency; the nth harmonic has n times the fundamental frequency"}
                ],
                "guided_notes_outline": ["How Standing Waves Form", "Nodes, Antinodes, and Harmonics", "Standing Waves in Strings and Pipes"],
                "cer": None
            },
            {
                "title": "Doppler Effect and Wave Applications",
                "learning_target": "At the end of 42 minutes I can explain the Doppler effect and describe how wave properties are applied in technology and nature.",
                "circle_prompt": "Have you noticed how a siren sounds different as an ambulance approaches and then drives away? Describe what you heard.",
                "do_now": "A car horn has a frequency of 500 Hz. As the car drives toward you, do you hear a higher or lower frequency? As it drives away? Explain why.",
                "standards": {
                    "pe": ["HS-PS4-1", "HS-PS4-3"],
                    "sep": ["Constructing Explanations", "Obtaining, Evaluating, and Communicating Information"],
                    "ccc": ["Cause and Effect", "Patterns"],
                    "dci": ["PS4.A: Wave Properties", "PS4.C: Information Technologies"]
                },
                "materials": ["Doppler effect demo (buzzer on a string)", "Simulation (PhET or similar)", "Wave applications reference materials"],
                "five_e": {
                    "engage": {"time": "5 min", "description": "Demo: Swing a buzzer on a string in a circle. Students note the pitch change. Connect to their experiences with sirens, cars, and trains."},
                    "explore": {"time": "10 min", "description": "Simulation: Students manipulate source and observer velocities in a Doppler effect simulation. Record observations about frequency shift direction and magnitude."},
                    "explain": {"time": "10 min", "description": "Explain Doppler effect mechanism: wavefronts compress ahead of moving source, spread behind. Introduce applications: radar, ultrasound, astronomical redshift."},
                    "elaborate": {"time": "7 min", "description": "CER activity: Students analyze redshift data to determine whether galaxies are moving toward or away from Earth."},
                    "evaluate": {"time": "3 min", "description": "Exit ticket: Explain why an ambulance siren sounds higher-pitched approaching and lower-pitched receding."}
                },
                "differentiation": {
                    "approaching": "Visual diagrams showing compressed/spread wavefronts with before/after frequency comparison; guided simulation worksheet.",
                    "on_level": "Complete simulation exploration and explain Doppler effect mechanism in writing.",
                    "advanced": "Use the Doppler equation to calculate observed frequency for given source velocity; explain sonic booms and Mach numbers.",
                    "ell": "Visual Doppler effect diagram with bilingual labels; video clips of real Doppler examples with captions.",
                    "iep": "Focus on qualitative understanding (higher/lower pitch for approaching/receding); simplified simulation with guided questions."
                },
                "crse_connection": "Doppler ultrasound in medicine — used worldwide to monitor fetal heartbeat and blood flow. Discuss access to prenatal care in underserved communities and how physics-based medical technology can improve health equity.",
                "hochman_activity": "Because/But/So using 'Doppler effect': Distant galaxies appear red-shifted because___. Both sound and light exhibit the Doppler effect, but___. The ambulance is moving toward you, so the siren sounds___.",
                "vocabulary": [
                    {"term": "Doppler effect", "definition": "The change in observed frequency of a wave when the source or observer is moving relative to the other"},
                    {"term": "Redshift", "definition": "An increase in wavelength (decrease in frequency) of light from objects moving away from the observer"},
                    {"term": "Blueshift", "definition": "A decrease in wavelength (increase in frequency) of light from objects moving toward the observer"}
                ],
                "guided_notes_outline": ["The Doppler Effect Mechanism", "Doppler Effect with Sound and Light", "Applications: Radar, Ultrasound, and Astronomy"],
                "cer": {
                    "topic": "Astronomical Redshift",
                    "phenomenon": "Astronomers observe that the hydrogen spectral lines from Galaxy A are shifted 2 nm toward the red end of the spectrum, while Galaxy B's lines are shifted 8 nm toward red. Both galaxies are in different directions from Earth.",
                    "claim_starter": "Based on the redshift data, Galaxy B is moving ___ compared to Galaxy A because...",
                    "evidence_source": "Compare the magnitude of the redshift for each galaxy and apply the relationship between redshift and recessional velocity.",
                    "reasoning_frame": "A larger redshift indicates... because the Doppler effect causes... so Galaxy B must be..."
                }
            }
        ],
        9: [
            {
                "title": "Total Internal Reflection and Fiber Optics",
                "learning_target": "At the end of 42 minutes I can explain total internal reflection and describe how it enables fiber optic technology.",
                "circle_prompt": "How does your internet get to your home? Has anyone seen a fiber optic cable?",
                "do_now": "When light passes from water to air, it bends away from the normal. What happens if the angle of incidence keeps increasing? At what point does the light stop leaving the water?",
                "standards": {
                    "pe": ["HS-PS4-5"],
                    "sep": ["Constructing Explanations", "Obtaining, Evaluating, and Communicating Information"],
                    "ccc": ["Cause and Effect", "Structure and Function"],
                    "dci": ["PS4.B: Electromagnetic Radiation", "PS4.C: Information Technologies"]
                },
                "materials": ["Laser pointer", "Semicircular glass or acrylic block", "Fiber optic cable demo", "Protractors", "Water tank"],
                "five_e": {
                    "engage": {"time": "5 min", "description": "Demo: Shine a laser into a semicircular glass block. Gradually increase the angle of incidence until the light no longer exits — it reflects back inside. Students observe the critical angle."},
                    "explore": {"time": "12 min", "description": "Investigation: Students find the critical angle for glass-to-air by gradually increasing incidence angle. Then observe light traveling through a curved stream of water (light pipe demo)."},
                    "explain": {"time": "8 min", "description": "Define total internal reflection and critical angle. Explain conditions: light must travel from more dense to less dense medium, angle must exceed critical angle. Connect to fiber optics."},
                    "elaborate": {"time": "7 min", "description": "Application: Students research and discuss how fiber optics transmit internet data. Calculate critical angles using Snell's law for different material pairs."},
                    "evaluate": {"time": "3 min", "description": "Exit ticket: Explain why diamonds sparkle using total internal reflection; calculate the critical angle for diamond (n=2.42)."}
                },
                "differentiation": {
                    "approaching": "Provide step-by-step critical angle calculation using Snell's law with sin(θc) = n2/n1; visual diagram of TIR conditions.",
                    "on_level": "Complete investigation, calculate critical angles, and explain fiber optic applications.",
                    "advanced": "Research and present on medical applications of fiber optics (endoscopy); calculate how many reflections light makes in a 1 km fiber.",
                    "ell": "Visual diagram showing refraction → critical angle → total internal reflection progression with bilingual labels.",
                    "iep": "Focus on qualitative understanding of TIR; hands-on fiber optic cable demo; simplified calculation with support."
                },
                "crse_connection": "Shirley Ann Jackson — first African American woman to earn a PhD from MIT. Her telecommunications research contributed to the development of fiber optics, touch-tone phones, and solar cells.",
                "hochman_activity": "Because/But/So using 'total internal reflection': Light reflects back into the glass instead of refracting because___. Both reflection and refraction involve light hitting a boundary, but___. Fiber optic cables are made of glass with a higher index of refraction than the cladding, so___.",
                "vocabulary": [
                    {"term": "Total internal reflection", "definition": "The complete reflection of light at a boundary when the angle of incidence exceeds the critical angle"},
                    {"term": "Critical angle", "definition": "The minimum angle of incidence at which total internal reflection occurs"},
                    {"term": "Fiber optics", "definition": "Thin glass or plastic fibers that transmit light signals using total internal reflection"}
                ],
                "guided_notes_outline": ["Conditions for Total Internal Reflection", "Critical Angle Calculation", "Fiber Optic Technology"],
                "cer": {
                    "topic": "Fiber Optic Data Transmission",
                    "phenomenon": "A telecommunications company offers two internet options: copper cable at $50/month (100 Mbps) and fiber optic at $70/month (1000 Mbps). A customer asks why fiber optic is faster and whether it's worth the extra cost.",
                    "claim_starter": "Fiber optic internet is faster than copper cable because...",
                    "evidence_source": "Compare how electrical signals travel through copper vs light signals through glass fiber, considering total internal reflection and signal loss.",
                    "reasoning_frame": "Light in fiber optic cables travels via total internal reflection, which means... because... so the data rate is higher because..."
                }
            },
            {
                "title": "Color, Filters, and the Interaction of Light with Matter",
                "learning_target": "At the end of 42 minutes I can explain how objects get their color through absorption, reflection, and transmission of light.",
                "circle_prompt": "What's your favorite color? Have you ever wondered why that object appears that color?",
                "do_now": "A white T-shirt appears white in sunlight. What color would it appear under only red light? What about a blue T-shirt under red light?",
                "standards": {
                    "pe": ["HS-PS4-4", "HS-PS4-5"],
                    "sep": ["Constructing Explanations", "Developing and Using Models"],
                    "ccc": ["Cause and Effect", "Energy and Matter"],
                    "dci": ["PS4.B: Electromagnetic Radiation"]
                },
                "materials": ["Color filters (red, green, blue)", "Flashlights", "White paper and colored paper", "Prism", "Colored pencils"],
                "five_e": {
                    "engage": {"time": "5 min", "description": "Demo: Shine white light through a prism to show the visible spectrum. Then use color filters to isolate colors. Place colored objects under filtered light — students observe color changes."},
                    "explore": {"time": "12 min", "description": "Investigation: Students view different colored objects through different color filters. Record what color each object appears. Build a model explaining why objects appear different colors under different lighting."},
                    "explain": {"time": "8 min", "description": "Explain selective absorption and reflection. White objects reflect all colors. Black absorbs all. A red object reflects red and absorbs other colors. Under blue light, a red object appears black (no red to reflect)."},
                    "elaborate": {"time": "7 min", "description": "Application: Stage lighting design — students plan colored lighting for a school performance, predicting how costumes will appear under different lights."},
                    "evaluate": {"time": "3 min", "description": "Exit ticket: Explain why a yellow banana appears black under blue light."}
                },
                "differentiation": {
                    "approaching": "Color absorption/reflection chart provided; guided data table for filter observations; visual model template.",
                    "on_level": "Complete investigation, build explanatory model, and predict color appearances independently.",
                    "advanced": "Explain additive vs subtractive color mixing; design a color filter combination to produce specific colors.",
                    "ell": "Color-labeled diagrams showing absorption/reflection; visual explanation cards; hands-on exploration prioritized.",
                    "iep": "Focus on hands-on filter exploration with partner; simplified recording sheet; verbal explanation accepted."
                },
                "crse_connection": "The physics of melanin — how the same principles of light absorption that make objects appear colored also determine skin color. Discuss the science behind melanin as a natural sunscreen and its evolutionary significance across human populations.",
                "hochman_activity": "Because/But/So using 'absorption': A red apple appears red in white light because___. A red apple and a green leaf both interact with light, but___. Under blue light, no red wavelengths are present, so the apple appears___.",
                "vocabulary": [
                    {"term": "Selective absorption", "definition": "The process by which a material absorbs certain wavelengths of light and reflects or transmits others"},
                    {"term": "Additive color", "definition": "Combining colored lights — red + green + blue = white"},
                    {"term": "Filter", "definition": "A material that selectively transmits certain wavelengths of light while absorbing others"}
                ],
                "guided_notes_outline": ["How Objects Get Their Color", "Filters and Selective Transmission", "Predicting Color Under Different Lights"],
                "cer": None
            },
            {
                "title": "Optics Unit Review and Problem Solving",
                "learning_target": "At the end of 42 minutes I can solve mirror, lens, and wave optics problems and connect optics concepts to real-world applications.",
                "circle_prompt": "What's one way that light and optics affect your daily life that you didn't think about before this unit?",
                "do_now": "Quick three-part review: (a) State the law of reflection. (b) If n1 sin θ1 = n2 sin θ2 and light enters glass (n=1.5) at 30°, find the refracted angle. (c) Is the image in a convex mirror real or virtual?",
                "standards": {
                    "pe": ["HS-PS4-4", "HS-PS4-5", "HS-PS4-6"],
                    "sep": ["Using Mathematics and Computational Thinking", "Constructing Explanations"],
                    "ccc": ["Patterns", "Cause and Effect", "Structure and Function"],
                    "dci": ["PS4.B: Electromagnetic Radiation"]
                },
                "materials": ["Review problem sets", "Calculators", "Ray diagram templates", "Reference tables"],
                "five_e": {
                    "engage": {"time": "5 min", "description": "Optics challenge round: rapid-fire questions covering reflection, refraction, mirrors, lenses, and EM spectrum. Identify class strengths and gaps."},
                    "explore": {"time": "12 min", "description": "Problem-solving stations: Station 1 — Mirror problems (ray diagrams + calculations). Station 2 — Lens problems. Station 3 — Snell's law and TIR. Station 4 — EM spectrum and photon energy."},
                    "explain": {"time": "8 min", "description": "Address top misconceptions. Review key relationships: mirror/lens equation, Snell's law, E=hf, critical angle formula."},
                    "elaborate": {"time": "7 min", "description": "Regents-style cluster practice: automotive optics scenario (mirrors, lenses, headlights) — similar to the sample cluster from the educator guide."},
                    "evaluate": {"time": "3 min", "description": "Comprehensive self-assessment covering all optics subtopics; students create a study plan for areas of weakness."}
                },
                "differentiation": {
                    "approaching": "Formula reference card for all optics equations; one station at a time with worked example at each.",
                    "on_level": "Complete all stations; solve cluster problems independently.",
                    "advanced": "Create a comprehensive optics concept map linking all topics; solve advanced combination problems.",
                    "ell": "Visual summary sheet with all ray diagrams and formulas labeled bilingually; diagram-heavy problem set.",
                    "iep": "Choose 2 of 4 stations; extended time; formula card and calculator provided; check-in after each station."
                },
                "crse_connection": "Review of optics CRSE connections — from Shirley Ann Jackson's fiber optics research to the physics of melanin, how understanding light has improved medicine, communication, and daily life across all communities.",
                "hochman_activity": "Kernel sentence expansion: 'Light behaves predictably.' Expand by adding details about reflection, refraction, and applications studied in this unit.",
                "vocabulary": [
                    {"term": "Review", "definition": "Consolidation of all optics concepts in preparation for assessment"}
                ],
                "guided_notes_outline": ["Key Optics Formulas and Relationships", "Ray Diagram Review", "Problem-Solving Strategies"],
                "cer": {
                    "topic": "Designing an Optical System",
                    "phenomenon": "An optician needs to design glasses for a patient who is nearsighted (can see close objects but not distant ones). The optician must choose between converging and diverging lenses and determine the correct focal length.",
                    "claim_starter": "To correct nearsightedness, the optician should use a ___ lens with a focal length of approximately ___ because...",
                    "evidence_source": "Use ray diagrams and the thin lens equation to show how the chosen lens redirects light to focus on the retina.",
                    "reasoning_frame": "Nearsightedness occurs because light focuses... A ___ lens corrects this because it... so the image shifts to..."
                }
            }
        ]
    }
}


def add_gap_fillers(config, course_name):
    """Add gap-filling lessons to units that are short."""
    fillers = GAP_FILLERS.get(course_name, {})

    for unit in config["units"]:
        unit_num = unit["number"]
        current_lessons = len(unit.get("lessons", []))
        target_days = unit["days"]

        if current_lessons < target_days and unit_num in fillers:
            filler_lessons = fillers[unit_num]
            needed = target_days - current_lessons

            for i, filler in enumerate(filler_lessons[:needed]):
                filler_copy = copy.deepcopy(filler)
                filler_copy["days"] = 1
                unit["lessons"].append(filler_copy)

            # Renumber all lessons
            for i, lesson in enumerate(unit["lessons"]):
                lesson["number"] = i + 1


def adjust_physics_totals(config):
    """Adjust physics unit days to total 175."""
    total = sum(len(u["lessons"]) for u in config["units"])
    diff = total - 175

    if diff > 0:
        # Need to remove lessons — trim from Unit 3 (over by 2) first
        for unit in config["units"]:
            if diff <= 0:
                break
            if unit["number"] == 3 and len(unit["lessons"]) > 23:
                # Remove last lesson(s) that are review/practice days
                while len(unit["lessons"]) > 23 and diff > 0:
                    unit["lessons"].pop()
                    diff -= 1
                unit["days"] = len(unit["lessons"])
                # Renumber
                for i, l in enumerate(unit["lessons"]):
                    l["number"] = i + 1


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_dir = os.path.join(base_dir, "generator", "configs")

    for course in ["chemistry", "physics"]:
        input_path = os.path.join(config_dir, f"{course}_daily.json")
        output_path = os.path.join(config_dir, f"{course}_daily.json")  # overwrite

        with open(input_path) as f:
            config = json.load(f)

        print(f"\n=== {course.upper()} ===")
        print(f"Before gap fill: {sum(len(u['lessons']) for u in config['units'])} lessons")

        add_gap_fillers(config, course)

        if course == "physics":
            adjust_physics_totals(config)

        total = sum(len(u["lessons"]) for u in config["units"])
        print(f"After gap fill: {total} lessons")

        for u in config["units"]:
            n = len(u["lessons"])
            print(f"  Unit {u['number']}: {n} lessons")

        with open(output_path, "w") as f:
            json.dump(config, f, indent=2)

        print(f"Written to: {output_path}")


if __name__ == "__main__":
    main()
