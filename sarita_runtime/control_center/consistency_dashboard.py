class ConsistencyDashboard:
    def render(self, state_manager) -> dict:
        return {
            "title": "Formal Consistency GCT",
            "ggci": state_manager.consistency.ggci,
            "dimensions_held": state_manager.consistency.dimensions_held
        }
