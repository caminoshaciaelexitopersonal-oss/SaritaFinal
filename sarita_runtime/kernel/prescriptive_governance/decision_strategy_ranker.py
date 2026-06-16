class DecisionStrategyRanker:
    """
    Ranks potential governance decisions based on multiple criteria.
    """
    def rank_decisions(self, decisions):
        """
        Orders decisions from most to least dominant.
        """
        return sorted(decisions, key=lambda x: x.get("utility", 0.0), reverse=True)
