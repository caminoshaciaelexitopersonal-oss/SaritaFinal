class StrategicTradeoffEngine:
    """
    Calculates and justifies strategic tradeoffs (e.g., sacrificing Performance for Security).
    """
    def calculate_tradeoff(self, target_gain: float, sacrifice_cost: float):
        ratio = target_gain / sacrifice_cost if sacrifice_cost > 0 else 100.0
        return ratio > 1.2 # Must have at least 20% net benefit
