from .variance_engine import VarianceEngine

class RobustnessEngine:
    """
    Evaluates robustness indexes of active system components under noise sweeps.
    """
    def __init__(self):
        self.variance_eng = VarianceEngine()

    def calculate_robustness_score(self, performance_array: list) -> float:
        """
        Robustness score is high (near 1.0) if variance is extremely low.
        Formula: 1.0 / (1.0 + standard_deviation)
        """
        if not performance_array:
            return 0.0
        std_dev = self.variance_eng.calculate_std_dev(performance_array)
        return round(1.0 / (1.0 + std_dev), 4)
