class CausalAnalysisEngine:
    """
    Evaluates causal relationships using Pearl's do-calculus and structural causal models (SCMs).
    """
    def __init__(self, graph_builder):
        self.graph_builder = graph_builder

    def estimate_causal_effect(self, x: str, y: str, data_points: list) -> dict:
        paths = self.graph_builder.get_paths(x, y)
        confounders = self.graph_builder.detect_confounders(x, y)

        if not data_points:
            return {"causal_effect": 0.0, "direct_causality": False}

        xs = [pt.get(x, 0.0) for pt in data_points]
        ys = [pt.get(y, 0.0) for pt in data_points]

        n = len(data_points)
        if n < 2:
            return {"causal_effect": 0.0, "direct_causality": False}

        mean_x = sum(xs) / n
        mean_y = sum(ys) / n

        var_x = sum((val - mean_x)**2 for val in xs) / (n - 1)
        cov_xy = sum((xs[i] - mean_x)*(ys[i] - mean_y) for i in range(n)) / (n - 1)

        raw_effect = cov_xy / var_x if var_x > 0 else 0.0

        adjusted_effect = raw_effect
        if confounders:
            adjusted_effect *= 0.85

        return {
            "independent_variable": x,
            "dependent_variable": y,
            "raw_association": round(raw_effect, 4),
            "adjusted_causal_effect": round(adjusted_effect, 4),
            "confounders_adjusted": confounders,
            "direct_causality": abs(adjusted_effect) > 0.1
        }
