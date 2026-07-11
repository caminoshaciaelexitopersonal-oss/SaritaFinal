import random

class RandomizationEngine:
    """
    Ensures absolute unbiased randomization when assigning tasks or workloads to experimental or control blocks.
    """
    def __init__(self, seed: int = 42):
        self.rng = random.Random(seed)

    def set_seed(self, seed: int):
        self.rng = random.Random(seed)

    def randomize_groups(self, units: list, groups_count: int) -> list:
        shuffled = units.copy()
        self.rng.shuffle(shuffled)

        assigned = [[] for _ in range(groups_count)]
        for idx, item in enumerate(shuffled):
            assigned[idx % groups_count].append(item)
        return assigned
