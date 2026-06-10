class ConstitutionalCoverageEngine:
    """
    Measures the coverage of constitutional axioms over decision scenarios.
    """
    def __init__(self, axiom_analyzer, scenario_validator, gap_detector):
        self.axiom_analyzer = axiom_analyzer
        self.scenario_validator = scenario_validator
        self.gap_detector = gap_detector

    def measure_coverage(self, axioms, scenarios):
        coverage_map = self.axiom_analyzer.map_axioms_to_scenarios(axioms, scenarios)
        gaps = self.gap_detector.find_uncovered_scenarios(scenarios, coverage_map)

        coverage_ratio = (len(scenarios) - len(gaps)) / len(scenarios) if scenarios else 1.0

        return {
            "coverage_ratio": float(round(coverage_ratio, 4)),
            "uncovered_scenarios": gaps,
            "axiom_utilization": coverage_map
        }
