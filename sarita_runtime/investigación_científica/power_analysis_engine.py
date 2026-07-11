import math

class PowerAnalysisEngine:
    """
    Computes statistical power for t-tests given sample size, effect size, and alpha.
    """
    def __init__(self):
        pass

    def calculate_power(self, effect_size: float, n: int, alpha: float = 0.05) -> float:
        if n <= 2 or effect_size == 0:
            return 0.05

        z_alpha = 1.96 if alpha == 0.05 else (2.58 if alpha == 0.01 else 1.64)
        delta = effect_size * math.sqrt(n / 2.0)
        z_beta = z_alpha - delta

        if z_beta < -3.0:
            return 0.999
        if z_beta > 3.0:
            return 0.001

        power = 1.0 / (1.0 + math.exp(1.654 * z_beta))
        return round(power, 4)
