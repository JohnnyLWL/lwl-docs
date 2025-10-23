---
source: SDD - System Design Document - Consolidated Communication PART ONE v1.docx
section: 2.0 SYSTEM ARCHITECTURE
integrity: full
format: preservation_mode
encoding: utf-8
extraction_method: paragraph_and_table_parser
order_preserved: true
tables_preserved: true
revision: 1.1
strict_lossless_mode: true
---

## 2.0 SYSTEM ARCHITECTURE

## 2.1 Architecture Overview

The Consolidated Client Communications Hub uses a distributed architecture with three primary platforms, each serving as the authoritative source for its respective domain.

High-level architecture flow:

-   Clients communicate via Email (Gmail) and SMS (HubSpot SMS Add-On)

-   Gmail syncs to HubSpot via OAuth connection

-   HubSpot Conversations Inbox serves as operational interface for team

-   Airtable stores authoritative project metadata

-   Zapier middleware synchronizes Airtable project data to HubSpot via event-driven webhooks

## 2.2 System Components

| **Component** | **Function** | **Authority** | **Owner** |
| --- | --- | --- | --- |
| Gmail (Google Workspace) | Email message transport and permanent archive | Email content storage and compliance backup | Google Workspace Admin |
| HubSpot Sales Hub Professional | Operational interface for email/SMS management, conversation routing, POC assignments, internal notes | Conversation ownership, status, and operational context | LWL IT Lead |
| HubSpot Marketing Hub Professional + SMS Add-On | Business phone number SMS messaging | SMS message display and threading | LWL IT Lead |
| Airtable | Authoritative project database containing Project IDs, client contact information, POC assignments, project phase status | Project metadata and routing rules | Airtable Administrator (Josh) |
| Zapier | Middleware for event-driven synchronization between Airtable and HubSpot | Integration workflow orchestration | Airtable Administrator (Josh) with LWL IT Lead collaboration |
| Google Chat | Internal team collaboration (separate from client communications) | Internal coordination only | All LWL Staff |
| Salesmsg | Urgent communications hotline for time-sensitive client emergencies | SMS message display and emergency routing | Lauren, Brandie, Robin (shared admin) |
| Slack | Internal team alerting and communication visibility | Real-time notifications and daily inbox summaries | All LWL Staff |

## 2.3 Data Ownership Model

The system implements distributed data ownership to prevent synchronization conflicts:

### 2.3.1 Gmail: Email Message Content Authority

-   Authoritative For: Raw SMTP email messages, complete message headers, email attachments

-   Retention: Indefinite (Gmail Vault for compliance)

-   Backup Role: Disaster recovery source if HubSpot data loss occurs

-   Data Flow: Gmail to HubSpot (one-way, read-only from HubSpot perspective)

### 2.3.2 HubSpot: Operational Context Authority

Authoritative For:

-   Conversation ownership (which POC owns each conversation)

-   Conversation status (Open, Closed)

-   Internal collaboration (notes, \@mentions, conversation threads)

-   SMS message content and threading

-   Client Contact records (may include multiple Contacts per project for field limit management)

-   Deal records representing projects (operational view of project status)

-   Email signature templates and enforcement rules

-   Vacation flag status for all team members (Out of Office property)

Retention: Per HubSpot subscription terms (minimum 3 years per BRD 4.7.3)

Data Flow: HubSpot does NOT write back to Gmail or Airtable

### 2.3.3 Airtable: Project Metadata Authority

Authoritative For:

-   Project IDs (unique identifiers)

-   Master client contact database

-   Primary POC and Backup POC assignments

-   Project phase status

-   Phase-to-POC mapping rules

Retention: Indefinite (LWL operational database)

Data Flow: Airtable to HubSpot via Zapier webhooks (one-way, event-driven)

## 2.4 Integration Patterns

### 2.4.1 Event-Driven Synchronization (Airtable to HubSpot)

Trigger Events:

1.  New Paid Project: Airtable project status changes to "Paid"

2.  Phase Change: Airtable project Phase field changes

Process Flow: Airtable Field Change → Airtable Automation → Webhook POST → Zapier Catch Hook → Zapier Actions → HubSpot API Update → HubSpot Deal Record Updated → Future Messages Route to New POC

Frequency: Real-time (webhook fires immediately upon field change)

### 2.4.2 Weekly Baseline Synchronization (Airtable to HubSpot)

Purpose: Safety net to catch manual updates or missed webhook triggers

Schedule: Every Sunday at 6:00 AM Arizona Time (UTC-7)

Process Flow: Zapier Schedule Trigger → Fetch All Paid Projects from Airtable → Compare with HubSpot Deals → Update/Create as Needed → Log Sync Report

Frequency: Weekly (168-hour interval)

### 2.4.3 Gmail-HubSpot Email Synchronization

Method: HubSpot native Gmail integration via OAuth 2.0

Process Flow: Email arrives in Gmail → HubSpot OAuth connection polls Gmail → HubSpot imports email → Associates with Contact/Deal → Creates/Updates Conversation → Routes to Primary POC

Frequency: Near real-time (HubSpot polls Gmail every 2-5 minutes)

### 2.4.4 HubSpot SMS Message Flow

Method: HubSpot SMS Access Add-On (native feature, no external integration)

Process Flow: Client sends SMS to LWL business number → HubSpot receives via SMS provider → Associates with Contact/Deal → Creates/Updates Conversation → Routes to Primary POC

