# Authority Regression Inventory (Phase 80.1)

| Current Sovereign Authority | Responsibility | Potential Regression Path |
| :--- | :--- | :--- |
| **UnifiedExecutionGraph** | Decision & Causal State | Creation of `LegacyDecisionEngine` or direct state mutation. |
| **PhysicalResourceAuthority**| Physical Hardware | Implementation of `CPUGovernor` or `MEMManager` as independent entities. |
| **SovereignScheduler** | Task Dispatch | Scheduler-local task prioritization bypassing graph authorize signals. |
| **SovereignAuditLedger** | Persistence | Use of raw `open()` or `json` files for bypassing the ledger. |

## Prevention Strategy
Implement static analysis and runtime guards that detect unauthorized class instantiations or forbidden module imports.
