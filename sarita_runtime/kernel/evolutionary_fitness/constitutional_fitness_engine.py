class ConstitutionalFitnessEngine:
    """
    The engine that measures the aptitude of the organism to persist and evolve.
    """
    def __init__(self, p_s_calc, estimator, adv_analyzer):
        self.p_s_calc = p_s_calc
        self.estimator = estimator
        self.adv_analyzer = adv_analyzer

    def assess_decision_fitness(self, decision_data: dict):
        p_s = self.p_s_calc.calculate_p_s(
            decision_data["stability"],
            decision_data["risk"],
            decision_data["authority_integrity"]
        )
        fitness = self.estimator.estimate_fitness(
            decision_data["value"],
            p_s,
            decision_data["complexity"]
        )

        return {
            "p_s": p_s,
            "fitness": fitness,
            "advantage": self.adv_analyzer.analyze_advantage(fitness, 0.5) # Baseline 0.5
        }
