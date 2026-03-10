# PRODUCTION ARCHITECTURE: SARITA v1.0
**Audit Date:** March 2026
**Lead Infrastructure Architect:** Jules

## 1. High-Level Architecture Overview
The SARITA ecosystem operates under a multi-tier, high-availability architecture designed for 24/7 operation and elastic scaling.

```text
[INTERNET]
    │
[Cloudflare CDN / WAF] <─── Shield & Static Cache
    │
[AWS Elastic Load Balancer (ALB)] <─── TLS Termination & Distro
    │
[Amazon EKS Cluster]
    ├── Namespace: frontend (Next.js Pods)
    ├── Namespace: backend (Django REST Pods)
    ├── Namespace: workers (Celery & AI Agent Pods)
    └── Namespace: monitoring (Prometheus & Grafana)
    │
    ├── [Amazon ElastiCache (Redis)] <─── Session, Cache, Queues
    ├── [Amazon RDS (PostgreSQL 15)] <─── Multi-AZ Persistence
    └── [Amazon S3 Buckets] <─── User Files, Backups, Logs
```

## 2. Infrastructure Segmentation
To maximize security and performance, the infrastructure is segmented as follows:
- **Public Tier**: ALB and Cloudflare CDN. Only HTTPS (443) is exposed.
- **Application Tier (Private)**: EKS Worker nodes in private subnets. Access only from ALB.
- **Data Tier (Private)**: RDS and ElastiCache. Access strictly restricted to Application Tier nodes.

## 3. Operational Benefits
- **Security**: Isolation of data and business logic from the public internet.
- **Performance**: Low latency via Multi-AZ internal networking and Redis caching.
- **Scalability**: Stateless application pods allow for near-instant horizontal scaling.

---
**Verdict**: The production architecture follows industry best practices for enterprise-grade SaaS platforms.
