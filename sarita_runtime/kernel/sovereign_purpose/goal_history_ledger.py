import time

class GoalHistoryLedger:
    """
    Persistent record of goal registrations, modifications, and retirements.
    """
    def __init__(self):
        self.history = []

    def record_goal_change(self, goal_id: str, change_type: str):
        self.history.append({"goal": goal_id, "type": change_type, "time": time.time()})
        print(f"GOAL HISTORY: Recorded {change_type} for {goal_id}")
