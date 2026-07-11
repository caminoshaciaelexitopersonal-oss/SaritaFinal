class AlertDashboard:
    def render(self, state_manager) -> dict:
        return {
            "title": "Axiomatic Alert Matrix",
            "active_alerts": state_manager.governance.violations_detected
        }
