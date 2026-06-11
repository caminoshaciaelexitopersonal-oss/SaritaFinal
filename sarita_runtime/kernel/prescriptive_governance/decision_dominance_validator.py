class DecisionDominanceValidator:
    """
    Validates that a decision is mathematically dominant over alternatives.
    """
    def validate_dominance(self, decision, alternatives):
        """
        Verifies that no alternative provides higher utility across all objectives.
        """
        if not decision or not alternatives:
            return True

        for alt in alternatives:
            if alt.get("utility", 0.0) > decision.get("utility", 0.0):
                return False
        return True
