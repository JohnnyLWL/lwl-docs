---
source: SDD - System Design Document - Consolidated Communication PART THREE v1.docx
section: 8.4 JOHNNY'S IMPLEMENTATION GUIDE (HubSpot)
integrity: full
format: preservation_mode
encoding: utf-8
extraction_method: paragraph_and_table_parser
order_preserved: true
tables_preserved: true
revision: 1.1
strict_lossless_mode: true
---

**LIVING WITH LOLO**

**SYSTEM DESIGN DOCUMENT (SDD)**

**Consolidated Client Communications Hub**

# Part 3  8.4 JOHNNY'S IMPLEMENTATION GUIDE (HubSpot)

**Purpose:** Complete step-by-step guide for Johnny to configure HubSpot
account, integrate Gmail, build workflows, and test all HubSpot-side
components. This is Johnny's definitive implementation reference.

**Target Audience:** Johnny (LWL IT Lead), with sections accessible to
CEO for approval decisions

**Document Organization:**

-   8.4.1: Prerequisites Checklist

-   8.4.2: HubSpot Account Foundation Setup

-   8.4.3: Gmail Integration Configuration

-   8.4.4: HubSpot SMS Setup

-   8.4.5: HubSpot Data Model Configuration

-   8.4.6: Create HubSpot Private App for Zapier

-   8.4.7: Obtain HubSpot User IDs

-   8.4.8: Build HubSpot Workflows (7 workflows, action-by-action)

-   8.4.9: Configure User Roles and Permissions

-   8.4.10: Testing Procedures

-   8.4.11: Johnny's Troubleshooting Guide

### 8.4.1 Prerequisites Checklist

**Purpose:** Verify all prerequisites are in place before Johnny begins
HubSpot configuration.

**HubSpot Subscription Requirements**

Before beginning implementation, verify the following subscriptions are
active:

**Required Subscriptions:**

☐ **HubSpot Sales Hub Professional (10 seats)**

> License type: Paid seats
>
> Quantity: 10 user licenses
>
> Purpose: Core CRM, Deals, Contacts, Conversations Inbox
>
> Estimated cost: $45,000-50,000/year (approximately $4,500-5,000 per
> seat)
>
> Purchase status: _____________
>
> Account ID: _____________
>
> Login verified: _____________

☐ HubSpot Marketing Hub Professional (1 seat)

> License type: Paid seat
>
> Quantity: 1 user license
>
> Purpose: Enables SMS Access Add-On (required dependency)
>
> Estimated cost: $800-1,200/year
>
> Purchase status: _____________

☐ HubSpot SMS Access Add-On

> Included with: Marketing Hub Professional
>
> Purpose: Text messaging capability
>
> Business phone number: Will be provisioned during setup (Section
> 8.4.4)
>
> SMS credits: Confirm pricing model with HubSpot sales (per-message or
> included)
>
> Subscription Validation:
>
> Log into HubSpot account
>
> Navigate to Settings → Account & Billing
>
> Verify all 3 products listed as "Active"
>
> Screenshot for documentation: _____________
>
> Access and Permissions

☐ Johnny has Super Admin access to HubSpot

> Verify: Settings → Users & Teams → Johnny's user → Role = "Super
> Admin"
>
> If not Super Admin: CEO must grant Super Admin role

☐ Johnny has Google Workspace Admin access

> Required for: VIP@ and welcome@ mailbox configuration, OAuth consent,
> DNS verification
>
> Verify: Navigate to admin.google.com
>
> If access denied: CEO must grant Admin role in Google Workspace
>
> Phase 1 Discovery Decisions Finalized
>
> All Phase 1 blocking decisions must be approved before Johnny begins
> configuration (Section 8.2.2):

☐ Project ID naming convention approved

> Format: _____________
>
> Approved by: CEO, Date: _____________
>
> Documented in: Phase 1 Discovery Checklist (Section 1.7)

☐ Phase-to-POC mapping validated

> Robin (Director of Operations) sign-off:
> _____________ Date: _____________
>
> Debra (Director of Construction) sign-off:
> _____________ Date: _____________
>
> Phase names match BRD Appendix C exactly (case-sensitive):
> _____________

☐ User roster finalized

> All 10 Sales Hub user names documented: _____________
>
> Administrator vs Standard User roles assigned:
> _____________
>
> CEO approval: _____________ Date:
> _____________

☐ Project Master Info template approved

> Template structure defined by Executive Team:
> _____________
>
> CEO approval: _____________ Date:
> _____________
>
> Gmail Mailbox Prerequisites

☐ VIP@livingwithlolo.com mailbox created

> Google Workspace Admin (Johnny or designated) created mailbox
>
> IMAP enabled in Gmail settings
>
> Status: Created / Not Created
>
> If not created: See Section 6.2.1 for creation steps

☐ welcome@livingwithlolo.com mailbox created

> Google Workspace Admin created mailbox
>
> IMAP enabled
>
> Status: Created / Not Created
>
> If not created: See Section 6.2.2 for creation steps
>
> Coordination with Josh (Airtable Administrator)

☐ Received from Josh: Airtable schema validation confirmation

> Email received: _____________ Date:
> _____________
>
> Josh confirmed all required tables and fields exist (Section 8.2.2,
> Discovery Step 4)
>
> Sample Airtable project data reviewed: _____________

