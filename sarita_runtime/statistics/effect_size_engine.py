import math
from .variance_engine import VarianceEngine

class EffectSizeEngine:
    """
    Computes statistical Cohen's d effect sizes between experimental and baseline groups.
    """
    def __init__(self):
        self.variance_eng = VarianceEngine()

    def calculate_cohens_d(self, group1: list, group2: list) -> float:
        """
        Calculates Cohen's d.
        Formula: (mean1 - mean2) / pooled_std_dev
        """
        n1, n2 = len(group1), len(group2)
        if n1 < 2 or n2 < 2:
            return 0.0

        mean1 = self.variance_eng.calculate_mean(group1)
        mean2 = self.variance_eng.calculate_mean(group2)

        var1 = self.variance_eng.calculate_variance(group1)
        var2 = self.variance_eng.calculate_variance(group2)

        pooled_var = ((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2)
        if pooled_var <= 0.0:
            return 0.0

        pooled_std = math.sqrt(pooled_var)
        return round((mean1 - mean2) / pooled_std, 4)
