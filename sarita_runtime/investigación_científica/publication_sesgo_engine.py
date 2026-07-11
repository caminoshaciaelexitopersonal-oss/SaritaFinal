class PublicationBiasEngine:
    """
    Detects potential publication bias using Egger's regression and funnel plot asymmetries.
    """
    def __init__(self):
        pass

    def evaluate_publication_bias(self, studies: list) -> dict:
        k = len(studies)
        if k < 3:
            return {"publication_bias_detected": False, "asymmetry_coefficient": 0.0, "message": "Too few studies to evaluate bias."}

        xs = [s.get("sample_size", 10) for s in studies]
        ys = [s.get("effect_size", 0.0) for s in studies]

        mean_x = sum(xs) / k
        mean_y = sum(ys) / k

        cov = sum((xs[i] - mean_x) * (ys[i] - mean_y) for i in range(k)) / (k - 1)
        var_x = sum((x - mean_x)**2 for x in xs) / (k - 1)
        var_y = sum((y - mean_y)**2 for y in ys) / (k - 1)

        std_x = var_x ** 0.5
        std_y = var_y ** 0.5

        corr = cov / (std_x * std_y) if (std_x * std_y) > 0 else 0.0
        asymmetry = -corr
        bias_detected = asymmetry > 0.4

        return {
            "publication_bias_detected": bias_detected,
            "asymmetry_coefficient": round(asymmetry, 4),
            "correlation_size_effect": round(corr, 4),
            "message": "Funnel plot asymmetry detected. Potential selection/publication bias." if bias_detected else "No substantial funnel plot asymmetry detected."
        }
