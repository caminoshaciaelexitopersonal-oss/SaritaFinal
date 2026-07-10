import math
from .variance_engine import VarianceEngine

class UncertaintyEngine:
    """
    Measures experimental uncertainties, entropy, and standard errors.
    """
    def __init__(self):
        self.variance_eng = VarianceEngine()

    def calculate_standard_error(self, data: list) -> float:
        if len(data) < 2:
            return 0.0
        std_dev = self.variance_eng.calculate_std_dev(data)
        return std_dev / math.sqrt(len(data))

    def calculate_entropy(self, probabilities: list) -> float:
        """
        Calculates Shannon entropy of a probability distribution.
        """
        ent = 0.0
        for p in probabilities:
            if p > 0.0:
                ent -= p * math.log2(p)
        return ent
