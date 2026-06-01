import logging
from typing import Dict, List, Any
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph

class PhysicalResourceAuthority:
    """
    Sovereign Physical Resource Authority (Phase 74).
    Single point of governance for IRQ, DMA, NUMA, and CPU Affinity.
    IMPLEMENTED AS SINGLETON per Nervous System.
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
        self._initialized = True

    def claim_irq_ownership(self, irq_id: int, owner_pid: int):
        logging.info(f"Hardware Authority: Assigning IRQ {irq_id} to PID {owner_pid}")
        self.irq_assignments[irq_id] = owner_pid
        self.graph.update_ownership(f"IRQ_{irq_id}", str(owner_pid))
        return True

    def allocate_dma_channel(self, channel_id: int, owner_pid: int):
        logging.info(f"Hardware Authority: Allocating DMA Channel {channel_id} to PID {owner_pid}")
        self.dma_ownership[channel_id] = owner_pid
        self.graph.update_ownership(f"DMA_{channel_id}", str(owner_pid))
        return True

    def set_numa_affinity(self, pid: int, node_id: int):
        logging.info(f"Hardware Authority: Pinning PID {pid} to NUMA Node {node_id}")
        self.numa_policy[pid] = node_id
        self.graph.register_material_decision(
            task_id=f"numa_{pid}",
            action="SET_NUMA_AFFINITY",
            evidence={"node": node_id}
        )
        return True

    def enforce_cpu_affinity(self, pid: int, cpus: List[int]):
        logging.info(f"Hardware Authority: Enforcing CPU Affinity {cpus} for PID {pid}")
        self.cpu_affinities[pid] = cpus
        return True

    def get_physical_topology(self):
        return {
            "irq": self.irq_assignments,
            "dma": self.dma_ownership,
            "numa": self.numa_policy,
            "cpu": self.cpu_affinities
        }
