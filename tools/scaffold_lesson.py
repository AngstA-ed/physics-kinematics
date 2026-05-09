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
    teacher_extra = {
        **common,
        "STRATEGY_CHIPS": chip_md,
        "NYSSLS_VERBATIM": "[Paste verbatim from Scope_and_Sequence.md, including the bold performance expectation and (parenthesized CCC).]",
        "PHENOMENON_VERBATIM": "[Paste the teacher-curated phenomenon and link from the MD row.]",
        "LABS_VERBATIM": "[Paste the teacher-curated lab links from the MD row, in MD order.]",
        "ASSESSMENTS_VERBATIM": "[Paste the teacher-curated assessment links from the MD row, in MD order.]",
        "CCC_FOCUS": "[One-line CCC focus.]",
        "MATERIALS": "[Materials list.]",
        "SAFETY": "[Safety notes or 'None'.]",
        "PRIOR_KNOWLEDGE": "[Prior knowledge bullets.]",
        "OBJECTIVES": "[I can… statements.]",
        "AGENDA_ROWS": "| 0–3 | Opening Connection (SEL) | … |\n| 3–7 | Phenomenon hook | … |\n| 7–12 | Notice & Wonder + Turn and Talk #1 | … |",
        "DISCUSSION_PROMPTS": "- [Prompt 1]\n- [Prompt 2]",
        "MISCONCEPTIONS": "- [Misconception → correction]",
        "ELL_SUPPORTS": "[Sentence frames, word-choice boxes, bilingual glossary.]",
        "SPED_SUPPORTS": "[Chunked tasks, graphic organizer.]",
        "EXTENSIONS": "[Extension prompt.]",
        "STRATEGY_SPOTLIGHT": "(none)" if not strategy_chips else "[Describe the specific Hochman/Active/BTC/Circle move and how to facilitate it.]",
        "EXIT_TICKET": "[Exit ticket prompt; new transfer phenomenon optional.]",
    }
    answer_extra = {
        **common,
        "MIMS_ANSWERS": "1. [Answer 1] · *Rubric:* … · NYSSLS: HS-PS2-1\n2. [Answer 2] · *Rubric:* … · NYSSLS: HS-PS2-1\n3. [Answer 3] · *Rubric:* … · NYSSLS: HS-PS2-1",
        "EXIT_TICKET_ANSWER": "[Expected answer + tolerance/rubric + NYSSLS tag.]",
    }

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
    )
    print(f"Scaffolded {lesson_dir.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
