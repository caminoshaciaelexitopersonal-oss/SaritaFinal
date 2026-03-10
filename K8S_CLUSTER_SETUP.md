# K8S CLUSTER SETUP: SARITA v1.0
**Audit Date:** March 2026
**Lead Infrastructure Architect:** Jules

## 1. Amazon EKS Configuration
- **Kubernetes Version**: 1.30+
- **Initial Node Count**: 3 Nodes (m5.large).
- **Auto Scaling**: Cluster Autoscaler enabled (Min 3 / Max 10 nodes).
- **Node Groups**: Managed Node Groups across 3 Availability Zones.

## 2. Namespace Segmentation
To ensure resource isolation and security:
- `sarita-frontend`: Next.js Web Dashboard.
- `sarita-backend`: Django REST API.
- `sarita-workers`: Celery Workers, Beat, and AI Agent executors.
- `sarita-monitoring`: Prometheus, Grafana, and Jaeger.

## 3. Deployment Configuration (Critical)
- **API Pods**: 3 replicas, HPA (CPU > 70%), RollingUpdate strategy.
- **Frontend Pods**: 2 replicas, standard Node.js optimized settings.
- **Workers**: 2 replicas (Scaling based on Celery queue length).
- **IA Agents**: Dedicated pods with higher memory limits for LLM context processing.

## 4. Resource & Health Management
- **LivenessProbe**: Checks `/api/v1/infra/health/liveness/` every 10s.
- **ReadinessProbe**: Checks `/api/v1/infra/health/readiness/` every 5s.
- **Resource Limits**:
  - Backend: CPU: 1.0, Mem: 1Gi.
  - Worker: CPU: 0.8, Mem: 1.5Gi.

---
**Verdict**: EKS cluster setup is optimized for high availability and automatic workload recovery.
