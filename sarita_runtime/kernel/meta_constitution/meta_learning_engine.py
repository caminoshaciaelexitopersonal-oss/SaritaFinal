class MetaLearningEngine:
    """
    Second-order learning: SARITA learns how to improve its own governance processes.
    """
    def __init__(self, analyzer, optimizer, core):
        self.analyzer = analyzer
        self.optimizer = optimizer
        self.core = core
        self.feedback_history = []

    def learn_how_to_learn(self, new_feedback: dict):
        self.feedback_history.append(new_feedback)

        # 1. Analyze success/failure patterns of previous learning/reforms
        analysis = self.analyzer.analyze_success_patterns(self.feedback_history)

        # 2. Optimize governance strategies
        current_strategy = {"risk_tolerance": 0.5, "complexity_threshold": 0.5}
        optimized_strategy = self.optimizer.optimize_strategy(current_strategy, analysis)

        # 3. Update Intelligence Core
        self.core.update_meta_knowledge("governance_strategy", optimized_strategy)
        self.core.update_meta_knowledge("learning_efficiency", {"accuracy": 0.95})

        return {
            "strategy_evolution": "IMPROVED" if optimized_strategy != current_strategy else "STABLE",
            "meta_knowledge_updated": True
        }
