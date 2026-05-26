import logging
from typing import Dict, Any, List
from sarita_runtime.kernel.runtime_graph.physical_execution_vertex import PhysicalExecutionVertex

class UnifiedExecutionGraph:
    """
    Runtime Nervous System (Phase 70).
    Central authority for physical execution and ownership.
    """
    def __init__(self):
        self.vertices = {}
        self.ownership_matrix = {}
        self.global_pressure_score = 0.0

    def register_material_execution(self, task_id: str, payload: Dict[str, Any]):
        logging.info(f"Nervous System: Materializing Task {task_id}")
        vertex = PhysicalExecutionVertex(task_id, payload)
        self.vertices[task_id] = vertex

        # Immediate resource ownership claim
        if "cpu" in payload:
            self.ownership_matrix[f"CPU-{payload['cpu']}"] = task_id

        return vertex

    def update_global_pressure(self, score: float):
        self.global_pressure_score = score
        logging.info(f"Nervous System: Assimilated physical pressure score: {score:.2f}")

    def resolve_physical_dependency(self, task_id: str):
        vertex = self.vertices.get(task_id)
        if not vertex: return False
        return all(self.vertices[d].status == "COMPLETED" for d in vertex.dependencies if d in self.vertices)

    def get_vertex(self, task_id: str):
        return self.vertices.get(task_id)
