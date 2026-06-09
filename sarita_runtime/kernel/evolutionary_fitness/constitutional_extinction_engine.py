class ConstitutionalExtinctionEngine:
    """
    Models and simulates scenarios of SARITA's constitutional disappearance.
    """
    def __init__(self, simulator, analyzer, estimator):
        self.simulator = simulator
        self.analyzer = analyzer
        self.estimator = estimator

    def run_extinction_analysis(self, p_s: float):
        scenario = self.simulator.simulate_failure("Default_Stress")
        chain_detected, reason = self.analyzer.analyze_chain([scenario])
        p_e = self.estimator.estimate_p_e(p_s, 0.2)

        return {
            "p_e": p_e,
            "catastrophic_risk": chain_detected,
            "extinction_reason": reason if chain_detected else "None",
            "verdict": "CRITICAL" if p_e > 0.1 else "STABLE"
        }
