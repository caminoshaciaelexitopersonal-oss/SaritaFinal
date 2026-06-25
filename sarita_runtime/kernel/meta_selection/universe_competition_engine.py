import random

class UniverseCompetitionEngine:
    def resolve_competition(self, universes):
        # Universes compete for substrate priority
        scored_universes = []
        for univ in universes:
            score = univ["genome"].get("innovation_velocity", 0.5) + random.uniform(0, 0.2)
            scored_universes.append((univ, score))

        scored_universes.sort(key=lambda x: x[1], reverse=True)
        return scored_universes
