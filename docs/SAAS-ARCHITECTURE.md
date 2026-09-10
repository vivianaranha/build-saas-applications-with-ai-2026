# Reference AI SaaS Architecture

**Created by School of AI**

```text
Browser / Mobile
      |
Frontend / BFF
      |
API Layer
 |    |       |
Auth  Tenant  Entitlements
      |
Application Services
 |        |          |
Database  Async Jobs  Notifications/Webhooks
 |
AI Provider Gateway
 |             |
RAG/Retrieval  Bounded Agent Tools
```

Cross-cutting: validation, audit logs, usage metering, security, evaluation, observability, migrations, CI/CD and rollback.

The tenant identity must flow through every data-access and asynchronous path. AI tools must not bypass application authorization.

---

**Created by School of AI**
