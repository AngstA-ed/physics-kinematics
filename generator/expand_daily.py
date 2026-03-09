#!/usr/bin/env python3
"""Expand multi-day lessons into individual daily lessons.

Each multi-day lesson is split into N daily lessons with distinct content
following a pedagogical progression:
  Day 1: Introduction — define, identify, describe
  Day 2: Guided Practice — apply, calculate, compare
  Day 3: Application/Assessment — evaluate, synthesize, explain

Usage:
    python -m generator.expand_daily --course chemistry
    python -m generator.expand_daily --course physics
"""

import json
import argparse
import copy
import os
import re

DAY_PROGRESSIONS = {
    1: [{"phase": "Complete Lesson", "verb_prefix": "", "do_now_prefix": ""}],
    2: [
        {
            "phase": "Introduction & Exploration",
            "verb_prefix": "define and identify",
            "do_now_prefix": "Look at the following scenario: ",
            "five_e_focus": {
                "engage": "Introduce the phenomenon and driving question. Students make initial observations and predictions.",
                "explore": "Hands-on exploration or guided investigation to build initial understanding.",
                "explain": "Teacher-led instruction introducing key vocabulary and foundational concepts.",
                "elaborate": "Hochman writing activity connecting new vocabulary to prior knowledge.",
                "evaluate": "Quick formative check — exit ticket with 2-3 questions on key definitions and concepts.",
            },
        },
        {
            "phase": "Practice & Application",
            "verb_prefix": "apply and analyze",
            "do_now_prefix": "Review: Based on yesterday's lesson, ",
            "five_e_focus": {
                "engage": "Brief review of Day 1 concepts through a warm-up problem or quick discussion.",
                "explore": "Students work through practice problems or applications in pairs or small groups.",
                "explain": "Address common misconceptions from practice; model problem-solving strategies.",
                "elaborate": "CER activity connecting evidence to claims about the topic.",
                "evaluate": "Exit ticket with application-level problems requiring multi-step reasoning.",
            },
        },
    ],
    3: [
        {
            "phase": "Introduction & Concept Development",
            "verb_prefix": "define and describe",
            "do_now_prefix": "Consider this: ",
            "five_e_focus": {
                "engage": "Anchoring phenomenon presentation. Students record initial observations and questions.",
                "explore": "Guided discovery activity — students investigate the concept through hands-on work.",
                "explain": "Direct instruction introducing core vocabulary, principles, and relationships.",
                "elaborate": "Hochman writing activity using new vocabulary in Because/But/So sentences.",
                "evaluate": "Exit ticket — match terms to definitions, identify key relationships.",
            },
        },
        {
            "phase": "Guided Practice & Deeper Understanding",
            "verb_prefix": "apply and compare",
            "do_now_prefix": "Recall from yesterday: ",
            "five_e_focus": {
                "engage": "Review warm-up connecting Day 1 vocabulary to a new example or context.",
                "explore": "Structured practice — students work through increasingly complex problems with scaffolds.",
                "explain": "Mini-lesson addressing patterns from practice; introduce additional complexity.",
                "elaborate": "Partner work on application problems with real-world contexts.",
                "evaluate": "Formative assessment — students solve 2-3 problems independently and self-check.",
            },
        },
        {
            "phase": "Application, Assessment & Extension",
            "verb_prefix": "evaluate and explain",
            "do_now_prefix": "Review: Using what you've learned this week, ",
            "five_e_focus": {
                "engage": "Present a novel scenario that requires synthesis of concepts from Days 1-2.",
                "explore": "CER activity — students construct evidence-based arguments about the topic.",
                "explain": "Whole-class discussion of CER responses; address remaining misconceptions.",
                "elaborate": "Extension or enrichment activity connecting to real-world applications.",
                "evaluate": "Summative check — quiz or performance task covering all concepts from the sequence.",
            },
        },
    ],
}

# Extend for 4+ day lessons
for n in range(4, 8):
    DAY_PROGRESSIONS[n] = []
    for i in range(n):
        if i == 0:
            DAY_PROGRESSIONS[n].append(DAY_PROGRESSIONS[3][0])
        elif i == n - 1:
            DAY_PROGRESSIONS[n].append(DAY_PROGRESSIONS[3][2])
        elif i == n - 2:
            DAY_PROGRESSIONS[n].append(DAY_PROGRESSIONS[3][1])
        else:
            DAY_PROGRESSIONS[n].append({
                "phase": f"Continued Practice & Exploration (Day {i+1})",
                "verb_prefix": "practice and extend",
                "do_now_prefix": f"Review: Based on our work so far, ",
                "five_e_focus": {
                    "engage": "Quick review activity connecting to previous day's learning.",
                    "explore": "Lab investigation or extended practice with new problem types.",
                    "explain": "Address questions from exploration; connect findings to core concepts.",
                    "elaborate": "Application problems in new contexts; peer discussion and comparison.",
                    "evaluate": "Progress check — students demonstrate understanding through practice problems.",
                },
            })


