---
source: SDD - System Design Document - Consolidated Communication PART ONE v1.docx
section: 3.0 HUBSPOT CONFIGURATION SPECIFICATIONS (Part 1 - Sections 3.1-3.3)
integrity: full
format: preservation_mode
encoding: utf-8
extraction_method: paragraph_and_table_parser
order_preserved: true
tables_preserved: true
revision: 1.1
strict_lossless_mode: true
---

## 3.0 HUBSPOT CONFIGURATION SPECIFICATIONS

## 3.1 HubSpot Subscription and Licensing

### 3.1.1 Required Subscriptions

| **Product** | **Tier** | **Quantity** | **Purpose** | **Estimated Annual Cost** |
| --- | --- | --- | --- | --- |
| Sales Hub | Professional | 10 seats | Core communication management, Deals, Contacts, Conversations Inbox | Approximately $4,500-5,000/user/year = Approximately $45,000-50,000/year |
| Marketing Hub | Professional | 1 seat | SMS Access Add-On requirement | Approximately $800-1,200/year |
| SMS Access Add-On | N/A | 1 business number | Text messaging capability | Included with Marketing Hub Pro |

Note: Exact pricing to be confirmed during HubSpot sales process. Estimates based on October 2025 public pricing.

### 3.1.2 User License Assignments (Planned)

| **Role** | **User** | **Hub** | **Seat Type** | **Admin Rights** |
| --- | --- | --- | --- | --- |
| CEO | Lauren Lerner | Sales Hub Pro | Paid Seat | Administrator |
| Director of Innovation and Technology | Johnny Chang | Sales Hub Pro | Paid Seat | Administrator |
| Director of Operations | Robin Vaughn | Sales Hub Pro | Paid Seat | Standard User |
| Director of Construction | Brandie Roberts | Sales Hub Pro | Paid Seat | Standard User |
| Lead Designer | Sara Morgan | Sales Hub Pro | Paid Seat | Standard User |
| Design Assistant | Megan Edmondo | Sales Hub Pro | Paid Seat | Standard User |
| Executive Assistant | Molly Oestreich | Sales Hub Pro | Paid Seat | Standard User |
| Construction PM | Debra Solomon | Sales Hub Pro | Paid Seat (1-2 seats) | Standard User |
| TBD | Name TBD | Marketing Hub Pro | Paid Seat | Standard User (SMS only) |
| Airtable Administrator | Josh | Sales Hub Pro | Paid Seat | Administrator |

Final user count and role assignments will be confirmed during Phase 1 Discovery (BRD 3.10.8.1).

## 3.2 HubSpot Account Configuration

### 3.2.1 Account-Level Settings

| **Setting** | **Configuration Value** | **Rationale** |
| --- | --- | --- |
| Account Timezone | America/Phoenix (UTC-7) | Arizona does not observe DST; ensures business hours logic remains accurate year-round (BRD 7.3.2.3) |
| Default Currency | USD | All LWL projects billed in US dollars |
| Date Format | MM/DD/YYYY | US standard date format |
| Language | English (US) | Primary business language |
| Fiscal Year Start | January 1 | Calendar year alignment |
| Email Signature Management | Organization-level locked template | Enforces brand consistency; users add only "First Name \| Title" above locked company block (BRD 3.2.1.3) |

### 3.2.2 Company Domain Verification

-   Verify ownership of livingwithlolo.com domain in HubSpot account settings

-   Required for email tracking and branded links

-   Process: Add HubSpot-provided TXT record to Google Workspace DNS settings

### 3.2.3 Two-Factor Authentication (2FA) Enforcement

-   Enable "Require two-factor authentication for all users" in Security settings

-   Aligns with BRD Section 4.4.3 MFA requirement

-   Users will configure 2FA on first login using authenticator app or SMS

## 3.3 Data Model: HubSpot Objects

### 3.3.1 Object Selection and Rationale

Per BRD Section 3.10.1.1, the implementation uses HubSpot's standard objects to minimize licensing costs:

| **HubSpot Object** | **Represents** | **Rationale** |
| --- | --- | --- |
| Deals | Client Projects | Standard object available in Professional tier; supports custom properties, pipeline stages, associations |
| Contacts | Clients and their contact persons | Standard object; supports multiple Contacts per Deal for clients with more than 3 emails or 4 phones |
| Companies | NOT USED | Projects are 1:1 with clients; Company object adds unnecessary complexity |
| Conversations | Email and SMS threads | Native Inbox object; automatic threading and POC assignment |
| Notes | Internal collaboration | Standard Timeline activity; supports \@mentions |

CRITICAL: HubSpot's custom "Projects" object (Enterprise tier) is explicitly OUT OF SCOPE per BRD 3.10.1.5. If standard Deals object proves insufficient during UAT, escalate to Executive Team for Enterprise tier consideration (approximately $30,000/year additional cost).

### 3.3.2 Deal Object Configuration

Purpose: Each Deal record represents one client project.

Deal Pipeline: "Client Projects" (new custom pipeline)

Pre-Sales Pipeline: "Pre-Sales Leads" (Phase 1 basic setup, full implementation Phase 1.5)

Pipeline Stages:

| **Stage Name** | **Stage Order** | **Probability** | **Category** | **Notes** |
| --- | --- | --- | --- | --- |
| Inquiry | 1 | 10% | Open | Basic stage created in Phase 1 |
| Initial Consultation | 2 | 25% | Open | Basic stage created in Phase 1 |
| Proposal Development | 3 | 50% | Open | Basic stage created in Phase 1 |
| Contract Negotiation | 4 | 75% | Open | Basic stage created in Phase 1 |
| Converted to Paid | 5 | 100% | Won | Lead becomes paid project, moves to VIP@ inbox |
| Lost | 6 | 0% | Lost | Lead did not convert |

Pipeline Stages: (Maps to Airtable project phases per BRD Appendix C)

| **Stage Name** | **Stage Order** | **Probability** | **Category** | **Automation Trigger** |
| --- | --- | --- | --- | --- |
| PreDesign | 1 | 20% | In Progress | Airtable Phase = "PreDesign" |
| Design | 2 | 40% | In Progress | Airtable Phase = "Design" |
| Procurement | 3 | 60% | In Progress | Airtable Phase = "Procurement" |
| PreConstruction | 4 | 80% | In Progress | Airtable Phase = "PreConstruction" |
| Construction | 5 | 90% | In Progress | Airtable Phase = "Construction" |
| Completed | 6 | 100% | Won | Manual close-out only |
| Cancelled | 7 | 0% | Lost | Manual status change only |

Custom Deal Properties:

| **Property Name** | **Internal Name** | **Field Type** | **Required** | **Purpose** | **Data Source** |
| --- | --- | --- | --- | --- | --- |
| Project ID | project_id | Single-line text | Yes | Unique project identifier; must match Airtable exactly | Airtable sync |
| Primary POC | primary_poc | HubSpot User (dropdown) | Yes | Active Primary Point of Contact for routing | Airtable sync |
| Backup POC | backup_poc | HubSpot User (dropdown) | Yes | Backup Point of Contact for coverage | Airtable sync |
| Project Phase | project_phase | Dropdown (single-select) | Yes | Current project phase; drives Deal Stage | Airtable sync |
| Project Master Info | project_master_info | Multi-line text | No | Centralized project information field with template structure | Manual entry by POCs |
| Airtable Record ID | airtable_record_id | Single-line text | No | Airtable internal record ID for troubleshooting sync issues | Airtable sync |
| Last Sync Date | last_sync_date | Date picker | No | Timestamp of last Airtable-to-HubSpot sync | Zapier automation |

Project Phase Dropdown Values: (Must match Airtable Phase field values exactly)

-   PreDesign

-   Design

-   Procurement

-   PreConstruction

-   Construction

Property Group: Create custom property group "LWL Project Management" containing all custom Deal properties above for easy viewing/editing.

**Note:** Phase 1 creates basic pipeline structure only. Phase 1.5 adds Airtable sync and phase-based POC routing for pre-sales.

### 3.3.3 Contact Object Configuration

Purpose: Each Contact represents an individual client contact person (spouse, family member, assistant, etc.). Projects may have multiple Contacts associated with the same Deal.

Standard Properties (Configured):

| **Property Name** | **Internal Name** | **Field Type** | **Required** | **Usage** |
| --- | --- | --- | --- | --- |
| Email | email | Email address | Yes (if email exists) | Primary email for routing |
| Secondary Email | hs_additional_emails | Email address | No | Additional email addresses |
| Phone Number | phone | Phone number | No | Primary phone for SMS routing |
| Mobile Phone Number | mobilephone | Phone number | No | Mobile phone for SMS |
| Work Phone Number | work_phone | Phone number | No | Work phone contact |
| First Name | firstname | Single-line text | Yes | Contact first name |
| Last Name | lastname | Single-line text | Yes | Contact last name |
| Contact Owner | hubspot_owner_id | HubSpot User | No | Not used; Deal owner determines routing |

Custom Contact Properties:

| **Property Name** | **Internal Name** | **Field Type** | **Required** | **Purpose** |
| --- | --- | --- | --- | --- |
| Contact Label | contact_label | Single-line text | No | Descriptive label (e.g., "John Cell", "Sarah Work Email") |
| Preferred Communication Channel | preferred_channel | Dropdown | No | Email, SMS, or No Preference |
| Airtable Contact ID | airtable_contact_id | Single-line text | No | Airtable internal ID for sync troubleshooting |

HubSpot Contact Limitations: Per BRD 3.11.2.2.1:

-   Maximum 3 email addresses per Contact (Email, Secondary Email, Additional Email fields)

-   Maximum 4 phone numbers per Contact (Phone, Mobile, Work Phone, Fax Number fields)

-   Multi-Contact Strategy: Projects requiring more than 3 emails or 4 phones will use multiple Contact records associated with the same Deal (e.g., one Contact for husband, one for wife)

### 3.3.4 Conversation Object (Native)

Purpose: HubSpot Conversations Inbox automatically creates Conversation objects for all emails and SMS messages.

Standard Properties (No Configuration Required):

-   Conversation ID (auto-generated)

-   Channel (Email or SMS)

-   Status (Open or Closed)

-   Owner (assigned POC)

-   Associated Contact(s)

-   Associated Deal(s)

-   Created Date

-   Last Message Date

Conversation Threading:

-   Email: Threads grouped by email subject line and References/In-Reply-To headers

-   SMS: Threads grouped by phone number

Configuration Note: No custom Conversation properties required for Phase 1. HubSpot native Conversations Inbox handles all routing and status management.

## 3.4 Conversations Inbox Configuration

### 3.4.1 Shared Inbox Setup

Inbox Name: "LWL Client Communications"

Connected Channels:

1.  Email: <VIP@livingwithlolo.com> (via Gmail OAuth connection - see Section 6.3)

2.  Email: <welcome@livingwithlolo.com> (via Gmail OAuth connection - see Section 6.3)

3.  Email: <info@livingwithlolo.com> (via Gmail OAuth connection - see Section 6.3)

4.  Email: <family@livingwithlolo.com> (via Gmail OAuth connection - see Section 6.3)

5.  SMS: HubSpot SMS Access Add-On business number (see Section 3.5)

**Note:** Salesmsg urgent hotline operates as standalone platform (not connected to HubSpot Conversations Inbox in Phase 1)

### 3.4.2 Inbox Views (Filters)

Configure the following saved views in Conversations Inbox:

| **View Name** | **Filter Criteria** | **Purpose** | **Visible To** |
| --- | --- | --- | --- |
| My Open Conversations | Status = Open AND Owner = Current User | POC's active work queue | All Users (personal view) |
| All Open Conversations | Status = Open | Team-wide visibility of all active communications | All Users |
| Unassigned Conversations | Owner = Unassigned | Administrator queue for unmatched communications (BRD 5.4) | Administrators Only |
| Closed Conversations | Status = Closed | Historical conversations for reference | All Users |
| PreDesign Phase | Associated Deal Stage = PreDesign AND Status = Open | Phase-specific filtering | All Users |
| Design Phase | Associated Deal Stage = Design AND Status = Open | Phase-specific filtering | All Users |
| Procurement Phase | Associated Deal Stage = Procurement AND Status = Open | Phase-specific filtering | All Users |
| PreConstruction Phase | Associated Deal Stage = PreConstruction AND Status = Open | Phase-specific filtering | All Users |
| Construction Phase | Associated Deal Stage = Construction AND Status = Open | Phase-specific filtering | All Users |
| welcome@ Inbox - All | Channel = Email AND Inbox = welcome@livingwithlolo.com | Pre-sales communications (all leads) | All Users |
| welcome@ Inbox - My Conversations | Channel = Email AND Inbox = welcome@livingwithlolo.com AND Owner = Current User | Molly's assigned pre-sales leads | All Users (personal view) |
| info@ Inbox - All | Channel = Email AND Inbox = <info@livingwithlolo.com> | General business inquiries (all messages) | All Users |
| info@ Inbox - My Conversations | Channel = Email AND Inbox = <info@livingwithlolo.com> AND Owner = Current User | Lauren/Robin's assigned inquiries | All Users (personal view) |
| family@ Inbox - All | Channel = Email AND Inbox = <family@livingwithlolo.com> | Post-project client care (all messages) | All Users |
| family@ Inbox - My Conversations | Channel = Email AND Inbox = <family@livingwithlolo.com> AND Owner = Current User | Lauren/Robin's assigned conversations | All Users (personal view) |

