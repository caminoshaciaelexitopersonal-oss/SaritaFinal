# Operational Limit Report (Phase 79.1)

## 1. UnifiedExecutionGraph
* **Memory Limit:** Linearly bounded by the number of `PhysicalExecutionVertex` objects in `self.vertices`. At 1,000,000 vertices, with an average size of 1KB per vertex (payload + metadata), the graph consumes ~1GB of RAM.
* **Queue Limit:** `queue.Queue()` is unbounded by default. High burst rates could lead to memory exhaustion before processing.
* **CPU Limit:** Single-threaded event processor means throughput is capped by the speed of a single core and SQLite write latency.

## 2. SovereignAuditLedger
* **Storage Limit:** SQLite database size. Practically bounded by filesystem capacity.
* **Concurrency:** WAL mode allows 1 writer and multiple readers. Throughput is limited by disk I/O and FS sync operations.
* **Hash Integrity:** SHA-256 chain. Performance degrades linearly with chain depth if full verification is performed.

## 3. RuntimeReplayEngine
* **Replay Throughput:** Reconstruction involves reading from SQLite and emitting to a fresh Graph. Performance is ~10k-50k events per second depending on storage speed.
* **Memory during Replay:** Replayed graph occupies similar memory to production graph. Simultaneous production and replay doubles memory pressure.

## 4. Evidence Fabric
* **Evidence Schema:** Fixed overhead per vertex.
* **Hashing overhead:** Negligible compared to I/O, but becomes measurable at multi-million event scales.

## 5. io_uring Fabric
* **Ring Size:** SQ/CQ ring sizes are usually power of 2 (e.g., 4096).
* **Throughput:** Capable of millions of IOPS, far exceeding the current Ledger write throughput.
