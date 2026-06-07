class ExtinctionProbabilityEstimator:
    """
    Estimates the probability of SARITA's extinction (P_e).
    """
    def estimate_p_e(self, p_s: float, risk_entropy: float):
        # P_e = (1 - P_s) * RiskEntropy
        return (1.0 - p_s) * risk_entropy
