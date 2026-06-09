class ConstitutionalValueEngine:
    """
    The engine that measures and manages the absolute value of constitutional objectives.
    """
    def __init__(self, calculator, analyzer, estimator):
        self.calculator = calculator
        self.analyzer = analyzer
        self.estimator = estimator

    def assess_objective_value(self, goal_id: str, cost: float, risk: float):
        utility = self.analyzer.analyze_utility(goal_id, 0.1)
        value = self.calculator.calculate_value(utility, cost, risk)

        return {
            "goal_id": goal_id,
            "utility": utility,
            "cost": cost,
            "risk": risk,
            "strategic_value": value,
            "verdict": "VALUABLE" if value > 0.5 else "IMPRODUCTIVE"
        }
