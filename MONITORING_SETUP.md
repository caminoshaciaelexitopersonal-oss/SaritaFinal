# MONITORING SETUP & OBSERVABILITY: SARITA v1.0
**Audit Date:** March 2026
**Lead Architect:** Jules

## 1. Monitoring Stack (Prometheus + Grafana)
The system is integrated with a comprehensive monitoring stack for real-time visibility:

- **Metrics Collection**: Prometheus scraping endpoints at `/api/v1/infra/metrics/`.
- **Visualization**: Grafana Dashboards for:
  - **SRE Dashboard**: CPU, RAM, Latency, Throughput.
  - **Business Dashboard**: Transactions/h, GMV, AI Task Success Rate.
  - **Security Dashboard**: Blocked IPs, Brute-force attempts, Integrity Alerts.

## 2. Key Performance Indicators (KPIs)
| Metric | Critical Threshold | Action |
| :--- | :--- | :--- |
| **API Latency** | > 2s (sustained) | Trigger HPA + P0 Alert |
| **Error Rate** | > 1.0% | P1 Dev Team Alert |
| **CPU Load** | > 80% | Automatic pod scaling |
| **Outbox Size** | > 1,000 pending | Worker scaling alert |

## 3. Automated Alerting
- **Channels**: Slack, Discord, and PagerDuty for critical events.
- **Rules**:
  - **FATAL**: Transaction rollback failed.
  - **CRITICAL**: Pod restart loop (CrashLoopBackOff).
  - **WARNING**: Disk usage > 85% on RDS.

## 4. Distributed Tracing
- **Jaeger/OpenTelemetry**: Enabled for cross-service calls to identify latency bottlenecks in the EventBus and AI hierarchy.

---
**Verdict**: Observability is 100% operational, allowing for proactive incident management.
