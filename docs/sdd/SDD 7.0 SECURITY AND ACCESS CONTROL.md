---
source: SDD - System Design Document - Consolidated Communication PART ONE v1.docx
section: 7.0 SECURITY AND ACCESS CONTROL (Part 1 - Sections 7.1-7.3)
integrity: full
format: preservation_mode
encoding: utf-8
extraction_method: paragraph_and_table_parser
order_preserved: true
tables_preserved: true
revision: 1.1
strict_lossless_mode: true
---

## 7.0 SECURITY AND ACCESS CONTROL

## 7.1 Authentication and Authorization

### 7.1.1 Multi-Factor Authentication (MFA) Requirements

Per BRD Section 4.4.3, MFA is REQUIRED for all HubSpot and Google Workspace accounts.

Google Workspace MFA:

-   Configuration: Google Workspace Admin Console \> Security \> 2-Step Verification

-   Enforcement: Enable "Allow users to turn on 2-Step Verification" → Set to "Enforcement ON"

-   Grace Period: 7-day enforcement period for existing users to configure MFA

-   Methods Allowed: Authenticator app (Google Authenticator, Authy), SMS backup codes

-   Responsibility: Google Workspace Admin (LWL IT Lead or designated admin)

HubSpot MFA:

-   Configuration: HubSpot Settings \> Security \> Account Security

-   Enforcement: Enable "Require two-factor authentication for all users"

-   Methods Allowed: Authenticator app, SMS (not recommended for security), backup codes

-   Setup Process: Users configure MFA on first login after enforcement enabled

-   Responsibility: LWL IT Lead (HubSpot Administrator)

User Training:

-   Phase 5 training includes MFA setup workshop

-   Provide step-by-step guides for installing authenticator apps

-   Emphasize backup codes storage (secure location, not on same device)

### 7.1.2 Google Workspace SSO Integration (Recommended)

Purpose: Simplify user authentication by allowing HubSpot login via Google Workspace credentials

Benefits:

-   Single sign-on experience (users click "Sign in with Google")

-   Centralized user management (disable Google account = disable HubSpot access automatically)

-   Leverages Google Workspace MFA for HubSpot authentication

Configuration Process:

1.  HubSpot Settings \> Integrations \> Google Workspace

2.  Enable "Allow users to sign in with Google"

3.  Domain verification (already completed in Section 3.2.2)

4.  Test SSO login with one user before rolling out to all

Decision Point: Discuss SSO adoption with CEO during Phase 1 Discovery; strongly recommended for security and user experience.

## 7.2 Role-Based Access Control (RBAC)

### 7.2.1 HubSpot Permission Model

Implemented via HubSpot Roles (Section 3.8 configuration):

| **Role** | **Assigned Users** | **Key Permissions** | **Restrictions** |
| --- | --- | --- | --- |
| Super Admin | CEO, LWL IT Lead, Josh (TBD) | Full account access, user management, workflow config, integration settings | None |
| Sales Professional | All other team members | View/reply to all conversations, create notes, reassign conversations, update Deal/Contact records | Cannot edit workflows, manage users, or change account settings |

Critical Design Principle (BRD 3.10.2):

-   ALL users (both Admins and Standard Users) have full visibility into ALL client communications across ALL projects

-   No data segmentation by owner, team, or project

-   Transparency is a core business value; technology enforces this

### 7.2.2 Conversations Inbox Access Control

All Users Can:

-   View all Open and Closed conversations (no restrictions)

-   Filter conversations by project, POC, phase, or status

-   Read internal notes and \@mentions

-   Reply to any conversation (though typically only assigned POC replies)

-   Manually reassign any conversation to another team member

-   Update conversation status (Open → Closed or vice versa)

Only Administrators Can:

-   Access "Unassigned Conversations" view (default view for admins)

-   Review and associate unmatched communications with projects

-   Configure inbox settings (channels, routing rules, business hours)

-   Manage user access and permissions

### 7.2.3 Deal and Contact Access Control

All Users Can:

-   View all Deal records (projects)

-   View all Contact records (clients)

-   Edit Deal properties (Project Master Info, custom fields)

-   Edit Contact properties

-   Add notes to Deal timeline

-   Associate Conversations with Deals/Contacts

Only Administrators Can:

-   Delete Deal or Contact records (restricted to prevent accidental data loss)

-   Bulk edit Deal/Contact properties

-   Import/export data

-   Configure custom properties and pipelines

