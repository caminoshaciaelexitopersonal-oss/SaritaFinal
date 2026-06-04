# Divergence Risk Report - SARITA Sovereign Kernel (Phase 78.1)

## 1. Non-Deterministic Identifiers (UUIDs)
* **Subsystem:** `PhysicalExecutionVertex`
* **Risk:** High. `uuid.uuid4()` is used to generate `vertex_id` during initialization.
* **Impact:** Replayed vertices will have different `vertex_id` values than the original ones, although the replayed `vertex_hash` is forced to match the original ledger hash. This creates a mismatch between the object state and its cryptographic evidence.
* **Mitigation:** Replay must restore the `vertex_id` from the ledger payload instead of generating a new one.

## 2. Temporal Divergence (Timestamps)
* **Subsystem:** `UnifiedExecutionGraph`, `PhysicalExecutionVertex`, `SovereignAuditLedger`
* **Risk:** High. `time.time()` is called in multiple places during event processing and ledger recording.
* **Impact:** Replay will generate new timestamps if not explicitly overridden. While hashes are forced during replay in the Graph, the Ledger itself records new entries with new timestamps and new hashes during replay if the `RuntimeReplayEngine` uses a standard Graph instance that writes to a ledger.
* **Mitigation:** Replay must use the timestamps stored in the evidence payload. `SovereignAuditLedger` should support deterministic entry recording for replay scenarios.

## 3. Single Writer Queue Timing
* **Subsystem:** `UnifiedExecutionGraph` (_event_queue)
* **Risk:** Low/Medium.
* **Impact:** If multiple events are emitted rapidly, their order in the queue is guaranteed, but external factors could theoretically influence emission order if not properly synchronized at the source.
* **Mitigation:** The system uses a Single Writer pattern which ensures linear processing once events reach the queue.

## 4. Floating Point Determinism
* **Subsystem:** `UnifiedExecutionGraph` (global_pressure)
* **Risk:** Low.
* **Impact:** `global_pressure` calculation (`sum(subsystem_signals.values()) / len(subsystem_signals)`) may have micro-divergences across different CPU architectures or Python versions due to IEEE 754 floating point handling.
* **Mitigation:** Use fixed-point arithmetic or round to a specific precision for pressure-based decisions.

## 5. JSON Serialization
* **Subsystem:** `SovereignAuditLedger`
* **Risk:** Medium.
* **Impact:** `json.dumps(vertex.payload)` in `record_vertex` does not use `sort_keys=True`.
* **Mitigation:** Ensure all JSON serialization uses `sort_keys=True` to maintain hash stability.
