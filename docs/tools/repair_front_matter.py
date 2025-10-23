#!/usr/bin/env python3
"""
Repairs YAML front matter for Markdown files in docs/brd/ and docs/sdd/:
- Adds missing front matter if absent.
- Fills in doc_type, section_id, and title if blank.
- Inferred from folder, heading, or filename.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
TARGETS = [DOCS / "brd", DOCS / "sdd"]

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL | re.MULTILINE)

def slugify(s: str) -> str:
    s = s.strip().lower()
    s = s.replace("&", "and")
    s = re.sub(r"[^\w\s\.-]+", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-{2,}", "-", s)
    return s.strip("-._")

def derive_title(text: str, fname: str) -> str:
    m = re.search(r"^\s*#\s+(.+?)\s*$", text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    name = Path(fname).stem
    name = re.sub(r"^\s*(brd|sdd)?\s*\d+(\.\d+)*\s*[-_]?\s*", "", name, flags=re.IGNORECASE)
    name = name.replace("_", " ").replace("-", " ")
    name = re.sub(r"\s+", " ", name).strip()
    return name.title() or "Untitled"

def parse_fm(block: str) -> dict:
    data = {}
    for line in block.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip().strip("'").strip('"')
    return data

def dump_fm(data: dict) -> str:
    out = ["---"]
    for k in ("doc_type", "section_id", "title"):
        if k in data:
            out.append(f"{k}: {data[k]}")
    out.append("---\n")
    return "\n".join(out)

def repair(md_path: Path):
    text = md_path.read_text(encoding="utf-8", errors="ignore")
    m = FRONT_MATTER_RE.match(text)
    has_fm = m is not None
    fm_data = parse_fm(m.group(1)) if has_fm else {}

    doc_type = "BRD" if "brd" in md_path.parts else "SDD"
    title = derive_title(text[m.end():] if has_fm else text, md_path.name)
    prefix = "brd" if doc_type == "BRD" else "sdd"
    section_id = f"{prefix}.{slugify(title).replace('.', '-')}"

    changed = False
    if not fm_data.get("doc_type"):
        fm_data["doc_type"] = doc_type
        changed = True
    if not fm_data.get("section_id"):
        fm_data["section_id"] = section_id
        changed = True
    if not fm_data.get("title"):
        fm_data["title"] = title
        changed = True

    if not has_fm:
        new_text = dump_fm(fm_data) + text
        md_path.write_text(new_text, encoding="utf-8")
        return True
    elif changed:
        new_text = dump_fm(fm_data) + text[m.end():]
        md_path.write_text(new_text, encoding="utf-8")
        return True
    return False

def main():
    updated = 0
    for base in TARGETS:
        if not base.exists():
            continue
        for md in base.glob("**/*.md"):
            if repair(md):
                print(f"Repaired: {md}")
                updated += 1
    print(f"\nUpdated {updated} file(s).")

if __name__ == "__main__":
    main()
