class ArchitectureDashboard:
    def render(self, state_manager) -> dict:
        return {
            "title": "Architecture & GSAI",
            "gsai": state_manager.architecture.gsai,
            "coupling": state_manager.architecture.coupling_degree
        }