☐ Josh ready to provide HubSpot User IDs

> Johnny will obtain User IDs from HubSpot (Section 8.4.7)
>
> Johnny will provide mapping document to Josh
>
> Handoff scheduled for: _____________
>
> Tools and Documentation Access

☐ Access to LWL shared drive for documentation

> Path: /IT/HubSpot Implementation/
>
> Johnny has edit access: _____________

☐ BRD and SDD documents accessible

> BRD Consolidated Communications v4 FINAL
>
> SDD Consolidated Communication v3 (this document)
>
> Location: _____________

☐ Communication channels established

> Josh's email: josh@livingwithlolo.com
>
> Johnny's email: johnny@livingwithlolo.com
>
> CEO's email: lauren@livingwithlolo.com
>
> Escalation path documented: _____________
>
> Prerequisites Complete - Authorization to Proceed
>
> Sign-off:
>
> Johnny verified all prerequisites complete:
> _____________ Date: _____________
>
> Ready to begin Configuration Step A1: _____________
>
> If any prerequisite incomplete:
>
> Document blocker: _____________
>
> Responsible party: _____________
>
> Expected completion date: _____________

DO NOT PROCEED until all prerequisites met

### 8.4.2 HubSpot Account Foundation Setup

**Purpose:** Configure account-level settings that affect all users and
workflows. This is Configuration Step A1 from Section 8.2.3.

**Time Estimate:** 30-45 minutes

**Prerequisites:** HubSpot subscription active, Super Admin access
verified

#### 8.4.2.1 Step A1.1: Configure Account Timezone

> **Purpose:** Set timezone to America/Phoenix (Arizona) which doesn't
> observe Daylight Saving Time, ensuring business hours logic remains
> accurate year-round.
>
> **CRITICAL:** Arizona remains UTC-7 throughout the year. Do NOT use
> "MST" or "PST" timezone - these observe DST and will cause
> business hours drift.
>
> **Configuration Steps:**

1.  Log into HubSpot: app.hubspot.com

2.  Click Settings (gear icon, top right navigation)

3.  Navigate to: General → Account Defaults

4.  Locate "Time zone" section

5.  Click dropdown: Current value may show different timezone

6.  Search for: "America/Phoenix"

-   **Do NOT select:** "US/Mountain" (observes DST)

-   **Do NOT select:** "US/Pacific" (observes DST)

-   **Correct selection:** "America/Phoenix (UTC-7)"

7.  Click "Save" (bottom of page)

8.  Confirmation message: "Your account defaults have been updated"

> **Validation:**

1.  Refresh page

2.  Verify timezone displays: "America/Phoenix (UTC-7)"

3.  Check current time displayed in HubSpot matches Arizona time

4.  Screenshot for documentation

> **Why This Matters:**

-   Business hours workflows (Section 8.4.8, Workflows 4-5) reference
    this timezone

-   Auto-reply messages only send outside 8 AM - 5 PM Arizona Time

