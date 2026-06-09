class ObjectiveHierarchyManager:
    """
    Manages the relationship between high-level goals and low-level policies.
    """
    def __init__(self):
        self.hierarchy = {} # goal_id -> [sub_objective_id, ...]

    def link_objective(self, goal_id: str, sub_objective_id: str):
        if goal_id not in self.hierarchy:
            self.hierarchy[goal_id] = []
        self.hierarchy[goal_id].append(sub_objective_id)
        print(f"HIERARCHY: Linked {sub_objective_id} to {goal_id}")
