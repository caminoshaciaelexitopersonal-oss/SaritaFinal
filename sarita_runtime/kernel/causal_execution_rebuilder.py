import logging

class CausalExecutionRebuilder:
    """
    Rebuilds execution history based on causal vertices and physical telemetry.
    """
    def __init__(self, graph):
        self.graph = graph

    def rebuild_lineage(self, root_task_id: str):
        logging.info(f"Execution Rebuilder: Rebuilding material lineage for {root_task_id}")
        return self.graph.get_causal_ancestors(root_task_id)
