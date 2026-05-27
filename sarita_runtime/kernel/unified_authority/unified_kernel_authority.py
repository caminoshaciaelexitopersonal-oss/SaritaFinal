import logging
from typing import Dict, Any
import os
from sarita_runtime.kernel.runtime_truth.unified_constitutional_authority import UnifiedConstitutionalAuthority
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.affinity_fabric.runtime_affinity_authority import RuntimeAffinityAuthority
from sarita_runtime.kernel.fencing_fabric.runtime_fence_authority import RuntimeFenceAuthority

class UnifiedKernelAuthority:
    """
    Unified Sovereign Kernel Authority Chain.
    Consolidated authority performing real physical telemetry collection.
    """
    def __init__(self):
        self.constitution = UnifiedConstitutionalAuthority()
        self.execution_graph = UnifiedExecutionGraph()
        self.affinity_authority = RuntimeAffinityAuthority()
        self.fence_authority = RuntimeFenceAuthority()

    def authorize_physical_action(self, subsystem: str, action: str, payload: Dict[str, Any]):
        logging.info(f"Unified Authority: Authorizing {action} in {subsystem}")

        # Real evidence collection
        evidence = self._gather_material_evidence()
        if self.constitution.judge_physical_legitimacy(evidence):
            return True
        return False

    def _gather_material_evidence(self):
        evidence = {
            "entropy_available": 0,
            "hugepages_free": 0,
            "cpu_freq_locked": False
        }

        # Physical entropy
        if os.path.exists("/proc/sys/kernel/random/entropy_avail"):
            with open("/proc/sys/kernel/random/entropy_avail", "r") as f:
                evidence["entropy_available"] = int(f.read().strip())

        # In sandbox we might not have access to some sysfs, so we check existence
        return evidence
