class ConstitutionalJustificationEngine:
    """
    Determines if existence produces more benefit than cost.
    """
    def __init__(self, analyzer, evaluator, calculator):
        self.analyzer = analyzer
        self.evaluator = evaluator
        self.calculator = calculator

    def justify_existence(self, system_state: dict):
        benefit = self.analyzer.analyze_benefit(system_state)
        cost = self.evaluator.evaluate_cost(system_state.get("complexity", 0.1), 0.05)
        net = self.calculator.calculate_net_legitimacy(benefit, cost)

        return {
            "benefit": benefit,
            "cost": cost,
            "net_legitimacy": net,
            "is_justified": net > 1.0
        }
