---
doc_type: SDD
section_id: sdd.implementation-roadmap-critical-path
title: Implementation Roadmap Critical Path
---
## 8.2 IMPLEMENTATION ROADMAP - CRITICAL PATH

### 8.2.1 Purpose of This Roadmap

This roadmap defines the mandatory sequence of implementation activities across Implementation 1, Phases 1-6 (Discovery through Stabilization). It identifies:

- **Blocking dependencies** - Activities that cannot begin until prerequisites complete

- **Parallel work streams** - Activities Josh and Johnny can execute simultaneously

- **Handoff moments** - Critical points where Josh provides deliverables to Johnny or vice versa

- **Go/No-Go decision gates** - Formal approval points required before proceeding to next phase

**Critical Success Factor:** Deviating from this sequence will cause implementation delays or integration failures. Josh and Johnny must coordinate timing of handoffs to maintain project momentum.

### 8.2.2 Phase 1 Discovery & Planning - Blocking Decisions

**Purpose:** Finalize all business requirements and technical prerequisites before any system configuration begins. Phase 2 Configuration CANNOT start until all items below receive written sign-off.

#### 8.2.2.1 Discovery Step 1: Project ID Naming Convention (BLOCKING for all Airtable and HubSpot work)

- **Owner:** Josh (proposes) → Johnny (validates) → CEO (approves)

- **Deliverable:** Written specification of Project ID format

- **Example formats for consideration:**

  - YYMM-ClientLastName-ShortAddress (e.g., "2410-Smith-Maple")

  - LWL-YYYY-### (e.g., "LWL-2024-047")

  - Airtable RECORD_ID() (e.g., "recABC123DEF456")

- **Acceptance Criteria:**

  - Format ensures uniqueness across all projects

  - Format is human-readable (preferred but not required)

  - Format contains no special characters that break HubSpot API calls

  - Johnny confirms HubSpot compatibility in writing

  - CEO approves final format via email

- **Handoff:** Josh emails final Project ID specification to Johnny and CEO for approval

- **Blocker Impact:** Without approved Project ID format, Josh cannot build Airtable Projects table; Zapier workflows cannot map Project IDs to HubSpot Deals

#### 8.2.2.2 Discovery Step 2: Phase-to-POC Mapping Validation (BLOCKING for HubSpot POC Assignment workflow)

- **Owner:** Johnny (validates with stakeholders) → Josh (implements in Airtable)

- **Deliverable:** Validated BRD Appendix C with stakeholder sign-off

- **Process:**

  1. Johnny reviews BRD Appendix C current mappings:

     - PreDesign: Molly (Primary) / Robin (Backup)

     - Design: Sara (Primary) / Meghan (Backup)

     - Procurement: Robin (Primary) / Molly (Backup)

     - PreConstruction: Brandie (Primary) / Debra (Backup)

     - Construction: Debra (Primary) / Brandie (Backup)

  2. Johnny validates with Robin (Director of Operations) that mappings reflect current team structure

  3. Johnny validates with Debra (Director of Construction) that mappings reflect current responsibilities

  4. Johnny obtains written approval (email acceptable) from both Directors

- **Critical Validation:** Airtable Administrator (Josh) confirms Airtable Phase field values match BRD Appendix C spelling EXACTLY (case-sensitive):

  - "PreDesign" (not "Pre-Design" or "pre-design")

  - "Design"

  - "Procurement"

  - "PreConstruction" (not "Pre-Construction")

  - "Construction"

- **Acceptance Criteria:**

  - Robin and Debra both provide written sign-off on phase-to-POC mappings

  - Josh confirms Airtable phase values match exactly (provides screenshot evidence)

  - Johnny documents any discrepancies requiring Airtable schema updates

- **Handoff:** Johnny provides validated Appendix C to Josh; Josh provides phase name validation screenshot to Johnny

- **Blocker Impact:** Without validated phase-to-POC mapping, Johnny cannot build HubSpot POC Assignment workflow; incorrect phase spelling causes complete POC assignment failure (BRD Risk T-12)

#### 8.2.2.3 Discovery Step 3: User Roster Finalization (BLOCKING for HubSpot and Airtable configuration)

- **Owner:** CEO (approves) → Johnny (documents) → Josh (implements)

- **Deliverable:** Complete list of all HubSpot users with role assignments

- **User List to Finalize:**

  1. Lauren Lerner - CEO - Administrator

  2. Johnny Chang - Director of Innovation & Technology - Administrator

  3. Robin Vaughn - Director of Operations - Standard User

  4. Brandie Roberts - Director of Construction - Standard User

  5. Sara Morgan - Lead Designer - Standard User

  6. Meghan Edmondo - Design Assistant - Standard User

  7. Molly Oestreich - Executive Assistant - Standard User

  8. Debra Solomon - Construction PM - Standard User

  9. Josh [Last Name] - Airtable Administrator - Administrator OR Standard User (TBD)

  10. [Name TBD] - Marketing Hub user for SMS - Standard User

- **Decision Required:** Josh's role in HubSpot (Administrator for integration troubleshooting OR Standard User for view-only access)

- **Acceptance Criteria:**

  - All 10 user names documented with email addresses

  - All role assignments (Administrator vs Standard User) finalized

  - CEO approves final user roster and seat allocation via email

- **Handoff:** Johnny provides final user roster to Josh for Airtable Users table population

- **Blocker Impact:** Without finalized user roster, Johnny cannot provision HubSpot user accounts; Josh cannot obtain HubSpot User IDs for POC assignment workflow

#### 8.2.2.4 Discovery Step 4: Airtable Schema Validation (BLOCKING for Phase 2 - BRD Section 1.6.3)

- **Owner:** Josh (validates/remediates) → Johnny (reviews) → Both sign off

- **Deliverable:** Confirmation that Airtable structure supports all communications hub requirements

- **Validation Checklist:**

☐ **Projects Table Exists and Contains Required Fields:**

- Project ID field (format TBD in Discovery Step 1)

- Project Status field with "Paid" value defined

- Phase field with all 5 phases enumerated (exact spelling per Discovery Step 2)

- Primary POC field (link to Users table)

- Backup POC field (link to Users table)

- Client Contacts field (link to Contacts table, multiple links allowed)

- Project Name field

☐ **Contacts Table Exists and Supports Multi-Contact Strategy:**

- Contact Name field

- Email 1, Email 2, Email 3 fields

- Phone 1, Phone 2, Phone 3, Phone 4 fields

- Associated Projects field (link to Projects table, multiple links allowed)

- Descriptive label fields for each email/phone

☐ **Users Table Exists or Can Be Created:**

- Full Name field

- Email field

- Role field

- HubSpot User ID field (Number type) - this will be populated in Phase 2

- Active field (Checkbox type)

☐ **Webhook Capability Confirmed:**

- Josh has Creator/Owner access level in Airtable (required for Automations)

- Josh successfully creates test automation in Airtable sandbox

- Josh successfully triggers test webhook to external URL

- Webhook payload structure validated (JSON format supported)

- **Remediation Process:** If any required fields missing or incorrectly configured, Josh updates Airtable schema before proceeding

- **Sample Data:** Josh provides Johnny with sample project record showing all fields populated (screenshot or Airtable share link)

- **Acceptance Criteria:**

  - All 4 validation checklist items complete

  - Johnny reviews sample project record and confirms all required data visible

  - Both Josh and Johnny sign off "Airtable Ready for Phase 2" via email

