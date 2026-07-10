import random

class CausalityEvolutionEngine:
    """
    Allows the laws of causality to evolve within a cosmos or across generations.
    Phase 127.4 - Causality Evolution Engine.
    """
    def __init__(self):
        self.mutation_rate = 0.05
        self.stability_threshold = 0.6

    def mutate_causality(self, architecture):
        causality = architecture["causality"]
        if random.random() < self.mutation_rate:
            # Shift propagation speed or reversibility
            causality["propagation_speed"] = round(max(0.1, min(1.0, causality["propagation_speed"] + random.uniform(-0.1, 0.1))), 4)
            causality["reversibility"] = round(max(0.0, min(1.0, causality["reversibility"] + random.uniform(-0.05, 0.05))), 4)
            return True
        return False

    def recombine_causality(self, arch_a, arch_b):
        """
        Mixes causal laws from two different architectures.
        """
        child_causality = {
            "mode": random.choice([arch_a["causality"]["mode"], arch_b["causality"]["mode"]]),
            "consistency_threshold": (arch_a["causality"]["consistency_threshold"] + arch_b["causality"]["consistency_threshold"]) / 2,
            "propagation_speed": (arch_a["causality"]["propagation_speed"] + arch_b["causality"]["propagation_speed"]) / 2,
            "reversibility": (arch_a["causality"]["reversibility"] + arch_b["causality"]["reversibility"]) / 2
        }
        return child_causality

    def evaluate_fitness(self, architecture):
        """
        Evaluates the 'fitness' of a causal model based on its stability and consistency.
        """
        score = architecture["consistency_score"]
        # Linear models are generally more stable but less 'innovative'
        if architecture["causality"]["mode"] == "LINEAR":
            score *= 1.1

        return min(1.0, score)

    def validate_stability(self, architecture):
        fitness = self.evaluate_fitness(architecture)
        return fitness >= self.stability_threshold
