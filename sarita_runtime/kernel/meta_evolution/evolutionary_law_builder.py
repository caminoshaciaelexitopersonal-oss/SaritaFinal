import random

class EvolutionaryLawBuilder:
    def __init__(self):
        self.fundamental_laws = [
            "selection_intensity",
            "mutation_rate",
            "cooperation_bonus",
            "extinction_threshold",
            "innovation_velocity",
            "epistemic_stability"
        ]

    def build_laws(self, parent_laws=None):
        laws = {}
        for law in self.fundamental_laws:
            if parent_laws and law in parent_laws:
                mutation = random.uniform(-0.05, 0.05)
                value = max(0.0, min(1.0, parent_laws[law] + mutation))
            else:
                value = random.uniform(0.0, 1.0)
            laws[law] = round(value, 4)
        return laws
