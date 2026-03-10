# MONITORING CONFIGURATION: SARITA v1.0
**Audit Date:** March 2026
**Lead Infrastructure Architect:** Jules

## 1. Observability Stack (Prometheus & Grafana)
- **Scraping**: Every 15 seconds from all EKS namespaces.
- **Dashboards**:
  - **Cluster Health**: Node CPU/RAM, Pod restarts, HPA status.
  - **Backend API**: Latency p95, HTTP 5xx errors, Throughput (req/s).
  - **Financial Metrics**: Outbox pending size, Ledger integrity status.
  - **AI Performance**: Token usage, Agent success rate, Plan generation latency.

## 2. Critical Alerting Rules
The system is configured to alert via **AWS SNS** (Slack/PagerDuty) on:
- **CPU Overload**: > 80% sustained for 5 minutes.
- **Error Spike**: > 2% HTTP errors in 2 minutes.
- **Latency Breach**: API Critical > 2s for 1 minute.
- **Pod OOM**: Any pod restart due to memory limits.

## 3. Log Aggregation (CloudWatch / S3)
- **Pod Logs**: Streamed to Amazon CloudWatch for real-time analysis.
- **Audit Logs**: Archived in S3 for forensic and regulatory compliance.
- **Structure**: Mandatory JSON format via `EnterpriseJSONFormatter`.

## 4. Availability Metrics
- **Uptime Monitor**: external health check from 3 global regions.
- **SLA Goal**: 99.95%.

---
**Verdict**: The monitoring setup provides 100% visibility and supports proactive maintenance of the entire system.
