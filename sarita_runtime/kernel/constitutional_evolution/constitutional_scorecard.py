class ConstitutionalScorecard:
    """
    Derives the Global Constitutional Fitness Index (GCFI).
    """
    def derive_gcfi(self, metrics):
        # Weighted average of all 7 fitness pillars
        weights = {
            "legitimacy_fitness": 0.2,
            "identity_fitness": 0.15,
            "purpose_fitness": 0.15,
            "governance_fitness": 0.1,
            "optimality_fitness": 0.15,
            "survival_fitness": 0.15,
            "civilizational_fitness": 0.1
        }

        gcfi = 0.0
        for key, weight in weights.items():
            gcfi += metrics.get(key, 0.0) * weight

        return float(round(max(0.0, min(1.0, gcfi)), 4))
