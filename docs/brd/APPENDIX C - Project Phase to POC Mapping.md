---
doc_type: BRD
section_id: brd.appendix-c-project-phase-to-poc-mapping
title: Appendix C Project Phase To Poc Mapping
---
**APPENDIX C: PROJECT PHASE TO POC MAPPING**

**C.1 Purpose**

**This appendix defines the default Primary and Backup Point of Contact (POC) assignments for each project phase. These mappings serve as:**

1. **HubSpot workflow configuration specifications for automated POC assignment logic**
2. **Training reference for team members understanding routing logic**
3. **Maintenance documentation for when POC responsibilities change**

**C.2 Phase-to-POC Mapping Table**

| **Project Phase (Airtable)** | **Deal Stage (HubSpot)** | **Primary POC** | **Backup POC** | **Description** |
|------------------------------|-------------------------|----------------|---------------|-----------------|
| **PreDesign** | **PreDesign** | **Molly** | **Robin** | **Initial client consultation, project scoping, preliminary planning** |
| **Design** | **Design** | **Sara** | **Meghan** | **Active design development, client design selections, design documentation** |
| **Procurement** | **Procurement** | **Robin** | **Molly** | **Material sourcing, vendor coordination, product ordering** |
| **PreConstruction** | **PreConstruction** | **Brandie** | **Debra** | **Permit acquisition, construction scheduling, trade coordination** |
| **Construction** | **Construction** | **Debra** | **Brandie** | **Active construction work, on-site management, construction communications** |

**C.3 Automated Routing Logic**

**C.3.1 HubSpot POC Assignment Workflow**

**HubSpot workflow automation maintains POC assignments based on project phase using conditional branch logic:**

**WORKFLOW: "Assign POCs Based on Phase"**

**TRIGGERS:**

**- Deal is created**

**- Phase property is updated**

**ACTIONS:**

**IF Phase = "PreDesign" THEN**

**Set Primary POC = Molly**

**Set Backup POC = Robin**

**IF Phase = "Design" THEN**

**Set Primary POC = Sara**

**Set Backup POC = Meghan**

**IF Phase = "Procurement" THEN**

**Set Primary POC = Robin**

**Set Backup POC = Molly**

**IF Phase = "PreConstruction" THEN**

**Set Primary POC = Brandie**

**Set Backup POC = Debra**

**IF Phase = "Construction" THEN**

**Set Primary POC = Debra**

**Set Backup POC = Brandie**

**ELSE (unrecognized phase value)**

**Log error: "Unknown phase value received: [phase_value]"**

**Send alert to: LWL IT Lead**

**Leave POC fields blank (triggers monitoring report)**

**C.3.2 Vacation Flag Routing**

**When a new inbound communication arrives, HubSpot applies vacation flag logic:**

**WORKFLOW: "Route New Conversation"**

**TRIGGER:**

**- New conversation created**

**ACTIONS:**

**1. Identify project Deal associated with sender**

**2. Read Deal's Primary POC assignment**

**3. Check Primary POC's "Out of Office" property:**

**IF Primary POC "Out of Office" = TRUE THEN**

**Assign conversation to Backup POC**

**Send notification to Backup POC**

**Log: "Routed to Backup POC - Primary on vacation"**

**IF Primary POC "Out of Office" = FALSE THEN**

**Assign conversation to Primary POC**

**Send notification to Primary POC**

**Log: "Routed to Primary POC - standard routing"**

**4. Record routing decision in conversation timeline**

**C.3.3 Phase Transition Behavior**

**Automatic Phase-Based Routing:**

- **When a project's phase changes in Airtable, the Airtable automation triggers a webhook to Zapier**
- **Zapier updates the HubSpot Deal record's phase property**
- **HubSpot POC assignment workflow automatically triggers on "Phase property changed"**
- **Workflow reads new phase value and updates Primary/Backup POC assignments per table above**
- **NEW conversations created after the phase change automatically route to the new Primary POC (subject to vacation flag check)**
- **EXISTING conversations (active threads) retain their current POC assignment and are not automatically reassigned (per Section 3.3.7)**

**C.3.4 Manual Override**

**Administrators (CEO, Director of Operations, LWL IT Lead) may manually override POC assignments on individual Deal records for special circumstances:**

- **Extended leave requiring temporary POC reassignment**
- **VIP client requiring specific POC regardless of phase**
- **Training period for new team member**

**Manual override procedure:**

1. **Navigate to Deal record in HubSpot**
2. **Manually edit Primary POC and/or Backup POC properties**
3. **Manual assignment persists until manually reverted or until workflow updates POCs due to phase change**
4. **All manual overrides are logged in Deal timeline with administrator name and timestamp**

**C.4 Vacation Flag Management**

**C.4.1 Individual Responsibility**

**Each team member is responsible for managing their own "Out of Office" vacation flag:**

| **Event** | **Action Required** | **Timing** |
|-----------|---------------------|-----------|
| **Last working day before time off** | **Enable "Out of Office" flag in HubSpot** | **End of business day** |
| **First working day upon return** | **Disable "Out of Office" flag in HubSpot** | **Start of business day** |

**C.4.2 Administrator Oversight**

**Administrators can view and manage vacation flags for all users:**

- **Monthly monitoring dashboard shows all users with "Out of Office" enabled and duration**
- **Dashboard identifies flags enabled >5 consecutive days (catches forgotten flags)**
- **Administrators may manually disable flags if team member forgot upon return**

**C.4.3 Backup POC Awareness**

**When serving as Backup POC:**

