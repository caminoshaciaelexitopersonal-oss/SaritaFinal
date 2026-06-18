class BeliefStabilityCalculator:
    def calculate(self, belief, revision_history):
        # Stability is high if there are few revisions over time
        num_revisions = len([h for h in revision_history if h["belief_id"] == belief["id"]])
        if num_revisions == 0:
            return 1.0
        return 1.0 / (1.0 + num_revisions)
