import time
from typing import Any
from sarita_runtime.kernel.evidence_fabric.runtime_evidence_registry import RuntimeEvidenceRegistry

class PhysicalActionRecorder:
    def __init__(self, registry: RuntimeEvidenceRegistry):
        self.registry = registry
    def record_action(self, action_name: str, resource: str, params: dict, result: Any):
        metadata = {"perf_timestamp": time.perf_counter(), "params": params, "raw_result": str(result)}
        return self.registry.register_physical_event(resource, action_name, "SUCCESS" if result is not None else "FAILURE", metadata)