## 7.3 Data Security Controls

### 7.3.1 Encryption Standards

Data in Transit:

-   All communications encrypted with TLS 1.2 or higher (BRD 8.1)

-   Gmail ↔ HubSpot: HTTPS with OAuth 2.0, TLS 1.2+

-   Airtable ↔ Zapier: HTTPS with API key authentication, TLS 1.2+

-   Zapier ↔ HubSpot: HTTPS with HubSpot Private App API key, TLS 1.2+

-   Client ↔ Systems: TLS 1.2+ for all email and SMS

Data at Rest:

-   HubSpot: AES-256 encryption (vendor-managed)

-   Gmail: AES-128 encryption (Google Workspace standard)

-   Airtable: AES-256 encryption (vendor-managed)

-   Zapier: AES-256 encryption for stored credentials (vendor-managed)

### 7.3.2 API Key and Credential Management

Credential Storage:

-   All API keys stored in platform-native secure vaults (Zapier secure vault, HubSpot credential manager)

-   Never store API keys in plain text, code repositories, or shared documents

-   Credentials encrypted at rest by platform vendors

API Key Rotation Schedule:

| **Credential** | **Rotation Frequency** | **Responsibility** |
| --- | --- | --- |
| HubSpot Private App API Key | Annually | LWL IT Lead |
| Airtable Personal Access Token | Annually | Josh (Airtable Admin) |
| Google OAuth Token | Automatic (no manual rotation required) | N/A |

Key Compromise Procedure:

1.  Immediately revoke compromised credential in source platform

2.  Generate new credential

3.  Update all integrations using old credential (Zapier workflows, etc.)

4.  Test all affected workflows end-to-end

5.  Document incident and root cause for future prevention

### 7.3.3 User Access Provisioning and Deprovisioning

New User Onboarding:

1.  Request: Hiring manager submits new user request to LWL IT Lead

2.  Approval: CEO approves HubSpot seat assignment and role

3.  Provisioning: (Steps completed by LWL IT Lead)

    -   Create user in HubSpot (Settings \> Users & Teams)

    -   Assign appropriate role (Administrator or Sales Professional)

    -   Configure email connection if user will send emails (typically NO - only VIP@ sends)

    -   Enable MFA enforcement

    -   Provide login credentials and initial setup instructions

4.  Training: Schedule user for Phase 5 training session

5.  Validation: New user successfully logs in and completes MFA setup within 48 hours

User Offboarding (Per BRD 4.4.7):

Requirement: Access must be revocable within ONE BUSINESS DAY of departure.

Offboarding Procedure:

1.  Notification: HR or manager notifies LWL IT Lead of employee departure (same day)

2.  Immediate Actions (Within 1 Hour):

    -   Deactivate HubSpot account (Settings \> Users & Teams \> Deactivate User)

    -   Deactivate Google Workspace account if applicable

    -   Revoke any API keys or personal access tokens issued to user

3.  Conversation Reassignment:

    -   Review user's Open conversations in HubSpot Inbox

    -   Reassign all Open conversations to appropriate backup POC or manager

    -   Document reassignments in internal note

4.  Data Preservation:

    -   User's conversation history, notes, and activities remain in HubSpot (company property per BRD 4.4.6)

    -   Export user's activity log if needed for transition documentation

5.  License Management:

    -   HubSpot seat becomes available for reassignment after deactivation

    -   Update user count in Airtable Users table (mark as Inactive)

Offboarding Checklist Template: (Maintained by LWL IT Lead)

☐ HubSpot account deactivated

☐ Google Workspace account deactivated (if applicable)

☐ API keys/tokens revoked (if any issued)

☐ Open conversations reassigned

☐ Activity log exported (if needed)

☐ Airtable Users table updated (Active = No)

☐ Exit interview conducted (HR)

☐ Equipment returned (IT inventory)
---
source: SDD - System Design Document - Consolidated Communication PART ONE v1.docx
section: 7.0 SECURITY AND ACCESS CONTROL (Part 2 - Sections 7.4-7.5)
integrity: full
format: preservation_mode
encoding: utf-8
extraction_method: paragraph_and_table_parser
order_preserved: true
tables_preserved: true
revision: 1.1
strict_lossless_mode: true
---

## 7.4 Audit Logging and Compliance

### 7.4.1 HubSpot Audit Log Configuration

Enabled by Default: HubSpot Professional tier includes comprehensive audit logging

Logged Activities:

-   User login/logout events

