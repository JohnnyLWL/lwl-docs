---
source: SDD - System Design Document - Consolidated Communication PART ONE v1.docx
section: 5.0 INTEGRATION ARCHITECTURE (ZAPIER WORKFLOWS) (Part 1 - Sections 5.1-5.2)
integrity: full
format: preservation_mode
encoding: utf-8
extraction_method: paragraph_and_table_parser
order_preserved: true
tables_preserved: true
revision: 1.1
strict_lossless_mode: true
---

## 5.0 INTEGRATION ARCHITECTURE (ZAPIER WORKFLOWS)

## 5.1 Zapier Configuration Overview

### 5.1.1 Zapier Account Setup

Account Owner: Josh (Airtable Administrator) maintains Zapier account

Subscription Tier: Starter ($19.99/month as of October 2025)

-   Supports 750 tasks/month

-   Adequate for event-driven + weekly baseline sync (approximately 200-300 tasks/month estimated)

Workspace Organization:

-   Workspace Name: "Living With Lolo - Communications Hub"

-   Folder Structure:

    -   /Production Workflows (live integrations)

    -   /Testing Workflows (development and QA)

Access Permissions:

-   Josh: Admin (full access)

-   LWL IT Lead: Collaborator (view and edit workflows)

-   Additional collaborators as needed during implementation

### 5.1.2 Zapier Workflow Inventory

| **Workflow Name** | **Trigger** | **Purpose** | **Status** |
| --- | --- | --- | --- |
| New Paid Project Sync | Airtable webhook (New Paid Project) | Create Deal + Contacts in HubSpot | Active |
| Phase Change Sync | Airtable webhook (Phase Change) | Update Deal Stage + POC assignments in HubSpot | Active |
| Weekly Baseline Sync | Schedule (Sunday 6 AM Arizona) | Reconcile all Paid projects Airtable → HubSpot | Active |
| Sync Error Notification | Built into above workflows | Email admins on workflow failure | Active |
| Salesmsg to Slack Alert | Salesmsg webhook (new inbound message) | Post real-time alert to #urgent-alerts Slack channel | Active |

## 5.2 Zapier Workflow 1: New Paid Project Sync

### 5.2.1 Workflow Overview

Trigger: Webhooks by Zapier - Catch Hook

Actions: Multi-step workflow creating Deal and associated Contacts in HubSpot

Expected Task Consumption: 1 task per new Paid project (low volume, approximately 3-5 projects/month)

### 5.2.2 Detailed Workflow Steps

Step 1: Catch Webhook from Airtable

-   App: Webhooks by Zapier

-   Action: Catch Hook

-   Configuration:

    -   Generate custom webhook URL

    -   Provide URL to Josh for Airtable automation configuration (Section 4.4.2)

    -   Test webhook reception with Airtable test trigger

-   Output Data: JSON payload from Airtable containing project metadata and contacts array

Step 2: Parse Webhook Payload

-   App: Formatter by Zapier (optional if needed)

-   Action: Utilities - Line Items to Text (if contacts array needs formatting)

-   Purpose: Extract individual contact objects from contacts array for iteration

-   Configuration: Extract each contact as separate line-item group

Step 3: Filter - Only Proceed if Project ID Exists

-   App: Filter by Zapier

-   Rule: project_id field IS NOT empty

-   Purpose: Prevent sync of incomplete project records

Step 4: Find Existing Deal in HubSpot

-   App: HubSpot

-   Action: Find Deal

-   Search Field: Project ID (custom property)

-   Search Value: Step 1: project_id

-   Purpose: Check if Deal already exists to avoid duplicates

-   If Found: Workflow updates existing Deal (idempotent sync)

-   If Not Found: Workflow proceeds to create new Deal

Step 5a: Create Deal in HubSpot (If Not Found)

-   App: HubSpot

-   Action: Create Deal