- **Handoff:** Josh provides schema validation report and sample data to Johnny; Johnny provides written approval

- **Blocker Impact:** Without validated Airtable schema, Zapier workflows cannot extract required data; webhook automations will fail; POC assignments cannot be synced

#### 8.2.2.5 Discovery Step 5: Project Master Info Template Development (BLOCKING for HubSpot Deal configuration)

- **Owner:** LWL Executive Team (defines) → Johnny (implements in HubSpot)

- **Deliverable:** Approved template structure for Project Master Info field

- **Process:**

  1. CEO, Robin, and Debra collaborate to define required information categories

  2. Proposed template structure includes:

     - PRIMARY CONTACTS: Decision maker, additional contacts, contact preferences

     - BUDGET & FINANCIAL: Budget range, payment terms, special considerations

     - COMMUNICATION PREFERENCES: Best contact times, preferred channel, response expectations

     - PROJECT CONSTRAINTS: Timeline constraints, access restrictions, special considerations

     - DESIGN & STYLE PREFERENCES: Design style notes, known likes/dislikes, reference projects

     - INTERNAL NOTES: Client personality, relationship history, red flags

  3. Executive Team approves template structure

- **Acceptance Criteria:**

  - Template structure document approved by CEO

  - Template includes all categories Executive Team requires

  - Template format compatible with HubSpot multi-line text field

- **Handoff:** CEO provides approved template document to Johnny

- **Blocker Impact:** Without approved template, Johnny cannot configure Project Master Info field with correct structure; team training in Phase 5 lacks standardized format

#### 8.2.2.6 Discovery Step 6: Integration Architecture Proposal (BLOCKING for Phase 2 - BRD Section 1.6.3.4)

- **Owner:** Josh (proposes) → Johnny (reviews) → Both approve

- **Deliverable:** Written integration architecture proposal documenting approach for Airtable-Zapier-HubSpot synchronization

- **Proposal Must Document:**

  - Webhook trigger configuration in Airtable (which field changes trigger webhooks)

  - Zapier workflow structure (event-driven + weekly baseline sync approach)

  - Error handling strategy (3 retries + log to Sync Errors table)

  - Notification strategy (who gets alerted on failures)

  - Monitoring procedures (initial intensive monitoring, then routine maintenance)

  - Maintenance procedures (who owns what ongoing)

  - Technical constraints or limitations (Zapier task limits, API rate limits)

  - Proposed approach for integration build/test during Phase 2-3

- **Acceptance Criteria:**

  - Josh provides written proposal document

  - Johnny reviews proposal and provides written feedback

  - Both agree on approach before Phase 2 begins

  - Any technical concerns or risks documented and mitigation planned

- **Handoff:** Josh emails proposal to Johnny; Johnny provides review comments; both sign off final approach

- **Blocker Impact:** Without agreed integration architecture, Josh and Johnny may build incompatible configurations; rework required during Phase 3 testing

#### 8.2.2.7 Discovery Step 7: Webhook Proof-of-Concept (RECOMMENDED but not blocking - BRD Section 1.6.3.3)

- **Owner:** Josh (builds and demonstrates)

- **Deliverable:** Screen recording of successful test webhook with payload visible

- **Process:**

  1. Josh builds test webhook automation in Airtable sandbox environment (not production)

  2. Josh configures webhook to POST to test Zapier catch hook (free tier acceptable for testing)

  3. Josh triggers webhook manually

  4. Josh captures screen recording showing:

     - Airtable automation executing successfully

     - Webhook POST action completing

     - Zapier catch hook receiving webhook

     - JSON payload structure visible in Zapier

  5. Josh validates authentication works and error handling catches failures

- **Acceptance Criteria:**

  - Screen recording demonstrates successful webhook delivery

  - JSON payload structure clearly visible

  - Josh confirms understanding of webhook configuration process

- **Blocker Impact:** Not blocking (can be completed during Phase 2 if needed), but significantly reduces Phase 2-3 risk by validating webhook approach early

**Phase 1 Go/No-Go Decision Gate**

**Decision Maker:** CEO (final authority) with input from Johnny and Josh

**Go Criteria - ALL must be complete:**

- [ ] Discovery Step 1: Project ID naming convention approved in writing by CEO

- [ ] Discovery Step 2: Phase-to-POC mapping validated by Robin and Debra; phase names in Airtable confirmed exact match

- [ ] Discovery Step 3: User roster finalized and approved by CEO

- [ ] Discovery Step 4: Airtable schema validated by Josh; reviewed and approved by Johnny

- [ ] Discovery Step 5: Project Master Info template approved by CEO

- [ ] Discovery Step 6: Integration architecture proposal agreed by Josh and Johnny

**No-Go Criteria - ANY of these triggers delay:**

- Project ID naming convention not finalized (cannot proceed to Phase 2 configuration per BRD 3.8.4.5)

- Phase name spelling mismatch between Airtable and BRD Appendix C (Risk T-12 - will cause POC assignment failure)

- Airtable schema gaps requiring remediation not yet complete

- Integration architecture disagreement between Josh and Johnny unresolved

**Decision Documentation:** CEO sends "Phase 2 Authorization" email to Johnny and Josh confirming all Go Criteria met

### 8.2.3 Phase 2 System Configuration & Setup - Build Order Sequence

**Purpose:** Configure HubSpot account, build Airtable data model, establish Zapier integration foundation. Josh and Johnny work in parallel once prerequisites complete, then coordinate for handoffs.

#### 8.2.3.1 Configuration Group A: Foundation Layer (Johnny's Prerequisites for Josh)

**CRITICAL:** Josh cannot begin Airtable or Zapier configuration until Johnny completes all Configuration Group A activities and provides required information.

8.2.3.1.1 **Configuration Step A1: HubSpot Account Foundation Setup**

- **Owner:** Johnny

- **Activities:**

  - Configure account timezone: America/Phoenix (UTC-7 year-round)

  - Enable MFA enforcement: Settings > Security > Require two-factor authentication for all users

  - Verify livingwithlolo.com domain: Add TXT record to Google Workspace DNS

  - Configure business hours: Monday-Friday 8:00 AM - 5:00 PM Arizona Time

  - Create holiday calendar: Manually enter 8-10 US holiday dates for 2026 as workflow exclusion dates

  - Set annual calendar reminder: November 15 to update holiday dates for following year

- **Deliverable:** Account foundation settings configured

- **Completion Indicator:** Johnny notifies Josh "HubSpot account foundation complete"

8.2.3.1.2 **Configuration Step A2: Create HubSpot Private App for Zapier**

- **Owner:** Johnny

- **Activities:**

  1. Navigate to HubSpot Settings > Integrations > Private Apps

  2. Click "Create a private app"

  3. App Name: "Zapier Integration - Communications Hub"

  4. Description: "Middleware integration for Airtable-to-HubSpot synchronization"

  5. Configure scopes (click "Scopes" tab):

     - crm.objects.deals.read

     - crm.objects.deals.write

     - crm.objects.contacts.read

     - crm.objects.contacts.write

     - crm.schemas.deals.read

     - crm.schemas.contacts.read

     - timeline (for creating notes/engagements)

  6. Click "Create app"

  7. Copy Private App API Key (appears once - store securely)

  8. **HANDOFF:** Email API key to Josh with subject "HubSpot Private App API Key for Zapier"

  9. Store API key in LWL password manager for backup

