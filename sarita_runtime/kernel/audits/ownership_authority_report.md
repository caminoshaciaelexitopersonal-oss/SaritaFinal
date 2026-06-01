# Ownership Authority Report - Phase 75.3

## Resource Authority Mapping

| Resource | Primary Authority | Material Implementation |
|----------|-------------------|-------------------------|
| **IRQ** | `PhysicalResourceAuthority` | IRQ SMP affinity management |
| **DMA** | `PhysicalResourceAuthority` | DMA channel tracking and allocation |
| **NUMA** | `PhysicalResourceAuthority` | NUMA node pinning and memory policy |
| **CPU** | `PhysicalResourceAuthority` | Processor affinity enforcement |
| **Memory** | `PhysicalResourceAuthority` | NUMA-aware allocation policy |
| **IO** | `IoUringExecutionEngine` | SQ/CQ ring ownership and buffer registration |

## Verification
- **One Authority per Resource:** Confirmed.
- **Ownership Lineage:** All changes in ownership are recorded in the `UnifiedExecutionGraph` via `update_ownership`.
- **Conflict Resolution:** Handled centrally by the Graph/Hardware Authority interaction.
