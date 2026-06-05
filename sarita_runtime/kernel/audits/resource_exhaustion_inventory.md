# Resource Exhaustion Inventory (Phase 79.1)

## 1. Memory Exhaustion (OOM)
* **Impact:** Kernel crash or Graph corruption if the OS kills the process mid-write.
* **Mitigation:** Persistent Ledger (SQLite) ensures that any event that was successfully committed is recoverable. Volatile state (Graph memory) is reconstructed from Ledger.

## 2. Storage Exhaustion (Disk Full)
* **Impact:** `SovereignAuditLedger` fails to record new vertices.
* **Mitigation:** The Single Writer must detect write failure and enter a "Fail-Safe" mode, halting execution to prevent non-persisted causal progress.

## 3. CPU Saturation
* **Impact:** Latency jitter in task authorization.
* **Mitigation:** `SovereignScheduler` uses PSI (Pressure Stall Information) to detect and react to CPU pressure.

## 4. SQLite WAL Growth
* **Impact:** Excessive storage use and slower checkpoints.
* **Mitigation:** Periodic `PRAGMA wal_checkpoint(PASSIVE)` or `AUTO_CHECKPOINT`.

## 5. Queue Overflow
* **Impact:** Massive RAM consumption if producers outpace the single writer.
* **Mitigation:** Implement backpressure in `emit_event` using bounded queues.
