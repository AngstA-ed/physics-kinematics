# Physics Curriculum Refactor — East Meadow × Valley Stream Design Spec

**Date:** 2026-05-08
**Author:** Curriculum lead (Adam Stanco) with Claude
**Status:** Approved for planning
**Pilot scope:** Unit: Kinematics (9 lessons)
**Source documents:**
- `Physics/NEW East Meadow Physics Scope and Sequence.md`
- `Physics/1. East Meadow Valley Stream Physics 5_7_26.pptx` (NYSSLS Lesson Observation Checklist, slide 5; Phenomenon-Based Lesson Flow, slide 32)

---

## 1. Goals and Non-Goals

### Goals

1. Refactor the Physics curriculum to mirror the **NEW East Meadow Scope and Sequence** verbatim — same units, same topic order, same topic names.
2. Preserve every teacher-curated resource (NYSSLS standards, phenomena, PhET/Javalab/Physics Classroom labs, assessments) so teachers see their work reflected in the published materials.
3. Integrate the "unreasonable effectiveness of HTML" approach from Thariq Shihipar (https://thariqs.github.io/html-effectiveness/) for student-facing exploration: rich, self-contained, interactive HTML pages with SVG, sliders, live diagrams.
4. Co-brand all artifacts for **East Meadow Schools × Valley Stream Central High School District**.
5. Embed VSCHSD pedagogical requirements (Hochman literacy strategies, active learning, differentiation/ELL, SEL, restorative opening circles, Building Thinking Classrooms) at the frequencies specified by the district.
6. Honor the NYSSLS Lesson Observation Checklist (slide 5) and the Phenomenon-Based Lesson Flow (slide 32) as the lesson backbone.
7. Produce both a **rich interactive** and a **OneNote-native static** flavor of every student artifact, so the curriculum can be hosted in SharePoint document libraries (or GitHub Pages fallback) **and** pasted into OneNote Class Notebook pages.
8. Pilot one unit (Kinematics) end-to-end before scaling to the other nine units.

### Non-Goals (explicit YAGNI)

- A static-site generator wrapper around the lessons (out of scope; "Approach B" deferred).
- Refactoring Chemistry / Earth and Space Science.
- Building Units 0, 2–9 of Physics.
- Auto-generating images via AI.
- LMS-specific exports (Schoology, Canvas).
- Translation / multilingual versions.
- Teacher dashboards or analytics.
- Auto-grading.
- Microsoft Graph API automation for OneNote Class Notebook page creation (manual paste workflow for pilot).
- Playwright snapshot tests (manual QA checklist for pilot).

---

## 2. Folder Layout

```
Publisher_Ready_Curriculum/
  _archive/
    01_Physics_East_Meadow_Refactor_2026-05-08/   # old partial work, moved here intact
  01_Physics_East_Meadow_Refactor/
    README.md                                      # unit index, scope/sequence summary, link map
    Scope_and_Sequence.md                          # copy of source MD, reviewable in git
    _assets/
      brand/
        em_logo.svg                                # placeholder until provided
        em_logo.png
        vs_logo.svg                                # placeholder until provided
        vs_logo.png
        brand.css                                  # CSS custom properties for brand tokens
        reference.docx                             # Pandoc reference doc with co-branded styles
      lesson.css                                   # shared typography, layout primitives
      lesson.js                                    # shared interactive helpers
      icons.svg                                    # shared icon sprite
    00_Math_in_Science/                            # stub
    01_Kinematics/                                 # PILOT UNIT
      Unit_Plan.md                                 # source for Unit_Plan.docx
      Unit_Plan.docx                               # built artifact
      Unit_Plan.onenote.html                       # OneNote-paste version
      Assessments/
        Kinematics_Regents_Style_Set.md
        Kinematics_Regents_Style_Set.docx
        Kinematics_Regents_Style_Set.onenote.html
      Visuals/
        Visual_Prompts.md
      01_Vectors/
        Student_Exploration.html                   # rich interactive
        Student_Exploration.onenote.html           # OneNote-paste static
        Teacher_Guide.md
        Teacher_Guide.docx
        Teacher_Guide.onenote.html
        Answer_Key.md
        Answer_Key.docx
        Answer_Key.onenote.html
      02_Distance_and_Displacement/
      03_Average_Speed_and_Velocity/
      04_Acceleration/
      05_Motion_Graphs/
      06_Freefall/
      07_Vertical_Projectiles/
      08_Horizontal_Projectile_Motion/
      09_Projectiles_at_an_Angle/
    02_Forces/                                     # stub
    03_Momentum_Impulse/                           # stub
    04_Energy/                                     # stub
    05_Thermodynamics/                             # stub
    06_Electrostatics/                             # stub
    07_Current_Electricity/                        # stub
    08_Waves/                                      # stub
    09_Modern_Physics/                             # stub
  tools/
    build_lessons.py                               # walks tree, runs Pandoc + static-ifier
    scaffold_lesson.py                             # creates new lesson folder from template
    publish_pages.py                               # copies interactives to gh-pages branch (fallback)
    lesson_schema.yaml                             # required sections + validation rules
    lesson_qa_checklist.md                         # manual QA steps for pilot
```

### Naming rules

- Folder slugs use numeric prefixes (`01_`, `02_`, …) for filesystem sort order.
- Folder slug body uses safe ASCII (e.g., `07_Vertical_Projectiles`).
- Document titles inside artifacts use the **verbatim MD topic name** (e.g., "Thrown Upwards / Vertical Projectiles") in the lesson cover block.
- Stub units contain only a `README.md` placeholder so the structure is visible but no content is committed yet.

---

## 3. Teacher Work Preservation

This section operationalizes the requirement that "teachers see the work they put in reflected."

### 3.1 The MD row is the source of truth

Each topic row in the East Meadow MD has five columns: Topic, NYSSLS, Phenomenon, Javalab/labs, Assessments. Every link, phenomenon description, and standard reference is preserved verbatim — not paraphrased.

### 3.2 Curated Resources block (every Teacher_Guide)

Every `Teacher_Guide.md` includes a fixed top section titled **"Curated Resources (from East Meadow Scope & Sequence)"** with four sub-headers matching the MD columns:

- **NYSSLS Standards** — pasted in full, including bold performance expectation and parenthesized crosscutting concept
- **Phenomenon** — teachers' chosen phenomenon, with the original link/video reference
- **Javalab / Labs** — every lab link from the MD row, in MD order
- **Assessments** — every assessment link from the MD row

Below this block, our authored content begins. The two are visibly separated with a tinted box so teachers can tell at a glance which content is theirs and which is the publisher's.

### 3.3 Student HTML "Explore Further" sidebar

Each `Student_Exploration.html` includes an "Explore Further" sidebar/footer with the teacher-curated PhET / Javalab / Physics Classroom resources from the MD row, in MD order. Our custom interactive sits at the top as the focused experience; the curated links are the natural follow-ups.

### 3.4 Unit Plan reproduces the MD table

`Unit_Plan.docx` opens with a one-page table that reproduces the MD's unit-level table verbatim (Topic / NYSSLS / Phenomenon / Lab / Assessment).

### 3.5 Source MD lives in git

A copy of the source MD is committed at `01_Physics_East_Meadow_Refactor/Scope_and_Sequence.md` so the curriculum is self-contained and reviewable.

---

## 4. Co-Branding (VSCHSD × East Meadow)

### 4.1 Brand tokens

Tokens are exposed as CSS custom properties in `_assets/brand/brand.css` and mirrored in the Pandoc reference DOCX styles.

| Token | Value | Source |
|---|---|---|
| `--em-purple` | `#662e80` | East Meadow primary (emufsd.us, public CSS inspection) |
| `--em-orange` | `#f37366` | East Meadow accent |
| `--vs-blue` | `#2ea3f2` | Valley Stream Central primary (vschsd.org, public CSS inspection) |
| `--ink` | `#1a1a1a` | Body text |
| `--paper` | `#ffffff` | Background |
| `--rule` | `#e6e6e6` | Borders / dividers |
| Body font | `Inter, "Open Sans", system-ui, sans-serif` | Intersection of both districts |
| Display font | `Inter`, weight 700 | Both districts use sans-serif display |

### 4.2 Visual lockup

Every artifact (HTML, DOCX, OneNote-paste HTML) opens with:

- **Top header:** Two logo slots side by side, separated by a thin vertical rule. Above the rule, small caps: "East Meadow Schools × Valley Stream Central High School District". Below, the unit and lesson name.
- **Color usage:** East Meadow purple for primary headings; VSCHSD blue for secondary accents (callouts, links, interactive controls); orange reserved for warnings/safety notes.
- **Tagline strip in footer:** "Learning, Achieving, Succeeding!" (VSCHSD's public tagline). East Meadow tagline TBD pending confirmation; placeholder shows district name only.

### 4.3 Asset placeholders

Logo SVGs/PNGs are placeholders. The lockup positions are fixed; only the file contents change when official assets are provided. All color/font choices come from public CSS inspection of the two district sites and may differ from official brand guidelines. If either district provides an internal brand book, those values supersede these and are updated in `brand.css` in one place.

---

## 5. Lesson Template

### 5.1 Lesson backbone (every lesson)

Every lesson — both Interactive and OneNote-native flavors — flows in this order, mirroring slide 32 of the source PPTX:

1. **Phenomenon** (local/relatable, drawn from MD)
2. **Notice & Wonder** + **Turn and Talk #1**
3. **Question prioritization** through a Crosscutting Concept (CCC) lens
4. **Initial model / explanation**
5. **Investigation** — interactive Explore (or static storyboard) plus curated PhET/Javalab links from MD
6. **Sense-making** + **Turn and Talk #2**
7. **Class consensus** + **Revise the model**
8. **Vocabulary** — limit to 3 key terms, introduced in the second half of the lesson (per slide 5, item 5)
9. **Transfer task assessment** — new phenomenon, students apply learning
10. **Exit ticket**

### 5.2 NYSSLS Observation Checklist crosswalk (every lesson)

Every Teacher_Guide includes a section that maps each of the eight checklist items (slide 5 of source PPTX) to the lesson section that satisfies it:

| # | Checklist item | How it shows up |
|---|---|---|
| 1 | Local/relatable phenomenon | "Local Hook" sub-section invites teacher to substitute Long Island / East Meadow / Valley Stream example |
| 2 | Turn and Talk (2–3×) | At least two scripted prompts in the agenda, plus a silence-breaker backup |
| 3 | Students develop questions/models/procedures | Initial-model and class-consensus blocks built into the student page |
| 4 | CCC defined and used | "CCC focus" field in cover block with one-line teacher-friendly definition |
| 5 | ENL — ≤3 vocab, second half of lesson | "Key Vocabulary (max 3)" box positioned after the investigation |
| 6 | Revisit phenomenon with evidence | "Return to the phenomenon" section before exit ticket |
| 7 | ENL/SPED supports | Sentence frames, word-choice boxes, graphic organizers (see 5.4) |
| 8 | Assessment check | Exit ticket + transfer task |

### 5.3 SEL — every lesson

- **Opening Connection** in Teacher Guide: teacher picks one of three options — a 1-question check-in, a "name something you noticed since last class" share, or a quick gratitude/effort acknowledgment.
- **Closing Reflection** added to the exit-ticket block: one prompt about *thinking* (e.g., "what's one thing that surprised you?") and one about *self/community* (e.g., "who helped you make sense of something today?").

### 5.4 Differentiation + ELL — every lesson

Fixed **"Access & Differentiation"** block in every Teacher_Guide:
- **ELL/ENL supports:** sentence frames, word-choice boxes, bilingual glossary slot, visuals-first framing
- **IEP/SPED supports:** chunked tasks, graphic organizer for model-building, scaffolded prompts
- **Extensions:** for students ready for the next layer

The Student Exploration page always includes:
- Sentence frames in "Make it Make Sense" prompts (visible by default, dismissable for advanced students)
- Printable graphic organizer for the model-building step
- Word-choice boxes for short responses

### 5.5 Rotating strategies — not every lesson

Tagged at unit level so the rotation is visible in `Unit_Plan.docx`:

| Strategy | Frequency | How tagged |
|---|---|---|
| Hochman writing strategy | 1–2× per week (~3 lessons across Kinematics' 9) | `[HOCHMAN]` chip on lesson cover; specific Hochman move named in agenda (single-sentence, sentence expansion, because/but/so, paragraph topic sentence) |
| Active learning structure | 1–2× per week (~3 lessons) | `[ACTIVE LEARNING]` chip; structure named (gallery walk, jigsaw, stations, 4 corners) |
| Building Thinking Classrooms | Occasional (~2 lessons in Kinematics) | `[BTC]` chip; specific BTC practice named (random groups, vertical non-permanent surfaces, thin-slicing tasks) |
| Restorative opening circle | Where appropriate (~1–2 lessons; unit-opening lesson and lesson after a high-stakes assessment are the canonical placements) | `[RESTORATIVE CIRCLE]` chip on the lesson cover; specific circle question provided in Strategy Spotlight |

### 5.6 Kinematics strategy rotation (proposed)

| Lesson | Strategy chips |
|---|---|
| 01 Vectors | Restorative Circle (unit opener) · Active Learning (vector golf stations) |
| 02 Distance/Displacement | — |
| 03 Average Speed and Velocity | Hochman (sentence expansion on rate of change) |
| 04 Acceleration | BTC (random groups + VNPS for graph interpretation) |
| 05 Motion Graphs | Active Learning (gallery walk of student-drawn graphs) |
| 06 Freefall | Hochman (because/but/so for misconceptions) |
| 07 Vertical Projectiles | — |
| 08 Horizontal Projectiles | BTC (thin-slicing tasks) · Hochman (paragraph topic sentence) |
| 09 Angled Projectiles | Active Learning (project-based design challenge) |

Total: Hochman 3, Active Learning 3, BTC 2, Restorative Circle 1 (unit opener). Aligns with district frequency targets across a ~2-week unit. A second restorative circle would land on the day after the unit assessment, which is in the *next* unit and out of scope for this pilot.

---

## 6. Lesson Artifacts (per lesson)

### 6.1 Two student-facing flavors

| Variant | Filename | Where hosted | What's in it |
|---|---|---|---|
| Interactive | `Student_Exploration.html` | SharePoint document library (Permissive browser file handling) or GitHub Pages fallback | Full JS/SVG interactives, sliders, live diagrams |
| OneNote-native | `Student_Exploration.onenote.html` | Pasted into OneNote Class Notebook page | Static-only: same content arc, but interactives replaced with 3–5 frame storyboard SVGs, video links with paste-time instructions for the teacher to embed via OneNote's "Insert → Online Video", and a printable graphic organizer. No JS. No external-link dependency from the HTML itself. |

Both share the same lesson backbone, observation-checklist sections, SEL bookends, strategy chips, curated MD resources, and co-branded header. The only difference is the Investigation block.

### 6.2 Student_Exploration.html — required sections

1. Co-branded header (logo lockup, unit name, lesson topic name verbatim from MD, strategy chips)
2. Hook / phenomenon framing (uses curated phenomenon link from MD; embedded YouTube as `<iframe>` when source is video)
3. Driving question
4. Notice & Wonder capture box
5. Initial Model sketch/text area (printable)
6. Turn and Talk #1 callout
7. Interactive Explore — custom SVG/JS specific to topic, with `<noscript>` storyboard fallback
8. Make it Make Sense — 3–5 prompt questions with collapsible hints
9. Turn and Talk #2 callout
10. Connect to the Math — equations and worked example, KaTeX (offline copy in `_assets/lesson.js`)
11. Key Vocabulary (max 3, positioned in second half)
12. Revise Your Model block
13. Return to the Phenomenon section
14. Exit Ticket + SEL Closing Reflection
15. Explore Further — bulleted list of teacher-curated PhET/Javalab/Physics Classroom links from MD row, in MD order
16. Co-branded footer (tagline, attribution, lesson ID)

### 6.3 Student_Exploration.onenote.html — required transformations

Same sections as 6.2, with these transformations applied by the build's static-ifier pass:
- All `<script>` tags removed
- Interactive widgets replaced with their `<noscript>` storyboard SVG (3–5 frames showing key states, captions explaining each frame)
- All CSS inlined; no external `<link>` tags
- All images base64-encoded
- No `<iframe>` tags (videos replaced with a "Watch on YouTube" link plus the OneNote-native instruction "Insert → Online Video → paste this URL")
- Layout uses tables instead of flexbox/grid for OneNote paste compatibility

### 6.4 Teacher_Guide — fixed structure (every lesson)

Source `.md` builds to `.docx` (Pandoc + reference doc) and `.onenote.html` (Pandoc standalone + self-contained):

1. Cover (co-brand lockup, "Unit: Kinematics — Lesson NN: <Topic>", strategy chips for this lesson)
2. Curated Resources (from MD — verbatim, in tinted box)
3. CCC Focus (one line)
4. NYSSLS Observation Checklist crosswalk (which sections satisfy items 1–8)
5. Opening Connection (SEL)
6. At-a-Glance (duration, materials, safety, prior knowledge)
7. Lesson Objectives ("I can…" statements aligned to NYSSLS)
8. Agenda (with Turn-and-Talks marked, vocab placement, transfer task; timing column)
9. Discussion Prompts (with sample student responses)
10. Common Misconceptions (with corrections)
11. Access & Differentiation (ELL/ENL, SPED, Extensions)
12. Strategy Spotlight (only present when a strategy chip is on the cover; explains the specific Hochman/Active/BTC/Circle move and how to facilitate it)
13. Exit Ticket + Closing Reflection
14. Companion Materials cross-references

### 6.5 Answer_Key — required structure

Source `.md` builds to `.docx` and `.onenote.html`. Each "Make it Make Sense" prompt and exit-ticket item from the student materials is reproduced with:
- Expected answer
- 1–2 sentence rubric / acceptable-range note (numerical answers get tolerances)
- NYSSLS standard tag in right margin

### 6.6 Unit-level files (one per unit)

- **Unit_Plan**: opens with verbatim MD unit table; pacing calendar; strategy rotation table (5.6); NYSSLS coverage matrix; vocabulary scope (3-words-per-lesson list aggregated)
- **Assessments/**: Regents-style multiple-choice and constructed-response items mapped to unit's NYSSLS standards, drawing from the assessment links the teachers curated in the MD
- **Visuals/Visual_Prompts.md**: text prompts for any AI-generated images used in HTML/DOCX, so visuals are reproducible

---

## 7. Authoring, Build, and Verification

### 7.1 Source-of-truth strategy

| Artifact | Source format | Generated outputs |
|---|---|---|
| Student_Exploration | Hand-authored interactive HTML/CSS/JS in lesson folder | itself + `.onenote.html` (static-ified) |
| Teacher_Guide | `Teacher_Guide.md` | `.docx` (Pandoc + reference doc) + `.onenote.html` (Pandoc standalone) |
| Answer_Key | `Answer_Key.md` | `.docx` + `.onenote.html` |
| Unit_Plan | `Unit_Plan.md` | `.docx` + `.onenote.html` |
| Assessments | `*.md` | `.docx` + `.onenote.html` |
| Brand tokens | `_assets/brand/brand.css` (HTML) + `_assets/brand/reference.docx` (Pandoc) | applied at build time |

Both source files (`.md`, hand-authored `.html`) and built outputs (`.docx`, `.onenote.html`) are committed. Source files are diffable in git; built artifacts are what teachers receive.

### 7.2 Build script: `tools/build_lessons.py`

Walks the unit tree and:
1. For every `*.md` source: runs `pandoc <name>.md -o <name>.docx --reference-doc=_assets/brand/reference.docx`.
2. For every `*.md` source: runs `pandoc <name>.md -o <name>.onenote.html --standalone --self-contained --no-highlight`.
3. For every hand-authored interactive `Student_Exploration.html`: passes through unchanged, then runs the static-ifier pass to produce `Student_Exploration.onenote.html`.
4. Validates required structure (see 7.4).
5. Writes `build_report.md` listing built/skipped/failed lessons.

Run with: `python tools/build_lessons.py 01_Kinematics` (no arg = all units).

### 7.3 Static-ifier pass

For each `Student_Exploration.html`, the pass:
- Strips `<script>` tags
- Locates each interactive widget (marked with `data-interactive="true"`) and replaces it with its sibling `<noscript>` storyboard SVG block
- Inlines all CSS from `<link>` tags into `<style>`
- Base64-encodes all `<img src="...">` references
- Replaces `<iframe>` tags with a "Watch on YouTube" link and OneNote-paste instruction
- Converts flexbox/grid layouts to nested `<table>` layouts where necessary for OneNote compatibility
- Wraps output in a OneNote-friendly skeleton

### 7.4 Validation rules

**Hard-fail (build aborts):**
- Lesson folder missing one of `Student_Exploration.html`, `Teacher_Guide.md`, `Answer_Key.md`
- Required Teacher_Guide section heading missing (per 6.4)
- Curated Resources block empty (must include NYSSLS row from MD)
- Key Vocabulary list exceeds 3 items
- Co-branded header lockup missing from HTML
- Interactive widget missing its `<noscript>` storyboard fallback
- `.onenote.html` output contains `<script>`, `<iframe>`, or external `<link>` tags

**Soft-warn (build succeeds, warning logged):**
- Lesson has no strategy chips
- Phenomenon section has no link/embed
- Transfer task uses the same phenomenon as the hook

### 7.5 Lesson scaffolding: `tools/scaffold_lesson.py`

Creates a new lesson folder with template files pre-filled with section headings:

```
python tools/scaffold_lesson.py 01_Kinematics 03 "Average Speed and Velocity" \
    --strategies "Hochman:sentence-expansion"
```

Generates:
- `01_Kinematics/03_Average_Speed_and_Velocity/Student_Exploration.html` (with all required sections + interactive stub + `<noscript>` storyboard stub)
- `Teacher_Guide.md` (with all 14 required headings)
- `Answer_Key.md` (with answer-block stubs)

Required sections come from `tools/lesson_schema.yaml` — the single source of truth for lesson structure rules; both scaffold and validation read from it.

### 7.6 Manual QA checklist (per lesson, pilot only)

`tools/lesson_qa_checklist.md`:
1. Open `Student_Exploration.html` via `file://` URL — verify it renders and interacts correctly with no server.
2. Print preview — verify print stylesheet hides interactive controls and shows static fallback.
3. Disable JavaScript — verify storyboard fallback and curated MD links remain usable.
4. Open `Student_Exploration.onenote.html` in browser — verify no JS warnings, no broken images, no external requests in network tab.
5. Select All → Copy → Paste into a OneNote page (manual test) — verify layout, images, and links survive the paste.
6. Open `Teacher_Guide.docx` in Word — verify cover lockup, fonts, and tinted Curated Resources box render correctly.
7. Run `python tools/build_lessons.py 01_Kinematics/NN_Topic/` and confirm zero hard-fails.

Future automation (Playwright snapshot tests, OneNote Graph API) is out of scope for the pilot.

### 7.7 Hosting workflow (documented in `README.md`)

**SharePoint (primary):**
- Drop the unit folder into a SharePoint document library.
- Teachers and students open `.html` and `.docx` files via library links.
- Requires Permissive browser file handling at the tenant or site-collection level for `.html` to open inline.

**GitHub Pages (fallback if SharePoint is Strict):**
- Run `python tools/publish_pages.py` to copy interactive `.html` files into the `gh-pages` branch.
- Public URLs replace SharePoint links inside OneNote pages.

**OneNote Class Notebook:**
- For each lesson, open `Student_Exploration.onenote.html` in a browser, Select All → Copy → Paste into the corresponding OneNote page.
- Same paste workflow for `Teacher_Guide.onenote.html` into the teacher section.
- A one-page "OneNote Import Guide" is produced as part of the pilot deliverables.

### 7.8 Git workflow

- Branch: `physics-east-meadow-refactor` off `main`.
- Per-lesson commits — one commit lands one lesson's full artifact set (HTML + Teacher_Guide.md/.docx/.onenote.html + Answer_Key.md/.docx/.onenote.html).
- Unit-level commits (Unit_Plan, Assessments) land separately.
- The archive move is a single commit at the start.
- Squash optional at PR time.

---

## 8. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| District SharePoint is Strict mode and blocks `.html` rendering | GitHub Pages fallback documented; build script supports it without code changes |
| Logo / brand assets not provided in time | Placeholder SVGs render acceptably; brand tokens swap-in at one location |
| OneNote paste fidelity varies by client (web vs. desktop vs. iPad) | Manual QA step 5 verifies on each target client during pilot; storyboard fallbacks use simple HTML that pastes well across all OneNote clients |
| Pandoc reference DOCX styling diverges from intended brand | Reference DOCX is committed; visual diff during pilot QA catches drift early |
| Storyboard SVG fallback authoring is high effort | Templated in `tools/scaffold_lesson.py`; authors copy and modify rather than build from scratch |
| Static-ifier breaks on edge cases (custom widgets) | Hard-fail validation forces every interactive to declare its storyboard inline; static-ifier just selects it, never generates it |
| District tagline / EM brand book differs from public-CSS-derived tokens | Single-file change in `brand.css`; no individual lessons need editing |

---

## 9. Open Questions

1. **East Meadow tagline** — VSCHSD uses "Learning, Achieving, Succeeding!" publicly; is there an East Meadow equivalent we should pair with it, or should the EM side stay neutral?
2. **Logo files** — when can we get official EM and VSCHSD logo SVG/PNG assets?
3. **District SharePoint mode** — confirm with district IT whether browser file handling is Strict or Permissive on the target document library.
4. **Class Notebook structure** — does the district want one OneNote notebook per course or per teacher?
5. **Vector Golf and other Google Doc resources** — these are linked from the MD; should we mirror them locally for offline access, or rely on the live links?

These are not blockers for writing the implementation plan. They surface during pilot lesson authoring.

---

## 10. Deliverables

End of pilot:
1. `_archive/` containing the old partial refactor work
2. `01_Physics_East_Meadow_Refactor/` with:
   - `README.md`, `Scope_and_Sequence.md`
   - `_assets/` populated (placeholder logos, brand.css, lesson.css/js, reference.docx)
   - `01_Kinematics/` fully built — Unit_Plan, Assessments, all 9 lessons in both flavors
   - Stub directories for the other 9 units
3. `tools/` populated with `build_lessons.py`, `scaffold_lesson.py`, `publish_pages.py`, `lesson_schema.yaml`, `lesson_qa_checklist.md`
4. One-page "OneNote Import Guide"
5. `build_report.md` showing zero hard-fails for the pilot unit

After pilot acceptance, the same template scales to Units 0 and 2–9.
