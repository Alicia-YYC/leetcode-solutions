from pathlib import Path

SOLUTIONS_DIR = Path("solutions")
README_PATH = Path("README.md")

def main():
    files = sorted(
        [p for p in SOLUTIONS_DIR.iterdir() if p.is_file()],
        key=lambda p: p.name
    )

    total = len(files)

    lines = []
    lines.append("# LeetCode Solutions\n")
    lines.append(f"\nTotal solved: **{total}**\n")
    lines.append("\n## Problem List\n")

    for f in files:
        lines.append(f"- `{f.name}`")

    README_PATH.write_text("\n".join(lines), encoding="utf-8")

if __name__ == "__main__":
    main()
