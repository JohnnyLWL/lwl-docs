---
source: SDD - System Design Document - Consolidated Communication PART ONE v1.docx
section: 1.0 INTRODUCTION
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

PART ONE

Document Control

-   Author: Johnny (LWL IT Lead)

-   Date: October 17, 2025

-   Status: Draft for Phase 1 Implementation

-   Related Documents: BRD Consolidated Communications v4 FINAL

## 1.0 INTRODUCTION

## 1.1 Document Purpose

This System Design Document (SDD) provides the complete technical specification for implementing the Living With Lolo Consolidated Client Communications Hub as defined in BRD v4. This document serves as the definitive implementation guide for all technical configuration, integration development, and system setup activities.

This SDD translates business requirements into actionable technical specifications that can be executed by:

-   LWL IT Lead (HubSpot configuration, Gmail integration, user training)

-   Airtable Administrator/Integration Architect (Josh - Airtable schema, webhook automations, Zapier workflows)

-   Living With Lolo Operations Team (business process adoption, testing, data validation)

## 1.2 Document Scope

This SDD covers Phase 1 implementation only, specifically:

IN SCOPE:

-   HubSpot Sales Hub Professional configuration (10 seats)

-   HubSpot Marketing Hub Professional configuration (1 seat) with SMS Access Add-On

-   Gmail-to-HubSpot email integration via OAuth

-   HubSpot SMS Access Add-On for text messaging

-   Airtable-to-HubSpot event-driven synchronization via Zapier

-   User roles, permissions, and notification configuration

-   Project Master Info field implementation

-   Dashboard and reporting views

-   Deployment checklists by role

-   welcome@livingwithlolo.com pre-sales inbox (basic email configuration in Phase 1)

-   Salesmsg urgent hotline configuration

-   Slack integration (#urgent-alerts and #client-inboxes channels)

-   family@livingwithlolo.com inbox (post-project client care)

-   info@livingwithlolo.com inbox (general business inquiries)

-   Email signature enforcement via Google Workspace Admin Console

OUT OF SCOPE:

-   Voice calling and voicemail integration

-   Automated escalation or SLA monitoring

-   BuilderTrend integration

-   DesignFiles integration

-   Marketing automation beyond SMS

-   AI capabilities (see BRD Addendum A)

-   Vacation mode automation (manual coordination only)

-   welcome@livingwithlolo.com SMS integration (deferred to Phase 1.5)

-   Pre-sales phase-based routing and Airtable sync (deferred to Phase 1.5)

-   Salesmsg integration with HubSpot Deal timeline (deferred to post-Phase 1)

## 1.3 Target Audience

-   LWL IT Lead (Primary): Complete HubSpot configuration authority

-   Airtable Administrator (Josh): Airtable schema and integration authority

-   CEO & Directors: Technical review and approval authority

-   LWL Operations Team: User acceptance testing participants

-   Future Support Resources: Maintenance and troubleshooting reference

## 1.4 Document Organization

-   Section 2: System architecture and component relationships

-   Section 3: HubSpot configuration specifications

-   Section 4: Airtable schema and automation specifications

-   Section 5: Integration architecture (Zapier workflows)

-   Section 6: Gmail integration configuration

-   Section 7: Security and access control

## 1.5 Reference Documents

| **Document** | **Version** | **Purpose** |
| --- | --- | --- |
| BRD Consolidated Communications v4 FINAL | 4.0 | Business requirements authority |
| HubSpot Sales Hub Professional Admin Guide | Current | Platform documentation |
| HubSpot SMS Access Add-On Documentation | Current | SMS feature specifications |
| Google Workspace Admin Console Guide | Current | Gmail configuration reference |
| Zapier Developer Documentation | Current | Webhook and API integration guide |
| Airtable API Documentation | Current | Webhook automation reference |

## 1.6 Assumptions and Constraints

Assumptions:

1.  Living With Lolo maintains active Google Workspace subscription with Gmail

2.  LWL IT Lead has administrative access to Google Workspace Admin Console

3.  Josh (Airtable Administrator) has Creator/Owner access to LWL's Airtable workspace

4.  LWL will purchase HubSpot Sales Hub Professional (10 seats) + Marketing Hub Professional (1 seat) + SMS Access Add-On

5.  LWL will maintain Zapier subscription (Starter tier minimum, approximately $20/month)

6.  All LWL team members have smartphones capable of running HubSpot mobile app

7.  Arizona Time Zone (UTC-7 year-round, no DST) applies to all business hours logic

8.  LWL will purchase Salesmsg subscription for urgent hotline (approximately $29-49/month for 10DLC number + shared inbox)

9.  LWL maintains active Slack workspace with emergency response team members

Constraints:

1.  HubSpot Professional tier limitations (no custom Projects object, limited workflow actions)

2.  HubSpot Contact object limits: 3 email addresses and 4 phone numbers per Contact

3.  Gmail API rate limits may require batch processing during high-volume periods

4.  Zapier Starter tier supports approximately 750 tasks/month (adequate for event-driven approach)

5.  No custom code or middleware beyond Zapier's visual workflow builder

6.  Implementation must complete within 17-week timeline (BRD Section 7.2)

7.  Salesmsg operates as standalone platform in Phase 1 (no direct HubSpot integration)

8.  Slack integration requires n8n or Zapier workflows for webhook delivery

## 1.7 Phase 1 Discovery Completion Checklist 

All items below MUST be completed and documented before Phase 2 Configuration begins.

**\*\*Blocking Decisions:\*\***

☐ **\*\*Project ID Naming Convention\*\*** (Section 4.3)

\- Josh proposed format: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\- Robin validated business requirements: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\- Johnny confirmed HubSpot compatibility: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\- CEO final approval: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

☐ **\*\*User Roster Finalized\*\*** (Section 3.1.2)

\- All 10 Sales Hub user names documented: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\- Administrator designations confirmed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\- Josh's role (Admin vs. Standard User) decided: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\- CEO approval: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

☐ **\*\*Phase-to-POC Mapping Validated\*\*** (BRD Appendix C)

\- Robin (Operations) approval: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\- Debra (Construction) approval: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

☐ **\*\*Project Master Info Template\*\*** (Section 3.7.2)

\- Template structure finalized: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ - CEO approval: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

☐ **\*\*Airtable Pre-Implementation Requirements\*\*** (BRD 1.6.3)

\- Josh completed schema validation (1.6.3.2): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\- Josh completed webhook proof-of-concept (1.6.3.3): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\- Josh provided integration architecture proposal (1.6.3.4): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\- Johnny approved all deliverables: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**☐ HubSpot User ID Mapping (Section 4.2.4)**

-   **Johnny provided Josh with mapping document: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

-   **Josh entered HubSpot User IDs into Airtable Users table: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

-   **Mapping validated: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

-   **Johnny configured POC Assignment workflow with User IDs: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**☐ \*\*HubSpot User ID Mapping\*\* (Section 4.2.4)**

\- Johnny provided Josh with mapping document: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\- Josh entered HubSpot User IDs into Airtable Users table: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\- Mapping validated: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\- Johnny configured POC Assignment workflow with User IDs: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

☐ **\*\*Phase 2 Authorization:\*\***

\- All blocking decisions complete: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\- Discovery sign-off: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\- Phase 2 start date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_