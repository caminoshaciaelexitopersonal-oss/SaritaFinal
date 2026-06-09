class ConstitutionalResourceAllocator:
    """
    Allocates strategic resources to competing constitutional goals.
    """
    def allocate_resources(self, goals: list, budget: float):
        # Proportional allocation based on goal priority/value
        allocation = {}
        total_priority = sum(g.get("priority", 1) for g in goals)

        for goal in goals:
            share = (goal.get("priority", 1) / total_priority) * budget
            allocation[goal["id"]] = share

        return allocation
