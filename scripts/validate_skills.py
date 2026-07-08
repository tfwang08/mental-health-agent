"""Basic repository checks for mental-health skills.

This script intentionally performs lightweight static validation. It is not a clinical evaluator.
"""

from pathlib import Path

REQUIRED_SECTIONS = [
    "Purpose",
    "Clinical Basis",
    "Allowed Behaviors",
    "Not Allowed",
]


def validate_skill(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    problems = []

    for section in REQUIRED_SECTIONS:
        if f"## {section}" not in text:
            problems.append(f"{path}: missing section '{section}'")

    if "diagnos" not in text.lower():
        problems.append(f"{path}: missing non-diagnostic boundary")

    return problems


def main() -> int:
    problems = []
    for skill in Path(".agents/skills").glob("*/SKILL.md"):
        problems.extend(validate_skill(skill))

    if problems:
        for problem in problems:
            print(problem)
        return 1

    print("Skill validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
