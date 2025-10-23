---
document: DECISIONS
project: Communications Hub
owner: Johnny Chang
status: Active
---

# Decision Registry (immutable once LOCKED)

> Rule: Do not edit a LOCKED decision. If reversed, create D###-R1 and mark the original as `SUPERSEDED_BY: D###-R1`.

---

## D001: HubSpot Tier Selection
**Decision:** HubSpot Professional + 2 additional shared inboxes (3 total)  
**Cost:** $650/month ($500 base + $150 for 2 inboxes)  
**Date locked:** 2025-10-23  
**Decided by:** Johnny Chang (IT)  
**Stakeholder approval:** Lauren (CEO) — 2025-10-23  
**Rationale:**
- Enterprise ($1,500/mo) exceeds monthly ceiling.
- One base inbox creates excessive manual routing; three supports role-based triage.
- Robin can absorb ~15 min/day triage; acceptable workaround vs. Enterprise.
- API/automation in Pro is sufficient for projected volumes.
**Alternatives considered:**
- Enterprise tier: rejected (cost).
- Single shared inbox on Pro: rejected (30+ min/day staff burden).
**Dependencies:** BRD §3.2; SDD §4.3; BRD §7.2 (Budget).  
**Revisit triggers:** If triage >30 min/day for 2 consecutive weeks; or budget ceiling increases ≥$500/mo.  
**Status:** LOCKED

---

## D002: Data Source of Truth
**Decision:** Airtable is the source of truth for client records; HubSpot is the communications layer.  
**Date locked:** 2025-10-23  
**Decided by:** Johnny Chang; validated by Robin (Ops)  
**Rationale:**
- Team proficiency + existing data in Airtable.
- Construction project tracking fits Airtable model better.
- Reduces conflict resolution complexity vs. bi-directional sync.
**Alternatives considered:**  
- HubSpot as SoT (rejected: weaker for construction PM);  
- Bi-directional sync (rejected: complexity/risk).  
**Dependencies:** BRD §2.1–§2.4; SDD §3.1; §6.2.  
**Revisit triggers:** If HubSpot releases project features meeting Airtable needs; or if sync lag causes >2 SLA breaches/week.  
**Status:** LOCKED

---

## D003: SMS Integration Approach
**Decision:** Twilio + Zapier for SMS (managed automation).  
**Cost:** ~$350/month (Twilio usage + Zapier Pro)  
**Date locked:** 2025-10-23  
**Decided by:** Johnny Chang; validated by Josh (Airtable/Zapier)  
**Rationale:**
- Native HubSpot SMS requires higher tier; out of budget.
- Zapier reduces maintenance vs. self-hosted n8n for this phase.
- Satisfies must-have “business number” requirement.
**Alternatives considered:**  
- HubSpot native SMS (rejected: tier/cost),  
- Twilio + self-hosted n8n (rejected: ongoing maintenance burden).  
**Dependencies:** BRD §3.4; SDD §5.1–§5.3; Budget §7.2.  
**Revisit triggers:** If Zapier cost/limits exceed plan for 2 consecutive months; or if n8n maintenance cost <2 hrs/month sustained.  
**Status:** LOCKED

---

## Decision Summary
| ID   | Title                       | Status  | Cost/mo | BRD refs | SDD refs |
|------|-----------------------------|---------|---------|----------|----------|
| D001 | HubSpot Tier Selection      | LOCKED  | $650    | §3.2     | §4.3     |
| D002 | Data Source of Truth        | LOCKED  | —       | §2.x     | §3.1, §6.2 |
| D003 | SMS Integration (Twilio/Zap)| LOCKED  | ~$350   | §3.4     | §5.1–§5.3 |

> To add a new decision: copy a block, assign next D###, fill all required fields, then link it in `_INDEX.md`.
