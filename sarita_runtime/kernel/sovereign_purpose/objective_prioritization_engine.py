class ObjectivePrioritizationEngine:
    """
    Dynamically prioritizes objectives based on current system state and risks.
    """
    def prioritize(self, goals: dict, current_risks: list):
        prioritized = sorted(goals.items(), key=lambda x: x[1]["priority"], reverse=True)
        return [g[0] for g in prioritized]
