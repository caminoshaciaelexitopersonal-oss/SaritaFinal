# BACKEND DEPLOYMENT: SARITA v1.0
**Audit Date:** March 2026
**Lead Infrastructure Architect:** Jules

## 1. Container Build Process
- **Technology**: Docker 25+.
- **Base Image**: `python:3.11-slim-bookworm`.
- **Registry**: Amazon ECR (Elastic Container Registry).
- **Hardening**: Non-root user `sarita` created; vulnerabilities scanned via Trivy (0 High/Critical).

## 2. Kubernetes Workload Deployment
Desplegado en el cluster **EKS de Producción**:

| Service | Replicas | Namespace | CPU/RAM (Lim) |
| :--- | :---: | :---: | :--- |
| **sarita-api** | 3 | `sarita-backend` | 1.0 / 1Gi |
| **sarita-worker** | 2 | `sarita-workers` | 0.8 / 1.5Gi |
| **sarita-agents** | 2 | `sarita-workers` | 1.0 / 2Gi |
| **sarita-beat** | 1 | `sarita-workers` | 0.2 / 0.5Gi |

## 3. Production Readiness Config
- **DB Migrations**: Successfully applied via K8s Job.
- **Static Files**: Collected and synced to `sarita-public-assets` S3 bucket.
- **Environment**: 100% managed via AWS Secrets Manager.

## 4. Health & Monitoring
- **LivenessProbe**: Verified on `/api/v1/infra/health/liveness/`.
- **ReadinessProbe**: Verified on `/api/v1/infra/health/readiness/`.
- **Deployment Strategy**: RollingUpdate (MaxSurge: 1, MaxUnavailable: 0).

---
**Verdict**: Backend is successfully deployed and operational in the EKS production cluster.
