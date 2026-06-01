# Material State Inventory - Phase 75.2

## Sovereign State Ownership

| State Type | Material Location | Authority | Duplicate Check |
|------------|-------------------|-----------|-----------------|
| Ownership | `UnifiedExecutionGraph.ownership` | UnifiedExecutionGraph | [x] 0 Duplicates |
| Pressure | `UnifiedExecutionGraph.global_pressure` | UnifiedExecutionGraph | [x] 0 Duplicates |
| Execution | `UnifiedExecutionGraph.material_runqueue` | UnifiedExecutionGraph | [x] 0 Duplicates |
| Memory | `PhysicalResourceAuthority.numa_policy` | PhysicalResourceAuthority | [x] 0 Duplicates |
| IRQ | `PhysicalResourceAuthority.irq_assignments` | PhysicalResourceAuthority | [x] 0 Duplicates |
| DMA | `PhysicalResourceAuthority.dma_ownership` | PhysicalResourceAuthority | [x] 0 Duplicates |
| NUMA | `PhysicalResourceAuthority.numa_policy` | PhysicalResourceAuthority | [x] 0 Duplicates |

## Verification
The audit confirms that all operational states are stored in either the `UnifiedExecutionGraph` (for high-level system state) or the `PhysicalResourceAuthority` (for low-level hardware state). No other components maintain local, non-synchronized replicas of these states.
