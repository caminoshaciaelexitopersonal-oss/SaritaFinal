class ConstitutionalEconomyEngine:
    """
    Governs the economic constraints of SARITA's evolution.
    """
    def __init__(self, budget_manager, allocator, capital_registry):
        self.budget_manager = budget_manager
        self.allocator = allocator
        self.capital_registry = capital_registry

    def fund_evolution_step(self, goal_id: str, cost: float):
        success, reason = self.budget_manager.allocate_budget(cost)
        if success:
            self.capital_registry.update_capital("STABILITY", -0.1) # Small cost to current stability
            return True, f"Funded {goal_id} with {cost} units."
        return False, reason
