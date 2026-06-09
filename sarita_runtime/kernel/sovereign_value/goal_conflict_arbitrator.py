class GoalConflictArbitrator:
    """
    Arbitrates between competing goals based on value and survival priority.
    """
    def arbitrate(self, goal_a: dict, goal_b: dict):
        # Survival always wins. Then Value.
        if goal_a.get("type") == "SURVIVAL" and goal_b.get("type") != "SURVIVAL":
            return goal_a
        return goal_a if goal_a["value"] > goal_b["value"] else goal_b
