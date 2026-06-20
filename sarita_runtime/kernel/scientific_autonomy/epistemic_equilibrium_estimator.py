class EpistemicEquilibriumEstimator:
    def estimate_equilibrium(self, trajectory):
        # Predicts the future stable state of the system
        if not trajectory:
            return 0.0
        return sum(trajectory[-5:]) / len(trajectory[-5:]) if len(trajectory) >= 5 else trajectory[-1]
