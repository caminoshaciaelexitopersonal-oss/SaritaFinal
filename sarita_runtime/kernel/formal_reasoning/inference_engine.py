class InferenceEngine:
    """
    Orchestrates formal reasoning and conclusion derivation.
    """
    def __init__(self, reasoner, premise_validator, conclusion_deriver):
        self.reasoner = reasoner
        self.premise_validator = premise_validator
        self.conclusion_deriver = conclusion_deriver

    def infer(self, premises, goal):
        """
        Attempts to infer the goal from the given premises.
        """
        valid_premises = [p for p in premises if self.premise_validator.validate(p)]
        return self.reasoner.derive(valid_premises, goal)
