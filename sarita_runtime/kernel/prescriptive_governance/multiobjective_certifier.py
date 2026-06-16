class MultiobjectiveCertifier:
    """
    Certifies decisions across efficiency, benefit, risk, cost, and impact.
    """
    def certify_objectives(self, candidate):
        """
        Validates that a candidate meets minimum criteria for all objectives.
        """
        objectives = ["efficiency", "benefit", "risk_inv", "cost_inv", "impact"]
        for obj in objectives:
            if candidate.get(obj, 0.0) < 0.5: # Threshold
                return False
        return True
