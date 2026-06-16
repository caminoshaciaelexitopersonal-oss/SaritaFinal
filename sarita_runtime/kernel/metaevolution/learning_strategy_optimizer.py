class LearningStrategyOptimizer:
    """Optimizes learning strategies based on acquisition performance metrics."""
    def optimize_strategy(self, evaluation):
        gain = evaluation.get("efficiency_gain", 0.5)

        # Strategy selection based on performance
        strategy_id = "STRAT-OPT-HIGH" if gain > 0.9 else "STRAT-OPT-STD"
        adjustment = 0.01 if gain > 0.8 else 0.05

        return {
            "id": strategy_id,
            "learning_rate_adjustment": round(adjustment, 4),
            "exploration_factor": round(1.0 - gain, 4)
        }
