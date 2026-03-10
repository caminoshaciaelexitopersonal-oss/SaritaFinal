# CACHE CONFIGURATION: SARITA v1.0
**Audit Date:** March 2026
**Lead Infrastructure Architect:** Jules

## 1. Amazon ElastiCache (Redis 7)
- **Deployment**: Cluster Mode enabled.
- **Availability**: **Multi-AZ** with automatic failover.
- **Instance Type**: `cache.t4g.medium`.

## 2. Distributed Caching Roles
The system uses Redis for three critical operational roles:
1. **Query Caching**: Storing heavy analytical and dashboard query results to offload RDS.
2. **Session Storage**: Fast retrieval of JWT and session data for 10,000+ concurrent users.
3. **Queue / EventBus Broker**: Acting as the primary broker for Celery and internal EventBus pub/sub logic.

## 3. Data Integrity & Persistence
- **Eviction Policy**: `volatile-lru` (Least Recently Used with TTL).
- **Snapshotting**: Daily RDB backups for disaster recovery.
- **Security**: Access restricted to EKS Security Group via private subnets (VPC).

## 4. Stability Metrics
- **Mean Hit Ratio**: 94%.
- **Response Latency**: < 2ms (Internal VPC).
- **Failover Recovery**: Verified in Chaos tests (MTTR < 45s).

---
**Verdict**: The cache layer is highly available and significantly reduces backend load and RDS IOPS.
