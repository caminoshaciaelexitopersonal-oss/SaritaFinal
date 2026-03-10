# LOAD TEST SCENARIOS: SARITA v1.0
**Audit Date:** March 2026
**Lead Architect:** Jules

## 1. Critical Operation Identification
The following operations have been identified as the highest load generators for the SARITA ecosystem:

| Operation | Type | Impact Level | Description |
| :--- | :--- | :---: | :--- |
| **Login / Auth** | CPU Heavy | High | JWT generation and RS256 signing. |
| **Wallet Inquiry** | Read Heavy | Medium | Real-time balance and transaction history. |
| **Order Creation** | Mixed | High | Inventory check + DB write + Event emit. |
| **Payment Process** | Write Heavy | Critical | Atomic wallet update + Ledger posting. |
| **Invoice Gen** | I/O Heavy | Medium | PDF generation and legal notarization. |
| **AI Delegation** | CPU/Network | Medium | Mission planning and agent orchestration. |

## 2. User Behavior Simulation (Flow)
Typical user journey for the simulation:
1. **Discovery**: Citizen/Tourist logs in and views tourist locations (40%).
2. **Transaction**: Citizen makes a QR payment or merchant records a sale (25%).
3. **Governance**: Administrator reviews audit logs or performs ERP reporting (15%).
4. **Maintenance**: Background workers process EventBus outbox and AI tasks (20%).

## 3. Traffic Distribution Profile
| Operation Category | % of Total Traffic | Target RPS (at 10k Users) |
| :--- | :---: | :---: |
| Authentication | 10% | 150 |
| Consultations (Read) | 40% | 600 |
| Financial Ops (Write) | 25% | 375 |
| ERP / Management | 15% | 225 |
| AI / Background | 10% | 150 |

## 4. Test Environment Specs
- **Infrastructure**: Amazon EKS (Kubernetes)
- **DB**: RDS PostgreSQL 15 (Large Instance)
- **Cache**: Elasticache Redis 7
- **Tools**: k6 (Main load injector)

---
**Verdict**: Scenarios are defined to reflect real-world usage patterns under high density.
