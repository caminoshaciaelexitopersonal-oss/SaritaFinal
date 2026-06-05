# Replay Consistency Matrix (Phase 78.1)

| Subsystem | Consistency Mechanism | Status | Risk of Divergence |
| :--- | :--- | :--- | :--- |
| **UnifiedExecutionGraph** | Single Writer Sovereignty | Verified | Low |
| **PhysicalExecutionVertex** | Cryptographic Hash Chaining | Verified | Medium (UUID dependency) |
| **SovereignAuditLedger** | Linear Append-Only Log | Verified | Medium (Timestamp dependency) |
| **RuntimeReplayEngine** | Incremental Rehydration | Verified | Medium (State cleanup) |
| **Evidence Fabric** | Constitutional Schema | Verified | Low |
| **PhysicalResourceAuthority**| Resource Isolation | Verified | Low |

## Consistency Evaluation

### 1. Hash Chain Integrity
The hash chain depends on the strict ordering of events. Any missing or reordered event will break the `parent_hash` linkage.

### 2. State Reconstruction
The `UnifiedExecutionGraph` re-applies transformations to `ownership`, `global_pressure`, and `completed_tasks`. These must be cleared before replay starts.

### 3. Ownership Tracking
Ownership is re-established during replay. If the initial state of the `ownership` dictionary is not empty, divergence occurs.
