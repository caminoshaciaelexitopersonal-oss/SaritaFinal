class ConstitutionalReturnEstimator:
    """
    Estimates the "Constitutional Return" of a proposed reform or action.
    """
    def estimate_return(self, proposed_action: dict):
        # Return = Stability Improvement / Complexity Increase
        stability_gain = proposed_action.get("expected_stability", 0.1)
        complexity_cost = proposed_action.get("complexity_cost", 0.05)

        if complexity_cost <= 0:
            return stability_gain
        return stability_gain / complexity_cost
