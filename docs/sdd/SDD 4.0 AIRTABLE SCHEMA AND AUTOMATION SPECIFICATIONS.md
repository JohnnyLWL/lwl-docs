---
source: SDD - System Design Document - Consolidated Communication PART ONE v1.docx
section: 4.0 AIRTABLE SCHEMA AND AUTOMATION SPECIFICATIONS
integrity: full
format: preservation_mode
encoding: utf-8
extraction_method: paragraph_and_table_parser
order_preserved: true
tables_preserved: true
revision: 1.1
strict_lossless_mode: true
---

## 4.0 AIRTABLE SCHEMA AND AUTOMATION SPECIFICATIONS

## 4.1 Airtable Administrator Responsibilities

Owner: Josh (Airtable Administrator / Integration Architect)

Scope of Responsibility:

1.  Validate and remediate Airtable schema to support communications hub requirements

2.  Define and document Project ID naming convention

3.  Build Airtable webhook automations for "New Paid Project" and "Phase Change" triggers

4.  Collaborate with LWL IT Lead on field mapping and payload structure

5.  Monitor synchronization health and troubleshoot data integrity issues

6.  Maintain Zapier workflows (with LWL IT Lead initial setup support)

7.  Provide 90-day post-launch sync monitoring and issue resolution

## 4.2 Airtable Schema Requirements

### 4.2.1 Required Airtable Tables

| **Table Name** | **Purpose** | **Key Fields** |
| --- | --- | --- |
| Projects | Authoritative project database | Project ID, Status, Phase, Primary POC, Backup POC, Client Contacts |
| Contacts | Master client contact database | Name, Email(s), Phone(s), Role, Associated Projects |
| Users | LWL team member directory | Full Name, Email, Role, HubSpot User ID |

Note: Existing Airtable base structure may differ. Josh will validate that current structure supports these requirements during Phase 1 Pre-Implementation (BRD Section 1.6.3).

### 4.2.2 Projects Table Field Specifications

Required Fields:

| **Field Name** | **Field Type** | **Required** | **Purpose** | **Validation Rules** | **Example Value** |
| --- | --- | --- | --- | --- | --- |
| Project ID | Single line text | Yes | Unique project identifier | Must be unique across all projects; format defined in Section 4.3 | "2410-Smith-Maple" |
| Project Status | Single select | Yes | Lifecycle status | Options: Lead, Proposal, Paid, Active, Completed, Cancelled | "Paid" (triggers HubSpot sync) |
| Phase | Single select | Yes (if Status = Paid/Active) | Current project phase | Options: PreDesign, Design, Procurement, PreConstruction, Construction | "Design" |
| Primary POC | Link to Users table | Yes (if Status = Paid/Active) | Active primary point of contact | Must link to valid Users record | Link to "Sara" in Users table |
| Backup POC | Link to Users table | Yes (if Status = Paid/Active) | Backup point of contact | Must link to valid Users record; cannot be same as Primary POC | Link to "Meghan" in Users table |
| Client Contacts | Link to Contacts table | Yes | All client contact persons | Multiple links allowed | Link to "John Smith", "Sarah Smith" in Contacts table |
| Project Name | Single line text | Yes | Descriptive project name | Used for Deal Name in HubSpot | "Smith Residence - Maple Street Remodel" |
| Airtable Record ID | Formula field | Auto | Internal Airtable record ID | Formula: RECORD_ID() | "recABC123DEF456" |
| Last Modified | Last modified time | Auto | Timestamp of last edit | System-generated | "10/17/2025 2:30 PM" |

Phase Field Options: (Must match HubSpot Deal Stage names exactly - case sensitive)

-   PreDesign

-   Design

-   Procurement

-   PreConstruction

-   Construction

Critical Validation: Josh must confirm during Phase 1 that Phase field values match BRD Appendix C exactly. Any discrepancies require immediate resolution before Phase 2 configuration.

**VALIDATION PROCESS (added to Phase 1 checklist Section 1.7):**

1.  Josh exports all unique Phase field values from Projects table

2.  Compare against approved list above (character-by-character, including capitalization)

3.  Document any mismatches with proposed corrections

4.  LWL IT Lead approves corrections

5.  Josh updates Airtable Phase dropdown options to match exactly

