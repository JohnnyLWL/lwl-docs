import subprocess, datetime, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]  # repo root
DOCS = REPO / "docs"
CHANGELOG = DOCS / "CHANGELOG.md"

def git(*args):
    return subprocess.check_output(["git", *args], cwd=REPO, text=True).strip()

# Grab latest commit metadata
sha   = git("log", "-1", "--pretty=%h")
title = git("log", "-1", "--pretty=%s")
date  = git("log", "-1", "--pretty=%ad", "--date=short")
files = git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").splitlines()
files = [f for f in files if f.endswith(".md")] or files  # prefer doc files

# Build entry (compact + readable)
entry_lines = [
    f"### {date} — {title}  ({sha})",
    f"**Files:** {', '.join(files) if files else 'n/a'}",
    "",
]
entry = "\n".join(entry_lines)

# Insert the entry right after the first heading in CHANGELOG.md
text = CHANGELOG.read_text(encoding="utf-8")
lines = text.splitlines()

# Find first H1 heading line (starts with '# ')
idx = next((i for i, ln in enumerate(lines) if ln.startswith("# ")), 0)
insert_at = idx + 1  # place after the H1
new_text = "\n".join(lines[:insert_at] + ["", entry] + lines[insert_at:]) + ("\n" if not text.endswith("\n") else "")

CHANGELOG.write_text(new_text, encoding="utf-8")
print(f"CHANGELOG updated with: {title} ({sha})")
