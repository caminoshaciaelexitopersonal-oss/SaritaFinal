class AdaptiveSelectionValidator:
    """
    Validates that selection decisions are adaptive and not regressive.
    """
    def validate_selection(self, p_s_after: float, p_s_before: float):
        # Never select a trajectory that decreases survival probability
        return p_s_after >= p_s_before
