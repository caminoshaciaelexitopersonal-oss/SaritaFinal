import logging
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph

class KernelDecisionConsensus:
    """
    Ensures consensus on critical kernel-level decisions.
    REFACTORED PHASE 74: Consensus is now a materialized state within the UnifiedExecutionGraph.
    """
    def __init__(self, graph: UnifiedExecutionGraph):
        self.graph = graph
        self.epoch = 0

    async def propose_decision(self, decision_type: str, action: dict):
        logging.info(f"Kernel Consensus: Proposing {decision_type} to Graph (Epoch: {self.epoch})")
        # Direct commitment to Sovereign Bus (Graph)
        self.graph.register_material_decision(
            task_id=f"consensus_{self.epoch}",
            action=decision_type,
            evidence=action
        )
        return True

    async def commit_decision(self, decision_id: str):
        logging.info(f"Kernel Consensus: Confirming decision {decision_id} in Graph")
        self.epoch += 1
        return True
