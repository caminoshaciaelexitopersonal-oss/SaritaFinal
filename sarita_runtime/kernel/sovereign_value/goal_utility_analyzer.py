class GoalUtilityAnalyzer:
    """
    Analyzes the utility of registered sovereign goals.
    """
    def analyze_utility(self, goal_id: str, historical_impact: float):
        # Utility is a function of historical impact and strategic relevance
        base_utility = 0.5
        relevance_bonus = 0.3
        return base_utility + historical_impact + relevance_bonus
