# Authority Call Graph - Phase 74.1

## Desired Sovereign Path
Telemetry -> UnifiedExecutionGraph -> Scheduler -> PhysicalResourceAuthority -> io_uring -> Ledger

## Current Fragmented Paths

### Execution Path
Task -> ConstitutionalAuthority -> UnifiedExecutionGraph -> SovereignScheduler -> SovereignEnforcementFabric -> Ledger

### Parallel Cortex Path
Intent -> DistributedRuntimeCortex -> DistributedSchedulerArbitrator -> RuntimeSovereignArbitrator (Conflict)

### IO Path
SovereignEnforcementFabric -> IoUringExecutionEngine (Stubs) -> Ledger