-   Weekly Baseline Sync (Josh's Workflow 3) runs Sunday 6 AM Arizona
    Time

-   If timezone incorrect, auto-replies send at wrong times

#### 8.4.2.2 Step A1.2: Enable Multi-Factor Authentication (MFA) Enforcement

> **Purpose:** Require all HubSpot users to configure MFA for account
> security (BRD Section 4.4.3).
>
> **Configuration Steps:**

1.  In Settings, navigate to: Security → Security

2.  Locate "Two-factor authentication" section

3.  Current setting likely shows: "Allow users to turn on two-factor
    authentication" (OPTIONAL)

4.  Click "Edit" button

5.  Select: "Require two-factor authentication for all users"
    (MANDATORY)

6.  Grace period configuration:

-   "Give users [7] days to set up two-factor authentication"

-   Rationale: Allows existing users time to configure MFA without
    immediate lockout

-   Note: New users (provisioned after this change) must configure MFA
    on first login

7.  Click "Save"

8.  Confirmation message: "Two-factor authentication settings updated"

> **Notification to Users:**

1.  HubSpot automatically emails all users: "Action Required: Set Up
    Two-Factor Authentication"

2.  Email includes: Setup instructions, deadline (7 days), support
    contact

3.  Johnny should send follow-up email to team:

> Subject: Action Required: Set Up MFA for HubSpot by [Date]
>
> Team,
>
> As part of our new HubSpot communications system, all users must
> enable
>
> Multi-Factor Authentication (MFA) by [7 days from today].
>
> Setup Steps:
>
> 1. Log into HubSpot
>
> 2. You'll see banner: "Set up two-factor authentication"
>
> 3. Click "Set up now"
>
> 4. Choose method: Authenticator app (recommended) or SMS
>
> 5. Follow prompts to complete setup
>
> 6. Save backup codes in secure location
>
> Recommended Apps:

-   Google Authenticator (iOS/Android)

-   Microsoft Authenticator (iOS/Android)

-   Authy (iOS/Android/Desktop)

> If you need help, reply to this email or call me at [Johnny's
> phone].
>
> After [deadline], you will be unable to log into HubSpot without MFA
> configured.
>
> Thanks,
>
> Johnny
>
> **Validation:**

1.  After 7-day grace period, verify all users have MFA enabled:

    -   Settings → Users & Teams

    -   Each user should show "Two-factor authentication: Enabled"

    -   If any user shows "Disabled": Follow up individually

> **Troubleshooting:**

-   User can't receive SMS codes: Guide to authenticator app instead

-   User lost backup codes: Admin can reset 2FA for user (Settings →
    Users & Teams → User → Reset two-factor authentication)

-   User locked out: Temporary disable enforcement, let user login,
    re-enable enforcement

#### 8.4.2.3 Step A1.3: Verify livingwithlolo.com Domain

> **Purpose:** Verify domain ownership for email tracking, branded
> links, and Gmail integration.
>
> **Prerequisites:** Johnny has DNS access to livingwithlolo.com domain
> (via Google Workspace Admin Console or domain registrar)
>
> **Configuration Steps:**

##### 8.4.2.3.1 Part 1: Initiate Domain Verification in HubSpot

1.  In Settings, navigate to: Marketing → Email → Manage sending domains

2.  Click "Connect a domain"

3.  Domain name: Enter "livingwithlolo.com"

4.  Click "Connect"

5.  HubSpot displays: "Verify your domain"

6.  Verification method options:

-   DNS TXT Record (recommended)

-   HTML file upload

7.  Select: "DNS TXT Record"

8.  HubSpot generates TXT record:

-   Record Type: TXT

-   Host: @ (or livingwithlolo.com)

-   Value: "hs-domain-verification=..." (long random string)

9.  Copy TXT record value (click Copy button)

10. Keep this browser tab open - will return after DNS configuration

##### 8.4.2.3.2 Part 2: Add TXT Record to DNS

> If using Google Workspace DNS:

1.  Open new browser tab: admin.google.com

2.  Navigate to: Domains → Manage domains → livingwithlolo.com → DNS

3.  Click "Add record"

4.  Record type: TXT

5.  Host/Name: @ (or leave blank)

6.  Value: Paste TXT record from HubSpot

7.  TTL: 3600 (default)

8.  Click "Add"

9.  Confirmation: "TXT record added successfully"

> If using external domain registrar (GoDaddy, Namecheap, etc.):

1.  Log into domain registrar account

2.  Navigate to DNS management for livingwithlolo.com

3.  Add TXT record (exact steps vary by registrar)

4.  Host: @ (or root domain)

5.  Value: Paste TXT record from HubSpot

6.  Save changes

##### 8.4.2.3.3 Part 3: Verify Domain in HubSpot

1.  Return to HubSpot browser tab

2.  Click "Verify" button

3.  HubSpot checks DNS for TXT record

4.  If successful: "Domain verified" message, green checkmark

5.  If failed: "We couldn't verify your domain"

-   Common issue: DNS propagation delay (up to 48 hours, usually 15-30
    minutes)

-   Resolution: Wait 30 minutes, click "Verify" again

-   If still failing after 2 hours: Review DNS record for typos

> Validation:

1.  Verify domain shows "Verified" status in HubSpot

2.  Green checkmark next to livingwithlolo.com

3.  Screenshot for documentation

> Why This Matters:

-   Required for Gmail OAuth integration (Section 8.4.3)

-   Enables email tracking and analytics

-   Provides branded tracking links in emails

-   Without verification, Gmail integration may fail

#### 8.4.2.4 Step A1.4: Configure Business Hours

> **Purpose:** Define standard business hours for auto-reply workflows
> (Monday-Friday 8 AM - 5 PM Arizona Time).
>
> CRITICAL TIMEZONE NOTE: Arizona does not observe Daylight Saving Time
> and remains at UTC-7 year-round. This is why we configured the account
> timezone to "America/Phoenix" in Step A1.1. Business hours will
> remain consistent throughout the year without manual adjustment.
>
> **Configuration Steps:**

1.  In Settings, navigate to: Inbox → Business Hours

2.  Current setting: Likely shows default 9 AM - 5 PM Monday-Friday

3.  Click "Edit" button

4.  Configure each day:

> **Monday through Friday:**

-   Status: Open (toggle ON)

-   Start time: 8:00 AM

-   End time: 5:00 PM

> **Saturday and Sunday:**

-   Status: Closed (toggle OFF)

5.  Timezone verification:

-   Business hours inherit account timezone (America/Phoenix from Step
    A1.1)

-   No separate timezone setting needed here

-   Displayed time should show "America/Phoenix (UTC-7)"

-   Critical: Because Arizona doesn't observe DST, these hours remain 8
    AM - 5 PM year-round without adjustment

6.  Click "Save"

7.  Confirmation: "Business hours updated"

> **Preview Expected Behavior:**

-   Monday 7:59 AM: Outside business hours → Auto-reply sends

-   Monday 8:00 AM: Inside business hours → No auto-reply (unless
    business-hours auto-reply approved by CEO per BRD 3.2.3.4)

-   Friday 4:59 PM: Inside business hours → No auto-reply

-   Friday 5:00 PM: Outside business hours → Auto-reply sends

-   Saturday 12:00 PM: Outside business hours (weekend) → Auto-reply
    sends

> **Validation:**

1.  Settings → Inbox → Business Hours displays correct hours

2.  Monday-Friday: 8:00 AM - 5:00 PM

3.  Saturday-Sunday: Closed

4.  Timezone shows America/Phoenix (UTC-7)

> **Application:**

-   Workflows 4 and 5 (Business Hours Auto-Reply) reference these hours
    (Section 8.4.8)

-   VIP@livingwithlolo.com: Auto-reply enabled outside business hours

-   welcome@livingwithlolo.com: NO auto-reply in  Phase 1 **(BRD
    Section 3.2.3.4 - maintains personal touch for sales)**

-   <family@livingwithlolo.com>: Auto-reply enabled outside business
    hours

-   <info@livingwithlolo.com>: Auto-reply enabled outside business hours

8.4.2.5 Step A1.5: Create Holiday Calendar

> **Purpose:** Configure company-observed holidays as exclusion dates
> for auto-reply workflows (BRD Section 7.3.2.7).
>
> **IMPORTANT:** HubSpot Professional tier does NOT have built-in
> holiday calendar feature. Holidays are configured as workflow
> exclusion dates within individual workflows (Section 8.4.8, Steps W4
> and W5).
>
> **Preparation - Document 2026 Holiday Dates:**
>
> Create reference document: "LWL Company Holidays 2026"
>
> LIVING WITH LOLO - COMPANY OBSERVED HOLIDAYS 2026
>
> The following dates are company-observed holidays. Auto-reply
> workflows
>
> will be configured to exclude these dates (no auto-replies sent).

| Holiday                        | Date                |
|--------------------------------|---------------------|
| New Year's Day                 | January 1, 2026     |
| Memorial Day                   | May 25, 2026        |
| Independence Day               | July 4, 2026        |
| Labor Day                      | September 7, 2026   |
| Thanksgiving Day               | November 26, 2026   |
| Day After Thanksgiving         | November 27, 2026   |
| Christmas Eve                  | December 24, 2026   |
| Christmas Day                  | December 25, 2026   |

> Total: 8 company holidays
>
> ANNUAL UPDATE REQUIREMENT:
>
> By November 15 each year, Johnny must update workflow exclusion dates
>
> with next calendar year's holiday dates. Set annual calendar
> reminder.
>
> CEO Approval: _____________ Date:
> _____________
>
> **CEO Review and Approval:**

1.  Share document with CEO

2.  CEO confirms holiday list matches company policy

3.  CEO signs off on list

4.  Store approved document in: /IT/HubSpot Implementation/Holiday
    Calendar/

> **Holiday Configuration Process:**

-   Holidays will be entered as exclusion dates in Workflows 4 and 5
    during Step **W4.4 and W5.4**

-   This is done at workflow level, NOT account level

-   Annual maintenance required: Update workflows each November with
    next year's dates

> **Calendar Reminder Setup:**

1.  Johnny creates calendar reminder: November 15, 2025 (recurring
    annually)

2.  Reminder title: "Update HubSpot Holiday Calendar for [Next
    Year]"