- **Monitor shared inbox regularly (Backup POCs may receive routed messages at any time)**
- **Be aware of your paired Primary POC's vacation schedule through team coordination**
- **Respond to routed messages with same service standard as Primary POC**

**C.5 Phase Name Validation**

**CRITICAL: Airtable phase values must exactly match (case-sensitive) the phase names in the table above.**

**Validated Phase Names:**

- **PreDesign *(not "Pre-Design" or "pre-design")***
- **Design**
- **Procurement**
- **PreConstruction *(not "Pre-Construction" or "PreConst")***
- **Construction**

**Validation Process:**

- **Airtable Administrator (Josh) confirms exact spelling during Phase 1 Discovery**
- **Monthly Phase Name Validation Report identifies Deals with unrecognized phase values**
- **HubSpot workflow logs errors when unrecognized phase values are received**

**C.6 Cross-Phase Collaboration**

**C.6.1 Phase Transition Communications**

**When a project transitions between phases (e.g., Design → Procurement), best practices include:**

- **Outgoing Primary POC uses internal notes to brief incoming Primary POC on any open client issues or pending questions**
- **Use @mentions to notify incoming Primary POC**
- **Administrators may facilitate handoff communication if needed**

**C.6.2 Cross-Phase Questions**

**If a client in one phase asks a question related to a different phase:**

- **Option 1: Current Primary POC manually reassigns that specific conversation to the relevant POC**
- **Option 2: Current Primary POC collaborates using internal notes with @mentions (no reassignment needed)**

**Example: Client in Construction phase asks a design question**

- **Debra (Construction Primary) can reassign conversation to Sara (Design Primary)**
- **OR Debra can @mention Sara in internal note to get answer, then respond to client**

**C.7 Maintenance & Version Control**

**C.7.1 Review Schedule**

- **Frequency: Annually, or when organizational roles change**
- **Approval Authority: Director of Operations + Director of Construction**
- **Last Reviewed: *[Date to be added during Phase 1 Discovery]***
- **Current Version: 1.0**

**C.7.2 Update Procedure**

**When POC responsibilities change (new hires, role changes, departures):**

1. **Update Appendix C with new POC assignments**
2. **Update HubSpot workflow conditional branch logic within 1 business day**
   - **Test workflow changes in sandbox environment**
   - **Deploy to production**
   - **Verify with test phase change**
3. **Communicate change to all team members**
4. **Document in version history:**
   - **Date of change**
   - **What changed (which POC assignments)**
   - **Who approved the change**
   - **Who implemented the workflow update**

**C.7.3 Responsibility Matrix**

| **Task** | **Owner** | **Timeline** |
|----------|-----------|-------------|
| **Identify need for POC mapping change** | **LWL Executive Team** | **As needed** |
| **Approve new POC mappings** | **Director of Operations + Director of Construction** | **Within 2 business days** |
| **Update Appendix C documentation** | **LWL IT Lead** | **Same day as approval** |
| **Update HubSpot workflow logic** | **LWL IT Lead** | **Within 1 business day** |
| **Test workflow changes** | **LWL IT Lead** | **Before production deployment** |
| **Deploy to production** | **LWL IT Lead** | **Within 1 business day** |
| **Communicate to team** | **LWL Operations** | **Same day as deployment** |

**C.8 Pre-Sales Phase to POC Mapping (Phase 1.5)**

**Note: The following mappings will be finalized during Phase 1.5 Discovery in collaboration with Molly (Director of Operations) and Lauren (CEO).**

**Preliminary Pre-Sales Phase Mapping:**

| **Pre-Sales Phase (Airtable)** | **Deal Stage (HubSpot)** | **Primary POC** | **Backup POC** | **Description** |
|-------------------------------|-------------------------|----------------|---------------|-----------------|
| **Inquiry** | **Lead - New Inquiry** | **Molly** | **Lauren** | **Initial contact from prospective client** |
| **Initial Consultation** | **Lead - Consultation Scheduled** | **Molly** | **Lauren** | **First meeting scheduled or completed** |
| **Proposal Development** | **Lead - Proposal In Progress** | **Molly** | **Lauren** | **Preparing project proposal and estimate** |
| **Contract Negotiation** | **Lead - Contract Review** | **Molly** | **Lauren** | **Contract terms under discussion** |
| **Paid (Conversion)** | ***Transitions to VIP@ Inbox*** | ***Per Paid Project Phase Mapping*** | ***Per Paid Project Phase Mapping*** | **Lead converts to paid project, moves to VIP@ inbox** |

**C.8.1 Routing Logic for Pre-Sales**

- **New communications to welcome@livingwithlolo.com automatically route to the Primary POC for the lead's current pre-sales phase (subject to vacation flag check)**
- **Phase changes in Airtable trigger webhook to update HubSpot Deal record with new phase and corresponding POC assignments**
- **Active conversation threads retain their currently assigned POC (same persistence logic as paid projects per Section 3.3.7)**

**C.8.2 Conversion to Paid Project**

**When a lead's status changes to "Paid" in Airtable:**

- **Airtable automation triggers webhook indicating conversion**
- **Lead record transitions to paid project structure**
- **Future communications automatically route to VIP@livingwithlolo.com inbox**
- **welcome@livingwithlolo.com conversation history remains accessible for reference**
- **New VIP@ inbox conversation inherits complete communication context**
- **POC assignments update to match initial paid project phase (typically PreDesign: Molly/Robin)**

**C.8.3 Maintenance**

- **Review Frequency: Annually, or when pre-sales process changes**
- **Approval Authority: Director of Operations (Molly) + CEO (Lauren)**
- **Last Updated: *[Date to be added during Phase 1.5 Discovery]***