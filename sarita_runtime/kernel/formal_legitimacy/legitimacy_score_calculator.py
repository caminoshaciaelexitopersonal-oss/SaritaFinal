class LegitimacyScoreCalculator:
    """
    Calculates the absolute legitimacy score of the system state.
    """

    def calculate_score(self,
                        existential_score: float,
                        purpose_alignment: float,
                        identity_fidelity: float,
                        causal_integrity: float) -> float:
        """
        Derives the Legitimacy Score (L_s) as a product of core sovereignty pillars.
        """
        # All inputs must be 0.0 to 1.0
        l_s = (existential_score * 0.4) + (purpose_alignment * 0.2) + \
              (identity_fidelity * 0.2) + (causal_integrity * 0.2)

        return float(round(max(0.0, min(1.0, l_s)), 4))
