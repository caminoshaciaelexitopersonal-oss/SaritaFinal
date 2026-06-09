class SurvivalProbabilityCalculator:
    """
    Calculates the mathematical probability of constitutional survival (P_s).
    """
    def calculate_p_s(self, stability: float, risk: float, authority_integrity: float):
        # P_s = (Stability * AuthorityIntegrity) * (1 - Risk)
        return (stability * authority_integrity) * (1.0 - risk)
