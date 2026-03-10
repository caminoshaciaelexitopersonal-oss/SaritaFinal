# SCALABILITY PLAN: SARITA v1.0
**Audit Date:** March 2026
**Lead infrastructure Architect:** Jules

## 1. Container Scaling (Kubernetes HPA)
The system is configured to scale horizontally based on real-time demand:
- **Metrics**: CPU > 70% or Memory > 80%.
- **Ceiling**: Configured to scale up to **50 pods** for the API service to handle traffic spikes.
- **Cool-down**: 300s window to avoid "flapping" during transient spikes.

## 2. Database Tier (PostgreSQL)
- **Read Scalability**: 2 existing Read Replicas; capacity to add up to 5 replicas dynamically in different regions.
- **Write Scalability**: Planned transition to **RDS Proxy** for connection multiplexing if simultaneous sessions exceed 5,000.
- **Partitioning**: Automated monthly partitioning for high-growth tables (`JournalEntry`, `AuditLog`).

## 3. Storage & Cache Growth
- **S3 Scaling**: Native scalability provided by AWS; no manual intervention required for Petabyte-scale storage.
- **Redis Scaling**: Cluster mode active; can scale from `t4g.medium` to `r6g.large` instances with zero downtime via AWS ElastiCache.

## 4. Key Growth Thresholds
| Milestone | Action Required |
| :--- | :--- |
| **50k Active Users** | Enable Database Sharding for Financial Core. |
| **100k Active Users** | Move to Multi-Region Cluster (EKS Cross-Region). |
| **1M Active Users** | Full transition to Microservices Architecture. |

---
**Verdict**: The infrastructure is highly elastic and prepared for rapid growth from 10k to 1M users.
