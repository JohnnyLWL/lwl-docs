---
document: INDEX
project: Communications Hub
owner: Johnny Chang
status: Active
---

# LWL Communications Hub — Master Index

## Document Inventory
- BRD.md — Business Requirements (authoritative business “what”)
- SDD.md — System Design (authoritative technical “how”)
- DECISIONS.md — Locked decisions (the “why”)
- GLOSSARY.md — Canonical terminology
- CHANGELOG.md — Audit trail of changes (drives commit messages)

## Capability Map (cross-references)

### Email Routing
- **BRD:** §3.2
- **SDD:** §4.3
- **DECISIONS:** D001
- **Glossary:** email routing, shared inbox, email triage
- **Status:** Requirements locked

### SMS Integration
- **BRD:** §3.4
- **SDD:** §5.1–§5.3
- **DECISIONS:** D003
- **Glossary:** SMS integration, programmable messaging
- **Status:** Requirements locked

## Document Dependencies
- Changing **D001 (HubSpot tier)** impacts BRD §3.2, SDD §4.3, Budget (§7.2).
- Changing **data source of truth** (D002) impacts BRD §2.x and SDD §3.1 & §6.2.

## Navigation Shortcuts
- Find *where something lives*: search here first, then jump to BRD/SDD.
- Find *why it’s that way*: check DECISIONS.md entry.
- Add/remove terms: update GLOSSARY.md, then re-run AI glossary checks.

## Validation Checkpoints
- Before editing sections, list impacted references from this file.
- After edits, record rationale and impacts in CHANGELOG.md (same day).

