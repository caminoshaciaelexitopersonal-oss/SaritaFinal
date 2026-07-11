class HeterogeneityEngine:
    """
    Computes heterogeneity metrics (Cochran's Q, I-squared, Tau-squared) across multiple studies in a meta-analysis.
    """
    def __init__(self):
        pass

    def calculate_heterogeneity(self, studies: list) -> dict:
        k = len(studies)
        if k < 2:
            return {"cochran_q": 0.0, "i_squared": 0.0, "tau_squared": 0.0}

        total_weight = 0.0
        weighted_sum = 0.0
        for s in studies:
            var = s.get("variance", 0.001) or 0.001
            weight = 1.0 / var
            weighted_sum += s.get("effect_size", 0.0) * weight
            total_weight += weight

        mean_effect = weighted_sum / total_weight if total_weight > 0 else 0.0

        q = 0.0
        for s in studies:
            var = s.get("variance", 0.001) or 0.001
            weight = 1.0 / var
            diff = s.get("effect_size", 0.0) - mean_effect
            q += weight * (diff ** 2)

        df = k - 1
        i_squared = max(0.0, (q - df) / q) if q > 0 else 0.0

        sum_w2 = sum((1.0 / (s.get("variance", 0.001) or 0.001))**2 for s in studies)
        c = total_weight - (sum_w2 / total_weight) if total_weight > 0 else 1.0
        tau_squared = max(0.0, (q - df) / c) if c > 0 else 0.0

        return {
            "cochran_q": round(q, 4),
            "degrees_of_freedom": df,
            "i_squared": round(i_squared, 4),
            "tau_squared": round(tau_squared, 4)
        }
