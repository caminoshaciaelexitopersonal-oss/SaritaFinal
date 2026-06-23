class CausalDecisionReconstructor:
    """Reconstructs the causal context of a specific decision."""
    def reconstruct_decision(self, decision_id):
        return {"id": decision_id, "evidence": ["link_1", "link_2"]}