Default View for All Users: "My Open Conversations"

Default View for Administrators: "Unassigned Conversations" (daily review required per BRD 5.4.3)

### 3.4.3 Conversation Assignment Workflow

Automatic Assignment Logic:

**For <VIP@livingwithlolo.com> (Paid Projects):**

-   IF Conversation has Associated Deal: Assign to Deal.Primary_POC (subject to vacation flag check), Send notification to assigned POC

-   ELSE IF Contact exists but no Deal association: Route to "Unassigned Conversations" view, No automatic notifications (per BRD 3.3.8.3)

-   ELSE (unknown sender): Route to "Unassigned Conversations" view, No automatic notifications

**For <welcome@livingwithlolo.com> (Pre-Sales):**

-   IF Conversation has Associated Deal (pre-sales pipeline): Assign to Deal Owner (manual assignment in Phase 1; automated phase-based routing in Phase 1.5)

-   ELSE (new inquiry): Assign to Molly (Primary POC), Check Molly's vacation flag (if TRUE, assign to Lauren as Backup), Send notification to assigned POC

-   Note: Manual assignment in Phase 1; automated phase-based routing deferred to Phase 1.5

**For <info@livingwithlolo.com> (General Business):**

-   All new messages: Route to "Unassigned Conversations" view

-   Primary Owner (Lauren) and Secondary Owner (Robin) manually review and assign

-   No automatic notifications (self-service queue per BRD 3.3.8.3)

**For <family@livingwithlolo.com> (Post-Project Care):**

-   All new messages: Route to "Unassigned Conversations" view

-   Primary Owner (Lauren) and Secondary Owner (Robin) manually review and assign

-   Optional: Manually associate with historical project Deal if relevant

-   No automatic notifications (self-service queue per BRD 3.3.8.3)

Implementation Method: HubSpot Workflow (see Section 3.6.2 - updated specifications)

### 3.4.4 Conversation Status Management

Status Values:

-   Open: Requires LWL action or response (active)

-   Closed: Fully addressed/resolved (archived from active inbox views)

Status Change Rules:

-   Any POC or Administrator can manually change status between Open and Closed (BRD 5.5.4)

-   Closing a conversation removes it from "Open" inbox views but preserves it in Deal timeline

-   Re-opening a Closed conversation returns it to assigned POC's "My Open Conversations" view

**Spam/Irrelevant Message Handling:**

-   Any Standard User or Administrator can close obvious spam or irrelevant communications without requiring escalation (per BRD 3.3.8.5)

-   Team members should use judgment; if uncertain, use internal notes to \@mention colleagues for input

-   Closed spam conversations removed from Open inbox views but retained in audit trail

No Automatic Status Changes: Per BRD Section 3.4, no automated closure or escalation. All status changes are manual POC decisions.

## 3.5 HubSpot SMS Access Add-On Configuration

**Note:** Living With Lolo operates a dual-channel SMS architecture:

1.  **Standard Client SMS** (this section): HubSpot SMS Access Add-On for routine project communication

2.  **Urgent Communications Hotline** (Section 3.5A): Salesmsg platform for time-sensitive emergencies

This section covers only the HubSpot SMS integration for standard client communications during active projects.

### 3.5.1 SMS Provider and Phone Number

Provider: HubSpot SMS Access Add-On (native feature, no third-party integration)

Business Phone Number: Provision new US phone number with local area code (480 or 623 recommended for Scottsdale, Arizona)

Number Type: Standard business SMS number (not toll-free, which has higher cost and delivery issues)

Provisioning Process:

1.  Navigate to Settings \> Inbox \> SMS

2.  Click "Get a phone number"

3.  Select area code 480 or 623

4.  Choose available number from HubSpot inventory

5.  Assign number to "LWL Client Communications" inbox

Expected Provisioning Time: Immediate (HubSpot native feature)

### 3.5.2 SMS Routing Configuration

Inbound SMS Routing Logic: (Same as email routing per Section 3.4.3)

IF SMS sender phone matches existing Contact: Associate with Contact's Deal record Assign to Deal.Primary_POC Send notification to Primary_POC

ELSE IF SMS sender phone is unknown: Create new Contact record (phone number only) Route to "Unassigned Conversations" view Notify Administrators for manual association

Outbound SMS Sending:

-   POCs send SMS replies directly from HubSpot Conversations Inbox

-   Replies automatically thread with original inbound SMS

-   All SMS sent from LWL business number (never personal phones)

### 3.5.3 SMS Compliance Configuration

Opt-Out Management: (Required for TCPA compliance per BRD 4.4.3)

-   Configure auto-reply for "STOP", "UNSUBSCRIBE", "QUIT" keywords

-   Auto-reply message: "You have been unsubscribed from Living With Lolo text messages. Reply START to re-subscribe or call us at \[LWL main phone\]."

-   Unsubscribed contacts are automatically suppressed from future SMS sends

Opt-In Confirmation:

-   First SMS to new contacts includes: "This is Living With Lolo. Reply YES to confirm you'd like to receive project updates via text. Reply STOP to opt out."

-   Not required for 1:1 conversations initiated by client

### 3.5.4 SMS Signature Configuration

All SMS messages sent from HubSpot SMS number must include sender identification:

**Signature Format:** \[First Name\] \| \[Title\]

**Example:** "Sara \| Lead Designer"

**Implementation:**

-   Configure in HubSpot Settings → Inbox → SMS → Message Templates

-   Create signature template with personalization tokens: {{owner.firstName}} \| {{owner.role}}

-   Signature automatically appends to all outbound SMS from HubSpot

**Rationale:** SMS messages use Name \| Title only; company signature block is not included to maintain message brevity and readability (per BRD 3.2.2.3).
## 3.5A Salesmsg Urgent Hotline Configuration

### 3.5A.1 Purpose and Scope

The Salesmsg urgent hotline serves as Living With Lolo's dedicated channel for time-sensitive client emergencies and urgent project issues requiring immediate attention outside standard business hours or standard communication channels.

**Purpose:** Handle client emergencies, urgent project issues requiring immediate response

**Scope:**

-   Dedicated 10DLC phone number (separate from HubSpot SMS number)

-   Shared inbox accessible to emergency response team only