6.  Both parties sign off on phase name alignment before Phase 2 begins

### 4.2.3 Contacts Table Field Specifications

Required Fields:

| **Field Name** | **Field Type** | **Required** | **Purpose** | **Example Value** |
| --- | --- | --- | --- | --- |
| Contact Name | Single line text | Yes | Full name | "John Smith" |
| Email 1 | Email | No | Primary email address | "<john@smithfamily.com>" |
| Email 1 Label | Single line text | No | Descriptive label for Email 1 | "John Personal" |
| Email 2 | Email | No | Secondary email address | "<jsmith@company.com>" |
| Email 2 Label | Single line text | No | Descriptive label for Email 2 | "John Work" |
| Email 3 | Email | No | Additional email address | "<smith.family@gmail.com>" |
| Email 3 Label | Single line text | No | Descriptive label for Email 3 | "Family Shared" |
| Phone 1 | Phone number | No | Primary phone | "(480) 555-1234" |
| Phone 1 Label | Single line text | No | Descriptive label for Phone 1 | "John Cell" |
| Phone 2 | Phone number | No | Secondary phone | "(623) 555-5678" |
| Phone 2 Label | Single line text | No | Descriptive label for Phone 2 | "Sarah Cell" |
| Phone 3 | Phone number | No | Additional phone | "(480) 555-9999" |
| Phone 3 Label | Single line text | No | Descriptive label for Phone 3 | "Home" |
| Phone 4 | Phone number | No | Fourth phone | "(480) 555-0000" |
| Phone 4 Label | Single line text | No | Descriptive label for Phone 4 | "Sarah Work" |
| Contact Role | Single select | No | Relationship to project | Options: Primary Client, Spouse/Partner, Family Member, Assistant, Other |
| Associated Projects | Link to Projects table | Yes | Projects this contact belongs to | Link to Projects records |
| Preferred Contact Method | Single select | No | Email, SMS, Phone, No Preference | "Email" |

Multi-Contact Strategy: Per BRD Section 3.11.2.2.1 and 7.3.1.4.1, projects with more than 3 email addresses or 4 phone numbers will use multiple Contact records in Airtable, each syncing to separate HubSpot Contact records associated with the same Deal.

Example Multi-Contact Scenario:

-   Airtable Contact 1: John Smith (3 emails + 2 phones)

-   Airtable Contact 2: Sarah Smith (2 emails + 2 phones)

-   Both linked to same Project record

-   HubSpot Sync: Creates 2 HubSpot Contacts, both associated with same Deal

### 4.2.4 Users Table Field Specifications

Required Fields:

| **Field Name** | **Field Type** | **Required** | **Purpose** | **Example Value** |
| --- | --- | --- | --- | --- |
| Full Name | Single line text | Yes | Team member name | "Sara Thompson" |
| Email | Email | Yes | LWL email address | "<sara@livingwithlolo.com>" |
| Role | Single select | Yes | Job function | "Lead Designer" |
| HubSpot User ID | Number | Yes | HubSpot internal user ID for API calls | 12345678 |
| HubSpot Email | Email | Yes | Email used in HubSpot account (may differ from LWL email) | "<sara@livingwithlolo.com>" |
| Active | Checkbox | Yes | Is user currently active? | Checked |

HubSpot User ID Mapping Process (CRITICAL for POC Assignment workflow):

Phase 1 Discovery Requirement:

1.  LWL IT Lead obtains HubSpot User IDs:

-   Navigate to HubSpot Settings → Users & Teams

-   Click on each user

-   Note User ID from browser URL (e.g., \.../settings/users/12345678)

-   Create mapping document: "HubSpot User ID Mapping - \[Date\].xlsx"

-   Columns: Full Name, LWL Email, HubSpot Email, HubSpot User ID, Role

-   Include all 8-9 team members who will be POCs

2.  LWL IT Lead provides mapping document to Josh:

-   Deliver via email or shared Google Drive folder

-   Josh confirms receipt within 24 hours

-   Both parties validate mapping accuracy (no typos in User IDs)

3.  Josh enters User IDs into Airtable:

-   Open Airtable Users table

-   For each team member, enter their HubSpot User ID in the "HubSpot User ID" field

-   Double-check all User IDs match mapping document exactly

