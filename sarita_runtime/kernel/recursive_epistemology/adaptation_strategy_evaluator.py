class AdaptationStrategyEvaluator:
    def evaluate_strategy(self, strategy, outcome_history):
        # Measures how effectively a strategy led to better governance
        return sum(1 for o in outcome_history if o.get("success")) / len(outcome_history) if outcome_history else 1.0
