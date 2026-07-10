class CosmogenesisCalculator:
    """
    Calculates the Global Cosmogenesis Index (GCI) based on multiverse metrics.
    Phase 127.8.
    """
    def calculate_gci(self, metrics):
        """
        metrics = {
            "cosmic_diversity": 0.0-1.0,
            "causal_diversity": 0.0-1.0,
            "logic_diversity": 0.0-1.0,
            "reality_stability": 0.0-1.0,
            "observer_emergence": 0.0-1.0,
            "meta_reality_gen": 0.0-1.0
        }
        """
        weights = {
            "cosmic_diversity": 0.2,
            "causal_diversity": 0.2,
            "logic_diversity": 0.15,
            "reality_stability": 0.15,
            "observer_emergence": 0.15,
            "meta_reality_gen": 0.15
        }

        gci = 0.0
        for key, weight in weights.items():
            gci += metrics.get(key, 0.0) * weight

        return round(gci, 4)