- **Deliverable:** HubSpot Private App API Key provided to Josh

- **Security Note:** Treat API key as highly sensitive credential; never share via unsecured channels

- **Handoff Confirmation:** Josh replies to email confirming API key received

8.2.3.1.3 **Configuration Step A3: Obtain HubSpot User IDs for POC Assignment**

- **Owner:** Johnny

- **Activities:**

  1. Navigate to HubSpot Settings > Users & Teams

  2. For each user in finalized roster (Discovery Step 3), click user name

  3. Note User ID from browser URL (format: .../settings/users/USER_ID)

  4. Create mapping document (Excel or Google Sheet):

| **Full Name** | **Email** | **HubSpot User ID** |
| --- | --- | --- |
| Molly Oestreich | molly@livingwithlolo.com | 12345678 |
| Robin Vaughn | robin@livingwithlolo.com | 23456789 |
| (Continue for all 10 users) | | |

  5. **HANDOFF:** Email mapping document to Josh with subject "HubSpot User ID Mapping for Airtable"

- **Deliverable:** HubSpot User ID mapping document provided to Josh

- **Purpose:** Josh enters these IDs into Airtable Users table; POC Assignment workflow uses numeric IDs (not email addresses) to assign conversations

- **Handoff Confirmation:** Josh replies to email confirming mapping document received and User IDs entered in Airtable

8.2.3.1.4 **Configuration Step A4: Gmail Integration Setup**

- **Owner:** Johnny

- **Activities:**

  1. **VIP@livingwithlolo.com OAuth Connection:**

     - Navigate to HubSpot Settings > Inbox > Email

     - Click "Connect personal email"

     - Select "Gmail"

     - Sign in as VIP@livingwithlolo.com

     - Review permissions (read, send, manage email)

     - Click "Allow"

     - Select "LWL Client Communications" inbox

     - Configure sync settings: Real-time, automatic threading, historical sync last 30 days

     - Test: Send email to VIP@, verify appears in HubSpot Conversations within 5 minutes

  2. **welcome@livingwithlolo.com OAuth Connection:**

     - Repeat above process for welcome@livingwithlolo.com

     - Select same "LWL Client Communications" inbox (or create separate "welcome@ Inbox" if preferred)

     - Test: Send email to welcome@, verify appears in HubSpot Conversations

  3. **info@livingwithlolo.com OAuth Connection:**

     - Repeat above process for info@livingwithlolo.com

     - Select "LWL Client Communications" inbox

     - Test: Send email to info@, verify appears in HubSpot Conversations

  4. **family@livingwithlolo.com OAuth Connection:**

     - Repeat above process for family@livingwithlolo.com

     - Select "LWL Client Communications" inbox

     - Test: Send email to family@, verify appears in HubSpot Conversations

  5. Configure email signatures for both inboxes (use personalization tokens for POC name/title)

- **Deliverable:** All four Gmail inboxes connected and tested

- **Notification to Josh:** Email Josh "Gmail integration complete - all four inboxes ready for email routing"

**Configuration Group A Completion Checkpoint:**

**Johnny → Josh Handoff Summary:**

- [ ] HubSpot Private App API Key provided to Josh (Step A2)

- [ ] HubSpot User ID mapping document provided to Josh (Step A3)

- [ ] Gmail integration complete notification sent to Josh (Step A4)

**Josh Can Now Begin:** Configuration Group B activities (Airtable data model build)

#### 8.2.3.2 Configuration Group B: Data Layer (Josh's Foundation)

**PREREQUISITE:** Configuration Group A complete (Johnny provided API key and User ID mapping)

8.2.3.2.1 **Configuration Step B1: Create Airtable Tables and Fields**

- **Owner:** Josh

- **Activities:**

**Create Projects Table:**

1. New table: "Projects"

2. Add fields in this order:

   - Project ID (Single line text, Required)

   - Project Name (Single line text, Required)

   - Project Status (Single select, Required) - Options: Lead, Proposal, Paid, Active, Completed, Cancelled

   - Phase (Single select, Required if Status=Paid/Active) - Options: PreDesign, Design, Procurement, PreConstruction, Construction (EXACT spelling per Discovery Step 2)

   - Primary POC (Link to Users table, single link, Required if Status=Paid/Active)

   - Backup POC (Link to Users table, single link, Required if Status=Paid/Active)

   - Client Contacts (Link to Contacts table, multiple links allowed, Required)

   - Airtable Record ID (Formula: RECORD_ID(), auto-generated)

   - Last Modified (Last modified time, auto-generated)

   - Last HubSpot Sync (Date, optional - updated by Zapier Weekly Baseline Sync)

**Create Contacts Table:**

1. New table: "Contacts"

2. Add fields:

   - Contact Name (Single line text, Required)

   - Email 1 (Email, optional - but need at least one email OR one phone)

   - Email 1 Label (Single line text, optional)

   - Email 2, Email 2 Label (same as above)

   - Email 3, Email 3 Label (same as above)

   - Phone 1 (Phone number, optional)

   - Phone 1 Label (Single line text, optional)

   - Phone 2, Phone 2 Label, Phone 3, Phone 3 Label, Phone 4, Phone 4 Label (same pattern)

   - Contact Role (Single select, optional) - Options: Primary Client, Spouse/Partner, Family Member, Assistant, Other

   - Associated Projects (Link to Projects table, multiple links allowed, Required)

   - Preferred Contact Method (Single select, optional) - Options: Email, SMS, Phone, No Preference

   - Airtable Contact ID (Formula: RECORD_ID(), auto-generated)

**Create Users Table:**

1. New table: "Users"

2. Add fields:

   - Full Name (Single line text, Required)

   - Email (Email, Required)

   - Role (Single select, Required) - Options: CEO, Director, Designer, PM, Admin, etc.

   - HubSpot User ID (Number, Required) - Josh will populate from Johnny's mapping document

   - HubSpot Email (Email, Required) - Usually same as Email field

   - Active (Checkbox, Required) - Default checked

**Create Sync Errors Table:**

1. New table: "Sync Errors"

2. Add fields:

   - Error Timestamp (Date & time, auto-generated by automation)

   - Project ID (Single line text, Required)

   - Error Type (Single select, Required) - Options: Webhook Failed, Invalid Data, HubSpot API Error, Unknown

   - Error Message (Long text, Required)

   - Retry Count (Number, auto-generated by automation)

   - Resolved (Checkbox, optional)

   - Resolution Notes (Long text, optional)

- **Deliverable:** All 4 tables created with complete field structure

8.2.3.2.2 **Configuration Step B2: Populate Airtable Users Table with HubSpot User IDs**

- **Owner:** Josh

- **PREREQUISITE:** Johnny provided HubSpot User ID mapping document (Configuration Step A3)

- **Activities:**

  1. Open HubSpot User ID mapping document from Johnny

  2. Create record in Airtable Users table for each team member

  3. Copy HubSpot User ID from mapping document → paste into HubSpot User ID field

  4. Verify all 10 users entered correctly

  5. Check Active checkbox for all current employees

  6. **Validation:** Take screenshot showing all users with populated HubSpot User IDs

  7. **HANDOFF:** Email screenshot to Johnny with subject "HubSpot User IDs entered in Airtable - Validation Requested"

- **Deliverable:** Users table populated and validated

