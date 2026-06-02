import logging
from typing import Dict, Any
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph

class RuntimeEvidenceRegistry:
    def __init__(self, graph: UnifiedExecutionGraph):
        self.graph = graph
    def register_physical_event(self, resource: str, action: str, result: str, metadata: dict = None):
        payload = {"resource": resource, "action": action, "result": result, "metadata": metadata or {}}
        self.graph.emit_event(f"res_{resource}", action, payload)
        return "event_observed"
