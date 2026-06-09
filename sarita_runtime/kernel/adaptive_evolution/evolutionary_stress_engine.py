class EvolutionaryStressEngine:
    """
    Subjects constitutional variants to extreme scenarios to measure resilience.
    """
    def __init__(self, scenario_generator, breakpoint_detector, resilience_engine):
        self.scenario_generator = scenario_generator
        self.breakpoint_detector = breakpoint_detector
        self.resilience_engine = resilience_engine

    def run_stress_test(self, constitution):
        scenarios = self.scenario_generator.generate_extreme_scenarios()
        results = []

        for scenario in scenarios:
            impact = self.resilience_engine.measure_impact(constitution, scenario)
            breakpoint_found = self.breakpoint_detector.check_breakpoint(constitution, impact)

            results.append({
                "scenario": scenario["type"],
                "impact_score": impact,
                "is_resilient": not breakpoint_found
            })

        return results
