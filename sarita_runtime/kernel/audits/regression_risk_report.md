# Regression Risk Report (Phase 80.1)

## 1. Single Writer Sovereignty Risks
* **Component:** `UnifiedExecutionGraph`
* **Risk:** High. Future engineers might attempt to add direct mutation methods to `UnifiedExecutionGraph` (bypass `emit_event`) to solve performance issues or during "hotfix" attempts.
* **Impact:** Loss of linear causality, race conditions, and non-deterministic replay.

## 2. Authority Fragmentation Risks
* **Component:** `PhysicalResourceAuthority`
* **Risk:** Medium. New hardware subsystems might be implemented as standalone "Authorities" instead of being integrated into the unified authority structure.
* **Impact:** Split governance, inconsistent resource allocation, and lack of unified pressure arbitration.

## 3. Causal Path Parallelization
* **Component:** Execution flow (Telemetry -> Graph -> Scheduler).
* **Risk:** Low. Parallel execution paths that bypass the graph for "low priority" events.
* **Impact:** Incomplete evidence chain and invisible system state transitions.

## 4. State Duplication
* **Component:** Local caches in Scheduler or IO subsystems.
* **Risk:** Medium. Keeping local copies of graph state for "performance" can lead to stale data and divergent decision-making.
* **Impact:** Desynchronization between authority and execution.
