class CivilizationalEvolutionCalculator:
    def calculate_gcei2(self, metrics):
        # Normalizes and weights various metrics to produce GCEI-2 (0.0 to 1.0)
        # diversity, resilience, legitimacy, cooperation, competition, sustainability

        diversity = min(1.0, metrics.get("institutional_diversity", 0) / 20.0)
        resilience = metrics.get("avg_survival_prob", 0)
        legitimacy = metrics.get("avg_reputation", 0.5) / 5.0
        cooperation = min(1.0, metrics.get("active_treaties_count", 0) / 10.0)
        competition = min(1.0, metrics.get("competitive_intensity", 0.5))
        sustainability = min(1.0, metrics.get("avg_resources", 0) / 5.0)

        # Weighted sum
        gcei2 = (
            (diversity * 0.15) +
            (resilience * 0.20) +
            (legitimacy * 0.15) +
            (cooperation * 0.20) +
            (competition * 0.15) +
            (sustainability * 0.15)
        )
        return round(max(0.0, min(1.0, gcei2)), 4)

class GlobalCivilizationalEvolutionIndex:
    def __init__(self):
        self.calculator = CivilizationalEvolutionCalculator()

    def get_index(self, ecosystem_metrics):
        return self.calculator.calculate_gcei2(ecosystem_metrics)
