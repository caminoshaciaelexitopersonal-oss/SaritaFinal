import logging
from typing import Dict, Any, List
from sarita_runtime.kernel.runtime_graph.physical_execution_vertex import PhysicalExecutionVertex

class UnifiedExecutionGraph:
    """
    Unified Execution Graph (Phase 72).
    Sovereign Bus and absolute system nervous system.
    Eliminates all local caches and duplicate states outside the graph.
    """
    def __init__(self):
        self.vertices = {}
        # Absolute physical state stored in the graph
        self.physical_ownership = {} # resource_id -> vertex_id
        self.causal_pressure = 0.0
        self.global_deadlines = {}
        self.irq_lineage = {}
        self.dma_lineage = []

    def register_material_vertex(self, task_id: str, payload: Dict[str, Any]):
        logging.info(f"Sovereign Bus: Registering Vertex {task_id}")
        vertex = PhysicalExecutionVertex(task_id, payload)
        self.vertices[task_id] = vertex
        return vertex

    def update_physical_state(self, resource: str, owner_id: str):
        logging.debug(f"Sovereign Bus: Updating ownership {resource} -> {owner_id}")
        self.physical_ownership[resource] = owner_id

    def get_vertex(self, task_id: str):
        return self.vertices.get(task_id)

    def resolve_absolute_causality(self, task_id: str):
        vertex = self.vertices.get(task_id)
        if not vertex: return False
        # Absolute dependency resolution from material status
        return all(self.vertices[d].status == "COMPLETED" for d in vertex.dependencies if d in self.vertices)
