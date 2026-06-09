class ConstitutionalGoalAdjudicator:
    """
    Adjudicates between competing constitutional goals.
    """
    def adjudicate(self, goal_a: str, goal_b: str, priorities: list):
        idx_a = priorities.index(goal_a) if goal_a in priorities else 999
        idx_b = priorities.index(goal_b) if goal_b in priorities else 999

        return goal_a if idx_a < idx_b else goal_b
