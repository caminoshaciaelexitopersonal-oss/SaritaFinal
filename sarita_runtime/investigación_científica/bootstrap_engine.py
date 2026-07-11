import random

class BootstrapEngine:
    """
    Implements bootstrap resampling to estimate confidence intervals and standard errors of arbitrary metrics.
    """
    def __init__(self, seed: int = 42):
        self.rng = random.Random(seed)

    def bootstrap_ci(self, data: list, estimator_func, confidence: float = 0.95, n_resamples: int = 1000) -> tuple:
        if not data:
            return (0.0, 0.0)

        estimates = []
        n = len(data)
        for _ in range(n_resamples):
            resample = [self.rng.choice(data) for _ in range(n)]
            estimates.append(estimator_func(resample))

        estimates.sort()
        alpha = 1.0 - confidence
        lower_idx = int(n_resamples * (alpha / 2.0))
        upper_idx = int(n_resamples * (1.0 - alpha / 2.0))

        lower_idx = max(0, min(n_resamples - 1, lower_idx))
        upper_idx = max(0, min(n_resamples - 1, upper_idx))

        return (round(estimates[lower_idx], 4), round(estimates[upper_idx], 4))