CIRCLE_PROMPTS_BY_DAY = {
    0: None,  # Keep original
    1: [
        "What's one thing from yesterday's lesson that surprised you or that you're still thinking about?",
        "Share one connection you made between yesterday's topic and something in your daily life.",
        "What's one question you still have from our last class?",
    ],
    2: [
        "Share something you learned this week that you could explain to a friend or family member.",
        "What's one way the topic we've been studying connects to your community or neighborhood?",
        "If you could teach one thing from this week's lessons to a younger student, what would it be?",
    ],
}


def make_daily_learning_target(original_target, day_idx, total_days, progression):
    """Create a day-specific learning target from the original."""
    # Extract the "I can..." part
    match = re.search(r"I can (.+)", original_target, re.IGNORECASE)
    if not match:
        return original_target

    core_skill = match.group(1).rstrip(".")

    if total_days == 1:
        return original_target

    prefix = progression["verb_prefix"]
    if day_idx == 0:
        # First day: introduction level
        return f"At the end of 42 minutes I can {prefix} key concepts related to: {core_skill}"
    elif day_idx == total_days - 1:
        # Last day: application/assessment level
        return f"At the end of 42 minutes I can {prefix} my understanding to {core_skill}"
    else:
        # Middle days: practice level
        return f"At the end of 42 minutes I can {prefix} concepts and {core_skill}"


def make_daily_do_now(original_do_now, day_idx, total_days, progression, prev_target=""):
    """Create a day-specific Do Now."""
    if day_idx == 0:
        return original_do_now

    prefix = progression["do_now_prefix"]
    # For subsequent days, reference previous learning
    if prev_target:
        core = re.search(r"I can (.+)", prev_target, re.IGNORECASE)
        if core:
            return f"{prefix}explain one key idea from yesterday about how to {core.group(1).rstrip('.')}."

    return f"{prefix}{original_do_now}"


def make_daily_five_e(original_five_e, day_idx, total_days, progression, topic_title):
    """Create day-specific 5E sequence."""
    five_e = copy.deepcopy(original_five_e)
    focus = progression["five_e_focus"]

    for phase in ["engage", "explore", "explain", "elaborate", "evaluate"]:
        if phase in five_e and phase in focus:
            orig_desc = five_e[phase].get("description", "")
            # Blend original content with day-specific framing
            if day_idx == 0:
                five_e[phase]["description"] = f"{focus[phase]} Topic focus: {topic_title}. {orig_desc}"
            elif day_idx == total_days - 1:
                five_e[phase]["description"] = f"{focus[phase]} Building on previous days: {orig_desc}"
            else:
                five_e[phase]["description"] = f"{focus[phase]} Continuing: {orig_desc}"

    # Adjust times for each day
    time_plans = {
        "engage": "5 min",
        "explore": "12 min",
        "explain": "8 min",
        "elaborate": "7 min",
        "evaluate": "3 min",
    }
    for phase, time in time_plans.items():
        if phase in five_e:
            five_e[phase]["time"] = time

    return five_e


def make_daily_hochman(original_hochman, day_idx, total_days, vocab_terms):
    """Create day-specific Hochman activity."""
    if day_idx == 0:
        return original_hochman

    if not vocab_terms:
        return original_hochman

    # Pick a term for the activity
    term_idx = day_idx % len(vocab_terms)
    term = vocab_terms[term_idx]["term"]

    if day_idx == total_days - 1:
        return (
            f"Kernel sentence expansion using '{term}': Start with '{term} is important.' "
            f"Expand by adding when, where, why, and how details to create a complex sentence "
            f"that demonstrates understanding of the concept."
        )
    else:
        return (
            f"Because/But/So using '{term}': Write three sentences — "
            f"'{term}... because ___.' / '{term}... but ___.' / '{term}... so ___.'"
        )


def split_vocabulary(vocab_list, total_days):
    """Split vocabulary across days."""
    if not vocab_list:
        return [[] for _ in range(total_days)]

    result = [[] for _ in range(total_days)]
    for i, term in enumerate(vocab_list):
        result[i % total_days].append(term)

    return result


def split_guided_notes(notes_outline, total_days):
    """Split guided notes sections across days."""
    if not notes_outline:
        return [[] for _ in range(total_days)]

    result = [[] for _ in range(total_days)]
    for i, section in enumerate(notes_outline):
        result[i % total_days].append(section)

    # Ensure each day has at least one section
    for i in range(total_days):
        if not result[i]:
            result[i] = [f"Continued Practice and Review (Day {i+1})"]

    return result


