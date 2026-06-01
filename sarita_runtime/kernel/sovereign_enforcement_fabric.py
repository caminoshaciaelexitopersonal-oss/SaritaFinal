import logging
import os
from sarita_runtime.kernel.io_uring_fabric.io_uring_execution_engine import IoUringExecutionEngine
from sarita_runtime.kernel.hardware_authority.physical_resource_authority import PhysicalResourceAuthority

class SovereignEnforcementFabric:
    """
    Consolidated Sovereign Enforcement Fabric (Phase 73).
    REFACTORED PHASE 74: Delegating hardware authority to PhysicalResourceAuthority.
    """
    def __init__(self, nervous_system):
        self.graph = nervous_system
        self.io_engine = IoUringExecutionEngine()
        self.io_engine.initialize_material_rings()
        self.hardware_authority = PhysicalResourceAuthority(nervous_system)
        self.cgroup_base = "/sys/fs/cgroup/sarita_governance"

    # --- Hardware Ownership ---
    def claim_hardware_path(self, device_id: str, irq_id: int, cpu_id: int):
        logging.info(f"Enforcement: Delegating path claim for {device_id} to Hardware Authority")
        self.hardware_authority.claim_irq_ownership(irq_id, cpu_id) # cpu_id used as owner here for simplicity
        self.hardware_authority.allocate_dma_channel(1, cpu_id) # Assuming channel 1
        return True

    # --- Memory Authority ---
    def materialize_memory_allocation(self, pid: int, numa_node: int):
        logging.info(f"Enforcement: Delegating memory allocation for PID {pid} to Hardware Authority")
        self.hardware_authority.set_numa_affinity(pid, numa_node)
        return True

    def audit_physical_pressure(self):
        return {"psi": self._get_psi_metrics()}

    def _get_psi_metrics(self):
        metrics = {}
        try:
            for resource in ["cpu", "memory", "io"]:
                path = f"/proc/pressure/{resource}"
                if os.path.exists(path):
                    with open(path, "r") as f:
                        metrics[resource] = f.read().strip()
        except Exception:
            logging.error(f"Enforcement: Critical failure accessing PSI metrics")
        return metrics

    # --- IO Pipeline ---
    def execute_material_io(self, task_id: str, op_type: str, params: dict):
        logging.info(f"Enforcement: Materializing IO {op_type} for vertex {task_id}")
        self.graph.register_material_decision(task_id, "IO_SUBMISSION", {"type": op_type})

        res = self.io_engine.submit_and_wait(1)

        self.graph.register_material_decision(task_id, "IO_COMPLETION", {"result": res})
        return res
