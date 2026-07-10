import time

class KnowledgeHistory:
    """
    Tracks and records the exact history of knowledge mutations, nodes, and relationships.
    """
    def __init__(self):
        self.mutations = []

    def record_mutation(self, mutation_type: str, node_id: str, diff: dict):
        self.mutations.append({
            "timestamp": time.time(),
            "mutation_type": mutation_type,
            "node_id": node_id,
            "diff": diff
        })
