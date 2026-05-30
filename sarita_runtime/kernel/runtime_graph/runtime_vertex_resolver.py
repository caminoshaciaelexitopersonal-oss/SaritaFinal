import logging

class RuntimeVertexResolver:
    """
    Physical vertex resolver.
    Consolidates causal dependencies exclusively via UnifiedExecutionGraph.
    """
    def __init__(self, nervous_system):
        self.nervous_system = nervous_system

    def is_vertex_ready(self, task_id: str):
        # Decisions originate exclusively from the graph
        return self.nervous_system.resolve_absolute_causality(task_id)
