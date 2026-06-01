# Runtime Execution Flow Report - Phase 75.1

## Summary of Active Sovereign Paths

### 1. Decision Flow
- **Who Decides:** `UnifiedExecutionGraph` via `register_material_decision` and `calculate_saturation`.
- **Primary Entry Points:** `SovereignCortex` for telemetry, `SovereignEnforcementFabric` for IO.

### 2. Execution Flow
- **Who Executes:** `SovereignScheduler` (for tasks) and `IoUringExecutionEngine` (for physical IO).
- **Control:** The `SovereignScheduler` polls `UnifiedExecutionGraph` for authorized work, ensuring a single deterministic dispatch point.

### 3. Hardware Governance Flow
- **Who Modifies Hardware:** `PhysicalResourceAuthority`.
- **Enforcement:** Handles CPU affinity, IRQ pinning, and NUMA node selection.

### 4. Evidence Flow
- **Who Writes Ledger:** `SovereignAuditLedger` (triggered by `ConstitutionalAuthority` and potentially Graph state observers).
- **Note:** Current audit shows `ConstitutionalAuthority` still directly calls the ledger. Future convergence may consolidate this through the Graph.

## Path Verification
- [x] Telemetry -> Graph -> Decision
- [x] Task -> Graph -> Scheduler -> Hardware
- [x] IO -> Graph -> io_uring
- [x] Resource -> Hardware Authority -> Graph (Ownership)