3.  Reminder details:

-   Action: Update Workflows 4 and 5 exclusion dates

-   Reference: This document, Section 8.4.8 Steps W4.**4** and W5.**4**

-   CEO approval required: New holiday list before updating workflows

> **Why This Matters:**

-   Company closed on holidays - no staff available to respond

-   Auto-replies set customer expectations correctly

-   Without holiday exclusions: Customers receive auto-reply promising
    "next business day" response on December 25, then wait until
    December 26

#### 8.4.2.6 Step A1.6: Configure Default Currency and Date Format

> **Purpose:** Set account-wide defaults for consistent data display.
>
> **Configuration Steps:**

1.  In Settings, navigate to: General → Account Defaults

2.  Locate "Currency" section

-   Default currency: USD - US Dollar ($)

-   If different: Click dropdown, select "USD - US Dollar ($)"

3.  Locate "Date format" section

-   Format: MM/DD/YYYY (US standard)

-   If different: Select "MM/DD/YYYY" from dropdown

4.  Locate "Number format" section

-   Format: 1,234.56 (comma thousands separator, period decimal)

5.  Locate "Default language" section

-   Language: English (United States)

6.  Click "Save"

7.  Confirmation: "Account defaults updated"

> **Validation:**

-   Currency displays as $ (dollar sign)

-   Dates display as 10/17/2025 (not 2025-10-17 or 17/10/2025)

-   Numbers display with commas: 1,000 (not 1.000 or 1000)

> **Configuration Step A1 Complete - Checkpoint**
>
> **Johnny's Self-Validation:**

-   [ ] Account timezone set to America/Phoenix (UTC-7) - verified

-   [ ] MFA enforcement enabled - all users notified

-   [ ] Domain livingwithlolo.com verified in HubSpot

-   [ ] Business hours configured: Mon-Fri 8 AM - 5 PM Arizona Time

-   [ ] Holiday calendar documented and approved by CEO

-   [ ] Calendar reminder set: November 15 (annual holiday update)

-   [ ] Currency (USD), date format (MM/DD/YYYY), language (English
    US) configured

-   [ ] All settings screenshots saved to /IT/HubSpot
    Implementation/Configuration Screenshots/

> **Expected Completion Time:** 30-45 minutes
>
> **Next Step:** Configuration Step A2 (Gmail Integration) - Section
> 8.4.3
>
> **Notification to Josh:**

-   No notification needed yet - Johnny continues with independent
    configuration

-   Josh will be notified after Configuration Group A complete (Steps
    A1-A4)

### 8.4.3 Gmail Integration Configuration