def expand_lesson(lesson, unit_title):
    """Expand a multi-day lesson into individual daily lessons."""
    days = lesson.get("days", 1)
    if days <= 0:
        days = 1

    if days == 1:
        out = copy.deepcopy(lesson)
        out["days"] = 1
        return [out]

    progressions = DAY_PROGRESSIONS.get(days, DAY_PROGRESSIONS[max(DAY_PROGRESSIONS.keys())][:days])
    vocab_split = split_vocabulary(lesson.get("vocabulary", []), days)
    notes_split = split_guided_notes(lesson.get("guided_notes_outline", []), days)

    daily_lessons = []
    for day_idx in range(days):
        prog = progressions[day_idx] if day_idx < len(progressions) else progressions[-1]
        daily = copy.deepcopy(lesson)
        daily["days"] = 1

        # Update title
        daily["title"] = f"{lesson['title']} (Day {day_idx + 1} of {days})"
        daily["_phase"] = prog["phase"]

        # Learning target
        daily["learning_target"] = make_daily_learning_target(
            lesson["learning_target"], day_idx, days, prog
        )

        # Circle prompt
        if day_idx > 0:
            prompts = CIRCLE_PROMPTS_BY_DAY.get(day_idx, CIRCLE_PROMPTS_BY_DAY[2])
            if prompts:
                daily["circle_prompt"] = prompts[day_idx % len(prompts)]

        # Do Now
        prev_target = daily_lessons[-1]["learning_target"] if daily_lessons else ""
        daily["do_now"] = make_daily_do_now(
            lesson["do_now"], day_idx, days, prog, prev_target
        )

        # 5E sequence
        daily["five_e"] = make_daily_five_e(
            lesson["five_e"], day_idx, days, prog, lesson["title"]
        )

        # Hochman
        daily["hochman_activity"] = make_daily_hochman(
            lesson.get("hochman_activity", ""), day_idx, days, vocab_split[day_idx]
        )

        # Vocabulary — split across days
        daily["vocabulary"] = vocab_split[day_idx]

        # Guided notes — split across days
        daily["guided_notes_outline"] = notes_split[day_idx]

        # CER — only on final day
        if day_idx < days - 1:
            daily["cer"] = None

        # Differentiation — adjust for day
        if day_idx == 0:
            pass  # Keep original differentiation
        elif day_idx == days - 1:
            diff = daily.get("differentiation", {})
            if diff.get("approaching"):
                diff["approaching"] = (
                    f"Review key concepts from the full sequence before assessment. "
                    f"{diff['approaching']}"
                )
            if diff.get("advanced"):
                diff["advanced"] = (
                    f"Complete extension challenge connecting to real-world applications. "
                    f"{diff['advanced']}"
                )
        else:
            diff = daily.get("differentiation", {})
            if diff.get("approaching"):
                diff["approaching"] = (
                    f"Provide completed examples from Day 1 as reference. "
                    f"{diff['approaching']}"
                )

        daily_lessons.append(daily)

    return daily_lessons


def expand_course(config):
    """Expand all units in a course config to daily lessons."""
    expanded = copy.deepcopy(config)

    for unit in expanded["units"]:
        unit_title = unit["title"]
        all_daily = []

        for lesson in unit.get("lessons", []):
            daily_lessons = expand_lesson(lesson, unit_title)
            all_daily.extend(daily_lessons)

        # Renumber sequentially
        for i, lesson in enumerate(all_daily):
            lesson["number"] = i + 1

        unit["lessons"] = all_daily

    return expanded


def main():
    parser = argparse.ArgumentParser(description="Expand multi-day lessons to daily lessons")
    parser.add_argument("--course", required=True, help="Course name (chemistry or physics)")
    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_dir = os.path.join(base_dir, "generator", "configs")

    input_path = os.path.join(config_dir, f"{args.course}.json")
    output_path = os.path.join(config_dir, f"{args.course}_daily.json")

    with open(input_path) as f:
        config = json.load(f)

    print(f"Expanding {args.course}...")
    print(f"Input: {len(config['units'])} units")

    original_lessons = sum(len(u.get("lessons", [])) for u in config["units"])
    print(f"Original lessons: {original_lessons}")

    expanded = expand_course(config)

    total_lessons = sum(len(u.get("lessons", [])) for u in expanded["units"])
    print(f"Expanded lessons: {total_lessons}")
    print()

    for u in expanded["units"]:
        lesson_count = len(u.get("lessons", []))
        print(f"  Unit {u['number']}: {u['title']} — {lesson_count} daily lessons")

    with open(output_path, "w") as f:
        json.dump(expanded, f, indent=2)

    print(f"\nWritten to: {output_path}")


if __name__ == "__main__":
    main()
