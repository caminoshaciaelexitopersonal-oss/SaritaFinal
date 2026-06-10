class DecisionOptimizationEngine:
    """
    Specifically optimizes decision parameters for constitutional alignment.
    """
    def __init__(self, multi_objective_optimizer):
        self.optimizer = multi_objective_optimizer

    def optimize_decision(self, decision_context, constraints):
        """
        Refines a decision to maximize constitutional utility.
        """
        return self.optimizer.optimize(decision_context, constraints)