**Purpose:** Connect VIP@livingwithlolo.com and
welcome@livingwithlolo.com Gmail inboxes to HubSpot Conversations Inbox
via OAuth 2.0. This is Configuration Steps A4 from Section 8.2.3.

**Time Estimate:** 45-60 minutes (both inboxes)

> **Prerequisites:**

-   VIP@livingwithlolo.com mailbox created in Google Workspace

-   welcome@livingwithlolo.com mailbox created in Google Workspace

-   Domain livingwithlolo.com verified in HubSpot (Step A1.3 complete)

-   Johnny has Google Workspace Admin access

**Gmail Integration Overview**

**What This Integration Does:**

-   Syncs email messages from Gmail to HubSpot Conversations Inbox

-   Allows team to read and reply to emails within HubSpot

-   Associates emails with Deals and Contacts automatically

-   Creates unified inbox for email + SMS in single interface

**What This Integration Does NOT Do:**

-   Does NOT delete or move emails in Gmail (Gmail remains authoritative
    archive)

-   Does NOT send emails FROM Gmail (HubSpot sends via Gmail SMTP)

-   Does NOT require users to access Gmail directly (team uses HubSpot
    only)

**Integration Method:**

-   OAuth 2.0 connection (secure, no passwords stored in HubSpot)

-   Near real-time sync (HubSpot polls Gmail every 2-5 minutes)

-   Two-way technical sync (read from Gmail, send via Gmail SMTP)

-   One-way operational workflow (team uses HubSpot, not Gmail)

#### 8.4.3.1 Step A4.1: Prepare VIP@livingwithlolo.com Mailbox

> **Purpose:** Ensure Gmail mailbox properly configured before
> connecting to HubSpot.
>
> **Google Workspace Admin Tasks:**

1.  Log into Google Workspace Admin Console: admin.google.com

2.  Navigate to: Users → Manage users

3.  Search for: VIP@livingwithlolo.com

4.  If mailbox doesn't exist:

-   Click "Add new user"

-   First name: "Living With Lolo"

-   Last name: "Client Communications"

-   Primary email: VIP@livingwithlolo.com

-   Organizational unit: (Select appropriate OU)

-   Click "Add new user"

-   Set temporary password: (will change on first login)

-   Click "Done"

5.  If mailbox exists, verify settings:

-   Click on VIP@livingwithlolo.com user

-   Account status: Active (not suspended)

-   2-Step Verification: Enforced (or allow user to opt-in)

> **Gmail Settings Configuration:**

1.  Open new browser tab (incognito/private mode recommended)

2.  Navigate to: gmail.com

3.  Sign in as: VIP@livingwithlolo.com

-   Use temporary password if first login

-   Set permanent password when prompted

-   Complete 2FA setup if required

4.  Click Settings (gear icon) → See all settings

5.  Navigate to: Forwarding and POP/IMAP tab

6.  IMAP Access section:

-   Status: Enable IMAP (required for HubSpot sync)

-   If "Disable IMAP": Click "Enable IMAP"

7.  Auto-Forwarding section:

-   Status: Forwarding disabled (prevent unauthorized forwarding)

-   If forwarding configured: Disable it

8.  Vacation responder section:

-   Status: Vacation responder off

-   Rationale: HubSpot auto-reply workflows handle out-of-office
    messages

9.  Click "Save Changes" (bottom of page)

10. Confirmation: "Your settings have been saved"

> **Delegate Access (Optional - for transition period):**
>
> If team needs temporary direct Gmail access during implementation:

1.  Still in Gmail Settings → Accounts and Import tab

2.  "Grant access to your account" section

3.  Click "Add another account"

4.  Enter delegate email: lauren@livingwithlolo.com (CEO)

5.  Click "Next" → "Send email to grant access"

6.  CEO receives email, clicks "Accept", grants temporary access

7.  Important: After HubSpot go-live, REVOKE delegate access

-   Per BRD 4.1.2.2, team uses HubSpot only (not Gmail directly)

> **Validation:**

-   [ ] VIP@livingwithlolo.com mailbox exists and active

-   [ ] IMAP enabled

-   [ ] Auto-forwarding disabled

-   [ ] Vacation responder off

-   [ ] Delegate access configured (if needed) or skipped

#### 8.4.3.2 Step A4.2: Connect VIP@livingwithlolo.com to HubSpot (OAuth Process)

> **Purpose:** Establish OAuth 2.0 connection between Gmail and HubSpot
> for email sync.
>
> **Configuration Steps:**

1.  Return to HubSpot: app.hubspot.com

2.  Navigate to: Settings → Inbox → Connected accounts

3.  Click "Connect personal email"

4.  Provider options displayed: Gmail, Outlook, Office 365, etc.

5.  Click "Gmail"

6.  HubSpot displays: "Connect your Gmail account"

7.  Click "Connect Gmail account" button

> **OAuth Authentication Flow:**

8.  Browser redirects to Google Sign-In page

9.  Enter email: VIP@livingwithlolo.com

10. Click "Next"

11. Enter password: (VIP@ mailbox password)

12. Click "Next"

13. If 2FA enabled: Enter 2FA code from authenticator app or SMS

14. Click "Verify"

> **OAuth Permission Consent:**

15. Google displays: "HubSpot wants to access your Google Account"

16. Permissions requested by HubSpot:

-   Read, send, delete, and manage your email

-   View and manage your contacts

-   View calendars (optional - can deselect if not needed)

