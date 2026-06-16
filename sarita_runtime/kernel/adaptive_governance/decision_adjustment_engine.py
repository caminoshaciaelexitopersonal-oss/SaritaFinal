class DecisionAdjustmentEngine:
    """
    Adjusts governance decisions automatically based on feedback.
    """
    def adjust_decision(self, decision, error_delta):
        """
        Modifies a decision's parameters to reduce error relative to goal.
        """
        adjusted = decision.copy()
        adjusted["utility"] += error_delta * 0.1
        return adjusted
