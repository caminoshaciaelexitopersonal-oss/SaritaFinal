class InterventionEngine:
    """
    Simulates interventions using Pearl's do-calculus to estimate P(Y | do(X)).
    """
    def __init__(self, causal_engine):
        self.causal_engine = causal_engine

    def simulate_intervention(self, x: str, value: float, y: str, data_points: list) -> dict:
        effect_report = self.causal_engine.estimate_causal_effect(x, y, data_points)
        beta = effect_report.get("adjusted_causal_effect", 0.0)

        ys = [pt.get(y, 0.0) for pt in data_points]
        baseline_y = sum(ys) / len(ys) if ys else 0.0

        xs = [pt.get(x, 0.0) for pt in data_points]
        mean_x = sum(xs) / len(xs) if xs else 0.0

        intervened_y = baseline_y + beta * (value - mean_x)

        return {
            "intervention": f"do({x}={value})",
            "predicted_dependent_value": round(intervened_y, 4),
            "baseline_value": round(baseline_y, 4),
            "expected_change": round(intervened_y - baseline_y, 4)
        }
