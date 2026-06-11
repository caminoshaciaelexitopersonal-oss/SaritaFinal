class CausalStrengthAnalyzer:
    """
    Analyzes the strength of a causal effect vs a simple correlation.
    """
    def analyze(self, counterfactual_results):
        with_a = counterfactual_results["effect_with_a"]
        without_a = counterfactual_results["effect_without_a"]

        # Causal effect is the difference caused by the presence/absence of A
        causal_effect = abs(with_a - without_a)

        # Correlation effect is a baseline (here simplified)
        correlation_effect = 0.5 * causal_effect

        return causal_effect, correlation_effect
