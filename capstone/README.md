# Northstar AI Workspace — Capstone

**Created by School of AI**

Build a production-oriented **multi-tenant AI SaaS workspace** for business teams.

## Product
Each customer gets a workspace where users can:
- invite members
- upload knowledge
- ask evidence-grounded questions
- configure approved AI automations
- request agent actions
- review approvals and audit history
- track usage and plan limits

## Reference architecture

```text
React / Web App
      |
FastAPI / API Layer
 |       |        |
Auth   Tenant   Entitlements
      |
Application Services
 |        |          |
SQL DB   Job Queue   Notifications/Webhooks
 |
AI Gateway
 |             |
Tenant RAG     Bounded Agent Tools
```

## 26 deliverables
1 customer/problem brief
2 ICP/JTBD
3 MVP scope
4 activation metric
5 responsive user journey
6 frontend architecture
7 backend/API contract
8 tenant-aware data model
9 migrations
10 authentication
11 RBAC/resource authorization
12 plan/entitlement matrix
13 usage metering
14 AI provider abstraction
15 structured AI outputs
16 tenant-aware RAG
17 RAG evaluation
18 bounded agent/tool policy
19 human approval
20 async/idempotent job flow
21 webhook/notification design
22 security/threat model
23 automated tests including cross-tenant negatives
24 logs/metrics/SLO/runbook
25 deployment/migration/rollback
26 AI economics + launch review

## Critical cap
Any confirmed cross-tenant data exposure, server-side authorization bypass, unapproved consequential agent action, exposed production secret, or absence of measurable AI evaluation caps the score at **69/100**.

---

**Created by School of AI**
