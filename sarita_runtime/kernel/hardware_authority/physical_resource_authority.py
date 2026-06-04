import logging
from typing import Dict, List, Any
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.hardware_authority.hardware_observability_engine import HardwareObservabilityEngine

class PhysicalResourceAuthority:
    """
    Sovereign Physical Resource Authority (Phase 74/76/77).
    """
    _instances = {}

    def __new__(cls, graph: UnifiedExecutionGraph):
        if graph not in cls._instances:
            cls._instances[graph] = super(PhysicalResourceAuthority, cls).__new__(cls)
            cls._instances[graph]._initialized = False
        return cls._instances[graph]

    def __init__(self, graph: UnifiedExecutionGraph):
        if self._initialized:
            return
        self.graph = graph
        self.irq_assignments = {}
        self.dma_ownership = {}
        self.numa_policy = {}
        self.cpu_affinities = {}
        self.observability = None
        self._initialized = True

    def set_observability_engine(self, engine: HardwareObservabilityEngine):
        self.observability = engine

    def claim_irq_ownership(self, irq_id: int, owner_pid: int):
        before = self.irq_assignments.get(irq_id)
        self.irq_assignments[irq_id] = owner_pid
        self.graph.update_ownership(f"IRQ_{irq_id}", str(owner_pid))
        if self.observability:
            self.observability.observe_transition("IRQ", irq_id, before, owner_pid, owner_pid)
        return True

    def allocate_dma_channel(self, channel_id: int, owner_pid: int):
        before = self.dma_ownership.get(channel_id)
        self.dma_ownership[channel_id] = owner_pid
        self.graph.update_ownership(f"DMA_{channel_id}", str(owner_pid))
        if self.observability:
            self.observability.observe_transition("DMA", channel_id, before, owner_pid, owner_pid)
        return True

    def set_numa_affinity(self, pid: int, node_id: int):
        before = self.numa_policy.get(pid)
        self.numa_policy[pid] = node_id
        self.graph.emit_event(f"numa_{pid}", "SET_NUMA_AFFINITY", {"node": node_id})
        if self.observability:
            self.observability.observe_transition("NUMA", pid, before, node_id, node_id)
        return True

    def enforce_cpu_affinity(self, pid: int, cpus: List[int]):
        before = self.cpu_affinities.get(pid)
        self.cpu_affinities[pid] = cpus
        if self.observability:
            self.observability.observe_transition("CPU", pid, before, cpus, cpus)
        return True

    def get_physical_topology(self):
        return {
            "irq": self.irq_assignments,
            "dma": self.dma_ownership,
            "numa": self.numa_policy,
            "cpu": self.cpu_affinities
        }
