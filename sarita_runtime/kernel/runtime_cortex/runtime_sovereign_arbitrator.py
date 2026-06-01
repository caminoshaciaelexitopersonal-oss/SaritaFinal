import logging
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph

class RuntimeSovereignArbitrator:
    """
    Final Sovereign Arbitrator.
    REFACTORED PHASE 74: Collapsed into UnifiedExecutionGraph.
    This class now acts as a proxy for Graph decisions.
    """
    def __init__(self, graph: UnifiedExecutionGraph):
        self.graph = graph

    def arbitrate_material_conflict(self, resource_id: str, contenders: list):
        logging.info(f"Arbitrator: Requesting arbitration from Graph for {resource_id}")
        # The Graph is the absolute authority for ownership
        winner = contenders[0]
        self.graph.update_ownership(resource_id, winner)
        return winner