-   Configuration:

    -   Deal Name: Step 1: project_name

    -   Deal Stage: Map from Step 1: project_phase:

        -   If "PreDesign" → Deal Stage "PreDesign"

        -   If "Design" → Deal Stage "Design"

        -   If "Procurement" → Deal Stage "Procurement"

        -   If "PreConstruction" → Deal Stage "PreConstruction"

        -   If "Construction" → Deal Stage "Construction"

    -   Pipeline: "Client Projects"

    -   Custom Properties:

        -   project_id: Step 1: project_id

        -   project_phase: Step 1: project_phase

        -   primary_primary_poc: Step 1: primary_poc_hubspot_id (HubSpot User ID) - backup_poc: Step 1: backup_poc_hubspot_id (HubSpot User ID) - airtable_record_id: Step 1: airtable_record_id - last_sync_date: Step 1: sync_timestamp

-   Deal Owner: Step 1: primary_poc_hubspot_id

Step 5b: Update Deal in HubSpot (If Found)

-   App: HubSpot

-   Action: Update Deal

-   Configuration: Same fields as Create, updates existing Deal with current data

Step 6: Loop Through Contacts Array

-   App: Looping by Zapier

-   Action: Create Loop from Line Items

-   Input: Step 2: contacts array

-   Purpose: Process each contact individually to create/update HubSpot Contacts

Step 7a (Inside Loop): Find Existing Contact in HubSpot

-   App: HubSpot

-   Action: Find Contact

-   Search Field: Email

-   Search Value: Loop: email1 (primary email from current contact)

-   Purpose: Check if Contact already exists

-   Create if Not Found: Yes (enable this option)

Step 7b (Inside Loop): Create or Update Contact

-   App: HubSpot

-   Action: Create or Update Contact

-   Configuration:

    -   Email: Loop: email1

    -   Additional Emails: Loop: email2, Loop: email3 (if not empty)

    -   First Name: Extract from Loop: contact_name (split on space, take first)

    -   Last Name: Extract from Loop: contact_name (split on space, take remainder)

    -   Phone Number: Loop: phone1

    -   Mobile Phone: Loop: phone2

    -   Work Phone: Loop: phone3

    -   Custom Properties:

        -   contact_label: Loop: contact_name (for reference)

        -   preferred_channel: Loop: preferred_contact_method

        -   airtable_contact_id: Loop: airtable_contact_id (if included in payload)

Step 8 (Inside Loop): Associate Contact with Deal

-   App: HubSpot

-   Action: Add Contact to Deal

-   Configuration:

    -   Deal ID: Step 5a or 5b: Deal ID

    -   Contact ID: Step 7b: Contact ID

-   Purpose: Link each client contact to the project Deal

Step 9: Create Timeline Note on Deal

-   App: HubSpot

-   Action: Create Engagement (Note)

-   Configuration:

    -   Associated Deal: Step 5a or 5b: Deal ID

    -   Note Body: "Project synced from Airtable. Project ID: Step 1: project_id. Sync timestamp: Step 1: sync_timestamp."

-   Purpose: Audit trail of sync activity

Step 10: Send Success Notification (Optional)

-   App: Email by Zapier

-   Action: Send Outbound Email

-   Configuration:

    -   To: josh@livingwithlolo.com, johnny@livingwithlolo.com

    -   Subject: "✓ HubSpot Sync Success - Step 1: project_id"

    -   Body: Summary of created/updated Deal and Contacts

-   Purpose: Confirmation of successful sync (can be disabled after stabilization)

### 5.2.3 Error Handling Configuration

Built-in Zapier Error Handling:

-   Enable "Automatic Error Handling" on workflow

-   Retry failed steps up to 3 times with exponential backoff (1 min, 5 min, 15 min)

Custom Error Notification:

Step 11 (Error Path): Send Error Alert

-   App: Email by Zapier

-   Trigger: Only if previous steps fail after retries

