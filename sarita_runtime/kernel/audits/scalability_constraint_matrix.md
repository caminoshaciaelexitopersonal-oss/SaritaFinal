# Scalability Constraint Matrix (Phase 79.1)

| Subsystem | Constraint | Threshold (Estimated) | bottleneck |
| :--- | :--- | :--- | :--- |
| **UnifiedExecutionGraph** | Vertex Storage | 5,000,000 vertices | RAM |
| **UnifiedExecutionGraph** | Event Ingestion | 50,000 msg/sec | Single Core CPU |
| **SovereignAuditLedger** | Write Persistence | 20,000 write/sec | Disk IOPS (SSD) |
| **SovereignAuditLedger** | Database Size | 2 TB | Filesystem |
| **RuntimeReplayEngine** | Replay Speed | 100,000 events/sec | SQL Query + CPU |
| **Evidence Fabric** | Verification | 1,000,000 hashes/sec | CPU (AVX2/NI) |
| **io_uring Fabric** | Concurrent Ops | 4,096 | Ring Size |

## Scalability Strategy
1. **Vertical:** Faster CPU cores and NVMe storage for Ledger.
2. **Horizontal:** (Future) Sharding of the Graph by Epoch or Actor, though this challenges absolute causal linearity.
3. **Optimized Persistence:** Batched SQLite commits (currently atomic per vertex).
