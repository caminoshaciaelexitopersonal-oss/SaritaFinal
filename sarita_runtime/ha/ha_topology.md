# RUNTIME HIGH AVAILABILITY CONFIGURATION

## 1. POSTGRES HA (Patroni + Repmgr)
- **Primary:** node-db-01
- **Standby:** node-db-02
- **Witness:** node-db-03
- **Replication:** Asynchronous with 0.5s lag target.

## 2. KAFKA HA (Strimzi)
- **Brokers:** 3 minimum.
- **Replication Factor:** 3.
- **Min Insync Replicas:** 2.

## 3. TEMPORAL HA
- **Matching Service:** 2 instances.
- **History Service:** 3 shards minimum.
- **Frontend Service:** Load balanced.

## 4. REDIS HA (Sentinel)
- Quorum-based failover for distributed locks and cache.