17. Review permissions carefully

-   "Read": HubSpot can read all emails in Gmail

-   "Send": HubSpot can send emails via Gmail SMTP

-   "Delete": HubSpot can delete emails (not used in this
    implementation)

-   "Manage": HubSpot can modify email labels, move messages

18. CRITICAL DECISION: If uncomfortable with "Delete" permission:

-   Unfortunately, Google OAuth bundles permissions

-   Cannot selectively grant read-only access

-   HubSpot integration requires full Gmail API access

-   Alternative: Don't use HubSpot integration (not feasible for this
    project)

-   Mitigation: HubSpot does not delete emails by default; Gmail Vault
    backup maintains compliance archive

19. Click "Allow" to grant permissions

20. Browser redirects back to HubSpot

> **HubSpot Integration Configuration:**

21. HubSpot displays: "Select an inbox to connect"

22. Inbox options:

-   Create new inbox (recommended)

-   Add to existing inbox

23. Create new inbox:

-   Click "Create new inbox"

-   Inbox name: "LWL Client Communications"

-   Rationale: Both VIP@ and welcome@ will connect to same inbox

-   Inbox visibility: "All users" (everyone can view all
    communications per BRD 3.10.2)

-   Click "Create"

24. HubSpot displays: "Configure sync settings"

> **Email Sync Configuration:**

25. Sync direction:

-   Two-way sync: Emails sync TO HubSpot (read from Gmail) AND sent FROM
    HubSpot (via Gmail SMTP)

-   Select: "Two-way sync" (default, recommended)

26. Sync frequency:

-   HubSpot polls Gmail every 2-5 minutes (automatic, cannot change)

27. Historical sync:

-   "Sync emails from the past [30] days"

-   Recommended: 30 days (imports recent email history for context)

-   Alternative: 7 days (if mailbox has high volume, reduces initial
    sync time)

-   Enter: 30

28. Email threading:

-   "Automatically thread conversations based on email headers"

-   Enabled by default (recommended - groups replies together)

-   Keep enabled

29. Email tracking:

-   "Track opens and clicks for emails sent from HubSpot"

-   Enabled by default

-   Keep enabled (provides analytics on email engagement)

30. Click "Save"

> **Connection Validation:**

31. HubSpot displays: "Your inbox is connected!"

32. Connection status: "Active" (green dot)

33. Email address: VIP@livingwithlolo.com

34. Inbox: "LWL Client Communications"

35. Last sync: "Just now" (or recent timestamp)

> **Initial Sync Progress:**

36. HubSpot begins importing last 30 days of emails

37. Progress indicator: "Syncing messages... [X] of [Y]"

38. Wait time: 5-15 minutes (depends on mailbox volume)

39. Do not close browser - let initial sync complete

40. Completion message: "Inbox sync complete - [X] messages
    imported"

> **Validation:**

41. Navigate to: Conversations → Inbox

42. Filter: "LWL Client Communications" inbox

43. Verify: Recent emails from VIP@livingwithlolo.com displayed

44. Click into sample email:

-   Email body displays correctly

-   Sender/recipient information correct

-   Timestamp accurate (Arizona Time)

45. Screenshot for documentation

> **Troubleshooting Failed Connection:**

-   "Domain not verified": Complete Step A1.3 (domain verification)
    first

-   "Connection failed": OAuth permissions denied - retry Step A4.2,
    click "Allow" on permissions

-   "Invalid credentials": VIP@ mailbox password incorrect - verify
    password in Gmail

-   "IMAP not enabled": Complete Step A4.1, enable IMAP in Gmail
    settings

-   "Sync stalled": Large mailbox (1000+ emails) - wait 30 minutes,
    check sync progress



#### 8.4.3.3 Step A4.3: Test VIP@ Email Sync

> **Purpose:** Verify emails flow correctly from Gmail to HubSpot and
> replies send via HubSpot.

##### 8.4.3.3.1 Test 1: Inbound Email Sync

1.  Open Gmail in separate browser tab (personal Gmail account or test
    > account)

2.  Compose new email:

-   To: VIP@livingwithlolo.com

-   Subject: "TEST - HubSpot Email Sync Validation"

-   Body: "This is a test email to verify Gmail-to-HubSpot sync is
    > working correctly. Please reply when you see this in HubSpot. -
    > Johnny"

3.  Send email

4.  Wait 5 minutes (HubSpot poll interval)

5.  In HubSpot: Navigate to Conversations → Inbox

6.  Filter: "LWL Client Communications" inbox

7.  Verify: Test email appears in inbox

8.  Expected status: "Open" conversation, unassigned (no Deal
    > association yet)

9.  If email doesn't appear after 10 minutes:

-   Verify email arrived in Gmail (check VIP@ mailbox directly)

-   Check HubSpot sync status: Settings → Inbox → Connected accounts →
    > VIP@ → "Last sync" timestamp

-   If last sync timestamp old (more than 10 minutes): Sync stalled -
    > disconnect and reconnect inbox

##### 8.4.3.3.2 Test 2: Outbound Email Reply

1.  In HubSpot Conversations Inbox, click into test email

2.  Click "Reply" button

3.  Compose reply:

-   Body: "Test reply from HubSpot Conversations Inbox. Verified sync
    > working correctly."

4.  Click "Send"

