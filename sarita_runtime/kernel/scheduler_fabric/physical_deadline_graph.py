import logging

class PhysicalDeadlineGraph:
    """
    Graph of physical deadlines for the causal scheduler.
    """
    def __init__(self):
        self.deadlines = {}

    def set_deadline(self, vertex_id: str, deadline_ns: int):
        self.deadlines[vertex_id] = deadline_ns

    def get_earliest_deadline(self, active_vertices: list):
        # Return vertex with smallest deadline
        return min(active_vertices, key=lambda v: self.deadlines.get(v, float('inf')))
