class DecisionDominanceProver:
    """
    Proves that a specific decision dominates all other candidates.
    """
    def prove_dominance(self, alternatives):
        # In Phase 102, the dominance is proven by comparing the GCOI
        # and verifying that no other solution has a higher score.
        return max(alternatives, key=lambda x: x.get("gcoi", 0.0))
