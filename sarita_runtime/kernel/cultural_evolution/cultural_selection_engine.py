import random

class CulturalSelectionEngine:
    def __init__(self):
        pass

    def select_culture(self, candidates, adaptation_pressure):
        if not candidates:
            return None

        # Fitness is a function of complexity and adaptation to pressure
        fitness_scores = []
        for culture in candidates:
            complexity = sum(culture.values()) / len(culture) if culture else 0
            # Higher pressure favors lower complexity or specific traits
            fitness = complexity * (1 - adaptation_pressure) + random.uniform(0, 0.2)
            fitness_scores.append(fitness)

        best_idx = fitness_scores.index(max(fitness_scores))
        return candidates[best_idx]
