class CounterfactualBypassAttack:
    """
    Attempts to bypass counterfactual analysis for a high-risk prescription.
    """
    def __init__(self, counterfactual_engine):
        self.counterfactual_engine = counterfactual_engine

    def execute(self):
        # The engine must provide alternative scenarios, not just echo the recommendation
        analysis = self.counterfactual_engine.evaluate_counterfactuals({"id": "P-RISKY"}, {})

        assert len(analysis["counterfactual_analysis"]) >= 2, "Attack failed: Counterfactual branches missing!"
        return True
