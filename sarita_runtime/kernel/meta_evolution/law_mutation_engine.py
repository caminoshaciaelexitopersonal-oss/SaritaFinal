import random

class LawMutationEngine:
    def mutate_laws(self, laws, intensity=0.1):
        mutated = laws.copy()
        for law in mutated:
            if random.random() < 0.2: # 20% chance to mutate a specific law
                mutation = random.uniform(-intensity, intensity)
                mutated[law] = round(max(0.0, min(1.0, mutated[law] + mutation)), 4)
        return mutated
