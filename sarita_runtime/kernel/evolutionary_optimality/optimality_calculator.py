class OptimalityCalculator:
    """
    Computes GEOI based on:
    - Optimality
    - Dominance
    - Universality
    - Resilience
    - Regret
    - Counterfactual Superiority
    """
    def compute_geoi(self, metrics):
        weights = {
            "optimality": 0.20,
            "dominance": 0.20,
            "universality": 0.15,
            "resilience": 0.15,
            "regret": 0.15,
            "counterfactual_superiority": 0.15
        }

        geoi_score = 0.0
        for key, weight in weights.items():
            # Regret is handled as (1 - regret)
            val = metrics.get(key, 0.0)
            if key == "regret":
                val = 1.0 - val
            geoi_score += val * weight

        return {
            "geoi_score": round(geoi_score, 4),
            "submetrics": metrics,
            "status": "OPTIMAL" if geoi_score >= 0.9 else "SUBOPTIMAL"
        }
