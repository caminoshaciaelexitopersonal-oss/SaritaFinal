import math

class SampleSizeCalculator:
    """
    Computes required sample size to achieve specified power, alpha, and expected effect size.
    """
    def __init__(self):
        pass

    def calculate_required_size(self, effect_size: float, power: float = 0.8, alpha: float = 0.05) -> int:
        if effect_size <= 0:
            return 1000

        z_alpha = 1.96 if alpha == 0.05 else 2.58
        z_beta = 0.84 if power == 0.8 else 1.28

        n = 2.0 * (((z_alpha + z_beta) / effect_size) ** 2)
        return max(3, int(math.ceil(n)))
