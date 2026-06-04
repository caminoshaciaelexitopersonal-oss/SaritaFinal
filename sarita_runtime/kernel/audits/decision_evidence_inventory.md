# Decision Evidence Inventory - Phase 76.1

| Decision/Event | Origin Evidence | Material Action | Ledger Proof |
|----------------|-----------------|-----------------|--------------|
| Task Auth | Cortex Dispatch | Graph Add Task | Vertex (TASK_AUTHORIZED) |
| IO Submit | Enforcement Req | io_uring Submission | Vertex (IO_SUBMISSION) |
| IO Complete | CQE Reap | Result Update | Vertex (IO_COMPLETION) |
| IRQ Assign | Path Claim | IRQ Affinity Change | Graph Ownership Entry |
| Pressure Res | PSI/Telemetry | Deterministic Throttling | Vertex (EXTREME_PRESSURE) |
| Memory Bind | NUMA Request | Node Binding | Graph Ownership Entry |

## Summary
The system currently captures evidence at the Graph level for high-level decisions and at the Ownership level for hardware assignments. Phase 76 will consolidate this into a unified evidence fabric.
