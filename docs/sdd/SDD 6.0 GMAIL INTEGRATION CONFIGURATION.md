---
doc_type: SDD
section_id: sdd.gmail-integration-configuration
title: Gmail Integration Configuration
---
## 6.0 GMAIL INTEGRATION CONFIGURATION

Purpose: Connect VIP@livingwithlolo.com and [welcome@livingwithlolo.com](mailto:hello@livingwithlolo.com) Gmail inboxes to HubSpot Conversations Inbox for unified email management

VIP@ Inbox: Paid project client communications welcome@ Inbox: Pre-sales inquiry and lead communications

Integration Method: HubSpot native Gmail integration via OAuth 2.0 (separate OAuth connections for each inbox)

## 6.1 Gmail Integration Overview

Purpose: Connect VIP@livingwithlolo.com Gmail inbox to HubSpot Conversations Inbox for unified email management

Integration Method: HubSpot native Gmail integration via OAuth 2.0

Authoritative Email Repository: Gmail retains all raw SMTP messages indefinitely (per BRD Section 4.1.3.1); HubSpot provides operational interface

## 6.2 Google Workspace Mailbox Configuration

## **6.2.1 Shared Mailbox Setup - All Inboxes**

**Responsibility:** Google Workspace Administrator (LWL IT Lead or designated admin)

Living With Lolo requires four shared email addresses, each with distinct purpose and routing:

1.  <VIP@livingwithlolo.com> - Active paid project communications

2.  <welcome@livingwithlolo.com> - Pre-sales inquiries and lead management

3.  <info@livingwithlolo.com> - General business inquiries, vendor communications

4.  <family@livingwithlolo.com> - Post-project client care, review requests, long-term relationships

Configuration Process (Repeat for Each Mailbox):

Step 1: Create Shared Mailbox

1.  Navigate to Google Workspace Admin Console (admin.google.com)

2.  Users → Add New User

3.  Email: \[inbox\]@livingwithlolo.com

4.  Name:

-   VIP@: "Living With Lolo - Client Communications"

-   welcome@: "Living With Lolo - Sales Inquiries"

-   info@: "Living With Lolo - General Inquiries"

-   family@: "Living With Lolo - Client Care"

5.  User Type: Standard user (not group, to maintain individual mailbox)

Step 2: Configure Mailbox Settings

1.  Enable IMAP access (required for HubSpot sync)

-   Gmail Settings → Forwarding and POP/IMAP → Enable IMAP

2.  Configure auto-forwarding restrictions (disable to prevent accidental forwarding outside organization)

3.  Set storage quota: Business Standard minimum (2 TB shared, adequate for email volume)

4.  Disable "Send as" delegation to enforce HubSpot-only sending (prevents direct Gmail usage)

Step 3: Delegate Access (Optional Pre-Launch Only)

-   During transition period, delegate access to key team members for monitoring:

-   VIP@: Delegate to Lauren, Robin, Johnny (pre-launch monitoring only)

-   welcome@: Delegate to Molly, Lauren (pre-launch monitoring only)

-   info@: Delegate to Lauren, Robin (pre-launch monitoring only)

-   family@: Delegate to Lauren, Robin (pre-launch monitoring only)

-   After HubSpot go-live, revoke ALL direct Gmail access (team uses HubSpot only per BRD 4.1.2.2)

Step 4: Email Signature Configuration

Configure organization-level locked email signature (per BRD Section 3.2.1.3):

1.  Navigate to Google Workspace Admin Console → Apps → Google Workspace → Gmail → User Settings

2.  Select organizational unit: Living With Lolo (all users)

3.  End User Settings → Email Signature

4.  Enable "End user can change signature"

5.  Create signature template in HTML editor:

