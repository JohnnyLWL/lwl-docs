import sys
import re
from pathlib import Path

# --- Configuration ---
DOCS_DIR = Path(__file__).resolve().parents[1]  # one level up (docs/)
GLOSSARY_FILE = DOCS_DIR / "GLOSSARY.md"

# --- Extract canonical terms from GLOSSARY.md ---
with open(GLOSSARY_FILE, encoding="utf-8") as f:
    content = f.read()

canonical_terms = re.findall(r"\*\*Canonical term:\*\*\s*(.+)", content)
forbidden_terms = re.findall(r"\*\*Never use:\*\*\s*(.+)", content)

canonical_terms = [t.strip() for t in canonical_terms]
forbidden_terms = [w.strip() for w in " ".join(forbidden_terms).split(",")]

print(f"🧠 Loaded {len(canonical_terms)} canonical terms and {len(forbidden_terms)} forbidden terms")

# --- Scan all Markdown docs except glossary and changelog ---
files = [p for p in DOCS_DIR.rglob("*.md") if p.name not in ["GLOSSARY.md", "CHANGELOG.md"]]

violations = []

for file in files:
    text = file.read_text(encoding="utf-8")
    for bad in forbidden_terms:
        if re.search(rf"\b{re.escape(bad)}\b", text, re.IGNORECASE):
            violations.append((file.relative_to(DOCS_DIR), bad))

# --- Report ---
if not violations:
    print("✅ No glossary violations found!")
    print("\nDone.")
    sys.exit(0)
else:
    print(f"\n🚫 Found {len(violations)} potential violations:")
    for f, bad in violations:
        print(f"  • {f}: uses forbidden term '{bad}'")
    print("\nDone.")
    sys.exit(1)  # <- Non-zero exit code so CI fails

