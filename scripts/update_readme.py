from pathlib import Path
from collections import Counter
from datetime import datetime, timezone

SOLUTIONS_DIR = Path("solutions")
README_PATH = Path("README.md")
LEETCODE_ID = "Yuechen_Yang"

EXTENSION_TO_LANGUAGE = {
    ".py": "Python",
    ".cpp": "C++",
    ".java": "Java",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".go": "Go",
    ".rs": "Rust",
    ".c": "C",
    ".cs": "C#",
}

def get_language(filename: Path) -> str:
    return EXTENSION_TO_LANGUAGE.get(filename.suffix.lower(), filename.suffix.lower().lstrip(".") or "Unknown")

def format_problem_name(filename: Path) -> str:
    stem = filename.stem
    return stem.replace("-", " ")

def main():
    if not SOLUTIONS_DIR.exists():
        files = []
    else:
        files = sorted(
            [p for p in SOLUTIONS_DIR.iterdir() if p.is_file()],
            key=lambda p: p.name.lower()
        )

    total = len(files)
    language_counter = Counter(get_language(f) for f in files)
    updated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = []
    lines.append("# LeetCode Solutions")
    lines.append("")
    lines.append(f"**LeetCode ID:** `{LEETCODE_ID}`")
    lines.append("")
    lines.append(f"**Total solved:** {total}")
    lines.append("")
    lines.append("## Language Stats")
    lines.append("")

    if total == 0:
        lines.append("No solutions yet.")
    else:
        for language, count in sorted(language_counter.items()):
            lines.append(f"- {language}: {count}")

    lines.append("")
    lines.append("## Problem List")
    lines.append("")

    if total == 0:
        lines.append("No problems added yet.")
    else:
        for idx, f in enumerate(files, start=1):
            lines.append(f"{idx}. `{f.name}`")

    lines.append("")
    lines.append("---")
    lines.append(f"_Last updated: {updated_at}_")
    lines.append("")

    README_PATH.write_text("\n".join(lines), encoding="utf-8")

if __name__ == "__main__":
    main()
