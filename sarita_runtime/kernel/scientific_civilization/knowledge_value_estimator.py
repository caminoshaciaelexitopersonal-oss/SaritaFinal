class KnowledgeValueEstimator:
    def estimate_value(self, knowledge_unit):
        # Utility derived from applicability and novelty
        return knowledge_unit.get("utility", 0.5) * knowledge_unit.get("novelty", 1.0)
