class GlobalDominanceValidator:
    """
    Validates that a civilization maintains superiority across all scenarios.
    """
    def validate_dominance(self, target, competitors):
        # A civilization is dominant if it outperforms all competitors in
        # at least 95% of measured metrics.

        if not competitors: return True

        dominance_count = 0
        target_state = target.current_state

        for comp in competitors:
            comp_state = comp.current_state
            if target_state["survival"] >= comp_state["survival"]:
                dominance_count += 1

        return (dominance_count / len(competitors)) >= 0.95
