from .variance_engine import VarianceEngine

class SensitivityEngine:
    """
    Evaluates sensitivity parameters by measuring output swings under minor input modifications.
    """
    def __init__(self):
        self.variance_eng = VarianceEngine()

    def evaluate_sensitivity(self, base_outputs: list, perturbed_outputs: list) -> float:
        """
        Measures the absolute sensitivity of outputs.
        """
        if not base_outputs or not perturbed_outputs:
            return 0.0
        m1 = self.variance_eng.calculate_mean(base_outputs)
        m2 = self.variance_eng.calculate_mean(perturbed_outputs)
        if m1 == 0.0:
            return 0.0
        return round(abs(m1 - m2) / abs(m1), 4)
