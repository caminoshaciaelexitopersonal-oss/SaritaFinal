class EvolutionaryBudgetManager:
    """
    Manages the budget for SARITA's evolution.
    Evolutionary Budget = Available CPU/MEM cycles for meta-tasks.
    """
    def __init__(self, total_budget: float = 1000.0):
        self.total_budget = total_budget
        self.spent = 0.0

    def allocate_budget(self, amount: float):
        if self.spent + amount > self.total_budget:
            return False, "Budget Exhausted"
        self.spent += amount
        return True, "Allocated"

    def get_remaining(self):
        return self.total_budget - self.spent
