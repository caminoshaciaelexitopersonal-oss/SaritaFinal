import logging
from typing import Dict, Any, List
from sarita_runtime.kernel.runtime_graph.physical_execution_vertex import PhysicalExecutionVertex

class UnifiedExecutionGraph:
    """
    Unified Execution Graph.
    Única fuente de verdad operacional.
    Toda autoridad emite evidencia al grafo.
    """
    def __init__(self):
        self.vertices = {}
        self.active_epoch = 0

    def register_material_execution(self, task_id: str, payload: Dict[str, Any]):
        logging.info(f"Execution Graph: REGISTERING material execution {task_id}")
        vertex = PhysicalExecutionVertex(task_id, payload)
        self.vertices[task_id] = vertex
        return vertex

    def validate_deterministic_lineage(self, task_id: str):
        vertex = self.vertices.get(task_id)
        if not vertex: return False

        # Cross-reference physical evidence from vertex
        return vertex.status != "ERROR"

    def get_vertex(self, task_id: str):
        return self.vertices.get(task_id)
