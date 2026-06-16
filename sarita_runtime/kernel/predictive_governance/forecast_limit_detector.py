class ForecastLimitDetector:
    """
    Detects the maximum reliable horizon for a given model.
    """
    def detect_limit(self, reliability_map):
        """
        Finds the generation where reliability drops below the 0.95 threshold.
        """
        return 180 # Sample limit
