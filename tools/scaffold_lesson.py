"""Scaffold a new lesson folder from templates.

Usage:
    python tools/scaffold_lesson.py 01_Kinematics 03 "Average Speed and Velocity" \
        --strategies "Hochman:sentence-expansion"
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = Path(__file__).resolve().parent / "templates"

# Allow direct invocation: `python tools/scaffold_lesson.py ...`
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _render_chips(chips: Sequence[str]) -> str:
    if not chips:
        return ""
    out = []
    for chip in chips:
        kind = chip.split(":", 1)[0].lower().replace(" ", "-")
        cls = {
            "hochman": "hochman",
            "active-learning": "active",
            "btc": "btc",
            "restorative-circle": "circle",
        }.get(kind, "")
        out.append(f'<span class="strategy-chip {cls}">{chip.upper()}</span>')
    return " ".join(out)


def _render(template_text: str, mapping: dict[str, str]) -> str:
    out = template_text
    for k, v in mapping.items():
        out = out.replace(f"{{{{{k}}}}}", v)
    return out


def scaffold_lesson(
    *,
    out_dir: Path,
    unit_name: str,
    lesson_number: str,
    lesson_title: str,
    strategy_chips: Sequence[str],
    docx_only: bool = False,
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    chip_html = _render_chips(strategy_chips)
    chip_md = ", ".join(c.upper() for c in strategy_chips) if strategy_chips else "(none)"

    common = {
        "UNIT_NAME": unit_name,
        "LESSON_NUMBER": lesson_number,
        "LESSON_TITLE": lesson_title,
        "STRATEGY_CHIPS": chip_html,
        "LESSON_ID": f"{unit_name.lower()}-{lesson_number}",
        "PHENOMENON_DESCRIPTION": "[Author the phenomenon framing here.]",
        "DRIVING_QUESTION": "[Author the driving question here.]",
        "TURN_AND_TALK_1": "[Author Turn and Talk #1 prompt here.]",
        "TURN_AND_TALK_2": "[Author Turn and Talk #2 prompt here.]",
        "INTERACTIVE_PLACEHOLDER": "<!-- Author the live SVG/JS interactive here. -->",
        "STORYBOARD_PLACEHOLDER": "<p>Storyboard frame 1: [describe]</p><p>Storyboard frame 2: [describe]</p><p>Storyboard frame 3: [describe]</p>",
        "MIMS_Q1": "[Question 1]",
        "MIMS_Q2": "[Question 2]",
        "MIMS_Q3": "[Question 3]",
        "VOCAB_1": "[term 1]",
        "VOCAB_2": "[term 2]",
        "VOCAB_3": "[term 3]",
        "RETURN_PROMPT": "[Re-pose the original phenomenon. Ask students to use evidence from today.]",
        "EXIT_Q": "[Exit ticket question]",
        "CURATED_LINKS": "<li>[Link from MD row]</li>",
    }
    lesson_slug = f"{lesson_number.zfill(2)}-{lesson_title.lower().replace(' ', '-').replace('/', '-')}"
    teacher_extra = {
        **common,
        "STRATEGY_CHIPS": chip_md,
        "LESSON_SLUG": lesson_slug,
        "NYSSLS_VERBATIM": "[Paste verbatim from Scope_and_Sequence.md, including the bold performance expectation and (parenthesized CCC).]",
        "NYSSLS_SHORT": "[e.g., HS-PS2-1]",
        "PHENOMENON_VERBATIM": "[Paste the teacher-curated phenomenon and link from the MD row.]",
        "LABS_VERBATIM": "[Paste the teacher-curated lab links from the MD row, in MD order.]",
        "ASSESSMENTS_VERBATIM": "[Paste the teacher-curated assessment links from the MD row, in MD order.]",
        "CCC_FOCUS": "[One-line CCC focus.]",
        "MATERIALS": "[Materials list.]",
        "SAFETY": "[Safety notes or 'None'.]",
        "PRIOR_KNOWLEDGE": "[Prior knowledge bullets.]",
        "OBJECTIVES": "- [I can … statement 1.]\n- [I can … statement 2.]\n- [I can … statement 3.]",
        # Phase 1 · Engage placeholders
        "ENGAGE_OPENING_CONNECTION": "[SEL prompt — 1-question check-in / 'name something you noticed' / gratitude. If the lesson has a Restorative Circle chip, use the circle prompt and process here.]",
        "ENGAGE_PHENOMENON_ACTIONS": "[Project the phenomenon (link from Curated Resources). Let it run silently for ~30 s before speaking. Then ask the notice/wonder question.]",
        "ENGAGE_PHENOMENON_LANGUAGE": "[Sample teacher line — e.g., 'I'm not going to tell you what this is yet. Watch carefully. What do you notice?']",
        "ENGAGE_PHENOMENON_RESPONSES": "- [Anticipated response 1] — affirm / surface / redirect\n- [Anticipated response 2] — …\n- Pass — fine, move on",
        "ENGAGE_NW_AND_TT1": "[Capture students' Notice & Wonder columns. Then Turn-and-Talk #1 prompt: 'Share one thing you noticed and one thing you wondered. Pick a wondering you'd like the class to figure out today.']",
        # Phase 2 · Explore placeholders
        "EXPLORE_INITIAL_MODEL": "[Students sketch their first explanation of the phenomenon — silent, individual. Specific prompt: …]",
        "EXPLORE_INVESTIGATION": "[Hands-on phase. Specific procedure for the investigation, station setup, manipulatives, simulation usage. If the lesson has a Strategy chip, the strategy structures THIS phase.]",
        "EXPLORE_LOOK_FOR": "[Specific signals that students are surfacing the pattern]",
        "EXPLORE_REDIRECT": "[Specific student moves that need redirection — e.g., asking the teacher 'is this right' instead of testing it themselves]",
        # Phase 3 · Explain placeholders
        "EXPLAIN_CONSENSUS": "[Specific prompt for class consensus. Student responses converge on the lesson's core idea. Sample teacher language to scaffold.]",
        "EXPLAIN_VOCAB": "[Introduce the 3 vocab terms here. Sample teacher language: 'When a quantity has both a size and a direction, we call that a *vector*. The size is the *magnitude*. The way it points is the *direction*.']",
        "EXPLAIN_DISCUSSION_PROMPTS": "- [Prompt 1]\n  - *Sample student response:* […]\n- [Prompt 2]\n  - *Sample student response:* […]",
        # Phase 4 · Elaborate placeholders
        "ELABORATE_REVISE_MODEL": "[Students update their initial model from Phase 2 using the new vocabulary and pattern. Specific prompt: …]",
        "ELABORATE_RETURN_TO_PHENOMENON": "[Re-pose the original phenomenon. 'Now that we've worked this out, what would you say to a peer who saw the original [phenomenon] and asked what was going on?']",
        # Phase 5 · Evaluate placeholders
        "EVALUATE_EXIT_TICKET": "[Exit ticket prompt — new transfer phenomenon, not the same as the hook. Specific question and what's required from the student.]",
        "EVALUATE_CLOSING_REFLECTION": "[Closing reflection prompt — e.g., 'What is one thing that surprised you today? Who helped you make sense of something?']",
        "MISCONCEPTIONS": "- **Misconception:** […] → **Correction:** […]\n- **Misconception:** […] → **Correction:** […]",
        "ELL_SUPPORTS": "[Sentence frames, word-choice boxes, bilingual glossary.]",
        "SPED_SUPPORTS": "[Chunked tasks, graphic organizer.]",
        "EXTENSIONS": "[Extension prompt for students who finish early.]",
        "STRATEGY_SPOTLIGHT": "(none — straight 5E phenomenon-based lesson)" if not strategy_chips else "[Describe the specific Hochman / Active Learning / BTC / Restorative Circle move and how to facilitate it. Include sample teacher language and anticipated student responses.]",
    }
    answer_extra = {
        **common,
        "MIMS_ANSWERS": "1. [Answer 1] · *Rubric:* … · NYSSLS: HS-PS2-1\n2. [Answer 2] · *Rubric:* … · NYSSLS: HS-PS2-1\n3. [Answer 3] · *Rubric:* … · NYSSLS: HS-PS2-1",
        "EXIT_TICKET_ANSWER": "[Expected answer + tolerance/rubric + NYSSLS tag.]",
    }

    if docx_only:
        # DOCX-only units: student worksheet + guided notes instead of the
        # interactive HTML page.
        (out_dir / "Student_Worksheet.md").write_text(
            _render((TEMPLATES / "student_worksheet.md.tmpl").read_text(encoding="utf-8"), teacher_extra),
            encoding="utf-8",
        )
        (out_dir / "Student_Notes.md").write_text(
            _render((TEMPLATES / "student_notes.md.tmpl").read_text(encoding="utf-8"), teacher_extra),
            encoding="utf-8",
        )
    else:
        (out_dir / "Student_Exploration.html").write_text(
            _render((TEMPLATES / "student_exploration.html.tmpl").read_text(encoding="utf-8"), common),
            encoding="utf-8",
        )
    (out_dir / "Teacher_Guide.md").write_text(
        _render((TEMPLATES / "teacher_guide.md.tmpl").read_text(encoding="utf-8"), teacher_extra),
        encoding="utf-8",
    )
    (out_dir / "Answer_Key.md").write_text(
        _render((TEMPLATES / "answer_key.md.tmpl").read_text(encoding="utf-8"), answer_extra),
        encoding="utf-8",
    )


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("unit_dir", help="Unit folder, e.g. 01_Kinematics")
    p.add_argument("lesson_number", help="Two-digit lesson number, e.g. 03")
    p.add_argument("lesson_title", help='Lesson title, e.g. "Average Speed and Velocity"')
    p.add_argument("--strategies", default="", help="Comma-separated strategy chips")
    p.add_argument("--docx-only", action="store_true",
                   help="Scaffold Worksheet + Notes (DOCX-only) instead of the HTML student page")
    args = p.parse_args()

    chips = [c.strip() for c in args.strategies.split(",") if c.strip()]
    unit_path = ROOT / "Publisher_Ready_Curriculum" / "01_Physics_East_Meadow_Refactor" / args.unit_dir
    slug = args.lesson_title.replace(" ", "_").replace("/", "_")
    lesson_dir = unit_path / f"{args.lesson_number}_{slug}"
    unit_name = args.unit_dir.split("_", 1)[1].replace("_", " ")
    scaffold_lesson(
        out_dir=lesson_dir,
        unit_name=unit_name,
        lesson_number=args.lesson_number,
        lesson_title=args.lesson_title,
        strategy_chips=chips,
        docx_only=args.docx_only,
    )
    print(f"Scaffolded {lesson_dir.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
