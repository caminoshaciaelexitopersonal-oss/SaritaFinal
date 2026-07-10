from .cosmos_birth_engine import CosmosBirthEngine
from .cosmos_divergence_engine import CosmosDivergenceEngine
from .cosmos_extinction_engine import CosmosExtinctionEngine

class MetaCosmogenesisEngine:
    """
    Main orchestrator for Phase 127.2 - Meta-Cosmogenesis.
    Coordinates birth, divergence, and extinction of multiple cosmos.
    """
    def __init__(self):
        self.birth_engine = CosmosBirthEngine()
        self.divergence_engine = CosmosDivergenceEngine()
        self.extinction_engine = CosmosExtinctionEngine()
        self.active_cosmos = {}
        self.lineage_registry = {}

    def spawn_cosmos(self, count=1, parent_id=None):
        parent = self.active_cosmos.get(parent_id) if parent_id else None
        new_cosmos_list = []

        for _ in range(count):
            cosmos = self.birth_engine.initiate_birth(parent=parent)
            cid = cosmos["identity"]["id"]
            self.active_cosmos[cid] = cosmos
            new_cosmos_list.append(cosmos)

            # Register lineage
            self.lineage_registry[cid] = {
                "parent": parent_id,
                "children": []
            }
            if parent_id in self.lineage_registry:
                self.lineage_registry[parent_id]["children"].append(cid)

        return new_cosmos_list

    def step_evolution(self):
        """
        Advances age and potentially triggers divergence or extinction.
        """
        to_extinguish = []
        for cid, cosmos in self.active_cosmos.items():
            cosmos["age"] += 1

            # Simple extinction check
            if not self.extinction_engine.is_viable(cosmos):
                to_extinguish.append(cid)

        results = []
        for cid in to_extinguish:
            cosmos = self.active_cosmos.pop(cid)
            results.append(self.extinction_engine.execute_extinction(cosmos, "INVIABLE_GENOME"))

        return results

    def get_multiverse_metrics(self):
        if not self.active_cosmos:
            return {"diversity": 0.0, "count": 0}

        cosmos_ids = list(self.active_cosmos.keys())
        total_divergence = 0
        comparisons = 0

        for i in range(len(cosmos_ids)):
            for j in range(i + 1, len(cosmos_ids)):
                total_divergence += self.divergence_engine.calculate_divergence(
                    self.active_cosmos[cosmos_ids[i]],
                    self.active_cosmos[cosmos_ids[j]]
                )
                comparisons += 1

        return {
            "diversity": total_divergence / comparisons if comparisons > 0 else 1.0,
            "count": len(self.active_cosmos)
        }
