class FutureStateSelector:
    """
    Selects the optimal future state based on sovereign goals.
    """
    def select_future_state(self, available_scenarios: list):
        if not available_scenarios:
            return None
        # Select the scenario with the highest stability and goal alignment
        best_scenario = max(available_scenarios, key=lambda x: x.get("alignment_score", 0))
        return best_scenario
