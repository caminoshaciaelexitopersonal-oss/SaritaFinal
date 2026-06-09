class EvolutionaryDirectionEngine:
    """
    Determines and manages SARITA's evolutionary trajectory.
    """
    def __init__(self, path_generator, state_selector, trajectory_validator):
        self.path_generator = path_generator
        self.state_selector = state_selector
        self.trajectory_validator = trajectory_validator
        self.current_trajectory = None

    def update_direction(self, current_state: dict, goals: dict):
        # 1. Select desired future
        target_state = {"governance_efficiency": 0.99, "alignment": 1.0}

        # 2. Generate path
        path = self.path_generator.generate_path(current_state, target_state)

        # 3. Validate current trajectory
        is_converging = self.trajectory_validator.validate_trajectory([], target_state)

        self.current_trajectory = {
            "target": target_state,
            "path": path,
            "is_converging": is_converging
        }

        return self.current_trajectory