-   Configuration:

    -   To: josh@livingwithlolo.com, johnny@livingwithlolo.com

    -   Subject: "⚠ HubSpot Sync FAILED - Step 1: project_id"

    -   Body: Sync failed for Project ID: Step 1: project_id

Error Details:

Error Message

Airtable Record ID: Step 1: airtable_record_id

Timestamp: Step 1: sync_timestamp

Action Required: Review Zapier workflow history and retry manually if needed.

Error Logging:

-   Zapier automatically logs all workflow runs in Workflow History

-   Failed runs visible with error details for troubleshooting

-   Josh reviews Workflow History weekly (daily during first 30 days post-launch)

## 5.3 Zapier Workflow 2: Phase Change Sync

### 5.3.1 Workflow Overview

Trigger: Webhooks by Zapier - Catch Hook (different webhook URL than New Paid Project)

Actions: Update existing Deal Stage and POC assignments in HubSpot

Expected Task Consumption: 1 task per phase change (approximately 5-10 phase changes/month per project × 50 projects = approximately 250-500 tasks/year total, well within Starter tier limits)

### 5.3.2 Detailed Workflow Steps

Step 1: Catch Webhook from Airtable

-   App: Webhooks by Zapier

-   Action: Catch Hook

-   Configuration: Generate separate webhook URL for Phase Change automation

-   Output Data: JSON payload from Airtable (lighter payload than New Paid Project, per Section 4.4.3)

Step 2: Filter - Only Proceed if Project ID Exists

-   App: Filter by Zapier

-   Rule: project_id field IS NOT empty

Step 3: Find Deal in HubSpot

-   App: HubSpot

-   Action: Find Deal

-   Search Field: Project ID (custom property)

-   Search Value: Step 1: project_id

-   Should This Step Be Considered a Success When Nothing Is Found: No (error if Deal not found)

-   Purpose: Locate existing Deal to update

Step 4: Update Deal Stage

-   App: HubSpot

-   Action: Update Deal

-   Configuration:

    -   Deal ID: Step 3: Deal ID

    -   Deal Stage: Map from Step 1: new_phase:

        -   If "PreDesign" → Deal Stage "PreDesign"

        -   If "Design" → Deal Stage "Design"

        -   If "Procurement" → Deal Stage "Procurement"

        -   If "PreConstruction" → Deal Stage "PreConstruction"

        -   If "Construction" → Deal Stage "Construction"

    -   Custom Properties:

        -   project_phase: Step 1: new_phase

        -   primary_poc: Step 1: primary_poc_hubspot_id

        -   backup_poc: Step 1: backup_poc_hubspot_id

        -   last_sync_date: Step 1: sync_timestamp

    -   Deal Owner: Step 1: primary_poc_hubspot_id (updates owner to new Primary POC)

Step 5: Create Timeline Note on Deal

-   App: HubSpot

-   Action: Create Engagement (Note)

-   Configuration:

    -   Associated Deal: Step 3: Deal ID

    -   Note Body: "Project phase updated to Step 1: new_phase. Primary POC: Step 1: primary_poc_email, Backup POC: Step 1: backup_poc_email. Sync timestamp: Step 1: sync_timestamp."

Step 6: Send Success Notification (Optional)

-   Same configuration as Workflow 1 Step 10

Step 7 (Error Path): Send Error Alert

-   Same configuration as Workflow 1 Step 11

### 5.3.3 Important Note on Conversation Ownership Persistence

Per BRD Section 3.3.7:

-   Phase changes in Airtable DO NOT trigger reassignment of active (Open) conversations in HubSpot

-   Existing conversation threads retain their currently assigned POC regardless of phase changes

-   NEW conversations created after phase change will route to the updated Primary POC

Implementation: This behavior is automatic in HubSpot. The Phase Change Sync workflow only updates the Deal record; HubSpot's Conversation Assignment Routing workflow (Section 3.6.2) handles new conversation routing based on current Deal.Primary_POC value.

