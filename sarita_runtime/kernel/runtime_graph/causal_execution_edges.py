import logging

class CausalExecutionEdges:
    """
    Manages causal links and physical dependencies in the execution graph.
    """
    def __init__(self):
        self.edges = {} # Dependent -> [Parents]

    def register_dependency(self, parent_id: str, dependent_id: str):
        if dependent_id not in self.edges:
            self.edges[dependent_id] = []
        self.edges[dependent_id].append(parent_id)
        logging.info(f"Causal Edges: Linked {dependent_id} to parent {parent_id}")

    def get_parents(self, task_id: str):
        return self.edges.get(task_id, [])
