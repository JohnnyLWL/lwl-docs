---
document: GLOSSARY
project: Communications Hub
owner: Johnny Chang
status: Active
---

# Canonical Glossary (enforced)

### client record
**Canonical term:** client record  
**Definition:** The complete set of information about a client stored in Airtable (source of truth), including contact info, project history, preferences, and assigned staff.  
**Used in:** BRD §2.1–§2.4; SDD §3.1; §6.2  
**Never use:** “customer record”, “customer data”, “contact information”, “client profile”.

### email routing
**Canonical term:** email routing  
**Definition:** Automated and/or manual process directing inbound emails to the correct staff/inbox. Current approach: role-based shared inboxes + manual triage by Robin.  
**Used in:** BRD §3.2; SDD §4.3  
**Never use:** “email forwarding”, “distribution list”, “assignment rules”.

### shared inbox
**Canonical term:** shared inbox  
**Definition:** HubSpot shared mailbox for a role (e.g., Sales, Support, Operations).  
**Used in:** BRD §3.2; SDD §4.3  
**Never use:** “group mailbox”, “alias inbox”, “DL”.

### source of truth
**Canonical term:** source of truth  
**Definition:** The authoritative system of record for a domain. For client data, Airtable is SoT; HubSpot mirrors for communications.  
**Used in:** BRD §2.x; SDD §3.1; §6.2  
**Never use:** “master file”, “golden copy” (ambiguous).

### vacation flag
**Canonical term:** vacation flag  
**Definition:** Operational indicator used to temporarily re-route communications when a staff member is unavailable.  
**Used in:** BRD §3.2; SDD §4.3; §5.x  
**Never use:** “OOO tag”, “out-of-office bit”, “holiday mode”.

> Enforcement tip: before commit, ask AI “scan changes for non-canonical terms per GLOSSARY.md”.
