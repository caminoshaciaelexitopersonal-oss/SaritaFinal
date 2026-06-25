import random

class UniverseGenomeBuilder:
    def __init__(self):
        pass

    def build_genome(self, laws):
        # A universe's genome is the expression of its laws in its physical/logical substrate
        genome = {}
        for law, value in laws.items():
            # The genome might amplify or dampen certain laws
            expression = value * random.uniform(0.8, 1.2)
            genome[law] = round(max(0.0, min(1.0, expression)), 4)
        return genome
