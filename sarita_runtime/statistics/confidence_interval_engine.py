import math
from .variance_engine import VarianceEngine
from .uncertainty_engine import UncertaintyEngine

class ConfidenceIntervalEngine:
    """
    Computes standard confidence intervals (e.g. 95%) of sample data.
    """
    def __init__(self):
        self.variance_eng = VarianceEngine()
        self.uncertainty_eng = UncertaintyEngine()

    def calculate_95_ci(self, data: list) -> tuple:
        """
        Calculates standard 95% Confidence Interval using a z-score of 1.96.
        """
        if not data:
            return (0.0, 0.0)
        mean = self.variance_eng.calculate_mean(data)
        std_err = self.uncertainty_eng.calculate_standard_error(data)
        margin = 1.96 * std_err
        return (round(mean - margin, 4), round(mean + margin, 4))
