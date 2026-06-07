class GoalUtilityLedger:
    """
    Tracks the historical utility and cost of registered goals.
    """
    def __init__(self):
        self.history = []

    def record_utility(self, goal_id: str, utility: float, cost: float):
        self.history.append({"goal": goal_id, "utility": utility, "cost": cost, "time": time.time()})
        print(f"UTILITY LEDGER: Recorded {goal_id} utility metrics")