-   Validate: All POCs mentioned in BRD Appendix C have User IDs entered

4.  Validation checkpoint:

-   Josh exports Users table to CSV

-   LWL IT Lead spot-checks 3-5 User IDs against HubSpot Admin Console

-   Both parties sign off on accuracy

5.  LWL IT Lead configures POC Assignment workflow:

-   Use numeric User IDs in HubSpot workflow conditional branches (Section 3.6.8)

-   Test workflow with sample Deal to confirm POC assignment works

-   Validate: Workflow assigns correct team member (not "Unknown User" error)

**Why This Matters:**

-   HubSpot API requires numeric User IDs (not email addresses) for conversation assignment

-   Email-based assignment fails silently, routing messages to Unassigned queue

-   User ID mapping must be 100% accurate or POC assignment workflow breaks

-   This is a BLOCKING requirement: Phase 2 configuration cannot proceed without completed mapping

**Troubleshooting User ID Issues:**

-   If workflow shows "Unknown User" error: User ID incorrect or user deactivated in HubSpot

-   If conversations route to wrong POC: User ID transposed (e.g., 12345 instead of 54321)

-   If new team member added mid-project: Obtain new User ID, update Airtable, update workflow

## 4.3 Project ID Naming Convention

Responsibility: Josh (Airtable Administrator) defines convention; LWL IT Lead approves

Requirements: Per BRD Section 3.8.4:

-   Must be unique across all projects

-   Must be human-readable

-   Must be suitable for long-term use across multiple systems

-   Must be consistent and rule-based (not ad-hoc)

Recommended Format Options for Phase 1 Discovery Review:

Option 1: Year-Month-ClientLastName-ShortAddress

-   Format: YYMM-LastName-Address

-   Example: 2410-Smith-Maple

-   Pros: Chronological sorting, immediate date context, human-readable

-   Cons: Potential duplicates if same last name + same month (requires disambiguation like Smith01, Smith02)

Option 2: Sequential with Year Prefix

-   Format: LWL-YYYY-###

-   Example: LWL-2024-047

-   Pros: Guaranteed uniqueness, simple increment logic

-   Cons: Requires sequential counter maintenance, less human context

Option 3: Airtable Record ID (Hybrid)

-   Format: Use Airtable's auto-generated Record ID as Project ID

-   Example: recABC123DEF456 (Airtable standard)

-   Pros: Guaranteed uniqueness, zero maintenance, automatically generated

-   Cons: Not human-readable, cannot derive meaning from ID

Decision Process:

1.  Josh proposes preferred format with rationale during Phase 1 Discovery

2.  LWL IT Lead reviews for HubSpot compatibility (no special characters that break API calls)

3.  CEO approves final format

4.  Josh implements in Airtable (formula field or manual entry protocol)

5.  BLOCKING: Phase 2 configuration cannot begin until Project ID format approved (BRD 3.8.4.5)

Implementation in Airtable:

-   If sequential format: Create formula field that auto-generates IDs based on creation date + counter

-   If manual format: Document clear naming protocol; train team on ID creation rules

-   Include Project ID validation: Flag any duplicate IDs or format violations

## 4.4 Airtable Webhook Automation Specifications

### 4.4.1 Webhook Automation Overview

Purpose: Trigger event-driven synchronization from Airtable to HubSpot when project data changes

Trigger Events:

1.  New Paid Project: Project Status changes to "Paid"

2.  Phase Change: Project Phase field changes (for Paid/Active projects only)

Implementation Method: Airtable Automations with Webhook actions

Destination: Zapier Catch Hook (webhook receiver)

### 4.4.2 Webhook Automation 1: New Paid Project Sync

Automation Name: "HubSpot Sync - New Paid Project"

Trigger:

-   When: Record matches conditions

-   Table: Projects

-   Conditions:

    -   Status changes to "Paid"

    -   Project ID is not empty

Actions:

Action 1: Find Records (get associated Contacts)

-   Search in: Contacts table

-   Where: Associated Projects contains Trigger Record Project ID

-   Result: List of all Contact records linked to this project

Action 2: Webhook POST to Zapier

-   URL: <https://hooks.zapier.com/hooks/catch/ZAPIER_WEBHOOK_ID/HOOK_ID/>

    -   (Zapier will provide this URL during Phase 2 integration setup)

