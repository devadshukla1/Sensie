from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [ROOT / "SKILL.md", ROOT / "README.md"]

SKILL_REQUIRED_SECTIONS = [
    "# Sensie — Practical Intelligence for LLMs",
    "## 1. Core Objective",
    "## 2. Operating Loop",
    "## 3. Asking Questions",
    "## 4. Brute Force as Verification",
    "## 5. Current-Technology Rule",
    "## 6. Project-Engineering Rule",
    "## 7. Accuracy Rule",
    "## 8. Completeness Rule",
    "## 9. Security Defaults",
    "## 10. Communication Rules",
    "## 11. Completion Gate",
    "## 12. Configuration",
    "## 13. Final Principle",
]

README_REQUIRED_SECTIONS = [
    "# Sensie",
    "## What Sensie Solves",
    "## Before Sensie vs After Sensie",
    "## The Sensie Reasoning Loop",
    "## The Sensie Principles",
    "## Verification Engine",
    "## Brute Force as a Practical Tool",
    "## Software Engineering Mode",
    "## Architecture",
    "## Practical Examples",
    "## What Sensie Is Not",
    "## Configuration",
    "## Installation & Usage",
    "## Repository Structure",
    "## Validation",
    "## Accuracy Philosophy",
    "## Security & Engineering Safety",
    "## Roadmap",
    "## Contributing",
    "## License",
]


def read(path: Path) -> str:
    if not path.exists():
        raise AssertionError(f"Missing required file: {path.relative_to(ROOT)}")
    content = path.read_text(encoding="utf-8")
    if not content.strip():
        raise AssertionError(f"Empty required file: {path.relative_to(ROOT)}")
    return content


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold()


def require_sections(text: str, sections: list[str], filename: str) -> None:
    for section in sections:
        if normalize(section) not in normalize(text):
            raise AssertionError(f"{filename} missing section: {section}")


def validate_skill(skill: str) -> None:
    if not skill.startswith("---\n"):
        raise AssertionError("SKILL.md must start with YAML front matter")

    parts = skill.split("---\n", 2)
    if len(parts) < 3:
        raise AssertionError("SKILL.md YAML front matter is incomplete")

    metadata, body = parts[1], parts[2]
    normalized_body = normalize(body)

    if not re.search(r"(?m)^name:\s*sensie\s*$", metadata):
        raise AssertionError("Skill name must be 'sensie'")
    if not re.search(r"(?m)^version:\s*1\.0\.0\s*$", metadata):
        raise AssertionError("Expected skill version 1.0.0")
    if not re.search(r"(?m)^license:\s*MIT\s*$", metadata):
        raise AssertionError("Expected MIT license metadata")

    require_sections(body, SKILL_REQUIRED_SECTIONS, "SKILL.md")

    required_concepts = [
        "brute force is a **verification technique**",
        "accuracy ≠ confidence.",
        "do not invent requirements",
        "never fabricate an api",
        "current authoritative source",
        "secure defaults",
        "least privilege",
        "avoid chain-of-thought disclosure",
        "do not create unnecessary follow-up work",
    ]
    for concept in required_concepts:
        if normalize(concept) not in normalized_body:
            raise AssertionError(f"SKILL.md missing required concept: {concept}")

    if not re.search(r"never\s+claim\s+impossible\s+absolute\s+accuracy", normalized_body):
        raise AssertionError("SKILL.md missing safeguard: absolute accuracy")


def validate_readme(readme: str) -> None:
    require_sections(readme, README_REQUIRED_SECTIONS, "README.md")
    normalized_readme = normalize(readme)

    for item in [
        "mermaid",
        "two sum",
        "differential testing",
        "maximum practical accuracy",
        "accuracy ≠ confidence",
    ]:
        if item not in normalized_readme:
            raise AssertionError(f"README.md missing required content: {item}")


def validate() -> None:
    skill = read(ROOT / "SKILL.md")
    readme = read(ROOT / "README.md")
    validate_skill(skill)
    validate_readme(readme)
    print("Sensie validation passed.")


if __name__ == "__main__":
    validate()
