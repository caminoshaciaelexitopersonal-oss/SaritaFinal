import random

class CulturalMutationGenerator:
    def __init__(self):
        self.mutation_types = ["linguistic", "artistic", "ritualistic", "philosophical", "technological"]

    def generate_mutation(self, current_culture):
        mutation_type = random.choice(self.mutation_types)
        intensity = random.uniform(0.01, 0.1)

        mutated_culture = current_culture.copy()
        if mutation_type in mutated_culture:
            change = random.uniform(-intensity, intensity)
            mutated_culture[mutation_type] = round(max(0.0, min(1.0, mutated_culture[mutation_type] + change)), 4)
        else:
            mutated_culture[mutation_type] = round(random.uniform(0.0, 1.0), 4)

        return mutated_culture, mutation_type
