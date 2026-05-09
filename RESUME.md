# Resume — Physics Kinematics Refactor

Open this in a fresh Claude Code session and the next prompt is one sentence.

## Where to start

```bash
cd /Users/hoopie/Projects/Curricula
git checkout physics-east-meadow-refactor
git pull origin physics-east-meadow-refactor
```

Last commit on this branch: see `git log --oneline -1`. The branch is fully pushed to `origin/physics-east-meadow-refactor`.

Branch is fully pushed (local HEAD == `origin/physics-east-meadow-refactor`). Run `git status` and you'll see DOCX files dirty from a local rebuild plus some pre-existing `generator/` and `Chemistry/` modifications unrelated to the Physics refactor — those regenerate from markdown via `python tools/build_lessons.py 01_Kinematics` and are safe to ignore.

## Project at a glance

| | |
|---|---|
| Repo | https://github.com/AngstA-ed/physics-kinematics |
| Live web edition | https://angsta-ed.github.io/physics-kinematics/ |
| Async demo link | https://angsta-ed.github.io/physics-kinematics/?tour=1 |
| Active branch | `physics-east-meadow-refactor` (16+ commits ahead of `main`) |
| Two tracks | OneNote-friendly (`01_Physics_East_Meadow_Refactor/`) · Web edition (`01_Physics_East_Meadow_Web/`) |
| Pilot unit | Kinematics — 9 lessons + Unit Plan + Regents-style cluster |
| Tests | 30 passing (`python -m pytest tests/tools/`) |

Design spec: `docs/superpowers/specs/2026-05-08-physics-east-meadow-refactor-design.md`
Implementation plan: `docs/superpowers/plans/2026-05-08-physics-east-meadow-refactor-plan.md`

## Recent additions worth knowing about

- **Lab-notebook visual redesign of the web edition** (cream paper, fountain-pen ink, Architects Daughter handwriting, taped vocab cards, hand-drawn outline buttons, paper-bookmark TOC) — live at `https://angsta-ed.github.io/physics-kinematics/`.
- **Strategy Spotlight asides** on the 7 web lessons that have a strategy chip — sticky-note-styled teacher's-notes blocks describing the Hochman / Active Learning / BTC / Restorative Circle move inline.
- **5E phenomenon-based teacher guides** — every Kinematics lesson's `Teacher_Guide.md` is now organized by Phase 1 Engage → Phase 5 Evaluate, with minute-by-minute facilitation script, sample teacher language, and anticipated student responses inside each phase. Generated DOCXes ship with the web edition; each lesson hero has a "Download teacher guide (DOCX)" button.
- **Tour fix** — the `?tour=1` guided demo works again under the redesigned scroll-in animations.
- **Validators** — schema, MC-answer-bold check (markdown), MC-answer-emphasis check (web HTML); 30/30 pytest tests; web validator runs as a pre-deploy CI step.

## What's next (the open task)

**Visual redesign of the web edition** — the user wants a more *educational / sciencey / fun / engaging* look than the current minimal-modern one. Hasn't been started yet.

Current visual language (from `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css`):
- Co-brand gradient hero (purple `#662e80` → blue `#2ea3f2`)
- Pill-shaped logo lockup
- Inter typography, 8px baseline grid, soft shadows, sticky TOC, reading-progress bar
- Neutral surface scale: `#fafafb`, `#ffffff`, `#f4f4f7`
- Strategy chips with colored dots

Open questions for the redesign that the user has *not* answered:
1. **Vibe target.** "Sciencey" could mean retro-textbook, NASA-mission-control, glowing-neon-Tron, Periodic-Videos colorful chalkboard, vintage Bill-Nye-ish. Which?
2. **Audience.** Visuals tuned for HS students or for adult adopters (teachers/admins/conferences) — these often pull in different directions.
3. **Animation budget.** Subtle (transitions, micro-interactions) or bold (full-page parallax, particle backgrounds, hover-explosions)?
4. **Iconography.** Geometric (current — emoji-free) or illustrated (custom SVG mascots, doodle-style diagrams)?
5. **Dark mode.** Add support, or stick with light only?
6. **Fonts.** Stay with Inter, or pair it with a more characterful display font (e.g., Space Grotesk, Fraunces, Inter Tight, Pixel-style for "sciencey")?

