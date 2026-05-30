import logging
import os
from sarita_runtime.kernel.io_uring_fabric.io_uring_execution_engine import IoUringExecutionEngine

class SovereignEnforcementFabric:
    """
    Consolidated Sovereign Enforcement Fabric (Phase 73).
    Single Authority for physical IO, Memory, and Hardware Ownership.
    Collapses previous Memory Plane, IO Fabric, and Interrupt Fabric.
    """
    def __init__(self, nervous_system):
        self.graph = nervous_system
        self.io_engine = IoUringExecutionEngine()
        self.io_engine.initialize_material_rings()
        self.cgroup_base = "/sys/fs/cgroup/sarita_governance"

    # --- Hardware Ownership ---
    def claim_hardware_path(self, device_id: str, irq_id: int, cpu_id: int):
        logging.info(f"Enforcement: Locking Path {device_id} -> IRQ {irq_id} -> CPU {cpu_id}")
        self.graph.update_ownership(f"IRQ-{irq_id}", f"CPU-{cpu_id}")
        self.graph.update_ownership(f"DMA-{device_id}", f"CPU-{cpu_id}")
        return True

    # --- Memory Authority ---
    def materialize_memory_allocation(self, pid: int, numa_node: int):
        logging.info(f"Enforcement: Materializing memory for PID {pid} on NUMA {numa_node}")
        self.graph.update_ownership(f"MEM-PID-{pid}", f"NUMA-{numa_node}")
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
