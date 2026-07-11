import random

class MonteCarloEngine:
    """
    Simulates high-dimensional probability spaces to predict index distributions and vulnerability thresholds.
    """
    def __init__(self, seed: int = 42):
        self.rng = random.Random(seed)

    def run_simulation(self, model_func, iterations: int = 5000) -> list:
        results = []
        for _ in range(iterations):
            rand_val = self.rng.gauss(0.0, 1.0)
            res = model_func(rand_val)
            results.append(res)
        return results
