# Causal Regression Matrix (Phase 80.1)

| Path Component | Sovereign Protocol | Regression Risk |
| :--- | :--- | :--- |
| **Ingestion** | `emit_event()` only | Direct property setting on Graph. |
| **Processing** | Single Writer Queue | Adding multiple worker threads to `_event_processor`. |
| **Decision** | Evidence-anchored vertices | Manual state changes without vertex creation. |
| **Persistence** | Ledger Hash Chaining | Disabling WAL or batch transactions for "speed". |
| **Execution** | Authorized task signals | Calling `_execute_material_task` directly. |

## Integrity Mandate
Any architectural change that allows two paths to achieve the same state transformation is a regression.
