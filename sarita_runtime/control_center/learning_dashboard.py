class LearningDashboard:
    def render(self, state_manager) -> dict:
        return {
            "title": "Continuous Learning Matrix",
            "cumulative_reward": state_manager.learning.cumulative_reward,
            "recorded_experiences": state_manager.learning.recorded_experiences
        }
