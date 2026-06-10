class EnvironmentStateRegistry:
    """
    Registry for current and historical environmental states.
    """
    def __init__(self):
        self.states = {
            "CURRENT": {
                "users": 1000,
                "operational_volume": 50000,
                "threat_level": 0.05,
                "resource_availability": 1.0,
                "regulatory_complexity": 0.2
            }
        }

    def get_current_state(self):
        return self.states["CURRENT"]

    def update_state(self, state_id, new_state):
        self.states[state_id] = new_state
