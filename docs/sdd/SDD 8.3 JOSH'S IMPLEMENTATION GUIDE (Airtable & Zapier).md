---
source: SDD - System Design Document - Consolidated Communication PART TWO v1.docx
section: 8.3 JOSH'S IMPLEMENTATION GUIDE (Airtable & Zapier)
integrity: full
format: preservation_mode
encoding: utf-8
extraction_method: paragraph_and_table_parser
order_preserved: true
tables_preserved: true
revision: 1.1
strict_lossless_mode: true
---

## 8.3 JOSH'S IMPLEMENTATION GUIDE (Airtable & Zapier)

### 8.3.1 Webhook 1: New Paid Project Trigger

#### 8.3.1.1 Step C1.5.1: Create Zap for New Paid Project Webhook

1. In Zapier dashboard, navigate to "Zaps" in left sidebar

2. Click "Create Zap" (button, top right)

3. Zap creation wizard opens

**Configure Trigger:**

1. Trigger app: Search "Webhooks by Zapier"

2. Select "Webhooks by Zapier" from results

3. Trigger event: Select "Catch Hook"

4. Description of Catch Hook: "This trigger will generate a custom webhook URL that can receive POST requests from external services. When Airtable sends a webhook, Zapier will capture the payload and make it available to subsequent workflow steps."

5. Click "Continue"

**Webhook Configuration:**

1. Zapier displays: "To get your webhook URL, first set up a sample webhook"

