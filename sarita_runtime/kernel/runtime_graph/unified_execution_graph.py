import logging
from typing import Dict, Any, List
from sarita_runtime.kernel.runtime_graph.physical_execution_vertex import PhysicalExecutionVertex

class UnifiedExecutionGraph:
    """
    Runtime Nervous System (Phase 69).
    Causal scheduler and absolute ownership authority.
    """
    def __init__(self):
        self.vertices = {}
        self.ownership_matrix = {}
        self.pressure_index = 0.0

    def register_material_execution(self, task_id: str, payload: Dict[str, Any]):
        logging.info(f"Nervous System: Registering Task {task_id}")
        vertex = PhysicalExecutionVertex(task_id, payload)
        self.vertices[task_id] = vertex

        # Phase 69: Register physical ownership immediately
        if "cpu_affinity" in payload:
            self.assign_physical_ownership(f"CPU-{payload['cpu_affinity']}", task_id)

        return vertex

    def assign_physical_ownership(self, resource_id: str, owner_id: str):
        logging.info(f"Nervous System: Resource {resource_id} owned by {owner_id}")
        self.ownership_matrix[resource_id] = owner_id

    def get_vertex(self, task_id: str):
        return self.vertices.get(task_id)

    def resolve_causal_readiness(self, task_id: str):
        """
        Material causal resolution.
        Returns True if all dependencies are COMPLETED.
        """
        vertex = self.get_vertex(task_id)
        if not vertex: return False

        for dep_id in vertex.dependencies:
            dep = self.get_vertex(dep_id)
            if not dep or dep.status != "COMPLETED":
                return False
        return True
