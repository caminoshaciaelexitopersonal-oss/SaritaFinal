class HorizonReliabilityEngine:
    """
    Evaluates the reliability of predictions at various future distances.
    """
    def evaluate_reliability(self, horizon):
        """
        Returns a reliability score (0.0 - 1.0) for a given horizon.
        """
        # Reliability decreases with distance
        if horizon <= 100: return 0.98
        if horizon <= 200: return 0.95
        if horizon <= 500: return 0.80
        return 0.50
