import time

class SovereignGoalRegistry:
    """
    The official registry for SARITA's long-term sovereign goals.
    """
    def __init__(self):
        self.goals = {}

    def register_goal(self, goal_id: str, description: str, priority: int = 5):
        self.goals[goal_id] = {
            "description": description,
            "priority": priority,
            "registered_at": time.time(),
            "status": "ACTIVE"
        }
        print(f"GOAL REGISTRY: Registered goal {goal_id}")

    def get_active_goals(self):
        return {k: v for k, v in self.goals.items() if v["status"] == "ACTIVE"}