\<div style=\"font-family: Arial, sans-serif; font-size: 10pt; color: #333333;\"\> \<p\>\<strong\>{{FirstName}} \| {{Title}}\</strong\>\</p\> \<hr style=\"border: 0; border-top: 2px solid #000000; width: 100%; margin: 10px 0;\"\> \<p\>\<strong\>Living With Lolo\</strong\>\<br\> \[Office Address\]\<br\> \[Office Phone\]\<br\> \<a href=\"mailto:VIP@livingwithlolo.com\" style=\"color: #0066cc;\"\>VIP@livingwithlolo.com\</a\>\<br\> \<a href=\"https://www.livingwithlolo.com\" style=\"color: #0066cc;\"\>www.livingwithlolo.com\</a\>\</p\> \<p\>\[Social Media Links\]\</p\> \<p style=\"font-size: 8pt; color: #666666;\"\>\[Brand Tagline or Disclaimer\]\</p\> \</div\>

6.  Assign signature to corresponding inbox in HubSpot Conversations settings

7.  HubSpot automatically applies correct signature based on sending inbox

Signature Enforcement (per BRD 3.2.1.3):

-   Google Workspace Admin Console enforces signature at organization level

-   HubSpot signatures must match Google Workspace template for consistency

-   Quarterly validation ensures both systems use identical signature structure

## 6.3 HubSpot Gmail Integration Setup

### 6.3.1 OAuth Connection Configuration

Responsibility: LWL IT Lead

Prerequisites:

-   VIP@livingwithlolo.com mailbox created and configured

-   LWL IT Lead has Super Admin access to HubSpot account

-   Google Workspace Admin has granted OAuth consent for HubSpot integration

Configuration Steps:

For VIP@livingwithlolo.com: (OAuth Process):

Step 1: Initiate Gmail Connection

1\. Navigate to HubSpot Settings → Inbox → Email

2\. Click "Connect Personal Email"

3\. Select "Gmail" from provider list

Step 2: OAuth Authentication

1\. Click "Connect Gmail Account"

2\. Sign in as VIP@livingwithlolo.com

3\. Review permissions requested by HubSpot: - Read, send, delete, and manage email - View and manage contacts

4\. Click "Allow"

Step 3: Select Inbox for Connection

1\. HubSpot displays available inboxes

2\. Select "LWL Client Communications" inbox

3\. Click "Save"

Step 4: Configure Sync Settings

-   Email sync: Enabled (two-way technical sync)

-   Sync frequency: Real-time (polls every 2-5 minutes)

-   Threading: Automatic (based on email headers)

Historical sync: Last 30 days recommended

Step 5: Test Connection

1\. Send test email to VIP@livingwithlolo.com

2\. Verify appears in HubSpot Conversations Inbox within 5 minutes

3\. Send reply and confirm threading works 4. Validate Contact auto-association

For welcome@livingwithlolo.com (Repeat OAuth Process):

Step 1: Initiate Second Gmail Connection

1.  Navigate to HubSpot Settings → Inbox → Email

2.  Click "Connect Personal Email" (connects second inbox)

3.  Select "Gmail" from provider list

Step 2: OAuth Authentication

1.  Click "Connect Gmail Account"

2.  Sign in as welcome@livingwithlolo.com

3.  Review and grant permissions (same as VIP@ inbox)

Step 3: Select Inbox for Connection

1.  HubSpot displays available inboxes

2.  Select "LWL Client Communications" inbox (or create new inbox view for welcome@ if preferred)

3.  Click "Save"

Step 4: Configure Sync Settings

-   Same configuration as VIP@ inbox (real-time sync, one-way, automatic threading)

Step 5: Test Connection

1.  Send test email to welcome@livingwithlolo.com

2.  Verify appears in HubSpot Conversations Inbox within 5 minutes

3.  Confirm routes to Molly (Primary POC for welcome@)

### 6.3.2 Email Sending Configuration

Outbound Email Behavior:

-   When POCs reply to client emails in HubSpot Conversations Inbox, replies are sent FROM: VIP@livingwithlolo.com

-   Client sees all emails as coming from single LWL address (per BRD Section 1.1, unified brand identity)

-   HubSpot uses Gmail SMTP for delivery (automatic via OAuth connection)

Email Signature:

Configure shared email signature for VIP@livingwithlolo.com:

1.  HubSpot Settings \> Inbox \> Email \> Signatures

2.  Create signature template:

POC Name POC Title Living With Lolo Office Phone VIP@livingwithlolo.com www.livingwithlolo.com

3.  Signature automatically appends to all outbound emails from HubSpot

Personalization Tokens:

-   Use HubSpot personalization tokens in signature template:

    -   {{owner.firstName}} {{owner.lastName}}

    -   {{owner.role}}

-   Signature dynamically reflects which POC is sending email

welcome@livingwithlolo.com Signature:

Configure separate signature for pre-sales communications:

{{owner.firstName}} {{owner.lastName}} {{owner.role}} Living With Lolo Office Phone welcome@livingwithlolo.com www.livingwithlolo.com

Signature Assignment:

-   VIP@ inbox uses VIP@ signature

-   welcome@ inbox uses welcome@ signature

-   HubSpot automatically applies correct signature based on sending inbox

## 6.4 Gmail Data Retention and Compliance

### 6.4.1 Gmail Vault Configuration

Purpose: Legal compliance and disaster recovery backup (per BRD 4.1.3.1)

Configuration:

1.  Google Workspace Admin Console \> Apps \> Google Workspace \> Gmail \> Vault

2.  Enable Vault for ALL Living With Lolo shared mailboxes:

-   <VIP@livingwithlolo.com>

-   <welcome@livingwithlolo.com>

-   <info@livingwithlolo.com>

-   <family@livingwithlolo.com>

3.  Retention Policy: Indefinite retention (do not delete emails automatically)

4.  Legal Holds: Configure if needed for litigation or regulatory requirements

Backup Frequency: Gmail Vault continuously archives all messages in real-time

### 6.4.2 Export and Audit Procedures

Monthly Email Export (Backup):

-   Responsibility: LWL IT Lead

-   Process:

    1.  Google Vault \> Create Export

    2.  Account: VIP@, welcome@, info@, family@ (create separate export for each)

    3.  Date Range: Previous calendar month

    4.  Format: MBOX

    5.  Download exported file

    6.  Store in LWL secure backup location (Google Drive folder or encrypted external drive)

    7.  Naming convention: \[Inbox\]-Backup-YYYY-MM.mbox

-   Example: VIP-Backup-2025-10.mbox

-   Example: welcome-Backup-2025-10.mbox

Audit Log Access:

-   Gmail Audit logs available in Google Workspace Admin Console

-   Tracks: Email sent/received, account access, setting changes

-   Retention: 6 months in Admin Console (export for longer retention if needed)

## 6.5 Gmail Troubleshooting and Monitoring

### 6.5.1 Common Sync Issues and Resolution

| **Issue** | **Symptom** | **Resolution** |
| --- | --- | --- |
| OAuth Token Expiration | Emails stop syncing; HubSpot shows "Reconnect Gmail" error | Re-authenticate OAuth connection (Section 6.3.1 Steps 2-3) |
| Gmail Storage Full | Cannot receive new emails; bounce-back messages | Increase Google Workspace storage quota or archive old emails |
| Rate Limiting | Sync delays during high-volume periods | Delay resolved automatically; consider batch processing during off-peak hours |
| Incorrect Threading | Emails not grouping as expected in HubSpot | Verify email headers (References, In-Reply-To) intact; may require HubSpot Support investigation |
| Missing Attachments | Attachments in Gmail but not visible in HubSpot | Check attachment size limits (HubSpot max 30 MB per file); manually upload if needed |

### 6.5.2 Monitoring Gmail Integration Health

Daily Checks (First 30 Days Post-Launch):

-   Verify new emails arriving in HubSpot Conversations Inbox

-   Check for OAuth connection errors in HubSpot Settings \> Inbox

-   Monitor Google Workspace Admin Console for delivery issues

Weekly Checks (Ongoing):

-   Review Gmail storage usage (alert if approaching 80% quota)

-   Validate sample emails threading correctly in HubSpot

-   Check HubSpot Inbox for any "Reconnect Required" banners

Alert Thresholds:

-   No emails synced in 24 hours → Investigate immediately

-   OAuth token expiration notice → Reauthenticate within 24 hours

-   Storage more than 80% quota → Plan for storage increase or archival