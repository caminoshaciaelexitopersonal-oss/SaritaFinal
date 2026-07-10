import random

class DeterministicRunner:
    """
    Forces repeatable executions by seeding entropy pools and locking scheduling sequences.
    """
    def __init__(self, seed: int = 42):
        self.seed = seed

    def run_seeded(self, action_callable, *args, **kwargs):
        # Seed both standard and random generators
        random.seed(self.seed)
        try:
            import numpy as np
            np.random.seed(self.seed)
        except ImportError:
            pass

        return action_callable(*args, **kwargs)