## 5.4 Zapier Workflow 3: Weekly Baseline Sync

### 5.4.1 Workflow Overview

Purpose: Safety net to reconcile all Paid projects from Airtable to HubSpot, catching any missed webhook triggers or manual updates

Trigger: Schedule by Zapier - Every Sunday at 6:00 AM Arizona Time (UTC-7)

Actions: Batch fetch all Paid projects from Airtable, compare with HubSpot, update/create as needed

Expected Task Consumption: Approximately 50 tasks per run (one task per project, assuming approximately 50 active projects) = approximately 200 tasks/month

### 5.4.2 Detailed Workflow Steps

Step 1: Schedule Trigger

-   App: Schedule by Zapier

-   Action: Every Week

-   Configuration:

    -   Day of Week: Sunday

    -   Time: 6:00 AM

    -   Timezone: America/Phoenix (UTC-7)

Step 2: Find Records in Airtable

-   App: Airtable

-   Action: Find Records

-   Configuration:

    -   Base: Living With Lolo Base (production)

    -   Table: Projects

    -   Filter: Status = "Paid" OR Status = "Active"

    -   Max Records: 100 (adjustable if project volume increases)

-   Output: Array of all Paid/Active projects

Step 3: Loop Through Projects

-   App: Looping by Zapier

-   Action: Create Loop from Line Items

-   Input: Step 2: Projects array

Step 4 (Inside Loop): Find Deal in HubSpot

-   App: HubSpot

-   Action: Find Deal

-   Search Field: Project ID

-   Search Value: Loop: Project ID

-   Create if Not Found: No (next step handles creation)

Step 5 (Inside Loop): Branch - Deal Exists or Not

Path A: Deal Exists → Update Deal

-   App: HubSpot

-   Action: Update Deal

-   Configuration: Same as Phase Change Sync Step 4, using Loop variables

Path B: Deal Not Found → Create Deal

-   App: HubSpot

-   Action: Create Deal

-   Configuration: Same as New Paid Project Sync Step 5a, using Loop variables

-   Note: Also includes creating/updating Contacts similar to Workflow 1

Step 6 (Inside Loop): Log Sync Activity

-   App: Airtable

-   Action: Update Record

-   Configuration:

    -   Record ID: Loop: Airtable Record ID

    -   Field: "Last HubSpot Sync" (date field in Airtable Projects table)

    -   Value: Current timestamp

-   Purpose: Track when each project was last synced to HubSpot

Step 7: Send Weekly Sync Summary

-   App: Email by Zapier

-   Action: Send Outbound Email

-   Configuration:

    -   To: josh@livingwithlolo.com, johnny@livingwithlolo.com

    -   Subject: "Weekly HubSpot Baseline Sync Complete - Step 1: Scheduled Time"

    -   Body: Weekly baseline synchronization completed.

Total Projects Processed: Step 2: Record Count

Deals Updated: Count from Path A

Deals Created: Count from Path B

Review Zapier workflow history for details: Link to Zapier History

### 5.4.3 Baseline Sync Optimization

Performance Consideration:

-   Initial implementation syncs ALL Paid/Active projects every Sunday

-   If project volume exceeds 100, increase "Max Records" in Step 2 or implement pagination

Future Optimization (Post-Phase 1):

-   After 90 days of stable event-driven sync, LWL may discontinue weekly baseline sync if event-driven triggers prove 100% reliable (per BRD Section 7.3.1.7)

-   Decision based on: Zero missed syncs in Workflow History, high confidence in webhook reliability

Monitoring: Josh reviews Zapier Workflow History after each Sunday sync to confirm all projects processed successfully.

## 5.5 Zapier Authentication and API Connections

### 5.5.1 Airtable Connection

Authentication Method: Airtable API Key (Personal Access Token)

Setup Process:

1.  Josh generates Personal Access Token in Airtable Account Settings

