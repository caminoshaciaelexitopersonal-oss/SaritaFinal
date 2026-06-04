# Causal Invariants Report - Phase 77.1

## Core Invariants

### 1. Decision-to-Evidence Invariant
- **Definition**: For every state change (ownership, pressure, task), there MUST be a corresponding `PhysicalExecutionVertex` and a `SovereignAuditLedger` entry.
- **Verification**: Verified via `UnifiedExecutionGraph.emit_event` which triggers both vertex registration and ledger persistence.

### 2. Hash Chain Invariant
- **Definition**: `current_vertex.previous_hash == previous_vertex.vertex_hash`.
- **Verification**: Enforced in `UnifiedExecutionGraph._process_material_event`.

### 3. State-Ledger Equivalence Invariant
- **Definition**: Replaying all ledger entries into a fresh `UnifiedExecutionGraph` MUST result in an identical `ownership` and `global_pressure` state.
- **Verification**: Verified in `test_case_6_replay_determinism`.

### 4. Timestamp Monotonicity
- **Definition**: `current_vertex.timestamp >= previous_vertex.timestamp`.
- **Verification**: Enforced by material clock collection during vertex creation.
