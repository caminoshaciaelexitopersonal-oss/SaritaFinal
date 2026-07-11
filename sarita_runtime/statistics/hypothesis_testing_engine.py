import math
from .variance_engine import VarianceEngine
from .significance_engine import SignificanceEngine

class HypothesisTestingEngine:
    """
    Performs independent samples Student's t-tests.
    """
    def __init__(self):
        self.variance_eng = VarianceEngine()
        self.significance_eng = SignificanceEngine()

    def run_t_test(self, group1: list, group2: list) -> dict:
        """
        Runs an independent samples t-test.
        """
        n1, n2 = len(group1), len(group2)
        if n1 < 2 or n2 < 2:
            return {"t_stat": 0.0, "p_value": 1.0, "significant": False}

        mean1 = self.variance_eng.calculate_mean(group1)
        mean2 = self.variance_eng.calculate_mean(group2)

        var1 = self.variance_eng.calculate_variance(group1)
        var2 = self.variance_eng.calculate_variance(group2)

        denom = math.sqrt((var1 / n1) + (var2 / n2))
        if denom == 0.0:
            return {"t_stat": 0.0, "p_value": 1.0, "significant": False}

        t_stat = (mean1 - mean2) / denom
        df = n1 + n2 - 2

        p_val = self.significance_eng.estimate_p_value(t_stat, df)

        return {
            "t_stat": round(t_stat, 4),
            "p_value": round(p_val, 4),
            "significant": p_val < 0.05
        }
