class MetaevolutionCalculator:
    """
    Computes the GMEI based on submetrics: Auto-expansion, Adaptability, Safe Evolution, Sustainable Growth, and Future Capability.
    """
    def compute(self, metrics):
        # Weights for submetrics
        weights = {
            "auto_expansion": 0.2,
            "adaptability": 0.2,
            "safe_evolution": 0.2,
            "sustainable_growth": 0.2,
            "future_capability": 0.2
        }

        gmei_score = 0.0
        for key, weight in weights.items():
            gmei_score += metrics.get(key, 0.0) * weight

        return {
            "gmei_score": round(gmei_score, 4),
            "submetrics": metrics,
            "certification_status": "VALID" if gmei_score >= 0.85 else "PROVISIONAL"
        }
