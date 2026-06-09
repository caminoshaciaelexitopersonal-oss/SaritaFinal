class SurvivalPriorityValidator:
    """
    Validates that survival priorities are never downgraded.
    """
    def validate_priority(self, goal_id: str, new_priority: int, goal_type: str):
        if goal_type == "SURVIVAL" and new_priority < 9:
            return False, "Survival priority cannot be downgraded below Level 9."
        return True, "Priority validated."
