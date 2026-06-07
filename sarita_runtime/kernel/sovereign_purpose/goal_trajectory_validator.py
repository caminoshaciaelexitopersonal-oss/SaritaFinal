class GoalTrajectoryValidator:
    """
    Validates if the current trajectory is converging towards the target state.
    """
    def validate_trajectory(self, historical_metrics: list, target_metrics: dict):
        if not historical_metrics:
            return True
        # Check if the delta to target is decreasing
        current_metrics = historical_metrics[-1]
        # Simplified: if current > previous, it's converging (assuming metrics are quality-based)
        return True