Recommend opening the redesign session with these questions so the visuals land first time. The Brainstorming skill (`superpowers:brainstorming`) is the right starting place — it's been used for every prior major decision in this project.

## Commands you'll reach for

```bash
# Activate venv (Python 3.14)
source .venv/bin/activate

# Run all tests (30 passing)
python -m pytest tests/tools/

# Build OneNote-friendly artifacts for Kinematics
python tools/build_lessons.py 01_Kinematics

# Validate the web edition for answer leaks (also runs in CI)
python tools/validate_web.py

# Open the local web edition
open Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/index.html

# See the live site
open https://angsta-ed.github.io/physics-kinematics/

# Push and CI auto-deploys (~30s)
git push origin physics-east-meadow-refactor

# Watch the latest deploy
gh run watch $(gh run list --workflow=deploy-pages.yml --limit 1 --json databaseId --jq '.[0].databaseId')
```

## What's protected

| Rule | Where it runs | What it forbids |
|---|---|---|
| Required Teacher Guide headings (14) | `tools/build_lessons.py` | Missing any of: Cover, Curated Resources, CCC Focus, etc. |
| Curated Resources sub-headings (4) | same | Missing NYSSLS / Phenomenon / Labs / Assessments |
| Vocab cap | same | More than 3 vocab terms per lesson |
| Interactive widget needs `<noscript>` storyboard | same | OneNote-friendly student HTML missing fallback |
| OneNote HTML output is JS-free | same | `<script>`, `<iframe>`, external `<link>` in `.onenote.html` |
| MC answer not bolded (markdown) | same | `**`, `__`, `<strong>`, `<b>` inside Multiple Choice option lines |
| MC answer not emphasized (web HTML) | `.github/workflows/deploy-pages.yml` | `<strong>`, `<b>`, `<em>` inside `<li>` of an `<ol>` in a "Multiple Choice" `<section>` |

Schema for all rules: `tools/lesson_schema.yaml`.

## Suggested first prompt for the next session

> "I want to redesign the web edition's look — more educational/sciencey/fun/engaging than the current minimal-modern style. Read RESUME.md for context, then run the brainstorming skill to walk me through visual direction options before changing any code."

That alone will: pull current branch state via `git pull`, read this file, invoke `superpowers:brainstorming`, and ask the 5–6 open questions listed above before touching CSS.

## Recent commit log (last 10)

```
2978268  docs: add RESUME.md for picking up the work in a fresh CLI session
54a9d8e  feat(ci): pre-deploy check for answer-revealing emphasis in web HTML
eb611d8  feat(validators): hard-fail on answer-revealing bold in MC options
126cfa8  feat(web): add guided tour for async demo sharing
0db56e2  ci: add GitHub Pages deploy workflow for web edition
a1a2cdf  feat(web): add modern web edition of the Kinematics unit
da97ccc  feat(kinematics): unit plan, Regents-style assessment, README, OneNote guide
58c1f9b  feat(kinematics): author Phase D lessons 02-09 with unique interactives
c9458aa  build(kinematics/vectors): pilot lesson green build + script path fix
c037a9e  feat(kinematics/vectors): author interactive vector-addition explorer + 3-frame storyboard
```

## Files the next session should read first

1. `RESUME.md` (this file) — orient
2. `docs/superpowers/specs/2026-05-08-physics-east-meadow-refactor-design.md` — design contract
3. `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/README.md` — web edition's authoring notes
4. `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/_assets/site.css` — current design system (the thing to redesign)
5. `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/lessons/01-vectors.html` — representative lesson page that all redesign decisions touch

Open questions tracked in the design spec at §9 (district SharePoint mode, official logo files, EM tagline) are still open and don't block the redesign.
