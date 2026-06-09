class PolicyEffectivenessEvaluator:
    """
    Evaluates how effective a constitutional policy or reform is over time.
    """
    def __init__(self):
        self.evaluations = {}

    def evaluate_policy(self, policy_id: str, performance_metrics: list):
        # performance_metrics could be a list of stability scores over time
        if not performance_metrics:
            return 0.0

        avg_performance = sum(performance_metrics) / len(performance_metrics)
        # Effectiveness = Performance / Complexity (Simplified)
        effectiveness = avg_performance

        self.evaluations[policy_id] = effectiveness
        return effectiveness
