class EpistemicMaturityCalculator:
    """
    Computes GEMI based on:
    - Frontier Awareness
    - Unknown Detection
    - Uncertainty Quantification
    - Robustness
    - Exploration Depth
    - Humility Score
    """
    def compute_gemi(self, metrics):
        weights = {
            "frontier_awareness": 0.20,
            "unknown_detection": 0.20,
            "uncertainty_quantification": 0.15,
            "robustness": 0.15,
            "exploration_depth": 0.15,
            "humility_score": 0.15
        }

        gemi_score = 0.0
        for key, weight in weights.items():
            gemi_score += metrics.get(key, 0.0) * weight

        return {
            "gemi_score": round(gemi_score, 4),
            "submetrics": metrics,
            "maturity_status": "EPISTEMIC_SOVEREIGN" if gemi_score >= 0.96 else "MATURING"
        }