-   After-hours coverage with escalation workflow

-   Operates as standalone platform (no HubSpot integration in Phase 1)

### 3.5A.2 Phone Number Provisioning

**Provider:** Salesmsg (salesmsg.com)

**Number Type:** 10DLC (10-Digit Long Code) business SMS number

**Provisioning Process:**

1.  Create Salesmsg account (salesmsg.com/signup)

2.  Select "Shared Inbox" plan (supports multiple team members)

3.  Provision 10DLC number with local area code (480 or 623 recommended for Scottsdale, Arizona)

4.  Complete carrier registration and compliance verification

5.  Expected provisioning time: 5-10 business days (carrier approval required)

**Estimated Cost:** $29-49/month (shared inbox + 10DLC number)

### 3.5A.3 Emergency Response Team Configuration

**Shared Inbox Name:** "LWL Urgent Hotline"

**Inbox Members:**

-   Lauren (CEO) - Full admin access

-   Brandie (Director of Construction) - Full admin access

-   Robin (Director of Operations) - Full admin access

**Access Configuration:**

1.  Navigate to Salesmsg Dashboard → Inboxes → Create Shared Inbox

2.  Add all three team members with "Admin" role

3.  Enable mobile push notifications for all three members

4.  Install Salesmsg mobile app on all three team members' devices

5.  Configure notification sound (unique/urgent tone recommended)

**Notification Settings:**

-   Real-time mobile push: Enabled (all three members)

-   In-app notifications: Enabled

-   Email notifications: Optional (secondary channel)

-   Desktop notifications: Optional

### 3.5A.4 Business Hours and After-Hours Configuration

**Business Hours Definition:**

-   Days: Monday through Friday

-   Time: 8:00 AM - 5:00 PM Arizona Time (UTC-7)

-   Timezone: America/Phoenix (no DST)

**Holiday Calendar:** Match HubSpot holiday calendar (Section 3.6.7)

**After-Hours Auto-Reply Configuration:**

Template (per BRD Section 3.2.2.4): "Thank you for contacting Living With Lolo's urgent hotline. We've received your message. For genuine emergencies requiring immediate assistance, one of our team members will respond as soon as possible. For non-urgent matters, please email <VIP@livingwithlolo.com> and we'll respond within one business day during office hours (Mon-Fri 8 AM-5 PM Arizona Time). In case of life-threatening emergency, call 911 immediately."

**Configuration Steps:**

1.  Salesmsg Dashboard → Automations → Create Auto-Reply

2.  Trigger: New conversation created outside business hours

3.  Delay: 0 seconds (immediate)

4.  Message: Paste template above

5.  Apply to: LWL Urgent Hotline inbox only

### 3.5A.5 Escalation Workflow (Optional)

**Purpose:** Secondary alert if urgent message remains unanswered for 10 minutes

**Implementation:** n8n or Zapier workflow (optional; evaluate during Phase 2)

**Workflow Logic:**

1.  Salesmsg webhook fires when new message received

2.  Wait 10 minutes

3.  Check if conversation has response from team

4.  IF no response: POST secondary alert to Slack #urgent-alerts with "⚠️ URGENT: Unanswered for 10 minutes" header

5.  ELSE: End workflow (no secondary alert needed)

**Decision Point:** Discuss with CEO during Phase 1 Discovery whether 10-minute escalation adds value or creates alert fatigue.

### 3.5A.6 TCPA Compliance

**Opt-Out Management:**

-   Configure auto-reply for "STOP", "UNSUBSCRIBE", "QUIT" keywords

-   Auto-reply message: "You have been unsubscribed from Living With Lolo urgent text messages. This number is for time-sensitive project emergencies only. For general inquiries, email <VIP@livingwithlolo.com> or call \[LWL main phone\]."

-   Unsubscribed contacts automatically suppressed from future SMS

**Opt-In Documentation:**

-   Clients informed of urgent hotline number through:

    -   Project kickoff documentation

    -   After-hours auto-reply from VIP@ email and HubSpot SMS

    -   Emergency contact card provided during Design phase

-   Usage limited to genuine emergencies (not marketing/promotional)

### 3.5A.7 Maintenance and Monitoring

**Weekly Review (Emergency Response Team):**

-   Review urgent hotline usage patterns

-   Validate appropriate usage (genuine emergencies vs. routine inquiries)

-   Discuss response time performance and coverage gaps

**Monthly Analysis:**

-   Count of urgent messages received

-   Average response time

-   Percentage requiring after-hours response

-   Trends indicating client communication preferences

**Escalation to Standard Channels:**

-   If non-urgent inquiry received via hotline, respond and redirect: "Thanks for reaching out. This urgent line is reserved for time-sensitive emergencies. For general project questions, please email <VIP@livingwithlolo.com> where your POC will respond within one business day."

## 3.5B Slack Integration Configuration

### 3.5B.1 Slack Workspace Setup

**Workspace Name:** Living With Lolo (existing Slack workspace)

**Required Channels:**

1.  #urgent-alerts (private channel - emergency response team only)

2.  #client-inboxes (public channel - all Standard Users and Administrators)

**Slack Admin:** Confirm existing workspace administrator during Phase 1 Discovery

### 3.5B.2 #urgent-alerts Channel Configuration

**Purpose:** Real-time notifications for inbound urgent text messages from Salesmsg hotline

**Channel Settings:**

-   Channel Type: Private

-   Members: Lauren, Brandie, Robin (emergency response team only)

-   Notification Preferences: All members enable "Notify me about all new messages" + mobile push

-   Channel Description: "🚨 Real-time alerts for urgent client text messages. Emergency response team only."

**Slack Incoming Webhook Setup:**

1.  Slack Workspace Settings → Apps → Incoming Webhooks

2.  Create new webhook for #urgent-alerts channel

3.  Copy webhook URL (format: <https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXX>)

4.  Provide webhook URL to integration developer (for n8n or Zapier configuration)

### 3.5B.3 #urgent-alerts Integration Workflow

**Trigger:** Salesmsg inbound message webhook

**Workflow Platform:** n8n (recommended) or Zapier

**Workflow Steps:**

1.  **Webhook Trigger:** Salesmsg fires webhook on new inbound message

2.  **Parse Payload:** Extract sender phone, message preview (first 100 characters), timestamp

3.  **Format Slack Message:** Create formatted alert per BRD Section 3.6.6.3 specification

4.  **POST to Slack:** Send formatted message to #urgent-alerts webhook URL

5.  **Error Handling:** Retry up to 3 times with exponential backoff; log failures

## 3.6 HubSpot Workflow Automation

### 3.6.1 Workflow Overview

