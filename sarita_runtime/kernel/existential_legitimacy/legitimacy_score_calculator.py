class LegitimacyScoreCalculator:
    """
    Calculates the mathematical Legitimacy Score (L_e) of SARITA's existence.
    """
    def calculate_l_e(self, benefit_index: float, cost_index: float, necessity_score: float):
        # L_e = (Benefit / Cost) * Necessity
        if cost_index <= 0:
            return benefit_index * necessity_score
        return (benefit_index / cost_index) * necessity_score