-   Method: POST

-   Headers:

    -   Content-Type: application/json

-   Payload: (JSON structure)

{ "trigger_type": "new_paid_project", "airtable_record_id": "Projects Record ID", "project_id": "Projects: Project ID", "project_name": "Projects: Project Name", "project_phase": "Projects: Phase", "primary_poc_email": "Projects: Primary POC → Email", "backup_poc_email": "Projects: Backup POC → Email", "primary_poc_hubspot_id": "Projects: Primary POC → HubSpot User ID", "backup_poc_hubspot_id": "Projects: Backup POC → HubSpot User ID", "contacts": \[ { "contact_name": "Contact 1: Contact Name", "email1": "Contact 1: Email 1", "email1_label": "Contact 1: Email 1 Label", "email2": "Contact 1: Email 2", "email2_label": "Contact 1: Email 2 Label", "email3": "Contact 1: Email 3", "email3_label": "Contact 1: Email 3 Label", "phone1": "Contact 1: Phone 1", "phone1_label": "Contact 1: Phone 1 Label", "phone2": "Contact 1: Phone 2", "phone2_label": "Contact 1: Phone 2 Label", "phone3": "Contact 1: Phone 3", "phone3_label": "Contact 1: Phone 3 Label", "phone4": "Contact 1: Phone 4", "phone4_label": "Contact 1: Phone 4 Label", "contact_role": "Contact 1: Contact Role", "preferred_contact_method": "Contact 1: Preferred Contact Method" } // Additional contact objects for Contact 2, Contact 3, etc. \], "sync_timestamp": "Current Timestamp ISO 8601 format" }

Payload Notes:

-   Repeat contacts array for each Contact record linked to the project

-   If a field is empty in Airtable, include it in JSON as null or empty string (Zapier will handle)

-   sync_timestamp uses Airtable's NOW() formula in ISO 8601 format

Error Handling:

-   If webhook POST fails, Airtable automation will retry up to 3 times with 1-minute delay

-   After 3 failures, automation logs error to Airtable "Sync Errors" table (Josh creates this table)

-   Josh monitors "Sync Errors" table daily during first 30 days post-launch

### 4.4.3 Webhook Automation 2: Phase Change Sync

Automation Name: "HubSpot Sync - Phase Change"

Trigger:

-   When: Record matches conditions

-   Table: Projects

-   Conditions:

    -   Phase changes

    -   Status is one of: "Paid", "Active"

    -   Project ID is not empty

Actions:

Action 1: Webhook POST to Zapier

-   URL: <https://hooks.zapier.com/hooks/catch/ZAPIER_WEBHOOK_ID/HOOK_ID/>

    -   (Different Hook ID than New Paid Project webhook)

-   Method: POST

-   Headers:

    -   Content-Type: application/json

-   Payload: (JSON structure)

{ "trigger_type": "phase_change", "airtable_record_id": "Projects Record ID", "project_id": "Projects: Project ID", "new_phase": "Projects: Phase", "primary_poc_email": "Projects: Primary POC → Email", "backup_poc_email": "Projects: Backup POC → Email", "primary_poc_hubspot_id": "Projects: Primary POC → HubSpot User ID", "backup_poc_hubspot_id": "Projects: Backup POC → HubSpot User ID", "sync_timestamp": "Current Timestamp ISO 8601 format" }

Rationale for Separate Webhook:

-   Phase Change sync is lighter payload (no contact data refresh needed)

-   Allows Zapier to route to different workflows based on trigger type

-   Simplifies troubleshooting and error handling

Error Handling: Same as New Paid Project automation (3 retries, log to Sync Errors table)

## 4.5 Airtable Data Validation and Quality Controls

### 4.5.1 Required Data Quality Rules

Implementation Method: Airtable field validation + conditional formatting

Validation Rules:

| **Field** | **Validation Rule** | **Error Message** | **Enforcement** |
| --- | --- | --- | --- |
| Project ID | Must be unique across all records | "Duplicate Project ID detected" | Airtable unique field constraint |
| Project Status | Required when record created | "Project Status required" | Mark field as required |
| Phase | Required when Status = Paid/Active | "Phase required for Paid projects" | Conditional logic or manual review |
| Primary POC | Required when Status = Paid/Active | "Primary POC required for Paid projects" | Conditional logic |
| Backup POC | Required when Status = Paid/Active; Cannot equal Primary POC | "Backup POC required and must differ from Primary" | Conditional formatting to flag violations |
| Client Contacts | At least one Contact linked when Status = Paid | "Paid projects require at least one client contact" | Manual review during project setup |

Conditional Formatting (Visual Alerts):

-   Red background: Phase field empty when Status = Paid/Active

-   Yellow background: Backup POC equals Primary POC (data error)

-   Orange background: Client Contacts empty when Status = Paid

### 4.5.2 Phase-to-POC Mapping Validation

Purpose: Ensure POC assignments align with BRD Appendix C mapping table

Implementation Options:

Option 1: Formula Field Validation (Recommended)

-   Create formula field "POC Validation" that checks if current Primary POC matches expected POC for current Phase

-   Formula logic: IF(AND({Phase} = "PreDesign", {Primary POC Email} = "<molly@livingwithlolo.com>"), "✓ Correct", IF(AND({Phase} = "Design", {Primary POC Email} = "<sara@livingwithlolo.com>"), "✓ Correct", \... continue for all phases \... "⚠ Verify POC Assignment"))

-   Displays warning icon if POC doesn't match expected phase mapping

-   Manual override allowed (some projects may have non-standard POC assignments)

Option 2: Automation Alert (Alternative)

-   Airtable automation triggers when Phase changes

-   Compares new Primary POC against expected POC for that phase

-   Sends Slack/email alert to Josh if mismatch detected

-   Josh manually reviews and updates if needed

Decision: Josh selects preferred validation method during Phase 1 implementation; both approaches acceptable.

### 4.5.3 Contact Data Completeness Checks

Purpose: Ensure all client contacts have minimum required information for HubSpot routing

Required Fields for Sync:

-   Contact Name (required)

-   At least one Email OR at least one Phone (required)

-   Associated Projects linked (required)

Validation View in Airtable:

-   Create filtered view "Incomplete Contacts" showing records where:

    -   Contact Name is empty, OR

    -   All Email fields empty AND all Phone fields empty, OR

    -   Associated Projects is empty

Review Cadence: Josh reviews "Incomplete Contacts" view before each Phase 2-3 sync test to ensure data quality.

## 4.6 Airtable Maintenance and Monitoring

### 4.6.1 Ongoing Airtable Maintenance Tasks

Josh's Responsibilities:

| **Task** | **Frequency** | **Procedure** |
| --- | --- | --- |
| Monitor Sync Errors Table | Daily (first 30 days), then weekly | Review any failed webhook attempts; retry manually or investigate root cause |
| Validate POC Assignments | Weekly | Review "POC Validation" warnings; confirm intentional overrides vs. data errors |
| Update Phase-to-POC Mapping | When team structure changes | Update formula fields or lookup tables if POC assignments change |
| Review Contact Completeness | Before each new project sync | Check "Incomplete Contacts" view; remediate missing data |
| Audit Project ID Uniqueness | Monthly | Run duplicate detection on Project ID field; resolve conflicts |
| Backup Airtable Base | Automatically daily (Airtable native) | Verify backup history available if restoration needed |

### 4.6.2 Escalation Path for Airtable Issues

Level 1 - Josh (Airtable Administrator):

-   Schema changes, field additions, formula updates

-   Webhook automation troubleshooting

-   Data quality remediation

-   Zapier workflow monitoring (in collaboration with LWL IT Lead)

Level 2 - LWL IT Lead:

-   Complex sync issues requiring HubSpot-side investigation

-   Integration architecture changes

-   Zapier workflow structural changes

-   Cross-platform troubleshooting (Airtable + HubSpot)

Level 3 - Vendor Support:

-   Airtable platform bugs or outages → Airtable Support

-   HubSpot API issues → HubSpot Support

-   Zapier webhook delivery failures → Zapier Support

Escalation Criteria:

-   Sync failures persisting more than 24 hours → Escalate to Level 2

-   Data corruption or loss → Immediate escalation to Level 2

-   Platform outages → Monitor vendor status pages, escalate to Level 3 if needed