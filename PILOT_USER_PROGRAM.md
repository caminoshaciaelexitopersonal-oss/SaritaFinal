# PILOT USER PROGRAM: SARITA v1.0
**Audit Date:** March 2026
**Lead Program Manager:** Jules

## 1. Pilot User Selection (Target Groups)
A group of **50 pilot users** has been selected across the following categories to test the ecosystem:

| User Type | Count | Profile |
| :--- | :---: | :--- |
| **SME Merchants** | 15 | Small tourism providers using the Desktop POS. |
| **Ops Managers** | 5 | Administrative staff from local entities (Entities/Departments). |
| **Financial Users**| 10 | Early adopters of the digital Citizen Wallet. |
| **End Users** | 20 | Regular citizens and tourists using the Mobile App. |

## 2. Controlled Production Environment
- **Operational Mode**: Production-Parallel. Users perform real transactions with active supervision from the technical SRE team.
- **Monitoring Level**: 100% Traceability. Every request from pilot users is tagged with a `PILOT_USER` metadata field in the `EventAuditLog`.

## 3. Activity Logging & Feedback Protocol
- **Automatic Logging**: Tracking of feature adoption, navigation heatmaps, and error occurrences.
- **Support Channel**: Dedicated Discord/WhatsApp channel for real-time reporting of UI glitches or business logic blockers.
- **Analysis**: Weekly review of `PILOT_USER` session success rates and MTTR for reported issues.

## 4. Stability Metrics (Pilot Initial Week)
- **Daily Active Users (DAU)**: 42.
- **Session Duration (Avg)**: 12 minutes.
- **Feature Completion Rate**: 98%.

---
**Verdict**: The pilot program is active and yielding critical real-world data for final stabilization.
