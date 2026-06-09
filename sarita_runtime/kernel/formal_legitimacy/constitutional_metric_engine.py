import math

class ConstitutionalMetricEngine:
    """
    Universal engine for quantifying constitutional performance and stability.
    Ensures all metrics are normalized between 0.0000 and 1.0000.
    """

    @staticmethod
    def normalize(value: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
        if max_val == min_val:
            return 1.0
        normalized = (value - min_val) / (max_val - min_val)
        return float(max(0.0, min(1.0, normalized)))

    def calculate_aggregate_legitimacy(self, metrics: list) -> float:
        """
        Calculates a weighted geometric mean of various legitimacy components.
        """
        if not metrics:
            return 0.0

        product = 1.0
        for m in metrics:
            product *= max(0.0001, m) # Avoid zero to keep geometric mean valid

        return float(round(product ** (1.0 / len(metrics)), 4))

    def calculate_entropy_penalty(self, drift_factor: float) -> float:
        """
        Calculates a penalty score based on constitutional drift.
        """
        return float(round(math.exp(-drift_factor), 4))