| **Workflow Name** | **Trigger** | **Purpose** | **Actions** |
| --- | --- | --- | --- |
| Conversation Assignment Routing | New Conversation created | Route to Primary POC or Unassigned queue | Assign owner, send notification |
| Deal Stage Update from Phase Change | Deal property "Project Phase" changes | Update Deal Stage when Airtable phase syncs | Update Deal Stage, log activity |
| Unassigned Conversation Alert | Conversation routed to Unassigned | Notify administrators of unmatched communication | Send email to CEO, Dir of Ops, LWL IT Lead |
| Business Hours Auto-Reply (Email) | New email received outside business hours | Acknowledge receipt with expected response time | Send auto-reply email |
| Business Hours Auto-Reply (SMS) | New SMS received outside business hours | Acknowledge receipt with expected response time | Send auto-reply SMS |
| POC Assignment Based on Phase | | | |

### 3.6.2 Workflow Specification: Conversation Assignment Routing

**Workflow Name:** "Conversation Assignment Routing"

**Purpose:** Route all new inbound conversations (email and SMS) to the appropriate POC based on project association and vacation flag status.

**Enrollment Trigger:**

-   Object: Conversation

-   Trigger: Conversation is created

-   Filters: None (enroll all new conversations)

**Workflow Actions:**

**Branch 1: VIP@ Inbox (Paid Projects)**

IF Conversation.Inbox = "VIP@livingwithlolo.com":

IF Conversation.Associated_Deal is known:

CHECK PRIMARY POC VACATION FLAG:

IF Deal.Primary_POC.Out_of_Office = TRUE:

\- Action 1: Set Owner = Deal.Backup_POC

\- Action 2: Send notification to Backup_POC

\- Action 3: Create internal note: "Routed to Backup POC - Primary POC on vacation"

ELSE (Primary POC available):

\- Action 1: Set Owner = Deal.Primary_POC

\- Action 2: Send notification to Primary_POC

\- Action 3: Create internal note: "Routed to Primary POC - standard routing"

ELSE (No Associated Deal): - Action 4: Set Owner = Unassigned - Action 5: NO automatic notification sent (self-service queue per BRD 3.3.8.3) - Action 6: Create internal note: "No Deal association found - routed to Unassigned queue" - Note: Administrators check Unassigned Conversations queue proactively 1-2 times daily

**Branch 2: welcome@ Inbox (Pre-Sales)**

IF Conversation.Inbox = "[welcome@livingwithlolo.com](mailto:hello@livingwithlolo.com)":

IF Conversation.Associated_Deal is known (pre-sales Deal in Pre-Sales pipeline): - Action 1: Set Owner = Associated Deal Owner - Action 2: Send notification to Deal Owner - Action 3: Create internal note: "Pre-sales Deal association found - routed to Deal Owner" - Note: Manual assignment in Phase 1; automated phase-based routing in Phase 1.5

ELSE (New inquiry, no Deal association):

CHECK MOLLY'S VACATION FLAG:

IF User "Molly".Out_of_Office = TRUE:

\- Action 4: Set Owner = Lauren (Backup POC for pre-sales)

\- Action 5: Send notification to Lauren

\- Action 6: Create internal note: "Routed to Lauren - Molly on vacation"

ELSE (Molly available):

\- Action 4: Set Owner = Molly (Primary POC for pre-sales)

\- Action 5: Send notification to Molly

\- Action 6: Create internal note: "Routed to Molly - standard routing"

\- Action 7: OPTIONAL - Create Deal in Pre-Sales pipeline (Stage = "Inquiry")

\- Can be manual in Phase 1; automated Deal creation deferred to Phase 1.5

**Re-enrollment:** No (conversations should only be assigned once upon creation)

**Important Configuration Notes:**

1.  **Out of Office Property:** Each HubSpot user must have a boolean custom property "Out_of_Office" configured in user settings. Administrators can view and manage all users' vacation flags.

2.  **Notification Delivery:** Notification method (email, mobile push, in-app) is configured per user in their HubSpot notification preferences (Section 3.8.3).

3.  **Conversation Ownership Persistence:** Once a conversation is assigned to a POC, that POC retains ownership for the entire conversation thread (including all future replies) until manually reassigned or closed. Phase changes do NOT trigger automatic reassignment per BRD Section 3.3.7.

4.  **Manual Reassignment Override:** Any POC or Administrator can manually reassign any conversation at any time. Reassignments are logged automatically in conversation timeline per BRD Section 3.3.6.

5.  **Unassigned Queue Self-Service:** No automatic notifications are sent for unmatched communications per BRD 3.3.8.3. All Standard Users and Administrators can proactively review and associate unmatched communications with projects.

**Testing Requirements:**

During Phase 3 Integration Testing and Phase 4 UAT, validate:

-   Messages route to Primary POC when vacation flag is FALSE

-   Messages route to Backup POC when Primary POC vacation flag is TRUE

-   Unassigned conversations appear in correct queue without triggering notifications

-   welcome@ new inquiries route to Molly by default, Lauren when Molly has vacation flag enabled

-   Conversation ownership persists through phase changes (active threads retain original POC)

### 3.6.3 Workflow Specification: Deal Stage Update from Phase Change

Workflow Name: "Deal Stage Update from Phase Change"

Enrollment Trigger:

-   Object: Deal

-   Trigger: Property "Project Phase" changes

-   Filters: Project Phase is known (not empty)

Workflow Actions:

Branch on Property: Project_Phase

IF Project_Phase = "PreDesign": Action: Update Deal Stage to "PreDesign"

ELSE IF Project_Phase = "Design": Action: Update Deal Stage to "Design"

ELSE IF Project_Phase = "Procurement": Action: Update Deal Stage to "Procurement"

ELSE IF Project_Phase = "PreConstruction": Action: Update Deal Stage to "PreConstruction"

ELSE IF Project_Phase = "Construction": Action: Update Deal Stage to "Construction"

End Branch

Action (All Branches): Create timeline note - Associated with: Current Deal - Note: "Project phase changed to Project_Phase. Deal stage updated automatically."

Re-enrollment: Yes (allow Deals to re-enroll when phase changes again)

### 3.6.4 Workflow Specification: Business Hours Auto-Reply (Email)

Workflow Name: "Business Hours Auto-Reply - Email"

Enrollment Trigger:

-   Object: Conversation

-   Trigger: Conversation is created

-   Filters:

    -   Channel = Email

    -   Conversation.Direction = Inbound (from client to LWL)

    -   Current time is OUTSIDE business hours (Monday-Friday 8 AM - 5 PM Arizona Time)