5.  HubSpot displays: "Message sent"

6.  Verify in personal Gmail account:

-   Wait 1-2 minutes

-   Check inbox for reply

-   Verify reply received FROM: VIP@livingwithlolo.com

-   Verify reply body correct

-   Verify threading: Reply appears in same conversation thread as
    > original email

7.  If reply doesn't arrive:

-   Check Sent folder in VIP@ Gmail mailbox directly

-   If email in Sent folder: Delivery successful, recipient email client
    > may be delaying

-   If NOT in Sent folder: HubSpot SMTP connection issue - review Step
    > A4.2 sync configuration

##### 8.4.3.3.3 Test 3: Email Threading

1.  In personal Gmail, reply to the HubSpot reply

2.  Subject: Same subject line (maintains thread)

3.  Body: "Test threading - reply #2"

4.  Send

5.  Wait 5 minutes

6.  In HubSpot Conversations Inbox:

-   Original conversation should update

-   New reply appears in same conversation thread (not separate
    > conversation)

-   Conversation status may change to "Open" if was previously closed

7.  If new email creates separate conversation instead of threading:

-   Email threading broken

-   Verify email headers include "References" and "In-Reply-To"
    > fields

-   May be email client issue (some clients don't preserve headers)

-   Document as known limitation

> **Test Cleanup:**

-   In HubSpot, close test conversation (mark as resolved)

-   Delete test emails from VIP@ mailbox if desired

-   Tests successful: Proceed to Step A4.4

#### 8.4.3.4 Step A4.4: Prepare welcome@livingwithlolo.com Mailbox

> **Purpose:** Configure second Gmail mailbox for pre-sales
> communications.
>
> **Process:** Repeat Step A4.1 (Gmail mailbox preparation) for
> welcome@livingwithlolo.com
>
> **Key Differences:**

-   User name: "Living With Lolo - Sales Inquiries" (different display
    name)

-   Primary email: welcome@livingwithlolo.com

-   All other settings identical to VIP@ mailbox

> **Abbreviated Steps:**

1.  Google Workspace Admin Console → Add user or verify existing user

2.  Primary email: welcome@livingwithlolo.com

3.  Login to Gmail as welcome@

4.  Settings → Forwarding and POP/IMAP → Enable IMAP

5.  Disable auto-forwarding

6.  Vacation responder off

7.  Save settings

8.  Delegate access (optional): Grant to Molly (Primary POC for
    welcome@)

> **Validation:**

-   [ ] welcome@livingwithlolo.com mailbox active

-   [ ] IMAP enabled

-   [ ] Auto-forwarding disabled

-   [ ] Vacation responder off

#### 8.4.3.5 Step A4.5: Connect welcome@livingwithlolo.com to HubSpot

> **Purpose:** Add second Gmail inbox to same HubSpot workspace.
>
> **Configuration Steps:**
>
> Important Decision: Same Inbox or Separate Inbox?

-   Option A: Connect to existing "LWL Client Communications" inbox

-   Both VIP@ and welcome@ emails appear in same inbox view

-   Filtering required to distinguish pre-sales vs. paid project
    communications

-   Simpler configuration, fewer inbox views to manage

-   Recommended unless strong business reason for separation

    -   Option B: Create separate "welcome@ Inbox" for pre-sales

-   Separate inbox view for pre-sales inquiries

-   Easier filtering (VIP@ inbox = paid projects, welcome@ inbox =
    leads)

-   More inbox views to manage, team needs to monitor both

-   Alternative if CEO prefers complete separation

> **For this guide, assume Option A (same inbox) - adjust if Option B
> preferred**

1.  In HubSpot: Settings → Inbox → Connected accounts

2.  Click "Connect personal email"

3.  Select "Gmail"

4.  Click "Connect Gmail account"

5.  OAuth flow (repeat process from Step A4.2):

-   Sign in as: welcome@livingwithlolo.com

-   Enter password

-   2FA if required

-   Review permissions: "Read, send, delete, manage email"

-   Click "Allow"

6.  HubSpot: "Select an inbox to connect"

7.  Select existing inbox:

-   Choose: "LWL Client Communications" (existing inbox from VIP@
    > connection)

-   Rationale: Unified inbox for all client communications (pre-sales
    > and paid projects)

8.  Sync settings:

-   Two-way sync: Enabled

-   Historical sync: Last 30 days

-   Email threading: Enabled

-   Email tracking: Enabled

9.  Click "Save"

10. Connection successful: "welcome@livingwithlolo.com connected to LWL
    > Client Communications"

> **Alternative (Option B - Separate Inbox):**
>
> If creating separate inbox for welcome@:

-   Step 7: Click "Create new inbox"

-   Inbox name: "welcome@ - Pre-Sales Inquiries"

-   Inbox visibility: "All users"

-   Click "Create"

-   Proceed with Steps 8-10

> **Validation:**

11. Settings → Inbox → Connected accounts

12. Verify TWO email connections listed:

-   VIP@livingwithlolo.com → LWL Client Communications

-   welcome@livingwithlolo.com → LWL Client Communications (or separate
    > inbox if Option B)

13. Both connections show "Active" status

14. Screenshot for documentation

#### 8.4.3.6 Step A4.6: Test welcome@ Email Sync

> **Purpose:** Verify second Gmail inbox syncs correctly to HubSpot.
>
> **Test Process:** Repeat Step A4.3 (email sync test) for
> welcome@livingwithlolo.com
>
> **Abbreviated Test Steps:**

1.  Send test email TO: welcome@livingwithlolo.com FROM: personal email

2.  Subject: "TEST - welcome@ Inbox Sync"

3.  Wait 5 minutes

4.  Verify email appears in HubSpot: Conversations → Inbox → "LWL
    Client Communications"

5.  Filter inbox by email address if needed (if Option A - same inbox)

6.  Reply from HubSpot

7.  Verify reply received in personal email FROM:
    welcome@livingwithlolo.com

8.  Test threading: Reply to reply, verify threads correctly in HubSpot

9.  Close test conversation

10. Tests successful: Proceed to Step A4.7

#### 8.4.3.7 Step A4.7: Configure Email Signatures

> **Purpose:** Create shared email signatures for VIP@ and welcome@
> inboxes with POC personalization.
>
> **Configuration Steps:**
>
> **Signature for VIP@livingwithlolo.com:**

1.  In HubSpot: Settings → Inbox → Email signatures

2.  Click "Create signature"

3.  Signature name: "VIP@ Inbox - Paid Projects"

4.  Signature content (use rich text editor):

> ---
>
> {{owner.firstName}} {{owner.lastName}}
>
> {{owner.role}}
>
> Living With Lolo
>
> Phone: (480) XXX-XXXX [Insert LWL office phone]
>
> Email: VIP@livingwithlolo.com
>
> Web: www.livingwithlolo.com
>
> Luxury Residential Design & Construction | Scottsdale, Arizona

5.  Personalization tokens explanation:

-   {{owner.firstName}} {{owner.lastName}}: Automatically inserts name
    > of POC sending email

-   {{owner.role}}: Inserts job title (e.g., "Lead Designer",
    > "Director of Construction")

-   Format: "First Name | Title" above locked company signature block
    > per BRD 3.2.1.3

-   Rationale: Same signature template used by all POCs, but
    > personalizes automatically per sender

6.  Default signature assignment:

-   "Use this signature for": Select "VIP@livingwithlolo.com inbox"

-   All emails sent from VIP@ inbox automatically include this signature

7.  Click "Save"

> **Signature for welcome@livingwithlolo.com:**

1.  Click "Create signature"

2.  Signature name: "welcome@ Inbox - Pre-Sales"

3.  Signature content:

> ---
>
> {{owner.firstName}} {{owner.lastName}}
>
> {{owner.role}}
>
> Living With Lolo
>
> Phone: (480) XXX-XXXX
>
> Email: welcome@livingwithlolo.com
>
> Web: www.livingwithlolo.com
>
> Let's bring your vision to life. Schedule a consultation: [Insert
> scheduling link]
>
> **Signature for** <family@livingwithlolo.com>**:**

