import random

class SamplingEngine:
    """
    Executes random, stratified, or systematic sampling on large-scale runtime traces or historical states.
    """
    def __init__(self, seed: int = 42):
        self.rng = random.Random(seed)

    def random_sample(self, population: list, k: int) -> list:
        if k > len(population):
            return population.copy()
        return self.rng.sample(population, k)

    def stratified_sample(self, population: list, strata_key_func, k: int) -> list:
        strata = {}
        for item in population:
            key = strata_key_func(item)
            if key not in strata:
                strata[key] = []
            strata[key].append(item)

        sampled = []
        per_stratum = max(1, k // len(strata))
        for key, items in strata.items():
            sampled.extend(self.random_sample(items, per_stratum))
        return sampled[:k]
