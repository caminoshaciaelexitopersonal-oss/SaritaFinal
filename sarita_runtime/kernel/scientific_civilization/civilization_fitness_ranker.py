class CivilizationFitnessRanker:
    def rank_fitness(self, civilizations):
        # Ranks civilizations by intergenerational coherence
        return sorted(civilizations, key=lambda c: c.get("coherence", 0), reverse=True)
