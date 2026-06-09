class ConstitutionalGapDetector:
    """
    Detects gaps where the constitution cannot prove optimality.
    """
    def find_uncovered_scenarios(self, scenarios, coverage_map):
        covered_ids = set()
        for scenario_ids in coverage_map.values():
            covered_ids.update(scenario_ids)

        gaps = [s["id"] for s in scenarios if s["id"] not in covered_ids]
        return gaps
