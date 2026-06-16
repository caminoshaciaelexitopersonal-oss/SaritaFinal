class FutureFeasibilityValidator:
    """
    Validates the feasibility of a future architecture and its transition plan.
    """
    def validate_feasibility(self, design, plan):
        """
        Checks if the design is reachable and stable.
        """
        # Feasibility depends on design robustness and plan depth
        if not design or not plan:
            return False

        return design.get("robustness", 0) > 0.90 and len(plan) >= 3
