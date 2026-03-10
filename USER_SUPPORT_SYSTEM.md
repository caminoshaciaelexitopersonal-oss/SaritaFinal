# USER SUPPORT SYSTEM: SARITA v1.0
**Audit Date:** March 2026
**Lead Support Architect:** Jules

## 1. Support Channels
The platform provides three official tiers of user assistance:
- **Level 1 (AI Support)**: 24/7 SADI Conversational Agent embedded in `app.sarita.app`.
- **Level 2 (Chat/Tickets)**: Real-time support dashboard for human agents located at `support.sarita.app`.
- **Level 3 (Email)**: Formal ticketing for complex legal or financial issues at `ayuda@sarita.app`.

## 2. Incident Classification & SLA
Service Level Agreements (SLA) for user requests:

| Category | Description | Priority | Target Response |
| :--- | :--- | :---: | :---: |
| **Critical** | Cannot process payments/log in | P0 | < 1 hour |
| **Major** | Feature not working as expected | P1 | < 6 hours |
| **Normal** | Account queries, UI feedback | P2 | < 24 hours |
| **Minor** | Suggestions, documentation typos| P3 | < 72 hours |

## 3. Support Workflow
1. **Intake**: AI Agent (SADI) attempts to resolve the issue using the internal knowledge base.
2. **Escalation**: If unresolved, a ticket is created and assigned to the relevant department (Finance, Tech, Ops).
3. **Resolution**: Solution provided to the user; ticket marked as closed in `AuditLog`.
4. **Feedback**: Automated satisfaction survey sent to the user.

## 4. Key Metrics
- **First Response Time (Avg)**: < 5 minutes (AI-assisted).
- **Resolution Rate (AI)**: Target > 70% of Level 1 queries.

---
**Verdict**: User support is integrated and automated, combining AI efficiency with human expertise.