- **Handoff Confirmation:** Johnny reviews screenshot, confirms User IDs match his source document, replies "Validated - proceed to Zapier setup"

8.2.3.2.3 **Configuration Step B3: Configure Data Validation and Create Sample Projects**

- **Owner:** Josh

- **Activities:**

**Data Validation Setup:**

1. Configure field validation rules:

   - Project ID: Set as unique field (Airtable prevents duplicates)

   - Phase: Conditional formatting - red background if empty when Status=Paid/Active

   - Backup POC: Conditional formatting - yellow background if equals Primary POC

2. Create view: "Incomplete Contacts" - Filter: Contact Name is empty OR (all Emails empty AND all Phones empty) OR Associated Projects is empty

3. Create view: "POC Validation Warnings" - Shows projects where Backup POC = Primary POC

**Sample Data Entry:**

1. Create 3 sample projects in Projects table:

   - Sample Project 1: Status=Paid, Phase=PreDesign, Primary POC=Molly, Backup POC=Robin, 2 linked Contacts

   - Sample Project 2: Status=Paid, Phase=Design, Primary POC=Sara, Backup POC=Meghan, 3 linked Contacts (test multi-contact scenario)

   - Sample Project 3: Status=Active, Phase=Construction, Primary POC=Debra, Backup POC=Brandie, 1 linked Contact

2. Create 6 sample contacts (2 contacts for Project 1, 3 for Project 2, 1 for Project 3):

   - Include variety: some with 3 emails, some with 4 phones, test label fields

   - Link each Contact to appropriate Project(s)

3. Validate sample data:

   - All Phase values match BRD Appendix C exactly (PreDesign, not Pre-Design)

   - All Primary/Backup POC links resolve correctly to Users table

   - All Contact-to-Project links bidirectional (visible from both tables)

- **Deliverable:** Data validation configured, sample projects created

- **Notification to Johnny:** Email Johnny "Airtable data model complete with sample data - ready for next integration setup step"

**Configuration Group B Completion Checkpoint:**

**Josh's Deliverables:**

- [ ] All 4 Airtable tables created with complete field structure (Step B1)

- [ ] HubSpot User IDs entered in Users table and validated by Johnny (Step B2)

- [ ] Data validation configured and sample projects created (Step B3)

**Johnny Can Now Begin:** Configuration Group C (HubSpot workflow configuration)

#### 8.2.3.3 Configuration Group C: Automation Layer Part 1 (Josh → Johnny → Josh)

**Purpose:** Establish Zapier webhook foundation, build HubSpot workflows, prepare for Airtable automation build

##### 8.2.3.3.1 Configuration Step C1: Josh Sets Up Zapier Account and Creates Catch Hook Webhooks

- **Owner:** Josh

- **PREREQUISITE:** Configuration Step A2 complete (Johnny provided HubSpot Private App API Key)

- **Activities:**

**Zapier Account Setup:**

1. Create Zapier account (if not exists): zapier.com/sign-up

2. Subscribe to Starter tier (minimum $19.99/month as of October 2025)

3. Create workspace: "Living With Lolo - Communications Hub"

4. Create folder structure:

   - /Production Workflows

   - /Testing Workflows

**Connect Airtable to Zapier:**

1. Zapier Settings > Connected Accounts > Add Connection > Airtable

2. Josh generates Personal Access Token in Airtable Account Settings

3. Scopes required: data.records:read, data.records:write, schema.bases:read

4. Copy token, paste into Zapier connection

5. Test connection: Run sample "Find Records" action, verify connection works

**Connect HubSpot to Zapier:**

1. Zapier Settings > Connected Accounts > Add Connection > HubSpot

2. Select "Private App" authentication method

3. Paste HubSpot Private App API Key provided by Johnny (Configuration Step A2)

4. Test connection: Run sample "Find Deal" action, verify connection works

**Create Catch Hook Webhooks (2 webhooks required):**

**Webhook 1: New Paid Project Trigger**

1. Create new Zap in /Testing Workflows folder

2. Name: "TEST - New Paid Project Sync"

3. Trigger: Webhooks by Zapier > Catch Hook

4. Click "Continue" - Zapier generates custom webhook URL

