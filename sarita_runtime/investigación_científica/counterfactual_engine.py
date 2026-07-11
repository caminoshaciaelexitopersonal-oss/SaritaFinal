class CounterfactualEngine:
    """
    Evaluates counterfactual queries: 'What would Y have been, if X had been x_prime, given that we observed X=x and Y=y?'
    """
    def __init__(self, causal_engine):
        self.causal_engine = causal_engine

    def evaluate_counterfactual(self, x: str, observed_x: float, target_x: float, y: str, observed_y: float, data_points: list) -> dict:
        effect_report = self.causal_engine.estimate_causal_effect(x, y, data_points)
        beta = effect_report.get("adjusted_causal_effect", 0.0)

        u = observed_y - beta * observed_x
        counterfactual_y = beta * target_x + u

        return {
            "query": f"Y_({x}={target_x}) given {x}={observed_x}, {y}={observed_y}",
            "observed_state": {x: observed_x, y: observed_y},
            "abducted_background_noise": round(u, 4),
            "counterfactual_prediction": round(counterfactual_y, 4),
            "net_causal_differential": round(counterfactual_y - observed_y, 4)
        }
