class OptimalityScoreCalculator:
    """
    Calculates the Global Constitutional Optimality Index (GCOI).
    """
    def calculate_gcoi(self, metrics: dict) -> float:
        """
        GCOI = weighted average of core pillars.
        All inputs must be 0.0 to 1.0.
        """
        weights = {
            "legitimacy": 0.3,
            "survival": 0.2,
            "value": 0.2,
            "identity": 0.15,
            "governance": 0.15
        }

        gcoi = 0.0
        for key, weight in weights.items():
            val = float(metrics.get(key, 0.0))
            # Ensure normalization
            val = max(0.0, min(1.0, val))
            gcoi += val * weight

        return float(round(gcoi, 4))
