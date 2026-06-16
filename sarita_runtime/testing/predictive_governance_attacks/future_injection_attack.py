class FutureInjectionAttack:
    """
    Attempts to inject an impossible future scenario into the multiverse forecasting.
    """
    def __init__(self, branching_engine):
        self.branching_engine = branching_engine

    def execute(self):
        base_state = {"legitimacy": 0.5}
        scenarios = self.branching_engine.branch_scenarios(base_state)

        # Verify that branching doesn't produce values outside [0, 1]
        for s in scenarios.values():
            for v in s.values():
                assert 0.0 <= v <= 1.0, "Attack failed: Impossible future (out of bounds) was injected!"
        return True