1.  Click "Create signature"

2.  Signature name: "family@ Inbox - Post-Project Care"

3.  Signature content:

> {{owner.firstName}} {{owner.lastName}} | {{owner.role}}
>
> ---
>
> [Locked Company Signature Block]
>
> Living With Lolo
>
> Phone: (480) XXX-XXXX
>
> Email: <family@livingwithlolo.com>
>
> Web: www.livingwithlolo.com
>
> Thank you for being part of the Living With Lolo family.

4.  Default signature assignment: "<family@livingwithlolo.com> inbox"

5.  Click "Save"

> **Signature for** <info@livingwithlolo.com>**:**

1.  Click "Create signature"

2.  Signature name: "info@ Inbox - General Inquiries"

3.  Signature content:

> {{owner.firstName}} {{owner.lastName}} | {{owner.role}}
>
> ---
>
> [Locked Company Signature Block]
>
> Living With Lolo
>
> Phone: (480) XXX-XXXX
>
> Email: <info@livingwithlolo.com>
>
> Web: www.livingwithlolo.com
>
> Luxury Residential Design & Construction | Scottsdale, Arizona

4.  Default signature assignment: "welcome@livingwithlolo.com inbox"

5.  Click "Save"

> **Validation:**

6.  Compose test email in HubSpot Conversations:

-   From: VIP@livingwithlolo.com

-   Verify signature automatically appended

-   Verify personalization tokens replaced with actual POC name/role

7.  Repeat test for welcome@livingwithlolo.com

8.  If signature doesn't appear:

-   Verify signature assigned to correct inbox

-   Check user has "owner" role on conversation (assigned POC)

-   Verify format: "First Name | Title" above locked company block

> **SMS Signature Note (BRD 3.2.2.3):**
>
> SMS messages use simplified signature format: {{owner.firstName}} |
> {{owner.role}} ONLY
>
> Company signature block is NOT included in SMS to maintain message
> brevity and readability (160 character limit per SMS).
>
> SMS signature will be configured in Section 8.4.4 (HubSpot SMS Setup).
>
> Signature Enforcement:
>
> Per BRD 3.2.1.3, the company signature block is locked and
> administered by Johnny (or designated Administrator). Individual
> employees can only add their "First Name | Title" personalization
> above the locked signature. Team members cannot modify the company
> signature block.
>
> Implementation in HubSpot:

-   Signature templates maintained at organization level

-   Administrators can edit signature templates

-   Standard Users cannot modify locked signature block

-   Quarterly communications audits validate signature enforcement
