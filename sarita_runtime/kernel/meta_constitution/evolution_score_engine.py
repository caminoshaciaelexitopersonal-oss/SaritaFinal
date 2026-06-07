class EvolutionScoreEngine:
    """
    Generates a global evolution score for SARITA.
    """
    def __init__(self, efficiency_index, maturity_calc):
        self.efficiency_index = efficiency_index
        self.maturity_calc = maturity_calc

    def generate_score(self, data: dict):
        efficiency = self.efficiency_index.calculate(data["stability"], data["complexity"])
        maturity = self.maturity_calc.calculate_maturity(
            data["prediction_accuracy"],
            data["reform_success_rate"],
            data["learning_velocity"]
        )

        return {
            "evolution_score": (efficiency + maturity) / 2,
            "governance_efficiency": efficiency,
            "adaptive_maturity": maturity
        }
