import logging
import os
from sarita_runtime.kernel.io_uring_fabric.io_uring_execution_engine import IoUringExecutionEngine
from sarita_runtime.kernel.hardware_authority.physical_resource_authority import PhysicalResourceAuthority
from sarita_runtime.kernel.evidence_fabric.runtime_evidence_registry import RuntimeEvidenceRegistry
from sarita_runtime.kernel.evidence_fabric.physical_action_recorder import PhysicalActionRecorder
from sarita_runtime.kernel.hardware_authority.hardware_observability_engine import HardwareObservabilityEngine

class SovereignEnforcementFabric:
    """
    Consolidated Sovereign Enforcement Fabric (Phase 73/76/77).
    """
    def __init__(self, nervous_system):
        self.graph = nervous_system

        # Evidence Plane
        self.evidence_registry = RuntimeEvidenceRegistry(nervous_system)
        self.recorder = PhysicalActionRecorder(self.evidence_registry)

        # IO Engine
        self.io_engine = IoUringExecutionEngine()
        self.io_engine.initialize_material_rings()

        # Hardware Authority & Observability
        self.hardware_authority = PhysicalResourceAuthority(nervous_system)
        self.obs_engine = HardwareObservabilityEngine(self.recorder)
        self.hardware_authority.set_observability_engine(self.obs_engine)

        self.cgroup_base = "/sys/fs/cgroup/sarita_governance"

    def claim_hardware_path(self, device_id: str, irq_id: int, cpu_id: int):
        self.recorder.record_action("START_PATH_CLAIM", device_id, {"irq": irq_id}, "PENDING")
        self.hardware_authority.claim_irq_ownership(irq_id, cpu_id)
        self.hardware_authority.allocate_dma_channel(1, cpu_id)
        self.recorder.record_action("COMPLETE_PATH_CLAIM", device_id, {"irq": irq_id}, "SUCCESS")
        return True

    def materialize_memory_allocation(self, pid: int, numa_node: int):
        self.hardware_authority.set_numa_affinity(pid, numa_node)
        return True

    def audit_physical_pressure(self):
        metrics = self._get_psi_metrics()
        self.recorder.record_action("AUDIT_PRESSURE", "system", {}, metrics)
        return {"psi": metrics}

    def _get_psi_metrics(self):
        return {"cpu": "some=0.0 avg10=0.0 avg60=0.0 avg300=0.0 total=0"}

    def execute_material_io(self, task_id: str, op_type: str, params: dict = None):
        self.graph.emit_event(task_id, "IO_SUBMISSION", {"type": op_type, "params": params or {}})
        res = self.io_engine.submit_and_wait(1)
        self.graph.emit_event(task_id, "IO_COMPLETION", {"result": res})
        return res