2.  Scopes: data.records:read, data.records:write, schema.bases:read

3.  Add connection in Zapier: Settings \> Connected Accounts \> Airtable

4.  Test connection by running "Find Records" test action

Security: API key stored securely in Zapier vault, never exposed in workflow logs

### 5.5.2 HubSpot Connection

Authentication Method: HubSpot Private App API Key

Setup Process:

1.  LWL IT Lead creates Private App in HubSpot

    -   Navigate to Settings \> Integrations \> Private Apps

    -   App Name: "Zapier Integration - Communications Hub"

    -   Scopes Required:

        -   crm.objects.deals.read

        -   crm.objects.deals.write

        -   crm.objects.contacts.read

        -   crm.objects.contacts.write

        -   crm.schemas.deals.read (for custom properties)

        -   crm.schemas.contacts.read

        -   timeline (for creating notes/engagements)

2.  Copy Private App API Key

3.  Provide API Key to Josh

4.  Josh adds HubSpot connection in Zapier using Private App authentication method

5.  Test connection by running "Find Deal" test action

Security: Private App API Key stored securely in Zapier vault, scoped to minimum required permissions

Token Rotation: HubSpot Private App tokens do not expire, but should be rotated annually as security best practice

### 5.5.3 Webhook Security

Airtable Webhook URLs:

-   Zapier-generated webhook URLs contain random hash (e.g., /hooks/catch/123456/abcdef/)

-   URLs are secret; treat as sensitive credentials

-   If URL is compromised, regenerate webhook in Zapier and update Airtable automations

Payload Validation:

-   Zapier workflows include Filter steps to validate required fields present before processing

-   Prevents processing of malformed or incomplete payloads

## 5.6 Zapier Monitoring and Maintenance

### 5.6.1 Workflow Monitoring Dashboard

Zapier Task Usage:

-   Monitor task consumption: Zapier Dashboard \> Usage

-   Alert threshold: 80% of Starter tier limit (600 tasks)

-   If approaching limit, evaluate: Upgrade to Professional tier or optimize workflows

Workflow History Review:

-   Frequency: Josh reviews daily (first 30 days), then weekly

-   Focus Areas:

    -   Failed workflow runs (red status)

    -   Workflows with extended run times (more than 5 minutes)

    -   Workflows triggering unexpectedly (investigate root cause)

Email Notifications:

-   Zapier sends automatic email alerts for workflow failures (enable in Zapier settings)

-   Custom error emails configured in Workflows 1, 2, 3 (Sections 5.2.3, 5.3.2, 5.4.2)

### 5.6.2 Quarterly Workflow Audit

Responsibility: Josh (Airtable Administrator) with LWL IT Lead review

Audit Checklist:

1.  Review past 90 days of workflow runs in Zapier History

2.  Identify patterns of failures or errors

3.  Validate field mappings still accurate (any Airtable or HubSpot schema changes?)

4.  Check for deprecated Zapier app integrations (Zapier occasionally updates apps)

5.  Test each workflow end-to-end with sample data

6.  Update workflow documentation if any changes made

7.  Export workflow configurations to JSON for backup

Deliverable: Quarterly audit report shared with CEO and LWL IT Lead

### 5.6.3 Backup and Disaster Recovery

Workflow Configuration Backup:

-   Export each production workflow to JSON monthly

-   Store in LWL shared drive: /IT/HubSpot Implementation/Zapier Backups/

-   Naming convention: Workflow-Name_YYYY-MM.json

Recovery Process:

-   If workflow accidentally deleted or corrupted, import from most recent JSON backup

-   Re-authenticate API connections (Airtable, HubSpot)

-   Test workflow with sample data before re-activating

Critical Workflow Priority:

1.  New Paid Project Sync (highest priority - impacts all new projects)

2.  Phase Change Sync (high priority - impacts routing)

3.  Weekly Baseline Sync (medium priority - safety net only)