-   Conversation view, reply, reassignment actions

-   Deal/Contact create, edit, delete actions

-   Workflow create, edit, activation/deactivation

-   User permission changes

-   Integration configuration changes

Audit Log Access:

-   HubSpot Settings \> Account \> Audit Log

-   Filterable by: User, Action Type, Object Type, Date Range

-   Retention: Per HubSpot subscription terms (minimum 3 years per BRD 4.7.3)

Review Cadence:

-   LWL IT Lead reviews audit log monthly for anomalous activity

-   Focus areas: Unexpected user actions, bulk data changes, integration errors

### 7.4.2 Google Workspace Audit Logging

Gmail Audit Log:

-   Tracks email sent/received, forwarding rules, delegation changes

-   Access: Google Workspace Admin Console \> Reports \> Audit \> Gmail

-   Retention: 6 months in Admin Console (export for longer retention if needed)

Admin Audit Log:

-   Tracks admin actions: User creation, settings changes, OAuth grants

-   Access: Google Workspace Admin Console \> Reports \> Audit \> Admin

-   Retention: 6 months in Admin Console

Export Procedure (For Long-Term Retention):

-   Monthly export of Gmail and Admin audit logs to CSV

-   Store in LWL secure archive (Google Drive folder with restricted access)

-   Naming convention: Gmail-Audit-YYYY-MM.csv

### 7.4.3 Compliance Documentation

CAN-SPAM Compliance (Email):

-   All outbound marketing/promotional emails include:

    -   Physical mailing address (LWL office address)

    -   Clear unsubscribe mechanism

    -   "This is a commercial message" disclosure (if applicable)

-   HubSpot automatically includes unsubscribe links in marketing emails

-   Transactional/1:1 client communication (Conversations Inbox) exempt from CAN-SPAM

TCPA Compliance (SMS):

-   SMS opt-out mechanism configured (Section 3.5.3)

-   Automatic suppression of unsubscribed contacts

-   Opt-in confirmation for first-time SMS contacts (Section 3.5.3)

-   Records of opt-in/opt-out maintained in HubSpot Contact properties

Data Privacy (General):

-   All client data classified as company property (BRD 4.4.6)

-   Data residency: US-based data centers (HubSpot, Google, Airtable, Zapier)

-   Client data not sold or shared with third parties (except integrated platforms for operational purposes)

-   Data retention aligns with LWL business needs (minimum 3 years per BRD 4.7.3)

## 7.5 Security Incident Response

### 7.5.1 Incident Classification

| **Severity** | **Definition** | **Examples** | **Response Time** |
| --- | --- | --- | --- |
| Critical | Data breach, unauthorized access, system compromise | API keys exposed publicly, unauthorized user accessing client data, malware infection | Immediate (within 1 hour) |
| High | Service disruption, potential security vulnerability | Extended platform outage, suspected account compromise, phishing attempt | Within 4 hours |
| Medium | Minor security concern, no immediate risk | Failed login attempts, suspicious activity requiring investigation | Within 24 hours |
| Low | Security hygiene, routine updates | MFA not configured for new user, outdated access permissions | Within 1 week |

### 7.5.2 Incident Response Procedure

Step 1: Detection and Reporting

-   Any team member identifying security concern reports to LWL IT Lead immediately

-   Automatic alerts (OAuth failures, unusual login locations, API errors) sent to LWL IT Lead email

Step 2: Containment (Critical/High Incidents)

-   Revoke compromised credentials immediately

-   Deactivate affected user accounts if account compromise suspected

-   Disable affected integrations if platform compromise suspected

-   Preserve audit logs and evidence for investigation

Step 3: Investigation

-   Review audit logs (HubSpot, Google Workspace, Zapier) for scope of incident

-   Identify affected data, users, or systems

-   Determine root cause and attack vector

Step 4: Remediation

-   Implement fixes to prevent recurrence (password reset, MFA enforcement, credential rotation)

-   Restore service from backup if data loss occurred

-   Update security controls or access policies as needed

Step 5: Communication

-   Internal: Notify CEO and affected users of incident and resolution

-   External: If client data compromised, legal counsel determines notification requirements (state breach notification laws)

-   Vendors: Contact HubSpot/Google/Airtable Support if platform vulnerability identified

Step 6: Post-Incident Review

-   Document incident timeline, root cause, and remediation steps

-   Update security procedures to prevent similar incidents

-   Conduct team training if human error contributed to incident