class ConstitutionalFitnessEstimator:
    """
    Estimates the "Constitutional Fitness" (F_c) of a decision or state.
    """
    def estimate_fitness(self, value: float, p_s: float, complexity: float):
        # Fitness = (Value * P_s) / (1 + Complexity)
        if complexity < 0:
            complexity = 0
        return (value * p_s) / (1.0 + complexity)
