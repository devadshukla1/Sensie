from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    ROOT / "SKILL.md",
    ROOT / "README.md",
]

REQUIRED_SECTIONS = [
    "# Sensie",
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
]

REQUIRED_SAFEGUARDS = [
    "Do not invent requirements.",
    "Never fabricate an API, version, parameter, benchmark, capability, or compatibility claim.",
    "Do not claim impossible absolute accuracy",
    "Avoid unnecessary abstractions",
    "STOP",
]


def read(path: Path) -> str:
    if not path.exists():
        raise AssertionError(f"Missing required file: {path.relative_to(ROOT)}")
    content = path.read_text(encoding="utf-8")
    if not content.strip():
        raise AssertionError(f"Empty required file: {path.relative_to(ROOT)}")
    return content


def validate_skill(skill: str) -> None:
    if not skill.startswith("---\n"):
        raise AssertionError("SKILL.md must start with YAML front matter")

    front_matter = skill.split("---\n", 2)
    if len(front_matter) < 3:
        raise AssertionError("SKILL.md YAML front matter is incomplete")

    metadata = front_matter[1]
    body = front_matter[2]

    if not re.search(r"(?m)^name:\s*sensie\s*$", metadata):
        raise AssertionError("Skill name must be 'sensie'")
    if not re.search(r"(?m)^version:\s*1\.0\.0\s*$", metadata):
        raise AssertionError("Expected skill version 1.0.0")
    if not re.search(r"(?m)^license:\s*MIT\s*$", metadata):
        raise AssertionError("Expected MIT license metadata")

    required_phrases = [
        "UNDERSTAND",
        "CHECK",
        "SIMPLIFY",
        "VERIFY",
        "OPTIMIZE",
        "EXECUTE",
        "CHECK COMPLETENESS",
        "# Sensie — Practical Intelligence for LLMs",
        "Brute force is a **verification technique**",
        "Accuracy ≠ confidence.",
    ]
    for phrase in required_phrases:
        if phrase not in body:
            raise AssertionError(f"SKILL.md missing required concept: {phrase}")

    for safeguard in REQUIRED_SAFEGUARDS:
        if safeguard not in body:
            raise AssertionError(f"SKILL.md missing safeguard: {safeguard}")


def validate_readme(readme: str) -> None:
    for section in REQUIRED_SECTIONS:
        if section not in readme:
            raise AssertionError(f"README.md missing section: {section}")

    required_content = ["mermaid", "Two Sum", "Differential testing"]
    for item in required_content:
        if item not in readme:
            raise AssertionError(f"README.md missing required content: {item}")


def validate() -> None:
    skill = read(ROOT / "SKILL.md")
    readme = read(ROOT / "README.md")

    for path in REQUIRED_FILES:
        read(path)

    validate_skill(skill)
    validate_readme(readme)
    print("Sensie validation passed.")


if __name__ == "__main__":
    validate()
