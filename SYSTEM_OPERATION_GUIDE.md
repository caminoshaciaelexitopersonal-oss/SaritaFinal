# SYSTEM OPERATION GUIDE: SARITA v1.0
**Audit Date:** March 2026
**Lead SRE Engineer:** Jules

## 1. 24/7 Monitoring Protocol
The platform is monitored continuously using the **Prometheus/Grafana** stack.

- **Infrastructure Watch**: Real-time tracking of EKS Node health and RDS IOPS.
- **Application Watch**: API throughput, Error spikes (5xx), and Latency p95.
- **Business Watch**: Real-time sales volume, active users, and AI task completion rate.

## 2. Key Performance Indicators (KPIs)
Operative thresholds for stable operation:
- **DAU (Daily Active Users)**: Target > 1,000 for Week 1.
- **Latency**: Mean < 200ms; Max < 2s for complex AI plans.
- **Errors**: < 1.0% of total requests.
- **Resource Usage**: CPU < 60% (Scaled automatically beyond this).

## 3. Incident Management Protocol
In the event of system failure or degradation:
1. **Detection**: Automated SNS/Slack alert triggered by Prometheus.
2. **Classification**: (P0: System Down, P1: Partial failure, P2: UX glitch).
3. **Response**:
   - **P0**: Emergency SRE team activation; Automatic rollback if deploy-related.
   - **P1**: Task delegated to the `N1 General` AI agent for initial diagnosis and remediation attempt.
   - **P2**: Logged in Jira for next business day resolution.

## 4. Stability Metrics
- **Uptime Target**: 99.95%.
- **MTTR (Mean Time to Repair)**: < 15 minutes.

---
**Verdict**: Operational protocols are established and automated to ensure continuous service.
