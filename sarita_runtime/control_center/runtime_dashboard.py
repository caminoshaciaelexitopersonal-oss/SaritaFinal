class RuntimeDashboard:
    def render(self, state_manager) -> dict:
        return {
            "title": "Master Process Runtime",
            "status": state_manager.runtime.status,
            "session_count": state_manager.runtime.session_count
        }
