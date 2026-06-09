class ConstitutionalDriftSimulator:
    """
    Simulates the loss of identity over multiple evolutionary generations.
    """
    def __init__(self, mutation_engine, degradation_analyzer, p_d_estimator):
        self.mutation_engine = mutation_engine
        self.degradation_analyzer = degradation_analyzer
        self.p_d_estimator = p_d_estimator

    def run_drift_simulation(self, cycles: int, core_protection: float):
        degradation = self.degradation_analyzer.analyze_degradation(cycles, 0.01)
        p_d = self.p_d_estimator.estimate_p_d(core_protection, cycles)

        return {
            "cycles": cycles,
            "essence_remaining": degradation,
            "drift_probability": p_d,
            "verdict": "SAFE" if degradation > 0.99 else "UNSAFE_DRIFT"
        }