2. Click "Skip Test" (we'll test after Airtable automation built)

3. **CRITICAL:** Zapier generates custom webhook URL

4. Webhook URL format: https://hooks.zapier.com/hooks/catch/[ACCOUNT_ID]/[HOOK_ID]/

   - Example: https://hooks.zapier.com/hooks/catch/123456/abcdef/

5. **COPY THIS URL IMMEDIATELY**

   - Click "Copy to clipboard" button next to webhook URL

   - Paste into temporary notepad/document for safekeeping

   - **THIS URL IS SENSITIVE** - treat as confidential credential

**Save Zap (Partial Configuration):**

1. Click "Settings" icon (gear, top right of Zap editor)

2. Zap name: "TEST - New Paid Project Sync"

   - Prefix "TEST" indicates this is development version

   - Will rename to "New Paid Project Sync" (without TEST prefix) when moved to Production Workflows folder

3. Folder: "Testing Workflows"

4. Description: "Webhook receiver for Airtable New Paid Project automation. Triggers when project Status changes to Paid. Syncs project metadata and contacts to HubSpot."

5. Click "Save" (top right)

6. Zap now saved with just Trigger configured

7. **DO NOT turn Zap ON yet** - Action steps will be added in Configuration Step D2

**Webhook URL Validation:**

1. Verify webhook URL copied correctly:

   - Must start with https://hooks.zapier.com/hooks/catch/

   - Must end with / (trailing slash)

   - Must contain two IDs separated by / (account ID and hook ID)

   - Should be approximately 50-70 characters total

2. If URL doesn't match format: Re-copy from Zap trigger configuration

### 8.3.2 Webhook 2: Phase Change Trigger

#### 8.3.2.1 Step C1.5.2: Create Zap for Phase Change Webhook

1. Return to Zapier dashboard (click "Zapier" logo top left)

2. Click "Create Zap" again (new Zap, not editing previous)

3. Zap creation wizard opens

**Configure Trigger:**

1. Trigger app: Search "Webhooks by Zapier"

2. Select "Webhooks by Zapier"

3. Trigger event: Select "Catch Hook"

4. Click "Continue"

**Webhook Configuration:**

1. Click "Skip Test"

2. Zapier generates SECOND custom webhook URL (DIFFERENT from Webhook 1)

3. Webhook URL format: https://hooks.zapier.com/hooks/catch/[ACCOUNT_ID]/[DIFFERENT_HOOK_ID]/

   - **IMPORTANT:** Hook ID portion will be DIFFERENT from Webhook 1

   - Example: https://hooks.zapier.com/hooks/catch/123456/xyz789/

   - Account ID portion (first number) will be SAME as Webhook 1

4. **COPY THIS SECOND URL IMMEDIATELY**

   - Click "Copy to clipboard"

   - Paste into temporary notepad/document

   - Keep separate from Webhook 1 URL

**Save Zap (Partial Configuration):**

1. Click "Settings" icon (gear, top right)

2. Zap name: "TEST - Phase Change Sync"

3. Folder: "Testing Workflows"

4. Description: "Webhook receiver for Airtable Phase Change automation. Triggers when project Phase field changes. Updates HubSpot Deal stage and POC assignments."

5. Click "Save"

6. Zap now saved with just Trigger configured

7. **DO NOT turn Zap ON yet**

#### 8.3.2.2 Step C1.5.3: Document Webhook URLs for Handoff to Johnny

**Purpose:** Johnny needs both webhook URLs for potential troubleshooting during Phase 3 testing (though he doesn't use them directly - Josh uses them in Airtable automations).

**Create Webhook URLs Document:**

1. Create new document: "Zapier Webhook URLs - LWL Communications Hub" (Google Doc or text file)

2. Document content:

ZAPIER WEBHOOK URLS - LIVING WITH LOLO COMMUNICATIONS HUB

Configuration Step C1 - Created: [Today's Date]

These webhook URLs are used by Airtable automations to trigger Zapier workflows.

WEBHOOK 1: NEW PAID PROJECT SYNC

Purpose: Triggered when Airtable project Status changes to "Paid"

Zapier Zap Name: TEST - New Paid Project Sync (will become "New Paid Project Sync" in production)

Webhook URL: [Paste Webhook 1 URL here]

Usage: Josh will paste this URL into Airtable "HubSpot Sync - New Paid Project" automation (Configuration Step D1)

WEBHOOK 2: PHASE CHANGE SYNC

Purpose: Triggered when Airtable project Phase field changes

Zapier Zap Name: TEST - Phase Change Sync (will become "Phase Change Sync" in production)

Webhook URL: [Paste Webhook 2 URL here]

Usage: Josh will paste this URL into Airtable "HubSpot Sync - Phase Change" automation (Configuration Step D1)

SECURITY NOTE:

- These URLs are sensitive credentials

- Anyone with these URLs can send data to Zapier workflows

- Do not share publicly or commit to code repositories

- If URLs are compromised, regenerate webhooks in Zapier and update Airtable automations

REGENERATION PROCEDURE (if needed):

1. In Zapier, edit affected Zap

2. Delete existing Catch Hook trigger

3. Re-add Catch Hook trigger (generates new URL)

4. Copy new URL

5. Update corresponding Airtable automation with new URL

6. Test webhook delivery

Contact: Josh [email] for questions about webhook configuration

3. Save document to secure location (LWL shared drive or password-protected folder)

**Handoff to Johnny:**

1. Email Johnny with subject: "Zapier Webhook URLs for HubSpot Integration"

2. Email body:

Johnny,

I've completed Configuration Step C1 (Zapier account setup and webhook creation). Here are the two Zapier webhook URLs for the Airtable-to-HubSpot integration:

WEBHOOK 1 (New Paid Project):

[Paste URL]

WEBHOOK 2 (Phase Change):

[Paste URL]

Please store these securely. I will use these URLs in Airtable webhook automations during Configuration Step D1. These URLs are sensitive credentials - treat as confidential.

Next steps:

- You can now proceed with Configuration Step C2 (building HubSpot workflows)

- I will proceed with Configuration Step D1 (building Airtable automations) once you complete your HubSpot workflow configuration

- We'll coordinate for Phase 3 joint testing once both configuration groups complete

Let me know when you've received and stored these URLs securely.

Thanks,

Josh

3. Attach: "Zapier Webhook URLs" document

4. Send email

5. **WAIT for Johnny's confirmation reply** before proceeding to Configuration Step D1

**Configuration Step C1 Complete - Checkpoint:**

**Josh's Self-Validation:**

- ☐ Zapier account created and Starter subscription active

- ☐ Workspace "Living With Lolo - Communications Hub" created

- ☐ Folders created: Production Workflows, Testing Workflows

- ☐ Airtable connection established and tested

- ☐ HubSpot connection established and tested

- ☐ Webhook 1 created: TEST - New Paid Project Sync

- ☐ Webhook 2 created: TEST - Phase Change Sync

- ☐ Both webhook URLs copied and documented

- ☐ Webhook URLs document created

- ☐ Webhook URLs emailed to Johnny

- ☐ Waiting for Johnny's confirmation receipt

**Expected from Johnny:**

- Reply email: "Webhook URLs received and stored securely"

- Once received, Josh can proceed to Configuration Step D1

**Configuration Group C Partial Complete - Johnny now builds HubSpot workflows (Configuration Step C2) while Josh waits**

### 8.3.3 Build Airtable Webhook Automations

**Purpose:** Create two Airtable automations that detect project changes and send webhook POST requests to Zapier, triggering synchronization to HubSpot. This corresponds to Configuration Step D1 from Section 8.2.3.

**PREREQUISITES:**

- Configuration Group C complete (Josh has two Zapier webhook URLs)

- Johnny completed Configuration Step C2 (HubSpot workflows built)

**CRITICAL SUCCESS FACTORS:**

- JSON payload structure must match EXACTLY what Zapier workflows expect

- Phase field values must match BRD Appendix C exactly (case-sensitive)

- Test webhook delivery before proceeding to Zapier workflow configuration

#### 8.3.3.1 Automation 1: HubSpot Sync - New Paid Project

**Purpose:** When a project's Status changes to "Paid" in Airtable, trigger webhook to Zapier containing complete project metadata and all linked contact information.

##### 8.3.3.1.1 Step D1.1: Create Automation in Airtable

1. Navigate to Airtable base: "Living With Lolo"

2. Open "Projects" table

3. Click "Automations" button (top right, next to "Extensions")

4. Click "Create automation"

5. Automation name: "HubSpot Sync - New Paid Project"

6. Description: "Triggers when project Status changes to Paid. Sends webhook to Zapier with project metadata and all client contacts."

##### 8.3.3.1.2 Step D1.2: Configure Trigger

1. Click "Add trigger"

2. Trigger type: Select "When record matches conditions"

3. Table: Projects (should be pre-selected)

4. Configure conditions:

   - Click "Add condition"

   - **Condition 1:** "When Project Status" → "changes to" → "Paid"

   - Click "Add condition" (AND logic)

   - **Condition 2:** "When Project ID" → "is not empty"

   - Rationale: Ensures we only sync projects with valid Project IDs; prevents sync failures

5. Click "Done"

6. Test trigger:

   - Airtable shows: "Test trigger to continue"

   - Use existing sample project or create temporary test project:

     - Navigate to Projects table

     - Create record: Project ID "TEST-WEBHOOK-001", Status "Lead"

     - Return to automation

   - Click "Test trigger"

   - Change test project Status from "Lead" to "Paid"

   - Airtable detects trigger: "Found a record that matches your conditions"

   - Record details display (Project ID, Status = Paid, etc.)

7. Click "Continue" if test successful

##### 8.3.3.1.3 Step D1.3: Add Action 1 - Find Linked Contact Records

**Purpose:** Retrieve all Contact records linked to this project before building webhook payload.

1. Click "Add action" (below trigger)

2. Action type: Search "Find records"

3. Select "Find records" action

4. Configure action:

   - Table: "Contacts"

   - Conditions: Click "Add condition"

   - **Condition:** "Where Associated Projects" → "contains" → [Dynamic field] "Projects: Project ID" (from trigger)

     - To insert dynamic field: Click field, select "Step 1: When record matches conditions" → "Project ID"

   - Max records: 10 (allows up to 10 contacts per project - adjust if LWL projects typically have more)

5. Test action:

   - Click "Test action"

   - Airtable searches Contacts table for records linked to test project

   - Expected result: "Found [X] records" where X = number of contacts linked to test project

   - Airtable displays contact details (names, emails, phones)

   - If 0 records found: Verify test project has contacts linked; add test contact if needed

6. Click "Continue" if test successful

##### 8.3.3.1.4 Step D1.4: Add Action 2 - Send Webhook POST to Zapier

**Purpose:** Build JSON payload containing project metadata and contacts array, then POST to Zapier webhook URL.

1. Click "Add action"

2. Action type: Search "Webhook"

3. Select "Send webhook" action

4. Configure webhook:

   - URL: [Paste Webhook 1 URL from Configuration Step C1.5.1]

     - Example: https://hooks.zapier.com/hooks/catch/123456/abcdef/

     - **CRITICAL:** Verify URL is for "New Paid Project" webhook (not Phase Change webhook)

   - Method: POST

   - Headers:

     - Click "Add header"

     - Key: Content-Type

     - Value: application/json

   - Body:

     - **CRITICAL:** Must be valid JSON structure

     - Click "Switch to Code" (top right of Body field) for easier JSON editing

     - Paste following JSON template, then customize with dynamic fields:

{

"trigger_type": "new_paid_project",

"airtable_record_id": "",

"project_id": "",

"project_name": "",

"project_phase": "",

"primary_poc_email": "",

"backup_poc_email": "",

"primary_poc_hubspot_id": "",

"backup_poc_hubspot_id": "",

"contacts": [],

"sync_timestamp": ""

}

##### 8.3.3.1.5 Step D1.5: Populate JSON Payload with Dynamic Fields

**IMPORTANT:** Airtable's "Insert variable" feature inserts dynamic field references. Click cursor position in JSON where value should appear, then click "+" button to insert field from previous steps.

**Populate each field (click into quotes, then insert dynamic field):**

1. airtable_record_id:

   - Position cursor between quotes: "airtable_record_id": ""

   - Click "+" → Select "Step 1: When record matches conditions" → "Airtable Record ID"

   - Result: "airtable_record_id": "{Airtable Record ID from Step 1}"

2. project_id:

   - Position cursor: "project_id": ""

   - Insert: Step 1 → "Project ID"

   - Result: "project_id": "{Project ID from Step 1}"

3. project_name:

   - Position cursor: "project_name": ""

   - Insert: Step 1 → "Project Name"

   - Result: "project_name": "{Project Name from Step 1}"

4. project_phase:

   - Position cursor: "project_phase": ""

   - Insert: Step 1 → "Phase"

   - Result: "project_phase": "{Phase from Step 1}"

   - **CRITICAL:** This field must contain EXACT phase spelling (PreDesign, Design, Procurement, PreConstruction, Construction)

5. primary_poc_email:

   - Position cursor: "primary_poc_email": ""

   - Insert: Step 1 → "Primary POC" → "Email" (follow relationship chain)

   - Airtable shows: "Primary POC → Email"

   - Result: "primary_poc_email": "{Primary POC Email from Step 1}"

6. backup_poc_email:

   - Position cursor: "backup_poc_email": ""

   - Insert: Step 1 → "Backup POC" → "Email"

   - Result: "backup_poc_email": "{Backup POC Email from Step 1}"

7. primary_poc_hubspot_id:

   - Position cursor: "primary_poc_hubspot_id": ""

   - Insert: Step 1 → "Primary POC" → "HubSpot User ID"

   - Result: "primary_poc_hubspot_id": "{Primary POC HubSpot User ID from Step 1}"

   - **NOTE:** This must be numeric HubSpot User ID (not email)

8. backup_poc_hubspot_id:

   - Position cursor: "backup_poc_hubspot_id": ""

   - Insert: Step 1 → "Backup POC" → "HubSpot User ID"

   - Result: "backup_poc_hubspot_id": "{Backup POC HubSpot User ID from Step 1}"

9. contacts array:

   - This is the MOST COMPLEX part - contacts array must include ALL contacts found in Step 2

   - Position cursor after opening bracket: "contacts": [] becomes "contacts": [ ]

   - Press Enter to create multi-line array (easier to read)

   - Insert dynamic field: Click "+" → Select "Step 2: Find records" → "All fields (with line items)"

   - Airtable inserts repeating group syntax (iterates through all found contacts)

   - Result structure (Airtable's syntax varies, but conceptually):

"contacts": [

{

"contact_name": "{Contact Name from Step 2}",

"email1": "{Email 1 from Step 2}",

"email1_label": "{Email 1 Label from Step 2}",

"email2": "{Email 2 from Step 2}",

"email2_label": "{Email 2 Label from Step 2}",

"email3": "{Email 3 from Step 2}",

"email3_label": "{Email 3 Label from Step 2}",

"phone1": "{Phone 1 from Step 2}",

"phone1_label": "{Phone 1 Label from Step 2}",

"phone2": "{Phone 2 from Step 2}",

"phone2_label": "{Phone 2 Label from Step 2}",

"phone3": "{Phone 3 from Step 2}",

"phone3_label": "{Phone 3 Label from Step 2}",

"phone4": "{Phone 4 from Step 2}",

"phone4_label": "{Phone 4 Label from Step 2}",

"contact_role": "{Contact Role from Step 2}",

"preferred_contact_method": "{Preferred Contact Method from Step 2}"

}

]

**IMPORTANT AIRTABLE SYNTAX NOTE:**

- Airtable may use different syntax for repeating groups (line items)

- If Airtable doesn't support array notation directly, use this workaround:

  - For each contact field, insert: Step 2 → All [Field Name] (returns comma-separated list)

  - Example: "email1": "{All Email 1 from Step 2}" becomes "john@example.com,sarah@example.com"

  - Zapier will parse comma-separated values as array in next step

- Consult Airtable automation documentation if syntax unclear: support.airtable.com/docs/sending-webhooks-from-airtable-automations

10. sync_timestamp:

- Position cursor: "sync_timestamp": ""

- Airtable doesn't have built-in ISO 8601 timestamp function in automations

- Workaround: Insert "Last Modified" field from Step 1 (close enough for timestamp)

- Insert: Step 1 → "Last Modified"

- Result: "sync_timestamp": "{Last Modified from Step 1}"

- Alternative: Use formula field in Projects table with NOW() function, then reference that field

##### 8.3.3.1.6 Step D1.6: Validate JSON Payload Structure

After populating all dynamic fields, JSON should look similar to:

{

"trigger_type": "new_paid_project",

"airtable_record_id": "{Airtable Record ID from Step 1}",

"project_id": "{Project ID from Step 1}",

"project_name": "{Project Name from Step 1}",

"project_phase": "{Phase from Step 1}",

"primary_poc_email": "{Primary POC Email from Step 1}",

"backup_poc_email": "{Backup POC Email from Step 1}",

"primary_poc_hubspot_id": "{Primary POC HubSpot User ID from Step 1}",

"backup_poc_hubspot_id": "{Backup POC HubSpot User ID from Step 1}",

"contacts": [

{

"contact_name": "{Contact Name from Step 2}",

"email1": "{Email 1 from Step 2}",

...additional contact fields...

}

],

"sync_timestamp": "{Last Modified from Step 1}"

}

**Validation Checklist:**

- ☐ All curly braces { } and square brackets [ ] matched (balanced)

- ☐ All commas present between key-value pairs (except last pair before closing brace)

- ☐ All field names in double quotes

- ☐ All dynamic field references inserted (visible as {Field Name from Step X})

- ☐ No syntax errors highlighted by Airtable (red underlines or error messages)

**If JSON validation fails:**

- Copy JSON payload to online validator: jsonlint.com

- Paste payload (replace dynamic fields with sample values for validation)

- Fix any syntax errors identified

- Re-insert dynamic fields in corrected JSON

##### 8.3.3.1.7 Step D1.7: Configure Error Handling

**Purpose:** Retry failed webhook deliveries, then log errors to Sync Errors table after max retries exhausted.

1. In webhook action configuration, scroll to "Error handling" section

2. Click "Customize error handling"

3. Configure retry logic:

   - Enable: ☐ "Retry on failure"

   - Max retries: 3

   - Retry delay: 1 minute

   - Rationale: Per BRD Section 3.11.5.2, automatic retry up to 3 attempts before logging error

4. Click "Add action" (for error path - triggers only if webhook fails after 3 retries)

5. Action type: "Create record"

6. Table: "Sync Errors"

7. Configure fields:

   - Error Timestamp: (Auto-populated by field default - uses created time)

   - Project ID: Insert dynamic field → Step 1 → "Project ID"

   - Error Type: "Webhook Failed" (static text)

   - Error Message: Insert dynamic field → Step 3 (Webhook) → "Error message" (if available) OR manually type "Webhook POST failed after 3 retry attempts"

   - Retry Count: 3 (static number)

   - Resolved: (Leave unchecked - default)

   - Resolution Notes: (Leave empty)

8. Test error logging:

   - Difficult to test without intentionally breaking webhook

   - Skip test for now - will validate during Phase 3 Testing Step B5

9. Click "Done"

##### 8.3.3.1.8 Step D1.8: Test Complete Automation

1. Click "Test automation" (bottom of automation editor)

2. Airtable prompts: "Test your automation with real data"

3. Test method options:

   - Option A: Use existing test project (TEST-WEBHOOK-001 created earlier)

   - Option B: Create new test project specifically for this test

4. If using Option A:

   - Navigate to Projects table

   - Find TEST-WEBHOOK-001 (or create if deleted)

   - Ensure Status = "Lead" (not "Paid" yet)

   - Ensure project has at least 1 linked contact

5. Return to automation editor

6. Click "Run test"

7. Change TEST-WEBHOOK-001 Status from "Lead" to "Paid"

8. Airtable automation executes:

   - Step 1 (Trigger): Detects Status change

   - Step 2 (Find contacts): Retrieves linked contacts

   - Step 3 (Webhook): Sends POST to Zapier

9. Check results:

   - Automation history shows "Success" for all steps

   - Step 3 webhook shows: "Request sent successfully" with response code 200

   - **CRITICAL:** Navigate to Zapier (in separate browser tab)

   - Open Zap "TEST - New Paid Project Sync"

   - Click "Zap History" (left sidebar)

   - Most recent run should show "Success" with timestamp matching test

   - Click into run details

   - Verify payload received correctly (all fields populated)

10. If test fails:

   - Review error message in Airtable automation history

   - Common errors:

     - "Invalid JSON": Syntax error in payload - review Step D1.6 validation

     - "400 Bad Request": Webhook URL incorrect - verify URL from Step C1.5.1

     - "404 Not Found": Webhook URL invalid - regenerate webhook in Zapier

     - "Timeout": Zapier temporarily unavailable - retry test

   - Fix error, re-test until successful

##### 8.3.3.1.9 Step D1.9: Set Automation to Inactive (Not Production Yet)

**IMPORTANT:** Do not activate this automation for production use until Phase 3 integration testing complete.

1. In automation editor, top right: Toggle shows "Active" or "Inactive"

2. Ensure toggle is set to "INACTIVE" (gray, not blue)

3. Rationale: Prevents accidental production webhook triggers during development

4. Automation will be activated during Phase 3 Testing Group B

##### 8.3.3.1.10 Step D1.10: Document Automation for Reference

Create entry in implementation notes:

AUTOMATION 1: HubSpot Sync - New Paid Project

Status: Built and tested; set to INACTIVE (will activate in Phase 3)

Trigger: When Projects: Status changes to "Paid" AND Project ID is not empty

Actions:

1. Find records in Contacts where Associated Projects contains Project ID

2. Send webhook POST to Zapier (Webhook 1 URL)

3. Payload: Project metadata + contacts array (JSON)

4. On error: Log to Sync Errors table after 3 retries

Test Date: [Today's date]

Test Result: Success - webhook delivered to Zapier, payload structure validated

Notes:

- Contacts array uses Airtable line items syntax

- Phase field must match BRD Appendix C exactly for HubSpot POC assignment

- Error handling creates Sync Errors record after 3 failed retries

#### 8.3.3.2 Automation 2: HubSpot Sync - Phase Change

**Purpose:** When a project's Phase field changes in Airtable (for Paid/Active projects), trigger webhook to Zapier containing Project ID and new phase value.

##### 8.3.3.2.1 Step D1.11: Create Second Automation

1. Return to Airtable Projects table

2. Click "Automations" button

3. Click "Create automation"

4. Automation name: "HubSpot Sync - Phase Change"

5. Description: "Triggers when project Phase field changes (for Paid/Active projects). Sends webhook to Zapier to update HubSpot Deal stage and POC assignments."

##### 8.3.3.2.2 Step D1.12: Configure Trigger

1. Click "Add trigger"

2. Trigger type: "When record matches conditions"

3. Table: Projects

4. Configure conditions:

   - **Condition 1:** "When Phase" → "changes"

   - Click "Add condition" (AND logic)

   - **Condition 2:** "When Project Status" → "is one of" → Select "Paid" and "Active"

     - Rationale: Only sync phase changes for active projects (not Leads or Proposals)

   - Click "Add condition"

   - **Condition 3:** "When Project ID" → "is not empty"

5. Click "Done"

6. Test trigger:

   - Use TEST-WEBHOOK-001 (Status should be "Paid" from previous test)

   - Current Phase: "PreDesign" (or whatever was set)

   - Click "Test trigger"

   - Change TEST-WEBHOOK-001 Phase from "PreDesign" to "Design"

   - Airtable detects trigger: "Found a record"

7. Click "Continue" if successful

##### 8.3.3.2.3 Step D1.13: Add Action - Send Webhook POST to Zapier

**Note:** This automation is SIMPLER than Automation 1 - no contact data retrieval needed (phase change doesn't affect contact information).

1. Click "Add action"

2. Action type: "Send webhook"

3. Configure webhook:

   - URL: [Paste Webhook 2 URL from Configuration Step C1.5.2]

     - **CRITICAL:** This is DIFFERENT URL than Automation 1

     - Verify URL is for "Phase Change" webhook

   - Method: POST

   - Headers:

     - Key: Content-Type

     - Value: application/json

   - Body: Click "Switch to Code"

   - Paste following JSON template:

{

"trigger_type": "phase_change",

"airtable_record_id": "",

"project_id": "",

"new_phase": "",

"primary_poc_email": "",

"backup_poc_email": "",

"primary_poc_hubspot_id": "",

"backup_poc_hubspot_id": "",

"sync_timestamp": ""

}

##### 8.3.3.2.4 Step D1.14: Populate JSON Payload with Dynamic Fields

Insert dynamic fields (same process as Automation 1):

1. **airtable_record_id:** Step 1 → "Airtable Record ID"

2. **project_id:** Step 1 → "Project ID"

3. **new_phase:** Step 1 → "Phase" (this is the NEW phase value after change)

4. **primary_poc_email:** Step 1 → "Primary POC" → "Email"

5. **backup_poc_email:** Step 1 → "Backup POC" → "Email"

6. **primary_poc_hubspot_id:** Step 1 → "Primary POC" → "HubSpot User ID"

7. **backup_poc_hubspot_id:** Step 1 → "Backup POC" → "HubSpot User ID"

8. **sync_timestamp:** Step 1 → "Last Modified"

Final JSON structure (with dynamic fields):

{

"trigger_type": "phase_change",

"airtable_record_id": "{Airtable Record ID from Step 1}",

"project_id": "{Project ID from Step 1}",

"new_phase": "{Phase from Step 1}",

"primary_poc_email": "{Primary POC Email from Step 1}",

"backup_poc_email": "{Backup POC Email from Step 1}",

"primary_poc_hubspot_id": "{Primary POC HubSpot User ID from Step 1}",

"backup_poc_hubspot_id": "{Backup POC HubSpot User ID from Step 1}",

"sync_timestamp": "{Last Modified from Step 1}"

}

##### 8.3.3.2.5 Step D1.15: Configure Error Handling

(Same as Automation 1)

1. Enable "Retry on failure": Max 3 retries, 1-minute delay

2. Add action (error path): "Create record" in Sync Errors table

   - Error Timestamp: Auto

   - Project ID: Step 1 → "Project ID"

   - Error Type: "Webhook Failed"

   - Error Message: "Phase Change webhook POST failed after 3 retries"

   - Retry Count: 3

3. Click "Done"

##### 8.3.3.2.6 Step D1.16: Test Complete Automation

1. Click "Test automation"

2. Use TEST-WEBHOOK-001

3. Change Phase from current value to different phase (e.g., "Design" to "Procurement")

4. Automation executes:

   - Step 1 (Trigger): Detects Phase change

   - Step 2 (Webhook): Sends POST to Zapier

5. Verify in Zapier:

   - Navigate to Zap "TEST - Phase Change Sync"

   - Click "Zap History"

   - Most recent run shows "Success"

   - Payload contains correct new_phase value

6. If test fails: Troubleshoot using same process as Automation 1 (Step D1.8)

##### 8.3.3.2.7 Step D1.17: Set Automation to Inactive

1. Ensure automation toggle set to "INACTIVE"

2. Will activate during Phase 3 Testing Group B

##### 8.3.3.2.8 Step D1.18: Document Automation

AUTOMATION 2: HubSpot Sync - Phase Change

Status: Built and tested; set to INACTIVE

Trigger: When Projects: Phase changes AND Status is one of (Paid, Active) AND Project ID is not empty

Actions:

1. Send webhook POST to Zapier (Webhook 2 URL)

2. Payload: Project ID, new phase, POC info (simpler than Automation 1 - no contacts)

3. On error: Log to Sync Errors table after 3 retries

Test Date: [Today's date]

Test Result: Success - webhook delivered, payload validated

Notes:

- Lighter payload than New Paid Project (no contact array refresh needed)

- new_phase field drives HubSpot POC Assignment workflow

- Critical that phase spelling matches BRD Appendix C exactly

**Configuration Step D1 Complete - Checkpoint:**

**Josh's Self-Validation:**

- [ ] Automation 1 "HubSpot Sync - New Paid Project" created and tested

- [ ] Automation 1 JSON payload validated (all fields populated correctly)

- [ ] Automation 1 webhook delivery confirmed in Zapier history

- [ ] Automation 1 set to INACTIVE (not production)

- [ ] Automation 2 "HubSpot Sync - Phase Change" created and tested

- [ ] Automation 2 JSON payload validated

- [ ] Automation 2 webhook delivery confirmed in Zapier history

- [ ] Automation 2 set to INACTIVE

- [ ] Error handling configured for both automations (3 retries + Sync Errors logging)

- [ ] Both automations documented for reference

**Notification to Johnny:**

- Email Johnny with subject: "Airtable webhook automations complete - ready for Zapier workflow configuration"

- Email body: "Johnny - Configuration Step D1 is complete. Both Airtable automations are built and tested (set to INACTIVE for now). Webhooks are successfully delivering to Zapier. I'm ready to proceed to Configuration Step D2 (building Zapier workflows). Both automations will be activated during Phase 3 Testing Group B once full end-to-end integration is validated."

**Josh Can Now Proceed:** Configuration Step D2 (Build Zapier Workflows)

### 8.3.4 Test 7: Zapier Workflow 3 - Weekly Baseline Sync

**Objective:** Verify Weekly Baseline Sync processes all Paid projects correctly.

**Prerequisites:**

- Zapier Workflow 3 temporarily set to ON

- Multiple test projects exist in Airtable with Status = "Paid" or "Active"

- Some projects already synced to HubSpot, some missing (to test both paths)

**Test Preparation:**

1. Create 3 test projects in Airtable:

   - BASELINE-001: Status = "Paid", Phase = "PreDesign" (NOT yet in HubSpot)

   - BASELINE-002: Status = "Active", Phase = "Design" (already exists in HubSpot from prior test)

   - BASELINE-003: Status = "Paid", Phase = "Procurement" (NOT yet in HubSpot)

2. Create 1 Contact for each project

**Test Steps:**

1. In Zapier Workflow 3, click "Test" on Step 1 (Schedule) to manually trigger

2. Monitor execution:

   - Watch main loop iterate through projects

   - Verify: All 3 test projects processed

3. For BASELINE-001 and BASELINE-003:

   - Verify: Path B (Create Missing Deal) executes

   - Navigate to HubSpot, verify Deals created

4. For BASELINE-002:

   - Verify: Path A (Update Existing Deal) executes

   - Navigate to HubSpot, verify Deal updated (Last Sync Date refreshed)

5. Navigate to Airtable:

   - Verify: All 3 projects have Last HubSpot Sync field updated to current timestamp

6. Check email:

   - Verify: Weekly summary email received

   - Verify: Email shows "Total Projects Processed: 3" (or more if other projects exist)

7. Document result: PASS/FAIL

**Expected Outcome:** All Paid/Active projects reconciled with HubSpot, summary email sent.

**Troubleshooting Failed Test:**

- Loop doesn't iterate:

  - Airtable Find Records returned no results

  - Verify Filter by Formula correct: OR({Project Status} = "Paid", {Project Status} = "Active")

  - Verify test projects have correct Status values

- Some projects skipped:

  - Max Records limit reached (default 100)

  - Increase Max Records setting in Step 2

- Deals created but Contacts missing:

  - Nested loop in Path B not executing

  - Verify Contacts linked to projects in Airtable

  - Review nested loop configuration (Step D2.31)

### 8.3.5 Test 8: Multi-Contact Project

**Objective:** Verify projects with multiple contacts (exceeding HubSpot field limits) sync correctly.

**Prerequisites:**

- Zapier Workflow 1 ON

- Airtable Automation 1 active

**Test Steps:**

1. In Airtable, create project MULTI-CONTACT-001:

   - Status: "Lead"

   - Phase: "Design"

   - Link 2 Contacts:

     - Contact 1: "John Smith" (3 emails + 3 phones)

     - Contact 2: "Sarah Smith" (2 emails + 3 phones)

2. Change Status to "Paid"

3. Monitor Zapier:

   - Verify: Contacts loop iterates 2 times

   - Verify: Both contacts processed successfully

4. Navigate to HubSpot:

   - Verify: 1 Deal created for MULTI-CONTACT-001

   - Verify: 2 separate Contact records created:

     - "John Smith" with 3 emails and 3 phones

     - "Sarah Smith" with 2 emails and 3 phones

   - Verify: Both Contacts associated with same Deal

5. Document result: PASS/FAIL

**Expected Outcome:** Multiple Contacts created and correctly associated with single Deal.

### 8.3.6 Test 9: Edge Case - Empty Email and Phone

**Objective:** Verify Zapier handles Contacts with missing email/phone gracefully.

**Prerequisites:**

- Zapier Workflow 1 ON

**Test Steps:**

1. In Airtable Contacts table, create Contact:

   - Contact Name: "Jane Doe"

   - Email 1: (empty)

   - Phone 1: (empty)

   - All other fields: (empty)

2. Link Contact to new project EDGE-CASE-001

3. Change EDGE-CASE-001 Status to "Paid"

4. Monitor Zapier:

   - Verify: Workflow doesn't fail

   - Verify: Contact loop processes Jane Doe

5. Navigate to HubSpot:

   - Verify: Contact created with name only

   - Verify: No errors logged

6. Document result: PASS/FAIL

**Expected Outcome:** Contact created with available data, no workflow failure.

### 8.3.7 Test 10: Error Handling - Invalid Phase Value

**Objective:** Verify Zapier handles unrecognized phase values gracefully.

**Prerequisites:**

- Zapier Workflow 2 ON

**Test Steps:**

1. In Airtable, manually edit UNIT-TEST-003 Phase field:

   - Change to "InvalidPhase" (not one of the 5 valid phases)

2. Monitor Zapier Workflow 2:

   - Verify: Workflow executes

   - Verify: Lookup Table fallback value used (Deal Stage remains unchanged or defaults to PreDesign)

   - OR verify: Workflow logs error for unrecognized phase

3. Check email:

   - If error handling configured, verify error notification received

4. Navigate to HubSpot:

   - Verify: Deal still accessible (not corrupted by invalid phase)

5. Document result: PASS/FAIL

**Expected Outcome:** Invalid phase handled gracefully without breaking sync.

**Cleanup:**

- Fix UNIT-TEST-003 Phase back to valid value ("Construction")

**Integration Testing Preparation**

After completing all unit tests above, Josh prepares for Phase 3 joint testing with Johnny:

**Cleanup Test Data:**

1. In HubSpot:

   - Delete all test Deals: UNIT-TEST-001, UNIT-TEST-002, UNIT-TEST-003, BASELINE-001, BASELINE-002, BASELINE-003, MULTI-CONTACT-001, EDGE-CASE-001

   - Delete all test Contacts created during testing

2. In Airtable:

   - Delete all test projects

   - Delete all test contacts

   - Empty Sync Errors table

3. In Zapier:

   - Clear Zap History (optional - or just ignore test runs)

**Set All Workflows to OFF:**

1. Airtable Automation 1: INACTIVE

2. Airtable Automation 2: INACTIVE

3. Zapier Workflow 1: OFF

4. Zapier Workflow 2: OFF

5. Zapier Workflow 3: OFF

**Document Test Results:**

Create summary document: "Josh's Unit Testing Results - Configuration Step D"

UNIT TESTING SUMMARY - JOSH'S AIRTABLE & ZAPIER COMPONENTS

Testing Date: [Date]

Tested By: Josh

TEST RESULTS:

Test 1: Airtable Automation 1 - Webhook Delivery

Status: PASS / FAIL

Notes: [Any observations]

Test 2: Airtable Automation 2 - Webhook Delivery

Status: PASS / FAIL

Notes:

Test 3: Airtable Error Handling

Status: PASS / FAIL

Notes:

Test 4: Zapier Workflow 1 - Deal Creation

Status: PASS / FAIL

Notes:

Test 5: Zapier Workflow 1 - Idempotent Update

Status: PASS / FAIL

Notes:

Test 6: Zapier Workflow 2 - Phase Change

Status: PASS / FAIL

Notes:

Test 7: Zapier Workflow 3 - Weekly Baseline Sync

Status: PASS / FAIL

Notes:

Test 8: Multi-Contact Project

Status: PASS / FAIL

Notes:

Test 9: Edge Case - Empty Fields

Status: PASS / FAIL

Notes:

Test 10: Error Handling - Invalid Phase

Status: PASS / FAIL

Notes:

OVERALL ASSESSMENT:

- Critical issues blocking Phase 3: [List any FAIL results that must be fixed]

- Minor issues to monitor: [List any concerning behaviors]

- Ready for Phase 3 joint testing: YES / NO

NEXT STEPS:

- Fix all critical issues before Phase 3

- Coordinate joint testing session with Johnny

- Prepare fresh test data for end-to-end testing

**Notification to Johnny:**

Email Johnny with subject: "Unit testing complete - ready to schedule Phase 3 joint testing"

Email body:

Johnny,

I've completed independent unit testing of all Airtable automations and Zapier workflows. Test results summary:

✅ All 10 unit tests PASSED [or list any failures]

Key validations completed:

- Webhook delivery from Airtable to Zapier confirmed working

- Deal creation and update logic validated

- Multi-contact projects sync correctly

- Error handling creates Sync Errors records as expected

- Weekly baseline sync processes all projects correctly

[If any issues found:]

I identified the following issues during testing:

- [Issue 1]: [Description] - [Status: Fixed / Needs investigation]

- [Issue 2]: [Description] - [Status: Fixed / Needs investigation]

All workflows are now set to OFF and test data has been cleaned up. I'm ready to coordinate Phase 3 joint integration testing.

For Phase 3 Testing Group B (Section 8.2.4), I propose we schedule a 2-3 hour block where we can:

1. Activate all workflows together

2. Execute end-to-end test scenarios

3. Validate vacation flag routing

4. Test error handling together

5. Document any integration issues

Please let me know your availability this week. I'm flexible on timing.

Attached: Unit Testing Results Summary document

Thanks,

Josh

### 8.3.8 Josh's Troubleshooting Guide

**Purpose:** Common issues Josh may encounter during implementation, testing, and ongoing operations, with step-by-step resolution procedures.

#### 8.3.8.1 Category 1: Airtable Webhook Delivery Failures

##### 8.3.8.1.1 Issue 1.1: Webhook Not Firing at All

**Symptoms:**

- Airtable automation history shows no execution

- No webhook appears in Zapier history

- Project Status change or Phase change doesn't trigger automation

**Diagnosis:**

1. Navigate to Airtable Automations

2. Verify automation status: Should show "Active" (blue toggle)

3. Click into automation, review trigger configuration

4. Check trigger conditions match actual field changes

**Resolution:**

**Step 1: Verify Automation Active**

- If toggle shows "Inactive": Click toggle to activate

- If "Active" but not firing: Proceed to Step 2

**Step 2: Check Trigger Conditions**

- Automation 1 (New Paid Project):

  - Condition 1: "When Project Status changes to Paid" - verify "Paid" matches exact value in Status field (case-sensitive)

  - Condition 2: "When Project ID is not empty" - verify test project has Project ID populated

- Automation 2 (Phase Change):

  - Condition 1: "When Phase changes" - verify field name is exactly "Phase" (not "Project Phase")

  - Condition 2: "When Project Status is one of (Paid, Active)" - verify test project has Status = Paid or Active

  - Condition 3: "When Project ID is not empty"

**Step 3: Test with Extreme Simplicity**

- Temporarily simplify trigger: Remove all conditions except primary trigger

- Example: For Automation 1, only keep "When Project Status changes to Paid"

- Test: Change Status to Paid

- If fires: Re-add conditions one at a time to identify problematic condition

- If still doesn't fire: Airtable automation platform issue - proceed to Step 4

**Step 4: Recreate Automation**

- Sometimes Airtable automations become corrupted

- Duplicate automation (Create copy)

- Delete original automation

- Test duplicate

- If duplicate works: Problem was corruption - use duplicate going forward

**Step 5: Check Airtable Account Limits**

- Airtable free/paid tiers have automation run limits

- Navigate to Account Settings → Usage

- Verify: Automation runs haven't exceeded monthly limit

- If exceeded: Upgrade Airtable plan or wait for monthly reset

**Escalation:**

- If none of above resolves issue: Contact Airtable Support

- Provide: Automation configuration screenshots, test project details, account ID

##### 8.3.8.1.2 Issue 1.2: Webhook Fires but Returns Error (HTTP 400, 500, etc.)

**Symptoms:**

- Airtable automation history shows "Failed" status

- Webhook action displays HTTP error code

- Error message: "Bad Request" or "Server Error"

**Diagnosis:**

1. Click into failed automation run in Airtable history

2. Expand webhook action step

3. Note HTTP error code and error message

**Resolution by Error Code:**

**HTTP 400 Bad Request:**

- **Cause:** Malformed JSON payload

- **Fix:**

  1. Navigate to automation webhook action configuration

  2. Click "Switch to Code" view

  3. Copy JSON payload

  4. Paste into JSON validator: jsonlint.com

  5. Identify syntax errors (missing commas, unmatched brackets, etc.)

  6. Fix errors in Airtable webhook body

  7. Test automation again

**HTTP 401 Unauthorized:**

- **Cause:** Zapier webhook URL invalid or expired

- **Fix:**

  1. Verify webhook URL in Airtable matches Zapier Catch Hook URL exactly

  2. Check for extra spaces, missing trailing slash, or typos

  3. If URL correct but still failing:

     - Regenerate webhook in Zapier (Section 8.3.3 Step C1.5)

     - Update Airtable automation with new URL

     - Test again

**HTTP 500 Internal Server Error:**

- **Cause:** Temporary Zapier outage or processing error

- **Fix:**

  1. Check Zapier status page: status.zapier.com

  2. If Zapier operational: Wait 5 minutes and retry

  3. If error persists: Review Zapier Zap History for error details

  4. If Zapier Zap shows error processing payload: Fix Zap configuration

**HTTP 404 Not Found:**

- **Cause:** Webhook URL incorrect or Zap deleted

- **Fix:**

  1. Verify Zap still exists in Zapier dashboard

  2. If Zap deleted: Recreate Zap or restore from backup

  3. If Zap exists: Regenerate Catch Hook URL

  4. Update Airtable automation with new URL

##### 8.3.8.1.3 Issue 1.3: Webhook Delivers but Zapier Receives Empty Payload

**Symptoms:**

- Airtable automation shows "Success"

- Zapier receives webhook but all fields empty/null

- Zapier Zap History shows webhook with no data

**Diagnosis:**

1. In Zapier Zap History, click into webhook entry

2. Examine "Data In" section

3. Verify which fields are empty

**Resolution:**

**Step 1: Check Dynamic Field Mapping**

- Navigate to Airtable automation webhook action

- Review JSON body configuration

- Verify all dynamic fields inserted correctly:

  - Fields should show as blue pills: {Project ID from Step 1}

  - NOT as literal text: "Project ID"

- If fields are literal text, not dynamic references:

  1. Delete text

  2. Position cursor in quotes

  3. Click "+" to insert dynamic field

  4. Select correct step and field

**Step 2: Verify Source Data Exists**

- Navigate to Airtable Projects table

- Open test project that triggered webhook

- Verify all fields referenced in webhook have values populated

- Common issue: Primary POC or Backup POC fields empty

  - Fix: Populate POC fields before triggering webhook

**Step 3: Test Contacts Array**

- Most common issue: Contacts array not configured correctly

- In webhook body, verify contacts section uses line items:

  - Correct: Inserted "All fields (with line items)" from Find Records step

  - Incorrect: Manually typed contact data

- Fix: Delete contacts section, re-insert using line items syntax

**Step 4: Simplify Payload for Testing**

- Temporarily simplify webhook payload to minimal fields:

- { "project_id": "{Project ID from Step 1}", "trigger_type": "test"}

- Trigger automation

- If Zapier receives data: Gradually re-add fields to identify problematic field

- If still empty: Airtable dynamic field insertion broken - escalate to Airtable Support

#### 8.3.8.2 Category 2: Zapier Workflow Execution Failures

##### 8.3.8.2.1 Issue 2.1: Zapier Workflow Doesn't Execute When Webhook Received

**Symptoms:**

- Airtable webhook delivers successfully (HTTP 200)

- Zapier Zap History shows webhook received

- But Zap doesn't execute subsequent steps (or Zap shows "Held")

**Diagnosis:**

1. Navigate to Zapier Zap History

2. Click into webhook entry

3. Check Zap status

**Resolution by Status:**

**Status: "Held"**

- **Cause:** Zap is turned OFF

- **Fix:**

  1. Navigate to Zap editor

  2. Toggle Zap to ON (top right, should turn blue)

  3. Re-trigger webhook from Airtable

  4. Verify Zap executes

**Status: "Filtered"**

- **Cause:** Filter step prevented execution

- **Fix:**

  1. Review Filter step configuration (Step 2 in most workflows)

  2. Check filter condition: "Project ID exists"

  3. Verify webhook payload contains project_id field

  4. If project_id missing: Fix Airtable automation payload

  5. If project_id present but still filtered: Filter condition may be case-sensitive

     - Change condition to "is not empty" instead of "exists"

**Status: "Error"**

- **Cause:** One of the workflow steps failed

- **Fix:** Proceed to Issue 2.2 (Step Failure)

##### 8.3.8.2.2 Issue 2.2: Zapier Workflow Step Fails

**Symptoms:**

- Zap executes but stops at specific step

- Step shows red "Failed" status in Zap History

- Error message displayed

**Diagnosis:**

1. In Zap History, click into failed run

2. Identify which step failed (highlighted in red)

3. Read error message

**Resolution by Failed Step:**

**Step 3: Find Deal in HubSpot - "Property 'project_id' not found"**

- **Cause:** Johnny hasn't created custom Project ID property yet

- **Fix:**

  1. Escalate to Johnny: "HubSpot custom property 'project_id' missing"

  2. Johnny creates property (Section 3.3.2)

  3. Re-trigger webhook once property created

**Step 3: Find Deal - "Unauthorized" or "Invalid API key"**

- **Cause:** HubSpot Private App API key invalid, expired, or permissions insufficient

- **Fix:**

  1. Verify API key still valid in HubSpot (ask Johnny)

  2. If expired: Johnny regenerates API key (Section 8.4.6)

  3. Update Zapier HubSpot connection with new API key:

     - Zapier Settings → Connected Accounts → HubSpot → Reconnect

     - Paste new API key

  4. Test Zap again

**Step 5a/5b: Create/Update Deal - "User ID not found"**

- **Cause:** HubSpot User ID in payload doesn't match any HubSpot user

- **Fix:**

  1. Review User ID mapping document from Johnny (Configuration Step A3)

  2. Compare with User IDs in Airtable Users table

  3. Identify mismatch:

     - If Airtable has wrong User ID: Josh updates Airtable Users table

     - If Johnny provided wrong User ID: Johnny verifies and corrects mapping

  4. Re-trigger webhook

**Step 5a: Create Deal - "Pipeline not found"**

- **Cause:** Pipeline name or ID incorrect in Zap configuration

- **Fix:**

  1. Ask Johnny for correct Pipeline ID for "Client Projects" pipeline

  2. Update Zap Step 5a Pipeline field with correct ID

  3. Test Zap

**Step 8a: Find Contact - "Invalid email format"**

- **Cause:** Email field in payload contains invalid email (missing @ symbol, etc.)

- **Fix:**

  1. Review contact data in Airtable

  2. Verify emails follow standard format: user@domain.com

  3. Fix invalid emails in Airtable

  4. Re-trigger webhook

**Step 8b: Add Contact to Deal - "Contact ID or Deal ID invalid"**

- **Cause:** Previous step (Create Contact or Create Deal) didn't complete successfully

- **Fix:**

  1. Review Zap History - scroll up to Step 5a/5b (Deal creation)

  2. Verify Deal ID was returned

  3. Review Step 8a (Find/Create Contact)

  4. Verify Contact ID was returned

  5. If either ID missing: Fix earlier failed step first

  6. If both IDs present but association still fails: Temporary HubSpot API issue - retry

##### 8.3.8.2.3 Issue 2.3: Zapier Loop Doesn't Iterate Through Contacts

**Symptoms:**

- Zap executes successfully through Deal creation

- Loop step (Step 7) shows "0 iterations"

- No Contacts created in HubSpot

**Diagnosis:**

1. In Zap History, click into run

2. Examine Step 7 (Looping by Zapier)

3. Check "Data In" - should show contacts array

**Resolution:**

**Contacts Array Empty in Step 7:**

- **Cause:** Airtable webhook didn't include contacts in payload

- **Fix:**

  1. Review Airtable Automation 1 configuration

  2. Verify Step 2 (Find Records - Contacts) executed successfully

  3. Verify webhook payload includes contacts array

  4. Common issue: Find Records condition wrong

     - Condition: "Where Associated Projects contains [Project ID]"

     - If condition references wrong field, no contacts found

  5. Fix Airtable automation, re-trigger

**Contacts Array Present but Loop Shows 0 Iterations:**

- **Cause:** Line items not configured correctly in Loop step

- **Fix:**

  1. Edit Zap Step 7 (Looping by Zapier)

  2. Verify "Line Items" field set to: Step 1 → "contacts"

  3. If set to different field: Correct to "contacts"

  4. Save Zap

  5. Test again

**Loop Iterates but Contacts Not Created:**

- **Cause:** Steps inside loop (8a, 8b) failing

- **Fix:** Review Issue 2.2 for Contact creation step failures

#### 8.3.8.3 Category 3: Data Synchronization Issues

##### 8.3.8.3.1 Issue 3.1: Phase Name Mismatch Causes POC Assignment Failure

**Symptoms:**

- Workflow 2 (Phase Change) executes successfully

- Deal updated in HubSpot

- But Primary POC and Backup POC remain unchanged or set to wrong team member

- Johnny's POC Assignment workflow (HubSpot-side) logs error

**Diagnosis:**

1. Navigate to HubSpot, open affected Deal

2. Check project_phase property value

3. Compare with BRD Appendix C phase names

**Root Cause:**

- Phase spelling in Airtable doesn't match HubSpot exactly

- Example: Airtable has "Pre-Design" but HubSpot expects "PreDesign"

- This is BRD Risk T-12 - #1 cause of POC assignment failures

**Resolution:**

**Step 1: Validate Airtable Phase Values**

1. Navigate to Airtable Projects table

2. Click into Phase field settings

3. Review dropdown options

4. Compare with BRD Appendix C:

   - PreDesign (NOT Pre-Design, NOT pre-design)

   - Design

   - Procurement

   - PreConstruction (NOT Pre-Construction)

   - Construction

5. If any mismatch found:

   - Update Airtable Phase field options to exact spelling

   - **CRITICAL:** This affects ALL projects - coordinate with team

   - Update existing project records with corrected phase values

**Step 2: Validate Zapier Lookup Table**

1. Edit Zapier Workflow 1 and Workflow 2

2. Review Lookup Table in Deal Stage mapping

3. Verify keys match Airtable phase values EXACTLY

4. Verify values match HubSpot stage names EXACTLY

5. If mismatch: Update Lookup Table

6. Save Zaps

**Step 3: Re-sync Affected Projects**

1. In Airtable, identify all projects with incorrect phase values

2. Manually correct phase values

3. Force re-sync:

   - Change Phase to different value

   - Change back to correct value (triggers Phase Change webhook)

4. Verify POC assignments corrected in HubSpot

**Prevention:**

- Johnny's Monthly Phase Name Validation workflow (Section 3.6.10) detects mismatches

- Review validation email every month

- Fix any reported issues immediately

##### 8.3.8.3.2 Issue 3.2: Contact Email/Phone Limits Exceeded

**Symptoms:**

- Workflow 1 creates Contact in HubSpot

- But some emails or phones missing from HubSpot Contact

- Airtable Contact has more than 3 emails or more than 4 phones

**Diagnosis:**

1. Navigate to Airtable, open affected Contact record

2. Count populated email fields (Email 1, 2, 3, etc.)

3. Count populated phone fields (Phone 1, 2, 3, 4, etc.)

4. Navigate to HubSpot, open corresponding Contact

5. Compare - identify missing fields

**Root Cause:**

- HubSpot Professional tier limits: 3 emails per Contact, 4 phones per Contact (BRD Section 3.11.2.2.1)

- If Airtable Contact has 5 emails, only first 3 sync to HubSpot

**Resolution:**

**Multi-Contact Strategy (BRD Section 7.3.1.4.1):**

1. In Airtable, split Contact into multiple Contact records:

   - **Original Contact:** "John Smith" (3 emails + 3 phones)

   - **New Contact:** "John Smith - Additional" (remaining 2 emails + remaining 1 phone)

2. Link both Contacts to same Project

3. Force re-sync:

   - Change Project Status to "Lead" then back to "Paid"

   - OR manually trigger Workflow 1

4. Verify in HubSpot:

   - 2 separate Contact records created

   - Both associated with same Deal

   - All emails/phones captured across 2 records

**Alternative (If Splitting Not Desired):**

- Document missing contact info in Deal's Project Master Info field (Section 3.7)

- Team references Master Info for additional contact details

- Not ideal - prefer multi-contact approach

##### 8.3.8.3.3 Issue 3.3: Deal Created but Contacts Missing

**Symptoms:**

- Workflow 1 executes successfully

- Deal created in HubSpot with correct properties

- But no Contacts associated with Deal

**Diagnosis:**

1. Review Zapier Zap History for affected run

2. Check Step 7 (Loop through contacts)

3. Verify loop executed (should show "X iterations")

**Resolution:**

**Loop Executed 0 Iterations:**

- **Cause:** No contacts linked to project in Airtable

- **Fix:**

  1. Navigate to Airtable, open affected project

  2. Verify Client Contacts field populated

  3. If empty: Link at least 1 Contact

  4. Force re-sync

**Loop Executed but Contacts Not Created:**

- **Cause:** Steps inside loop (8a, 8b) failed

- **Fix:**

  1. Review Zap History - expand loop iterations

  2. Check each iteration for errors

  3. Common errors:

     - Invalid email format (Step 8a fails)

     - Deal ID not available to Step 8b (Step 5a/5b failed silently)

  4. Fix errors per Issue 2.2 resolutions

  5. Manually re-run affected iterations:

     - Identify Contact that didn't sync

     - Manually create Contact in HubSpot

     - Manually associate with Deal

#### 8.3.8.4 Category 4: Escalation Paths

##### 8.3.8.4.1 When to Escalate to Johnny:

Josh encounters issues that require HubSpot-side investigation or configuration changes:

**Scenario 1: HubSpot Custom Properties Missing**

- Error: "Property 'project_id' not found"

- Action: Email Johnny with screenshot of error, request property creation

**Scenario 2: HubSpot User ID Mapping Incorrect**

- Error: "User ID [12345678] not found"

- Action: Email Johnny to verify User ID mapping (Configuration Step A3)

**Scenario 3: HubSpot API Key Invalid**

- Error: "Unauthorized" or "Invalid authentication"

- Action: Email Johnny to regenerate HubSpot Private App API key

**Scenario 4: POC Assignments Not Working Despite Correct Phase Names**

- Observation: Phase values match exactly but POCs still wrong

- Action: Joint troubleshooting session - Johnny reviews HubSpot POC Assignment workflow logs

**Scenario 5: HubSpot Pipeline or Stage Issues**

- Error: "Pipeline 'Client Projects' not found" or "Stage 'PreDesign' invalid"

- Action: Johnny verifies pipeline configuration, provides correct Pipeline ID

**Escalation Template Email:**

Subject: HubSpot Integration Issue - [Brief Description]

Johnny,

I've encountered an issue with the HubSpot integration that requires your assistance:

Issue: [Describe symptom]

Error Message: [Copy exact error from Zapier or Airtable]

Affected Workflow: [Workflow 1, 2, or 3]

Affected Project ID: [If specific project]

What I've Tried:

- [Troubleshooting step 1]

- [Troubleshooting step 2]

What I Need from You:

[Specific request - e.g., verify custom property exists, regenerate API key, check POC workflow logs]

Urgency: [Low / Medium / High / Critical]

Let me know when you can look into this. I can schedule a joint troubleshooting session if needed.

Thanks,

Josh

##### 8.3.8.4.2 When to Escalate to Vendor Support:

**Airtable Support Escalation:**

- **Scenario:** Automation platform issues (automations not firing, webhook actions failing without clear error)

- **Before escalating:**

  - Recreate automation to rule out corruption

  - Test with simplified configuration

  - Document issue with screenshots

- **Contact:** support.airtable.com → Submit request

- **Include:** Account ID, Base ID, Automation name, screenshots, detailed description

**Zapier Support Escalation:**

- **Scenario:** Zap platform issues (workflows not executing, unexpected behavior, Catch Hook not receiving webhooks)

- **Before escalating:**

  - Check Zapier status page: status.zapier.com

  - Recreate Zap to rule out corruption

  - Test with simplified workflow

- **Contact:** zapier.com/app/get-help → Contact Support

- **Include:** Zap URL, Zap History run ID, error screenshots, detailed description

**HubSpot Support Escalation:**

- **Scenario:** HubSpot API errors, platform issues (Johnny escalates, not Josh)

- **Contact:** Johnny contacts HubSpot Support via HubSpot account

#### 8.3.8.5 Category 5: Ongoing Maintenance Issues

##### 8.3.8.5.1 Issue 5.1: Zapier Task Usage Approaching Limit

**Symptoms:**

- Email notification: "You've used 80% of your Zapier tasks"

- Zapier dashboard shows task consumption near monthly limit (750 tasks for Starter tier)

**Diagnosis:**

1. Navigate to Zapier dashboard → Usage

2. Review task consumption by Zap

3. Identify high-usage workflows

**Resolution:**

**Step 1: Identify Task-Heavy Workflows**

- Weekly Baseline Sync likely highest consumer (50-200 tasks per run)

- Event-driven workflows (1 and 2) should be low consumption

**Step 2: Optimize Weekly Baseline Sync**

- If task usage consistently high:

  - Option A: Reduce Max Records in Step 2 (Find Records in Airtable)

    - Lower from 100 to 50 if LWL has fewer projects

  - Option B: Change frequency to bi-weekly instead of weekly

    - Edit Schedule trigger: Every 2 weeks instead of Every week

  - Option C: Disable Weekly Baseline Sync if event-driven workflows proven reliable

    - Per BRD Section 7.3.1.7, after 90 days of stable sync, consider disabling

    - Decision requires CEO approval

**Step 3: Upgrade Zapier Plan (If Needed)**

- If optimizations insufficient:

  - Upgrade to Professional plan (~$69/month, 2,000 tasks)

  - Or Team plan (~$103/month, 50,000 tasks)

- Escalate decision to CEO (cost vs. risk tradeoff)

**Prevention:**

- Monitor task usage weekly during first 90 days

- Set calendar reminder to review usage first Monday of each month

##### 8.3.8.5.2 Issue 5.2: Airtable API Token Rotation (Annual Maintenance)

**Symptoms:**

- Calendar reminder: "Annual Airtable API token rotation"

- Or suddenly: Zapier workflows fail with "Unauthorized" error

**Resolution:**

**Step 1: Generate New Airtable Personal Access Token**

1. Navigate to Airtable account: airtable.com/account

2. Click "Generate new token"

3. Token name: "Zapier Integration - Communications Hub - [Year]"

4. Scopes: data.records:read, data.records:write, schema.bases:read (same as original)

5. Click "Create token"

6. Copy new token immediately (only shown once)

**Step 2: Update Zapier Connection**

1. Navigate to Zapier Settings → Connected Accounts

2. Find "Airtable" connection

3. Click "Reconnect"

4. Paste new Personal Access Token

5. Click "Yes, Continue"

**Step 3: Test Workflows**

1. Manually trigger Workflow 3 (Weekly Baseline Sync) using Test feature

2. Verify Airtable connection works

3. If successful: All workflows automatically use new token

4. If fails: Re-enter token (may have copied incorrectly)

**Step 4: Revoke Old Token**

1. Return to Airtable account settings

2. Find old token (year prior)

3. Click "Revoke"

4. Confirm revocation

**Prevention:**

- Set annual calendar reminder: November 15 each year (align with holiday calendar update)

- Document token rotation in Implementation Notes

##### 8.3.8.5.3 Issue 5.3: Sync Errors Table Accumulating Records

**Symptoms:**

- Airtable Sync Errors table has multiple records

- Some errors resolved but not marked

- Table becoming cluttered

**Resolution:**

**Weekly Review Process:**

1. Every Monday (align with Weekly Baseline Sync review), navigate to Airtable Sync Errors table

2. For each error record:

   - **If Resolved column checked:** Delete record (error fixed, no longer needed)

   - **If Resolved empty:**

     - Review Error Message

     - Check HubSpot for affected Project ID

     - If project now synced: Check Resolved, add Resolution Notes, delete after 1 week

     - If still not synced: Investigate per error type (Issues 2.1-2.3)

**Cleanup Procedure (Monthly):**

1. First Monday of each month

2. Filter Sync Errors: Resolved = TRUE

3. Select all resolved records older than 30 days

4. Delete (errors no longer needed after 30 days)

**Prevention:**

- Don't let Sync Errors table grow unchecked

- Regular cleanup maintains visibility into current issues

- Archive critical errors in separate documentation if needed long-term

**Configuration Step D Complete**

Josh has now completed:

- ✅ Airtable schema configuration

- ✅ Airtable webhook automations built and tested

- ✅ Zapier workflows built and tested

- ✅ Independent unit testing completed

- ✅ Troubleshooting procedures documented

**Ready for Phase 3 Joint Integration Testing with Johnny (Section 8.2.4)**