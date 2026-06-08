class DriftProbabilityEstimator:
    """
    Estimates the probability of ontological drift (P_d).
    """
    def estimate_p_d(self, protection_level: float, evolution_cycles: int):
        # P_d increases with cycles and decreases with protection
        if protection_level >= 1.0:
            return 0.0 # Absolute protection
        return (evolution_cycles * 0.001) / protection_level
