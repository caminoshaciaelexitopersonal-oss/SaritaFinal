class ConstitutionalEvolutionCalculator:
    """
    Computes GCEI based on:
    - 25% Constitutionality
    - 20% Architectural Sovereignty
    - 20% Evolutionary Risk
    - 15% Traceability
    - 10% Reproducibility
    - 10% Reversibility
    """
    def compute(self, metrics):
        weights = {
            "constitutionality": 0.25,
            "sovereignty": 0.20,
            "risk": 0.20,
            "traceability": 0.15,
            "reproducibility": 0.10,
            "reversibility": 0.10
        }

        gcei_score = 0.0
        # Risk is a negative metric, so we use (1 - risk)
        metrics_normalized = metrics.copy()
        metrics_normalized["risk"] = 1.0 - metrics.get("risk", 0.0)

        for key, weight in weights.items():
            gcei_score += metrics_normalized.get(key, 0.0) * weight

        return {
            "gcei_score": round(gcei_score, 4),
            "submetrics": metrics,
            "certification": "CERTIFIED" if gcei_score >= 0.85 else "PROVISIONAL"
        }
