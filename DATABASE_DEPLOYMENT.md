# DATABASE DEPLOYMENT: SARITA v1.0
**Audit Date:** March 2026
**Lead Infrastructure Architect:** Jules

## 1. Amazon RDS Configuration
- **Engine**: PostgreSQL 15.
- **Instance Type**: `db.m5.xlarge` (Primary).
- **High Availability**: **Multi-AZ Deployment** (Synchronous replication to standby).
- **Storage**: EBS-optimized IOPS (SSD).

## 2. Scalability & Read Performance
- **Read Replicas**: 2 Replicas distributed in other AZs for read-heavy operations (Reports, Audits).
- **Load Balancing**: Read-heavy traffic from the backend is automatically routed to replicas.

## 3. Data Protection & Backups
- **Automated Backups**: Retention for 35 days (Full snapshot every 24h).
- **PITR**: Point-in-Time Recovery enabled (5-minute granularity).
- **Encryption**: AWS KMS disk encryption active.

## 4. Connection Management (Django)
- **Pooler**: Using `django-db-geventpool` for high-concurrency handling.
- **Max Connections**: 1,500 simultaneous sessions.
- **Migration Strategy**: Migrations are applied via a temporary EKS Job during the CI/CD pipeline to ensure schema consistency.

---
**Verdict**: The database tier is robust, auditable, and resilient to regional AZ failures.
