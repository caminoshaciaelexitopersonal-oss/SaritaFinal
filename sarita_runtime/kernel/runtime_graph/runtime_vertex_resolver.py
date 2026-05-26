import logging

class RuntimeVertexResolver:
    """
    Resolves physical dependencies for execution graph vertices.
    """
    def __init__(self, nervous_system):
        self.nervous_system = nervous_system

    def is_vertex_ready(self, task_id: str):
        vertex = self.nervous_system.get_vertex(task_id)
        if not vertex: return False
        # Phase 71: Material dependency resolution
        return all(self.nervous_system.get_vertex(d).status == "COMPLETED" for d in vertex.dependencies if self.nervous_system.get_vertex(d))