Frequency: Real-time (immediate delivery)

### 2.4.5 Salesmsg SMS Flow

Method: Salesmsg native platform (standalone, no HubSpot integration in Phase 1)

Process Flow: Client sends urgent SMS to Salesmsg 10DLC number → Salesmsg receives message → Emergency response team (Lauren, Brandie, Robin) receive mobile notifications → n8n/Zapier posts alert to Slack #urgent-alerts → Team member responds via Salesmsg mobile app or web interface

Frequency: Real-time (immediate delivery and notification)

### 2.4.6 Slack Integration Flow

Method: Webhook POST from n8n or Zapier to Slack Incoming Webhooks

Process Flow:

-   Urgent Alerts: Salesmsg inbound message triggers webhook → n8n/Zapier workflow → POST to Slack #urgent-alerts channel

-   Daily Inbox Summary: Zapier scheduled workflow (daily 8:00 AM Arizona Time) → Query HubSpot Conversations API → Format summary message → POST to Slack #client-inboxes channel

Frequency:

-   Urgent alerts: Real-time (immediate)

-   Daily summaries: Once daily at 8:00 AM Arizona Time

## 2.5 Network and Security Architecture

### 2.5.1 Communication Protocols

-   Gmail ↔ HubSpot: HTTPS with OAuth 2.0 authentication, TLS 1.2+ encryption

-   Airtable ↔ Zapier: HTTPS webhook POST with API key authentication

-   Zapier ↔ HubSpot: HTTPS REST API with HubSpot API key authentication

-   Client ↔ Systems: TLS 1.2+ encryption for all email and SMS

**2.5.2 Authentication Methods**

| **Connection** | **Method** | **Credential Storage** |
| --- | --- | --- |
| HubSpot User Login | Username/Password + MFA | Google Workspace SSO (recommended) |
| Gmail → HubSpot | OAuth 2.0 | HubSpot secure credential vault |
| Airtable → Zapier | Webhook URL + API Key | Zapier secure vault |
| Zapier → HubSpot | HubSpot Private App API Key | Zapier secure vault |

**2.5.3 Data Security Controls**

-   Multi-factor authentication (MFA) required for all HubSpot and Google Workspace accounts (BRD 4.4.3)

-   Role-based access control (RBAC) for HubSpot users (BRD Section 3.10)

-   Audit logging enabled for all user actions (BRD 4.4.8)

-   TLS 1.2+ encryption for all data in transit (BRD 8.1)

-   Data residency: All systems hosted in US data centers (HubSpot, Google, Airtable, Zapier)

## 2.6 Scalability and Performance

| **Metric** | **Current Requirement** | **Design Capacity** | **Monitoring Method** |
| --- | --- | --- | --- |
| Concurrent Projects | 50 projects (BRD 3.9.3) | 200+ projects | HubSpot Deal count report |
| Active Users | 8-9 users (BRD 3.10.8) | 10 Sales Hub seats | HubSpot user license dashboard |
| Message Volume | Low-volume, high-touch (BRD 4.2.3) | Approximately 200-300 messages/month | HubSpot Conversations report |
| Routing Latency | Less than 30 seconds (BRD 4.2.2) | Less than 10 seconds typical | Manual spot-check during UAT |
| Zapier Task Usage | Approximately 200-300 tasks/month | 750 tasks/month (Starter tier) | Zapier task usage dashboard |
| System Uptime | 99.5% during business hours (BRD 4.8) | 99.9% (vendor SLA) | HubSpot/Google status pages |

## 2.7 Disaster Recovery and Business Continuity

### 2.7.1 Data Backup Strategy

-   Gmail: Google Vault retention (indefinite, managed by Google Workspace Admin)

-   HubSpot: Monthly export of all Deals, Contacts, Conversations to CSV (manual task for LWL IT Lead)

-   Airtable: Daily automatic backups (Airtable native feature, managed by Josh)

-   Zapier: Workflow configuration exported quarterly to JSON (manual task for Josh)

### 2.7.2 Synchronization Failure Response

Per BRD Section 4.1.4.2, if synchronization fails:

1.  Detection: Zapier error notification emails to LWL IT Lead + Josh

2.  Validation: Check source system (Airtable) data integrity

3.  Recovery: Re-trigger failed workflow manually or wait for Sunday baseline sync

4.  Escalation: If failures persist beyond 24 hours, implement temporary manual operations:

    -   Team operates directly from Gmail (read-only)

    -   Maintain manual activity log in shared Google Doc

    -   Resume HubSpot operations once sync restored

### 2.7.3 System Failure Scenarios

| **Failure Type** | **Impact** | **Mitigation** | **Recovery Time** |
| --- | --- | --- | --- |
| HubSpot Outage | Cannot route new messages | Temporary Gmail direct access + manual log | Less than 4 hours (vendor SLA) |
| Gmail Outage | Cannot send/receive email | SMS remains operational; email queued by Google | Less than 1 hour (vendor SLA) |
| Airtable Outage | Cannot sync POC assignments | Use last-known POC assignments in HubSpot | Less than 2 hours (vendor SLA) |
| Zapier Outage | No real-time sync | Sunday baseline sync will reconcile | Less than 4 hours (vendor SLA) |
| Internet Outage (LWL Office) | Cannot access cloud systems | Mobile app access via cellular; critical only | Dependent on ISP |