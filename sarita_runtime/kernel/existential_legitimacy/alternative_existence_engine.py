class AlternativeExistenceEngine:
    """
    Engine that models the "Absence of SARITA".
    """
    def __init__(self, simulator, analyzer, estimator):
        self.simulator = simulator
        self.analyzer = analyzer
        self.estimator = estimator

    def run_necessity_audit(self):
        absence_report = self.simulator.simulate_absence()
        replacement_ok = self.analyzer.analyze_replacement()
        necessity = self.estimator.estimate_necessity(1.0, replacement_ok) # Baseline impact 1.0

        return {
            "absence_impact": absence_report,
            "replacement_feasibility": replacement_ok,
            "necessity_score": necessity
        }