Business Hours Definition: (See Section 3.6.6 for detailed configuration)

Workflow Actions:

Action 1: Send email - To: Original sender (Conversation.Contact.Email) - From: VIP@livingwithlolo.com - Subject: "Re: Original Subject" - Content: "Thank you for contacting Living With Lolo. We've received your message and will respond within one business day. Our office hours are Monday-Friday, 8:00 AM - 5:00 PM Arizona Time. For urgent construction matters, please contact emergency contact number."

Action 2: Create internal note on Conversation - Note: "Auto-reply sent - message received outside business hours"

Re-enrollment: No (one auto-reply per conversation)

Holiday Exclusions: Configure to suppress auto-reply on company-observed holidays (see Section 3.6.7)

### 3.6.5 Workflow Specification: Business Hours Auto-Reply (SMS)

Workflow Name: "Business Hours Auto-Reply - SMS"

Enrollment Trigger:

-   Object: Conversation

-   Trigger: Conversation is created

-   Filters:

    -   Channel = SMS

    -   Conversation.Direction = Inbound

    -   Current time is OUTSIDE business hours

Workflow Actions:

Action 1: Send SMS - To: Original sender (Conversation.Contact.Phone) - From: LWL business SMS number - Content: "Thanks for texting Living With Lolo! We'll respond by the next business day. Office hours: Mon-Fri 8 AM-5 PM AZ time. For emergencies: emergency number"

Action 2: Create internal note on Conversation - Note: "Auto-reply sent - SMS received outside business hours"

Re-enrollment: No

Holiday Exclusions: Same as email auto-reply (Section 3.6.7)

### 3.6.6 Business Hours Configuration

Standard Business Hours: (Per BRD Section 3.5)

-   Days: Monday through Friday

-   Time: 8:00 AM - 5:00 PM

-   Timezone: America/Phoenix (UTC-7 year-round, no DST)

HubSpot Configuration Path:

1.  Settings \> Account \> Business Hours

2.  Set timezone: America/Phoenix

3.  Configure hours: Monday-Friday 8:00 AM - 5:00 PM

4.  Saturday-Sunday: Closed

5.  Save configuration

Workflow Time Filters:

-   All business-hours-dependent workflows reference this account-level business hours setting

-   No hardcoded time values in individual workflows (ensures consistency)

Business Hours Application:

-   VIP@livingwithlolo.com: After-hours auto-reply enabled (per BRD Section 3.6.4, 3.6.5)

-   welcome@livingwithlolo.com: NO after-hours auto-reply in Phase 1 (maintains personal touch for sales communications per BRD 7.3.2.15)

-   Decision on welcome@ auto-reply deferred to Phase 1.5 Discovery based on inquiry volume

### 3.6.7 Holiday Calendar Configuration

Company Observed Holidays: (Per BRD Section 7.3.2.7)

Approximately 8-10 US holidays annually:

-   New Year's Day (January 1)

-   Memorial Day (Last Monday in May)

-   Independence Day (July 4)

-   Labor Day (First Monday in September)

-   Thanksgiving Day (Fourth Thursday in November)

-   Day After Thanksgiving (Fourth Friday in November)

-   Christmas Eve (December 24)

-   Christmas Day (December 25)

Additional holidays to be confirmed by CEO during Phase 1 Discovery

Configuration Method: (Per BRD Section 7.3.2.7)

-   Holidays configured as workflow exclusion dates (specific calendar dates, not recurring rules)

-   Configuration Path: Within each auto-reply workflow, add "Exclusion List" containing specific dates

-   CRITICAL MAINTENANCE REQUIREMENT: LWL IT Lead must update workflows each November with next calendar year's holiday dates

-   Set annual calendar reminder for November 15 to complete holiday updates

Example Exclusion Date Configuration:

Workflow: "Business Hours Auto-Reply - Email" Exclusions:

-   January 1, 2026 (New Year's Day)

-   May 25, 2026 (Memorial Day)

-   July 4, 2026 (Independence Day)

-   September 7, 2026 (Labor Day)

-   November 26, 2026 (Thanksgiving)

-   November 27, 2026 (Day After Thanksgiving)

-   December 24, 2026 (Christmas Eve)

-   December 25, 2026 (Christmas Day)

Testing Requirement: During Phase 4 UAT, validate that auto-replies are suppressed on configured holiday dates.

### 3.6.8 POC Assignment Based on Phase

**Purpose:** Automatically assign Primary and Backup POCs to Deal records based on current project phase, ensuring new communications route to the correct team member.

**Enrollment Trigger:**

-   Object: Deal

-   Triggers:

    1.  Deal is created (for new Paid projects synced from Airtable)

    2.  Property "Project Phase" changes (for phase transitions)

-   Filters: Project Phase is known (not empty)

**Workflow Actions:**

Branch on Property: Project_Phase

**IF Project_Phase = "PreDesign":**

-   Action 1: Set Primary POC = Molly (HubSpot User ID)

-   Action 2: Set Backup POC = Robin (HubSpot User ID)

**ELSE IF Project_Phase = "Design":**

-   Action 1: Set Primary POC = Sara (HubSpot User ID)

-   Action 2: Set Backup POC = Meghan (HubSpot User ID)

**ELSE IF Project_Phase = "Procurement":**

-   Action 1: Set Primary POC = Robin (HubSpot User ID)

-   Action 2: Set Backup POC = Molly (HubSpot User ID)

**ELSE IF Project_Phase = "PreConstruction":**

-   Action 1: Set Primary POC = Brandie (HubSpot User ID)

-   Action 2: Set Backup POC = Debra (HubSpot User ID)

**ELSE IF Project_Phase = "Construction":**

-   Action 1: Set Primary POC = Debra (HubSpot User ID)

-   Action 2: Set Backup POC = Brandie (HubSpot User ID)

**ELSE (unrecognized phase value):**

-   Action 1: Create internal note on Deal

    -   Note: "ERROR: Unknown phase value received: {{Project_Phase}}. POC assignment failed. Manual assignment required."

-   Action 2: Send email alert to LWL IT Lead

    -   To: <johnny@livingwithlolo.com>

    -   Subject: "⚠ POC Assignment Workflow Error - Unknown Phase Value"

    -   Body: "Deal ID: {{Deal ID}}, Project ID: {{Project_ID}}, Received Phase Value: {{Project_Phase}}"

**Action (All Branches):** Create timeline note on Deal

-   Note: "POC assignments updated. Primary POC: {{Primary_POC}}, Backup POC: {{Backup_POC}}. Triggered by: {{Project_Phase}} phase."

**Re-enrollment:** Yes (allow Deals to re-enroll when phase changes again)

**Important Notes:**

1.  **HubSpot User IDs:** During Phase 2 configuration, LWL IT Lead must obtain HubSpot User IDs for all team members and configure workflow with actual numeric IDs (not email addresses).

2.  **Phase Name Validation:** Phase values in webhook payload from Airtable must exactly match branch conditions above (case-sensitive). See Section 4.2.2 for validation requirements.

3.  **Conversation Ownership Persistence:** This workflow only updates POC assignments on the Deal record. Active (Open) conversations retain their currently assigned POC per BRD Section 3.3.7. Only NEW conversations created after phase change will route to the newly assigned Primary POC.

4.  **Deal Owner Update:** When Primary POC changes, the workflow should also update the Deal Owner field to match Primary POC for reporting consistency.

5.  **Monitoring:** Weekly POC Assignment Health Check workflow (Section 3.6.9) validates that all active Deals have both Primary and Backup POCs assigned.

### 3.6.9 Weekly POC Assignment Health Check Workflow

This workflow runs every Monday at 8:00 AM Arizona Time to detect Deals with missing POC assignments.

**What it does:**

-   Finds all active Deals in the Client Projects pipeline (stages: PreDesign through Construction)

-   Filters for Deals where Primary POC or Backup POC fields are empty

-   If blank POCs found: Sends email alert to Johnny (LWL IT Lead) and Lauren (CEO) with list of affected Deal IDs

-   If no issues: Logs success silently without sending email

**Why it matters:**

-   Detects when the POC Assignment workflow (Section 3.6.8) fails to execute

-   Provides early warning system for workflow failures

-   Common failure causes: Phase name mismatches, workflow accidentally disabled, User ID mapping errors

**Email alert should include:**

-   List of Deal IDs with Project IDs that have blank POCs

-   Instructions to manually assign POCs and investigate workflow logs

-   Direct link to POC Assignment workflow for troubleshooting

### 3.6.10 Monthly Phase Name Validation Workflow

This workflow runs on the 1st day of each month at 9:00 AM Arizona Time to detect invalid phase values.

**What it does:**

-   Finds all Deals where Project Phase is not empty

-   Filters for phase values that don't match the 5 valid options: PreDesign, Design, Procurement, PreConstruction, Construction

-   If invalid phases found: Sends email alert to Johnny and Josh (Airtable Admin) with list of affected Deals

-   If no issues: Logs success silently

**Why it matters:**

-   Catches phase name mismatches between Airtable and HubSpot (the #1 cause of POC assignment failures per BRD Risk T-12)

-   Phase names must match exactly (case-sensitive) for POC assignment workflow to function

-   Provides monthly data quality validation

**Email alert should include:**

-   List of Deal IDs with Project IDs showing what invalid phase value was received

-   Reminder of the 5 valid phase values

-   Instructions for Josh to validate Airtable Phase field values match exactly

## 3.7 Project Master Info Field Implementation

Purpose: Per BRD Section 3.2.3.2.3, provide a centralized project information field visible at top of each Deal record containing key client information, preferences, constraints, and decision-maker details.

### 3.7.1 Field Configuration

Object: Deal

Property Name: "Project Master Info"

Internal Name: project_master_info

Field Type: Multi-line text (rich text enabled)

Required: No (populated after project kickoff)

Visibility: All users (Standard Users and Administrators can view and edit)

Position: Custom property group "LWL Project Management" at top of Deal record layout

### 3.7.2 Template Structure

Template to be finalized by LWL Executive Team during Phase 1 Discovery (BRD 7.3.1.14)

Proposed Template Structure:

=== PROJECT MASTER INFO ===

PRIMARY CONTACTS: Auto-populated from associated Contacts or manual entry

-   Decision Maker: Name, role, preferred contact method

-   Additional Contacts: Names, relationships, contact preferences

BUDGET & FINANCIAL: Manual entry

-   Budget Range: $XXX,XXX - $XXX,XXX

-   Budget Sensitivity: High/Medium/Low

-   Payment Schedule Notes: Any special arrangements

COMMUNICATION PREFERENCES: Manual entry

-   Best Times to Contact: Morning/Afternoon/Evening preferences

-   Preferred Channel: Email/SMS/Phone

-   Response Expectations: Do they need same-day responses? Weekly updates?

PROJECT CONSTRAINTS: Manual entry

-   Timeline Constraints: Fixed move-in dates, events, seasonal considerations

-   Access Restrictions: Gate codes, pet considerations, security requirements

-   Special Considerations: Work-from-home schedules, noise sensitivities, etc.

DESIGN & STYLE PREFERENCES: Manual entry

-   Design Style: Modern, Traditional, Transitional, etc.

-   Known Likes/Dislikes: Colors, materials, vendors they love/hate

-   Reference Projects: Links to inspiration or past LWL projects

INTERNAL NOTES: Manual entry - team observations and context

-   Client Personality: Communication style, decision-making approach

-   Relationship History: How they found LWL, past interactions, referral source

-   Red Flags / Special Care Items: Anything team should know

Last Updated: Date by POC Name

### 3.7.3 Usage and Maintenance

Initial Population:

-   Primary POC responsible for populating Project Master Info during project kickoff (PreDesign phase)

-   Minimum required sections: Primary Contacts, Communication Preferences

-   Optional sections populated as information becomes available

Ongoing Maintenance:

-   Primary POC updates Master Info when client preferences or constraints change

-   POC handoff during phase transitions includes review of Master Info accuracy

-   All team members encouraged to add relevant observations to Internal Notes section

Training Emphasis:

-   Phase 5 training will include Project Master Info as required step for new Paid projects (BRD Risk A-10)

-   Executive Team reinforces usage expectations during team meetings

### 3.7.4 Future Enhancement: Auto-Population

Post-Phase 1 Opportunity (per BRD Risk A-10, Addendum A.2.9):

After Phase 1 stabilization (90+ days post-launch), LWL may implement Zapier automation to pre-populate structured sections from Airtable when project status changes to "Paid."

Automation Scope:

-   Auto-populate: Client names, budget (if available), known contact preferences from Airtable

-   Manual completion: Team adds qualitative information (personality notes, design preferences, special considerations)

-   Benefit: Reduces manual data entry time by approximately 60-70%

Implementation Details:

-   Trigger: Airtable "New Paid Project" webhook (already implemented in Phase 1)

-   Action: Zapier formats template with available data, populates Project Master Info field in HubSpot Deal

-   Format: Uses approved template structure with pre-filled sections where data available

-   Estimated Effort: 4-6 hours development + 2 hours testing

Prerequisites:

-   Template structure finalized and adoption patterns observed during Phase 1

-   Airtable contains all fields needed for auto-population

-   Validation that manual sections (qualitative insights) remain editable after auto-population

**Decision Point:** Implement after Phase 1 stabilization once team comfortable with manual workflow. Automation should reduce burden, not create confusion.

## 3.8 User Roles and Permissions

### 3.8.1 HubSpot Permission Sets

| **Permission Set** | **HubSpot Role** | **Capabilities** | **Assigned To** |
| --- | --- | --- | --- |
| Administrator | Super Admin | All capabilities including account settings, user management, workflow configuration, integration setup, audit logs | CEO, LWL IT Lead, Josh (TBD during Phase 1) |
| Standard User | Sales Professional | View all communications, reply to messages, create internal notes, update conversation status, reassign conversations, view dashboards | All other team members |

CRITICAL: Per BRD Section 3.10.2, ALL users must have visibility into ALL client communications across projects, channels, and POCs. Do not restrict data visibility by owner or team assignment.

### 3.8.2 Detailed Permission Configuration

Administrators (Super Admin Role):

-   Account Access: Edit account settings, manage users, configure integrations

-   Objects: View, create, edit, delete all Deals, Contacts, Conversations

-   Workflows: Create, edit, activate/deactivate workflows

-   Reporting: Access all reports, create custom reports

-   Conversations Inbox: View all conversations including Unassigned queue, reassign any conversation, close conversations

-   Settings: Manage business hours, holiday calendar, routing rules, notification templates

Standard Users (Sales Professional Role):

-   Account Access: View-only account settings (cannot edit)

-   Objects: View, create, edit all Deals, Contacts, Conversations (no delete)

-   Workflows: View-only (cannot create or edit)

-   Reporting: View all reports (cannot create custom reports)

-   Conversations Inbox: View all conversations, reply to assigned conversations, create internal notes, \@mention team members, update conversation status (Open/Closed), manually reassign conversations to other team members

-   Settings: View-only

-   Vacation Flags: View and manage own "Out of Office" status only; cannot view or edit other users' vacation flags

Key Differences:

-   Standard Users CANNOT edit workflows, manage users, or change account-level settings

-   Standard Users CAN manually reassign any conversation (per BRD 3.3.6 - team coordination flexibility)

-   Standard Users CAN close any conversation (per BRD 5.5.4 - POCs manage status for their phase)

### 3.8.3 Notification Preferences by Role

Configurable Per User (BRD Section 4.3.5):

Each user configures their own notification preferences in HubSpot Settings \> Notifications:

Administrators:

-   New Unassigned Conversation: Email + Mobile Push (immediate)

-   Conversation Assigned to Me: Email + In-App + Mobile Push

-   \@Mentioned in Note: Email + In-App + Mobile Push

-   Sync Errors: Email (immediate - requires custom Zapier notification, see Section 5.4.3)

Standard Users (POCs):

-   Conversation Assigned to Me: Email + In-App + Mobile Push

-   New Reply in My Conversation: In-App + Mobile Push (email optional)

-   \@Mentioned in Note: Email + In-App + Mobile Push

-   Conversation Reassigned Away from Me: In-App notification

Notification Delivery Timing:

-   In-App: Immediate (visible when user logs into HubSpot)

-   Mobile Push: Immediate (requires HubSpot mobile app installed)

-   Email: Immediate or Daily Digest (user configurable)

Training Guidance: Phase 5 training includes notification preference setup workshop to ensure all users configure preferences aligned with their role and work style.

### 3.8.4 User Custom Properties

Each HubSpot user account has the following custom properties configured:

**Out of Office (Vacation Flag)**

-   **Property Name:** Out of Office

-   **Internal Name:** out_of_office

-   **Field Type:** Checkbox (boolean)

-   **Default Value:** FALSE (not on vacation)

-   **Editable By:** User themselves (manage own flag) + Administrators (manage all flags)

-   **Purpose:** Controls vacation flag routing logic (per BRD Section 3.3.2); when TRUE, new conversations route to Backup POC instead of Primary POC

-   **Location:** User Settings → Preferences → Custom Properties

**Configuration Steps:**

1.  HubSpot Settings → Properties → User Properties

2.  Create new property: "Out of Office"

3.  Type: Checkbox

4.  Default: FALSE

5.  Description: "Enable when on vacation/PTO to route new messages to Backup POC. Disable upon return."

6.  Permissions: User can edit own; Administrators can edit all

**User Responsibility (per BRD 3.3.2.3):**

-   Enable flag on last working day before absence

-   Disable flag on first working day upon return

-   Administrators monitor via Vacation Flag Status Dashboard (Section 3.8.5)

### 3.8.5 Vacation Flag Status Dashboard

**Purpose:** Real-time visibility into team members' vacation flag status for administrators.

**Dashboard Configuration:**

**Dashboard Name:** "Team Vacation Flag Status"

**Dashboard Location:** HubSpot Reports → Custom Dashboards

**Widget 1: Users Currently Out of Office**

-   **Report Type:** Users list

-   **Filter:** Out of Office = TRUE

-   **Display Columns:** User Name, Out of Office (flag status), Date Last Modified

-   **Sort:** By Date Last Modified (oldest first - identifies forgotten flags)

-   **Purpose:** Show which team members currently have vacation flag enabled

**Widget 2: Vacation Flags Enabled \>5 Days (Alert)**

-   **Report Type:** Users list

-   **Filter:** Out of Office = TRUE AND (Current Date - Date Last Modified) \> 5 days

-   **Display Columns:** User Name, Days Enabled, "ACTION REQUIRED" badge

-   **Color Coding:** Red background (attention required)

-   **Purpose:** Catch team members who forgot to disable flag upon return

**Widget 3: Vacation Flag Activity Log**

-   **Report Type:** Activity timeline

-   **Data:** Recent vacation flag changes (enabled/disabled) with timestamps

-   **Display:** Last 30 days of activity

-   **Purpose:** Historical view of vacation patterns and flag discipline

**Access:** Administrators only (CEO, Director of Operations, LWL IT Lead)

**Refresh Frequency:** Real-time (dashboard queries live HubSpot user data)

**Administrator Actions:**

-   Review dashboard weekly (minimum)

-   Contact team members with flags enabled \>5 days (may have forgotten to disable)

-   Manually disable flag if confirmed team member returned from time off

-   Document patterns of forgotten flags for training reinforcement

**Monitoring Cadence:**

-   LWL IT Lead: Weekly review as part of system health checks

-   Director of Operations: Weekly review during operational planning

-   CEO: Ad-hoc review when planning coverage or team coordination