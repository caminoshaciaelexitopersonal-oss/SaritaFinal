import random

class CivilizationGenomeBuilder:
    def __init__(self):
        self.foundational_traits = [
            "constitutional_rigidity",
            "epistemic_openness",
            "economic_collectivism",
            "governance_centralization",
            "technological_focus",
            "cultural_homogeneity"
        ]

    def build_genome(self, parent_genome=None):
        genome = {}
        for trait in self.foundational_traits:
            if parent_genome and trait in parent_genome:
                # Mutation from parent
                mutation = random.uniform(-0.1, 0.1)
                value = max(0.0, min(1.0, parent_genome[trait] + mutation))
            else:
                # Random initialization
                value = random.uniform(0.0, 1.0)
            genome[trait] = round(value, 4)
        return genome

    def mutate_genome(self, genome, intensity=0.05):
        mutated_genome = genome.copy()
        for trait in mutated_genome:
            mutation = random.uniform(-intensity, intensity)
            mutated_genome[trait] = round(max(0.0, min(1.0, mutated_genome[trait] + mutation)), 4)
        return mutated_genome