5. **CRITICAL:** Copy webhook URL (format: https://hooks.zapier.com/hooks/catch/123456/abcdef/)

6. Store webhook URL securely - Josh will use this in Airtable automation

**Webhook 2: Phase Change Trigger**

1. Create second new Zap in /Testing Workflows folder

2. Name: "TEST - Phase Change Sync"

3. Trigger: Webhooks by Zapier > Catch Hook

4. Click "Continue" - Zapier generates DIFFERENT webhook URL

5. Copy this second webhook URL

6. Store securely

**HANDOFF:**

1. Create document listing both webhook URLs:

   - Webhook 1 (New Paid Project): https://hooks.zapier.com/hooks/catch/[URL_1]

   - Webhook 2 (Phase Change): https://hooks.zapier.com/hooks/catch/[URL_2]

2. **Email to Johnny with subject:** "Zapier Webhook URLs for HubSpot Integration"

3. **Email body:** "Johnny - these are the two Zapier webhook URLs for the Airtable-to-HubSpot integration. Please store these securely. I will use these URLs in Airtable webhook automations in Configuration Group D. These URLs are sensitive credentials - treat as confidential."

- **Deliverable:** Zapier account configured, 2 webhook URLs created and provided to Johnny

- **Security Note:** Webhook URLs contain secret hashes; anyone with URL can send fake payloads to Zapier

- **Handoff Confirmation:** Johnny replies to email confirming webhook URLs received and stored securely

##### 8.2.3.3.2 Configuration Step C2: Johnny Builds HubSpot Workflows

- **Owner:** Johnny

- **PREREQUISITE:** Configuration Group B complete (Josh populated Airtable with sample data and User IDs)

- **Activities:**

**Foundation Workflows:**

**Workflow 1: POC Assignment Based on Phase**

1. Navigate to HubSpot Automation > Workflows > Create workflow > Deal-based

2. Name: "POC Assignment Based on Phase"

3. Enrollment trigger: Deal is created OR Property "Project Phase" changes

4. Actions (build 5-way branch):

   - IF Project_Phase = "PreDesign" THEN:

     - Set property "Primary POC" = Molly (use HubSpot User ID from mapping document)

     - Set property "Backup POC" = Robin (use HubSpot User ID)

     - Set property "Deal Owner" = Molly (use HubSpot User ID)

   - IF Project_Phase = "Design" THEN:

     - Set Primary POC = Sara, Backup POC = Meghan, Deal Owner = Sara

   - IF Project_Phase = "Procurement" THEN:

     - Set Primary POC = Robin, Backup POC = Molly, Deal Owner = Robin

   - IF Project_Phase = "PreConstruction" THEN:

     - Set Primary POC = Brandie, Backup POC = Debra, Deal Owner = Brandie

   - IF Project_Phase = "Construction" THEN:

     - Set Primary POC = Debra, Backup POC = Brandie, Deal Owner = Debra

   - ELSE (unrecognized phase):

     - Create internal note: "ERROR: Unknown phase value [phase_value]. POC assignment failed."

     - Send email to Johnny: "POC Assignment workflow error - Deal ID [deal_id]"

5. Add action (all branches): Create timeline note documenting POC assignments

6. Re-enrollment: YES (allow re-enrollment when phase changes)

7. Save workflow (do not activate yet - will test in Phase 3)

**Workflow 2: Deal Stage Update from Phase Change**

1. Create workflow: Deal-based

2. Name: "Deal Stage Update from Phase Change"

3. Enrollment trigger: Property "Project Phase" changes

4. Filter: Project Phase is known (not empty)

5. Actions (build 5-way branch mapping phase to stage):

   - IF Project_Phase = "PreDesign" THEN Update Deal Stage = "PreDesign"

   - IF Project_Phase = "Design" THEN Update Deal Stage = "Design"

   - (Continue for all 5 phases)

6. Add action: Create timeline note documenting stage change

7. Re-enrollment: YES

8. Save workflow (do not activate yet)

**Routing Workflows:**

**Workflow 3: Conversation Assignment Routing**

1. Create workflow: Conversation-based

2. Name: "Conversation Assignment Routing"

3. Enrollment trigger: Conversation is created

4. Actions (dual inbox branch):

   - Branch 1: IF Inbox = "VIP@livingwithlolo.com"

     - IF Associated Deal exists:

       - CHECK Primary POC "Out of Office" flag:

         - IF Out_of_Office = TRUE: Assign to Backup POC, send notification

         - ELSE: Assign to Primary POC, send notification

     - ELSE (no Deal): Route to Unassigned, create note "No Deal association"

   - Branch 2: IF Inbox = "welcome@livingwithlolo.com"

     - CHECK Molly "Out of Office" flag:

       - IF TRUE: Assign to Lauren, send notification

       - ELSE: Assign to Molly, send notification

5. Re-enrollment: NO (conversations assigned once)

6. Save workflow (do not activate yet)

**Workflow 4: Business Hours Auto-Reply - Email**

1. Create workflow: Conversation-based

2. Name: "Business Hours Auto-Reply - Email"

3. Enrollment trigger: Conversation is created

4. Filters:

   - Channel = Email

   - Direction = Inbound

   - Current time is OUTSIDE business hours (Mon-Fri 8AM-5PM AZ)

5. Add exclusion list: 2026 holiday dates (Jan 1, May 25, Jul 4, Sep 7, Nov 26, Nov 27, Dec 24, Dec 25)

6. Action: Send email with "Thank you for contacting LWL" message

7. Action: Create internal note "Auto-reply sent"

8. Re-enrollment: NO

9. Save workflow (do not activate yet)

**Workflow 5: Business Hours Auto-Reply - SMS**

1. Duplicate Workflow 4

2. Name: "Business Hours Auto-Reply - SMS"

3. Change filter: Channel = SMS

4. Change action: Send SMS instead of email

5. Save workflow (do not activate yet)

**Monitoring Workflows:**

**Workflow 6: Weekly POC Assignment Health Check**

1. Create workflow: Deal-based

2. Name: "Weekly POC Assignment Health Check"

3. Enrollment trigger: Schedule - Every Monday at 8:00 AM Arizona Time

4. Filter: Find all Deals where Deal Stage IN (PreDesign, Design, Procurement, PreConstruction, Construction)

5. Filter: Primary POC is empty OR Backup POC is empty

6. IF any Deals found:

   - Send email to Johnny and Lauren: "POC Assignment failures detected - [list Deal IDs]"

7. ELSE: Log success silently

8. Save workflow (do not activate yet)

**Workflow 7: Monthly Phase Name Validation**

1. Create workflow: Deal-based

2. Name: "Monthly Phase Name Validation"

3. Enrollment trigger: Schedule - 1st day of month at 9:00 AM Arizona Time

4. Filter: Find all Deals where Project_Phase is not empty

5. Filter: Project_Phase NOT IN (PreDesign, Design, Procurement, PreConstruction, Construction)

6. IF any Deals found:

   - Send email to Johnny and Josh: "Invalid phase values detected - [list Deal IDs with phase values]"

7. ELSE: Log success silently

8. Save workflow (do not activate yet)

**HANDOFF:**

- **Email to Josh with subject:** "HubSpot workflows complete - ready for Phase 3 testing"

- **Email body:** "Josh - all 7 HubSpot workflows are built and saved (not activated yet). We can test end-to-end integration once you build Airtable automations and Zapier workflows. Workflows are ready to receive Deal creation and Phase updates from Zapier."

- **Deliverable:** 7 HubSpot workflows built (not activated - will activate during Phase 3 testing)

- **Handoff Confirmation:** Josh replies confirming ready to build Airtable automations next

**Configuration Group C Completion Checkpoint:**

**Josh → Johnny Handoff Complete:**

- [ ] Zapier webhook URLs provided to Johnny (Step C1)

**Johnny → Josh Handoff Complete:**

- [ ] HubSpot workflows complete notification sent to Josh (Step C2)

**Josh Can Now Begin:** Configuration Group D activities (build Airtable automations and Zapier workflows using webhook URLs and completed HubSpot workflows)

#### 8.2.3.3 Configuration Group C: Automation Layer Part 1 (Josh → Johnny → Josh)

##### 8.2.3.3.1 Configuration Step C1: Josh Sets Up Zapier Account and Creates Catch Hook Webhooks

##### 8.2.3.3.2 Configuration Step C2: Johnny Builds HubSpot Workflows

##### 8.2.3.3.3 Configuration Step C3: Configure info@ Inbox (NEW - Johnny)

##### 8.2.3.3.4 Configuration Step C4: Configure family@ Inbox (NEW - Johnny)

##### 8.2.3.3.5 Configuration Step C5: Configure Salesmsg Urgent Hotline (NEW - Johnny)

##### 8.2.3.3.6 Configuration Step C6: Configure Slack Integration - #urgent-alerts (NEW - Johnny)

##### 8.2.3.3.7 Configuration Step C7: Configure Slack Integration - #client-inboxes (NEW - Johnny)

##### 8.2.3.3.8 Configuration Step C8: Configure Email Signature Enforcement (NEW - Johnny)

**Configuration Group C Completion Checkpoint (UPDATED):** Johnny must complete C1-C8 before Josh begins Configuration Group D.

#### 8.2.3.4 Configuration Group D: Automation Layer Part 2 (Josh Completes Integration)

**PREREQUISITE:** Configuration Group C complete (Josh provided Zapier webhook URLs to Johnny; Johnny completed HubSpot workflows)

8.2.3.4.1 **Configuration Step D1: Josh Builds Airtable Webhook Automations**

- **Owner:** Josh

- **Activities:**

**Automation 1: HubSpot Sync - New Paid Project**

1. Navigate to Airtable Projects table > Automations > Create automation

2. Name: "HubSpot Sync - New Paid Project"

3. Trigger: When record matches conditions

   - Table: Projects

   - Conditions: Status changes to "Paid" AND Project ID is not empty

4. Action 1: Find records

   - Search in: Contacts table

   - Where: Associated Projects contains [Trigger record Project ID]

   - Result: List of all Contact records linked to this project

5. Action 2: Webhook POST

   - URL: [Paste Webhook 1 URL from Configuration Step C1]

   - Method: POST

   - Headers: Content-Type: application/json

   - Body: Build JSON payload (see Section 8.3.5 for complete payload structure - includes project metadata + nested contacts array)

6. Error handling: Configure retry (up to 3 attempts, 1-minute delay)

7. After 3 failures: Create record in Sync Errors table with error details

8. Test automation:

   - Change sample project Status to "Paid"

   - Verify webhook fires in Zapier webhook history

   - Verify payload structure correct

9. Set automation to inactive (will activate during Phase 3 testing)

**Automation 2: HubSpot Sync - Phase Change**

1. Create automation: "HubSpot Sync - Phase Change"

2. Trigger: When record matches conditions

   - Table: Projects

   - Conditions: Phase changes AND Status IN (Paid, Active) AND Project ID is not empty

3. Action: Webhook POST

   - URL: [Paste Webhook 2 URL from Configuration Step C1 - DIFFERENT URL than Automation 1]

   - Method: POST

   - Body: Build JSON payload (simpler than Automation 1 - just Project ID, new phase, POC info, timestamp)

4. Error handling: Same as Automation 1 (3 retries + log to Sync Errors)

5. Test automation:

   - Change sample project Phase from "PreDesign" to "Design"

   - Verify webhook fires in Zapier

6. Set automation to inactive

**Automation 3: Implicit Error Logging**

- This is not a separate automation - it's built into Actions 1 and 2 error handling

- When webhook POST fails after 3 retries, Automations 1 and 2 automatically create record in Sync Errors table

- Josh validates error logging works during testing

- **Deliverable:** 2 Airtable webhook automations built and tested (set to inactive)

8.2.3.4.2 **Configuration Step D2: Josh Builds Zapier Workflows**

- **Owner:** Josh

- **Activities:**

**Move TEST Zaps to Production:**

1. Navigate to /Testing Workflows folder

2. Rename "TEST - New Paid Project Sync" → "New Paid Project Sync"

3. Move to /Production Workflows folder

4. Rename "TEST - Phase Change Sync" → "Phase Change Sync"

5. Move to /Production Workflows folder

**Build Workflow 1: New Paid Project Sync** *(This is the most complex workflow - detailed action-by-action steps in Section 8.4.2)*

1. Trigger already configured (Catch Hook from Configuration Step C1)

2. Add Step 2: Formatter by Zapier - Parse webhook payload contacts array

3. Add Step 3: Filter - Only proceed if project_id exists

4. Add Step 4: HubSpot - Find Deal by Project ID

5. Add Step 5a: HubSpot - Create Deal (if not found in Step 4)

6. Add Step 5b: HubSpot - Update Deal (if found in Step 4)

7. Add Step 6: Looping by Zapier - Loop through contacts array

8. Add Step 7a (inside loop): HubSpot - Find Contact by email1

9. Add Step 7b (inside loop): HubSpot - Create or Update Contact

10. Add Step 8 (inside loop): HubSpot - Associate Contact with Deal

11. Add Step 9: HubSpot - Create timeline note on Deal

12. Add Step 10: Email by Zapier - Send success notification (optional)

13. Add Step 11 (error path): Email by Zapier - Send error alert to Johnny and Josh

14. Test with sample Airtable project

15. Leave workflow OFF (will activate during Phase 3)

**Build Workflow 2: Phase Change Sync** *(Simpler than Workflow 1)*

1. Trigger already configured (Catch Hook from Configuration Step C1)

2. Add Step 2: Filter - Only proceed if project_id exists

3. Add Step 3: HubSpot - Find Deal by Project ID (error if not found)

4. Add Step 4: HubSpot - Update Deal (Stage, project_phase, Primary POC, Backup POC, Deal Owner, last_sync_date)

5. Add Step 5: HubSpot - Create timeline note

6. Add Step 6: Email - Send success notification (optional)

7. Add Step 7 (error path): Email - Send error alert

8. Test with sample Airtable phase change

9. Leave workflow OFF

**Build Workflow 3: Weekly Baseline Sync**

1. Create new Zap in /Production Workflows: "Weekly Baseline Sync"

2. Trigger: Schedule by Zapier - Every week on Sunday at 6:00 AM Arizona Time

3. Add Step 2: Airtable - Find records (Status = Paid OR Active, max 100 records)

4. Add Step 3: Looping by Zapier - Loop through projects array

5. Add Step 4 (inside loop): HubSpot - Find Deal by Project ID

6. Add Step 5 (inside loop, Path A): If Deal exists, Update Deal

7. Add Step 5 (inside loop, Path B): If Deal not found, Create Deal (includes Contact creation like Workflow 1)

8. Add Step 6 (inside loop): Airtable - Update record (set Last HubSpot Sync = current timestamp)

9. Add Step 7: Email - Send weekly summary (projects processed, Deals updated/created counts)

10. Test by manually running scheduled trigger

11. Leave workflow OFF

- **Deliverable:** 3 Zapier workflows built and unit tested (all set to OFF)

- **Notification to Johnny:** Email Johnny "Zapier workflows complete - ready for Phase 3 joint testing"

**Configuration Group D Completion Checkpoint:**

**Josh's Deliverables:**

- [ ] 2 Airtable webhook automations built and tested (Step D1)

- [ ] 3 Zapier workflows built and unit tested (Step D2)

- [ ] All automations/workflows set to INACTIVE (will activate during Phase 3 testing)

**Phase 2 Complete - Ready for Phase 3 Integration & Testing**

### 8.2.4 Phase 3 Integration & Testing - Joint Collaboration

**Purpose:** Validate end-to-end integration from Airtable → Zapier → HubSpot with Josh and Johnny working together to test data flow, POC assignments, and error handling.

#### 8.2.4.1 Testing Group A: Unit Testing (Independent Work)

##### 8.2.4.1.1 Testing Step A1: Josh Tests Airtable and Zapier Components

- **Owner:** Josh

- **Activities:**

  - Activate Airtable Automation 1 (New Paid Project)

  - Change sample project Status to "Paid"

  - Verify webhook fires to Zapier

  - Verify Zapier workflow processes webhook correctly

  - Check Zapier workflow history for successful completion

  - Deactivate automation after testing

  - Repeat for Automation 2 (Phase Change)

  - Document any errors in shared Google Doc: "Phase 3 Testing Log"

##### 8.2.4.1.2 Testing Step A2: Johnny Tests HubSpot Workflows

- **Owner:** Johnny

- **Activities:**

  - Activate Workflow 1 (POC Assignment Based on Phase)

  - Manually create test Deal in HubSpot with Phase = "PreDesign"

  - Verify Primary POC assigned to Molly, Backup POC assigned to Robin

  - Check Deal timeline for workflow activity log

  - Manually change Deal Phase to "Design"

  - Verify Primary POC updated to Sara, Backup POC updated to Meghan

  - Repeat for all 5 phases

  - Test error handling: Manually set Phase to "InvalidPhase", verify error email sent to Johnny

  - Deactivate workflow after testing

  - Repeat unit tests for Workflow 2 (Deal Stage Update)

  - Document results in "Phase 3 Testing Log"

##### 8.2.4.1.3 Testing Step A3: Independent Testing of All Components

- **Josh:** Test all 3 Zapier workflows independently (using Zapier "Test" feature, not live Airtable triggers)

- **Johnny:** Test all 7 HubSpot workflows independently (manual Deal/Conversation creation)

- **Both:** Document all test results, errors, and observations in shared testing log

#### 8.2.4.2 Testing Group B: Integration Testing (Josh and Johnny Collaborate)

##### 8.2.4.2.1 Testing Step B1: End-to-End Test - New Paid Project

- **Owners:** Josh and Johnny (joint session, same time, screen share recommended)

- **Test Scenario:** Airtable project becomes Paid → Zapier creates Deal in HubSpot → HubSpot assigns POCs

- **Process:**

  1. **Josh activates:** Airtable Automation 1, Zapier Workflow 1

  2. **Johnny activates:** HubSpot Workflow 1, Workflow 2

  3. **Josh:** In Airtable, create new project:

     - Project ID: "TEST-2025-001"

     - Project Name: "Integration Test Project 1"

     - Status: "Lead"

     - Phase: "PreDesign"

     - Link 2 sample Contacts

  4. **Josh:** Change project Status from "Lead" to "Paid"

  5. **Josh monitors:** Airtable automation fires, Zapier workflow receives webhook

  6. **Johnny monitors:** HubSpot Deal appears, POC Assignment workflow fires

  7. **Validate together:**

     - Deal created in HubSpot with correct Project ID, Name, Stage

     - Deal custom properties populated (project_id, project_phase)

     - Primary POC = Molly, Backup POC = Robin (correct for PreDesign phase)

     - Deal Owner = Molly

     - 2 Contacts created in HubSpot, both associated with Deal

     - All Contact email/phone fields populated correctly

     - Timeline note on Deal: "Project synced from Airtable"

     - No errors in Airtable, Zapier, or HubSpot logs

  8. **Document results:** Both sign off "New Paid Project sync validated"

##### 8.2.4.2.2 Testing Step B2: End-to-End Test - Phase Change

- **Owners:** Josh and Johnny (joint session)

- **Test Scenario:** Airtable phase changes → Zapier updates Deal → HubSpot reassigns POCs

- **Process:**

  1. **Josh activates:** Airtable Automation 2, Zapier Workflow 2

  2. **Johnny activates:** HubSpot Workflow 1 (if not already active), Workflow 2

  3. **Josh:** In Airtable, change TEST-2025-001 Phase from "PreDesign" to "Design"

  4. **Josh monitors:** Airtable automation fires, Zapier receives webhook

  5. **Johnny monitors:** HubSpot Deal updates, POC Assignment workflow fires

  6. **Validate together:**

     - Deal project_phase property updated to "Design"

     - Deal Stage updated to "Design"

     - Primary POC updated to Sara, Backup POC updated to Meghan

     - Deal Owner updated to Sara

     - Timeline note: "Project phase changed to Design. POC assignments updated."

     - No errors logged

  7. **Test all phase transitions:** Repeat for PreDesign → Design → Procurement → PreConstruction → Construction

  8. **Document results:** Both sign off "Phase Change sync validated"

##### 8.2.4.2.3 Testing Step B3: Test Vacation Flag Routing

- **Owners:** Josh and Johnny (joint session)

- **Test Scenario:** Primary POC on vacation → messages route to Backup POC

- **Process:**

  1. **Johnny activates:** HubSpot Workflow 3 (Conversation Assignment Routing)

  2. **Johnny:** Enable vacation flag for Sara (Primary POC for Design phase):

     - Navigate to Sara's user settings

     - Enable "Out of Office" checkbox

  3. **Johnny:** Send test email to VIP@livingwithlolo.com from external email address

  4. **Johnny:** In HubSpot, manually associate test email with TEST-2025-001 Deal (currently in Design phase)

  5. **Validate:**

     - Conversation assigns to Meghan (Backup POC) instead of Sara (Primary POC)

     - Meghan receives notification

     - Conversation timeline note: "Routed to Backup POC - Primary POC on vacation"

  6. **Johnny:** Disable Sara's vacation flag

  7. **Johnny:** Send second test email to VIP@

  8. **Validate:**

     - New conversation assigns to Sara (Primary POC now available)

     - Sara receives notification

  9. **Test welcome@ inbox:** Enable Molly's vacation flag, send email to welcome@, verify routes to Lauren

  10. **Document results:** Both sign off "Vacation flag routing validated"

##### 8.2.4.2.4 Testing Step B4: Test Multi-Contact Projects

- **Owners:** Josh and Johnny (joint session)

- **Test Scenario:** Project with 5 emails and 6 phones (exceeds HubSpot Contact limits) → multiple Contacts created

- **Process:**

  1. **Josh:** In Airtable, create new project "TEST-2025-002":

     - Link 2 Contacts:

       - Contact 1: John Smith (3 emails + 3 phones)

       - Contact 2: Sarah Smith (2 emails + 3 phones)

     - Status: "Paid", Phase: "Design"

  2. **Josh monitors:** Airtable Automation 1 fires

  3. **Johnny monitors:** HubSpot Deal and Contacts created

  4. **Validate together:**

     - 1 Deal created

     - 2 separate Contacts created in HubSpot (one for John, one for Sarah)

     - Both Contacts associated with same Deal

     - John's Contact: 3 email fields populated, 3 phone fields populated

     - Sarah's Contact: 2 email fields populated, 3 phone fields populated

     - All email/phone labels preserved

  5. **Test routing:** Send test email from John's email2 (secondary address) to VIP@

  6. **Validate:** Conversation associates with correct Deal and routes to Sara (Design Primary POC)

  7. **Test routing:** Send test SMS from Sarah's phone3 to LWL business number

  8. **Validate:** SMS conversation associates with correct Deal and routes to Sara

  9. **Document results:** Both sign off "Multi-contact routing validated"

##### 8.2.4.2.5 Testing Step B5: Error Handling and Recovery Testing

- **Owners:** Josh and Johnny (joint session)

- **Test Scenarios:** Intentional failures to validate error handling

- **Process:**

**Test 1: Phase Name Mismatch**

1. **Josh:** In Airtable, manually edit sample project Phase to "Pre-Design" (incorrect spelling)

2. **Validate:** HubSpot POC Assignment workflow logs error, sends alert email to Johnny

3. **Josh:** Check Airtable Sync Errors table - no entry (because Airtable webhook fired successfully; error is in HubSpot)

4. **Johnny:** Manually correct Phase in HubSpot Deal to "PreDesign"

5. **Validate:** POC Assignment workflow triggers correctly, assigns Molly/Robin

**Test 2: Webhook Delivery Failure**

1. **Josh:** In Zapier, temporarily disable Workflow 1 (New Paid Project Sync)

2. **Josh:** In Airtable, change project Status to Paid (triggers webhook)

3. **Validate:** Airtable automation retries 3 times, then creates record in Sync Errors table

4. **Josh:** Review Sync Errors table entry - contains Project ID, error message, retry count

5. **Josh:** Re-enable Zapier Workflow 1

6. **Josh:** Manually re-trigger webhook (change project field to force re-sync)

7. **Validate:** Sync succeeds on retry

**Test 3: Missing Contact Email and Phone**

1. **Josh:** Create Contact in Airtable with only name (no emails, no phones)

2. **Josh:** Link Contact to project, trigger sync

3. **Validate:** Zapier workflow handles gracefully (Contact created in HubSpot with name only), no errors

**Test 4: Weekly Baseline Sync**

1. **Josh:** Manually trigger Zapier Workflow 3 (Weekly Baseline Sync) using "Test" feature

2. **Validate:** All Paid/Active projects in Airtable processed

3. **Josh:** Check Airtable - Last HubSpot Sync field updated for all projects

4. **Validate:** Summary email sent to Josh and Johnny with task counts

5. **Document results:** Both sign off "Error handling validated"

#### 8.2.4.3 Testing Group C: Edge Case Testing and Documentation

##### 8.2.4.3.1 Testing Step C1: Edge Case Scenarios

- **Owners:** Josh and Johnny (can work independently, coordinate results)

- **Test Scenarios:**

  - Rapid phase changes (change Phase 3 times within 5 minutes)

  - Multiple projects becoming Paid simultaneously

  - Contact email address changes in Airtable (verify HubSpot Contact updates)

  - POC manually overridden in HubSpot (verify manual override persists)

  - Conversation ownership persistence (phase changes don't reassign active conversations)

  - Unassigned Conversations queue (send email from unknown sender, verify routes to Unassigned)

  - SMS opt-out (send "STOP" keyword, verify unsubscribe works)

  - Business hours auto-reply (send email/SMS outside business hours, verify auto-reply)

  - Holiday exclusion (set test holiday date, verify auto-reply suppressed)

- **Document all results** in Phase 3 Testing Log

##### 8.2.4.3.2 Testing Step C2: Test Documentation and Issue Resolution

- **Owners:** Josh and Johnny

- **Activities:**

  1. Review Phase 3 Testing Log together

  2. Categorize all discovered issues:

     - Critical (blocks go-live): Must fix before Phase 4

     - High (impacts functionality): Fix before Phase 4 if possible

     - Medium (minor issues): Document as known issues, fix post-launch

     - Low (cosmetic): Defer to future enhancement

  3. For each Critical and High issue:

     - Josh and Johnny determine root cause

     - Assign owner (Josh for Airtable/Zapier, Johnny for HubSpot)

     - Owner implements fix

     - Both retest to confirm fix

  4. Create "Phase 3 Test Results Summary" document including:

     - Test scenarios executed (checklist)

     - Pass/Fail status for each scenario

     - Critical/High issues discovered and resolved

     - Medium/Low issues documented for future

     - Recommendations for Phase 4 UAT focus areas

  5. Both sign off "Phase 3 Integration Testing Complete - Ready for Phase 4 UAT"

**Phase 3 Go/No-Go Decision Gate:**

**Decision Maker:** CEO (with input from Johnny and Josh)

**Go Criteria - ALL must be complete:**

- [ ] All integration test scenarios executed (Testing Steps B1-B5)

- [ ] All Critical issues resolved and retested

- [ ] All High issues either resolved or documented with workarounds

- [ ] Phase 3 Test Results Summary document complete

- [ ] Josh and Johnny both sign off "Ready for Phase 4 UAT"

**No-Go Criteria - ANY of these triggers delay:**

- Any Critical issue unresolved (e.g., POC assignment failing consistently)

- More than 3 High issues unresolved without workarounds

- Data loss or corruption observed during testing

- Josh or Johnny recommends delay for technical reasons

**Decision Documentation:** CEO sends "Phase 4 Authorization" email to Johnny, Josh, and UAT participants

### 8.2.5 Phase 4 User Acceptance Testing

**Purpose:** Business users (CEO, Robin, Debra, design team, construction team) validate system meets BRD requirements in near-production environment.

**OUT OF SCOPE for Section 8.2:** Phase 4 UAT activities are defined in BRD Section 7.3.4 and will be detailed in separate UAT Plan document. Section 8.2 focuses on Josh and Johnny's technical implementation roadmap.

**Josh and Johnny's Role in Phase 4:**

- Provide UAT training to business users (how to test the system)

- Monitor UAT sessions, troubleshoot issues, implement fixes as needed

- Incorporate UAT feedback, prepare for Phase 5 go-live

### 8.2.6 Phase 5 Training & Deployment

**Purpose:** Train all team members, migrate from old communication methods to new system, activate all workflows in production.

**OUT OF SCOPE for Section 8.2:** Phase 5 training and deployment activities are defined in BRD Section 7.3.5. Section 8.2 focuses on Josh and Johnny's technical implementation.

**Josh and Johnny's Role in Phase 5:**

- Conduct user training sessions (how to use HubSpot Conversations, manage vacation flags)

- **GO-LIVE EVENT:**

  - Josh activates all Airtable automations (set to active, production)

  - Josh activates all Zapier workflows (turn ON)

  - Johnny activates all HubSpot workflows (production)

  - Both monitor system closely for first 24 hours

- Immediate post-launch support

### 8.2.7 Phase 6 Stabilization & Handover

**Purpose:** Monitor system stability, resolve post-launch issues, transition to ongoing operations.

**Josh and Johnny's Monitoring Schedule:**

**Initial Intensive Monitoring Period:**

- **Frequency:** Both Josh and Johnny review system health each morning

- **Review items:**

  - Zapier workflow history (any failures?)

  - HubSpot POC Assignment workflow logs (any errors?)

  - Airtable Sync Errors table (any entries?)

  - User feedback from team (any confusion or issues?)

- **Issue triage:** Any issues discovered, Josh and Johnny troubleshoot together same day

- **Duration:** Continue intensive monitoring until stable (typically 2 weeks post-launch)

**Transition to Routine Monitoring:**

- **After stabilization period:** Move to weekly sync checks (every Monday morning)

- **Handover documentation:** Josh and Johnny create "Ongoing Maintenance Procedures" document

- **Final sign-off:** CEO approves "Implementation 1 Complete"

**Ongoing Operations (Post-Phase 6):**

**Josh's Ongoing Responsibilities:**

- Monitor Zapier workflow history weekly

- Monitor Airtable Sync Errors table weekly

- Respond to sync failures within 24 hours

- Maintain Zapier account (subscription, task usage monitoring)

- Annual Airtable API token rotation

- Escalate to Johnny if HubSpot-side issues suspected

**Johnny's Ongoing Responsibilities:**

- Monitor HubSpot workflow health weekly (POC Assignment Health Check email every Monday)

- Monitor Monthly Phase Name Validation report

- Update holiday calendar annually each November

- Manage HubSpot user accounts (new hires, departures)

- Annual HubSpot Private App API key rotation

- Escalate to Josh if Airtable/Zapier sync issues suspected

**Escalation for Complex Issues:**

- If Josh and Johnny cannot resolve issue within 24 hours, jointly escalate to vendor support (Airtable, Zapier, or HubSpot)

- If issue requires BRD change or new functionality, escalate to CEO for scope decision

### 8.2.8 Critical Success Factors Summary

**Keys to Successful Implementation:**

1. **Phase 1 blocking decisions completed BEFORE Phase 2 begins**

   - Project ID format finalized

   - Phase-to-POC mapping validated with stakeholders

   - Airtable schema ready

   - No exceptions to this rule

2. **Handoffs executed on time**

   - Johnny provides API key and User IDs to Josh (Configuration Group A)

   - Josh provides webhook URLs to Johnny (Configuration Group C)

   - Both parties confirm receipt of handoff items via email

3. **Phase 3 integration testing thorough**

   - Don't skip edge cases

   - Resolve all Critical issues before Phase 4

   - Document all issues clearly for future reference

4. **Regular coordination between Josh and Johnny**

   - Frequent communication during Phase 2-3 to identify blockers early

   - Joint troubleshooting sessions for complex integration issues

   - Adjust timeline if needed rather than rushing incomplete work

5. **Post-launch monitoring discipline**

   - Initial intensive monitoring period is CRITICAL

   - Don't skip daily sync checks during stabilization

   - Resolve issues immediately, don't defer