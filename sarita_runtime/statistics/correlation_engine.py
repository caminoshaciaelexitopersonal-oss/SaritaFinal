import math
from .variance_engine import VarianceEngine

class CorrelationEngine:
    """
    Computes Pearson product-moment correlation coefficients.
    """
    def __init__(self):
        self.variance_eng = VarianceEngine()

    def calculate_pearson(self, x: list, y: list) -> float:
        if len(x) != len(y) or not x:
            return 0.0
        n = len(x)
        if n < 2:
            return 0.0

        mean_x = self.variance_eng.calculate_mean(x)
        mean_y = self.variance_eng.calculate_mean(y)

        num = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        den_x = sum((x[i] - mean_x) ** 2 for i in range(n))
        den_y = sum((y[i] - mean_y) ** 2 for i in range(n))

        if den_x == 0.0 or den_y == 0.0:
            return 0.0

        return round(num / math.sqrt(den_x * den_y), 4)
