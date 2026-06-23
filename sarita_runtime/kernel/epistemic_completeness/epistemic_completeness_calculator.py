class EpistemicCompletenessCalculator:
    """
    Computes GECI based on:
    - Coverage
    - Exhaustion
    - Confidence
    - Uncertainty
    - Novelty Discovery
    - Boundary Awareness
    """
    def compute_geci(self, metrics):
        weights = {
            "coverage": 0.20,
            "exhaustion": 0.20,
            "confidence": 0.20,
            "uncertainty": 0.15,
            "novelty": 0.15,
            "boundary": 0.10
        }

        geci_score = 0.0
        for key, weight in weights.items():
            val = metrics.get(key, 0.0)
            # Uncertainty is a negative factor
            if key == "uncertainty":
                val = 1.0 - val
            geci_score += val * weight

        return {
            "geci_score": round(geci_score, 4),
            "submetrics": metrics,
            "epistemic_status": "COMPLETE" if geci_score >= 0.95 else "PARTIAL"
        }
