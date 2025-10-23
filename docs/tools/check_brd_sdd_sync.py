#!/usr/bin/env python3
"""
BRD/SDD sync checker (Phase 2: front matter + flexible manifest + misplacement + anchors)
- Validates YAML front matter in each Markdown file under docs/brd/ and docs/sdd/
- Ensures doc_type, section_id, title exist and match folder
- Uses a flexible manifest (links/required/allowed_unpaired/ignore_patterns)
- Warns on "misplaced" content (design-ish in BRD; business-ish in SDD) with line numbers
- Verifies anchors:
    * H1 exists
    * H1 slug matches section_id suffix (e.g., 'brd.scope' → '# Scope' → 'scope')
    * OR an explicit anchor exists: '{#<section_id>}' or '<a id="<section_id">...'
    * Optional front matter 'canonical' path (warn if missing)
- Exit codes:
    0 = OK
    2 = Hard validation errors (front matter / required links)
    3 = Only misplacements (when --fail-on-misplacements is used)
    4 = Only anchor issues (when --fail-on-anchors is used)
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # repo root
DOCS = ROOT / "docs"
BRD_DIR = DOCS / "brd"
SDD_DIR = DOCS / "sdd"
MANIFEST = DOCS / "manifest" / "sections.json"

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*", re.DOTALL)
YAML_KV_RE = re.compile(r"^\s*([A-Za-z0-9_\-]+)\s*:\s*(.+?)\s*$", re.MULTILINE)

# --- Heuristic patterns -------------------------------------------------------
BRD_MISPLACED_PATTERNS = [
    r"\bsolution\s+architecture\b",
    r"\barchitecture\s+decision\b",
    r"\bcomponent\s+diagram\b",
    r"\bclass\s+diagram\b",
    r"\bsequence\s+diagram\b",
    r"\bmicroservice(s)?\b",
    r"\bkubernetes\b",
    r"\bhelm\b",
    r"\binfrastructure as code\b",
    r"\bterraform\b",
    r"\bcloudformation\b",
    r"\bapi (design|endpoint|contract)s?\b",
    r"\bdata\s+model\b",
    r"\bschema\b",
    r"\bimplementation\s+detail(s)?\b",
    r"\bnon[- ]functional requirement(s)?\b",
    r"\blatency\b",
    r"\bthroughput\b",
    r"\bavailability\b",
    r"\bobservability\b",
    r"\blogging\b",
    r"\btracing\b",
    r"\bdeployment\b",
    r"\brelease\s+plan\b",
    r"\brunbook\b",
]
SDD_MISPLACED_PATTERNS = [
    r"\bbusiness\s+goal(s)?\b",
    r"\bokrs?\b",
    r"\broi\b",
    r"\breturn on investment\b",
    r"\bsuccess\s+metric(s)?\b",
    r"\bnorth\s+star\b",
    r"\bmarket\b",
    r"\bpersona(s)?\b",
    r"\buser\s+story(ies)?\b",
    r"\bhigh[- ]level requirement(s)?\b",
    r"\bacceptance\s+criteria\b",
    r"\bout[- ]of[- ]scope\b",
    r"\bassumption(s)?\b",
    r"\bbusiness\s+context\b",
    r"\bstakeholder(s)?\b",
    r"\brisk(s)?\b",
]

# --- Helpers ------------------------------------------------------------------
def parse_front_matter(text: str) -> dict:
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return {}
    yaml_block = m.group(1)
    data = {}
    for key, val in YAML_KV_RE.findall(yaml_block):
        val = val.strip().strip('"').strip("'")
        data[key] = val
    return data

def strip_front_matter(text: str) -> str:
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return text
    return text[m.end():]

def _wildcard_match(pattern: str, value: str) -> bool:
    if pattern == value:
        return True
    if pattern.startswith("*") and pattern.endswith("*"):
        return pattern[1:-1] in value
    if pattern.startswith("*"):
        return value.endswith(pattern[1:])
    if pattern.endswith("*"):
        return value.startswith(pattern[:-1])
    return False

def load_manifest():
    if not MANIFEST.exists():
        return {"links": [], "allowed_unpaired": [], "ignore_patterns": []}
    with MANIFEST.open() as f:
        j = json.load(f)
    j.setdefault("links", [])
    j.setdefault("allowed_unpaired", [])
    j.setdefault("ignore_patterns", [])
    return j

def collect_files(base: Path):
    return sorted(base.glob("**/*.md"))

def normalize_expected_type(path: Path) -> str:
    if BRD_DIR in path.parents:
        return "BRD"
    if SDD_DIR in path.parents:
        return "SDD"
    return "UNKNOWN"

def slugify(s: str) -> str:
    s = s.strip().lower()
    s = s.replace("&", "and")
    s = re.sub(r"[^\w\s\.-]+", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-{2,}", "-", s)
    return s.strip("-._")

def find_misplacements(doc_type: str, body_text: str):
    results = []
    patterns = BRD_MISPLACED_PATTERNS if doc_type == "BRD" else SDD_MISPLACED_PATTERNS
    if not patterns:
        return results
    combined = re.compile("|".join(f"(?:{p})" for p in patterns), re.IGNORECASE)
    lines = body_text.splitlines()
    for i, line in enumerate(lines, start=1):
        m = combined.search(line)
        if m:
            snippet = line.strip()
            if len(snippet) > 140:
                snippet = snippet[:137] + "..."
            results.append((i, snippet, m.group(0)))
    return results

ANCHOR_INLINE_RE = re.compile(r"\{#([A-Za-z0-9_.\-]+)\}")
ANCHOR_HTML_RE = re.compile(r"<a\s+[^>]*id=['\"]([A-Za-z0-9_.\-]+)['\"][^>]*>", re.IGNORECASE)
H1_RE = re.compile(r"^\s*#\s+(.+?)\s*$", re.MULTILINE)

def check_anchors(doc_type: str, section_id: str, fm: dict, body_text: str):
    """
    Returns (warnings: list[str]) describing anchor/canonical issues.
    Rules:
      - If body contains '{#<section_id>}' or '<a id="<section_id>">', OK.
      - Else require an H1 whose slug matches the section_id suffix.
      - Optional FM key 'canonical' (warn if missing).
    """
    warnings = []

    # explicit anchor?
    if ANCHOR_INLINE_RE.search(body_text) or ANCHOR_HTML_RE.search(body_text):
        # Ensure at least one explicit anchor matches section_id
        explicit_ids = set(ANCHOR_INLINE_RE.findall(body_text)) | set(ANCHOR_HTML_RE.findall(body_text))
        if section_id not in explicit_ids:
            warnings.append(f"Anchor present but does not match section_id: expected '{{#{section_id}}}' or id='{section_id}'.")
    else:
        # No explicit anchor -> require H1 slug match
        m = H1_RE.search(body_text)
        if not m:
            warnings.append("Missing H1 heading.")
        else:
            h1 = m.group(1).strip()
            h1_slug = slugify(h1)
            expected_suffix = section_id.split(".", 1)[-1]
            if h1_slug != expected_suffix:
                warnings.append(f"H1 slug '{h1_slug}' doesn't match section_id suffix '{expected_suffix}'. (H1: '{h1}')")

    # Canonical path is optional but recommended
    if not fm.get("canonical"):
        warnings.append("Front matter missing 'canonical' path (recommended for cross-linking).")

    return warnings

# --- Main ---------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="BRD/SDD sync checker")
    parser.add_argument("--fail-on-misplacements", action="store_true",
                        help="Treat misplacement warnings as errors (exit 3 if only misplacements).")
    parser.add_argument("--fail-on-anchors", action="store_true",
                        help="Treat anchor warnings as errors (exit 4 if only anchor issues).")
    args = parser.parse_args()

    errors = []
    misplacements = []  # (path, lineno, excerpt, matched_phrase, doc_type)
    anchor_issues = []  # (path, warning)

    # Track seen section_ids
    seen = {"BRD": set(), "SDD": set()}
    file_by_section = {}

    # Scan files and validate front matter
    for base in (BRD_DIR, SDD_DIR):
        for md in collect_files(base):
            text = md.read_text(encoding="utf-8", errors="ignore")
            fm = parse_front_matter(text)
            if not fm:
                errors.append(f"{md}: Missing YAML front matter block.")
                continue

            expected_type = normalize_expected_type(md)
            doc_type = fm.get("doc_type", "").strip()
            section_id = fm.get("section_id", "").strip()
            title = fm.get("title", "").strip()

            if expected_type not in ("BRD", "SDD"):
                errors.append(f"{md}: File must be under docs/brd/ or docs/sdd/.")
            if doc_type not in ("BRD", "SDD"):
                errors.append(f"{md}: front matter doc_type must be 'BRD' or 'SDD' (found '{doc_type}').")
            if expected_type != doc_type:
                errors.append(f"{md}: doc_type '{doc_type}' does not match folder '{expected_type}'.")
            if not section_id:
                errors.append(f"{md}: Missing front matter 'section_id'.")
            if not title:
                errors.append(f"{md}: Missing front matter 'title'.")

            # Track sections
            if section_id:
                file_by_section[section_id] = md
                if doc_type in ("BRD", "SDD"):
                    seen[doc_type].add(section_id)

            # Body-only checks if doc_type recognized
            if doc_type in ("BRD", "SDD"):
                body = strip_front_matter(text)

                # Misplacements
                for lineno, excerpt, phrase in find_misplacements(doc_type, body):
                    misplacements.append((str(md), lineno, excerpt, phrase, doc_type))

                # Anchors
                for w in check_anchors(doc_type, section_id, fm, body):
                    anchor_issues.append((str(md), w))

    # === Manifest checks (soft expectations, no forced 1:1 pairs) ===
    manifest = load_manifest()
    links = manifest["links"]
    allowed_unpaired = set(manifest["allowed_unpaired"])
    ignore_patterns = manifest["ignore_patterns"]

    def is_ignored(sec_id: str) -> bool:
        return any(_wildcard_match(p, sec_id) for p in ignore_patterns)

    # Enforce only "required" counterparts defined in manifest.links[*].required
    brd_required_map = {}  # brd.section -> set(required sdd.section)
    for link in links:
        brd = link.get("from")
        req = set(link.get("required", []))
        if brd:
            brd_required_map.setdefault(brd, set()).update(req)

    for brd_sec, required_sdds in brd_required_map.items():
        if is_ignored(brd_sec):
            continue
        if brd_sec not in seen["BRD"]:
            continue  # advisory
        for sdd_sec in required_sdds:
            if is_ignored(sdd_sec):
                continue
            if sdd_sec not in seen["SDD"]:
                errors.append(
                    f"Missing required SDD counterpart for '{brd_sec}': '{sdd_sec}' (expected under docs/sdd/)."
                )

    # --- Output ----------------------------------------------------------------
    had_errors = bool(errors)
    had_misplacements = bool(misplacements)
    had_anchor_issues = bool(anchor_issues)

    if had_errors:
        print("\n=== BRD/SDD Sync Check: FAIL ===")
        for e in errors:
            print(f"- {e}")

    if had_misplacements:
        print("\n--- Potential misplacements (review) ---")
        for path, lineno, excerpt, phrase, doc_type in misplacements:
            hint = "Design/implementation language found in BRD" if doc_type == "BRD" else "Business/requirements language found in SDD"
            print(f"WARN: {path}:{lineno}: {hint}: matched '{phrase}'")
            print(f"      {excerpt}")

    if had_anchor_issues:
        print("\n--- Anchor/canonical warnings ---")
        for path, w in anchor_issues:
            print(f"WARN: {path}: {w}")

    if had_errors:
        print("\nSuggested next steps:")
        print("1) Ensure each file has valid front matter (doc_type, section_id, title).")
        print("2) Review docs/manifest/sections.json (links/required/allowed_unpaired/ignore_patterns) and adjust as needed.")
        sys.exit(2)

    if had_misplacements and args.fail_on_misplacements and not had_anchor_issues:
        sys.exit(3)

    if had_anchor_issues and args.fail_on_anchors and not had_misplacements:
        sys.exit(4)

    print("BRD/SDD sync check passed ✓")
    sys.exit(0)

if __name__ == "__main__":
    main()
