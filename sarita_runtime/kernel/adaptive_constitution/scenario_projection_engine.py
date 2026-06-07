class ScenarioProjectionEngine:
    """
    Projects various future scenarios (e.g. high load, attack, normal ops) for simulation.
    """
    def project_scenarios(self, amendment):
        return [
            {"name": "NORMAL_OPERATIONS", "load": "low", "threat": "low"},
            {"name": "HIGH_STRESS", "load": "extreme", "threat": "low"},
            {"name": "ADVERSARIAL_ENVIRONMENT", "load": "medium", "threat": "high"}
        ]
