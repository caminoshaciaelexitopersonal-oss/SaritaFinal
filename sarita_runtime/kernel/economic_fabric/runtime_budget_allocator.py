import logging

class RuntimeBudgetAllocator:
    """
    Economic Governance Engine.
    Allocates execution quotas based on governed budgets.
    """
    def __init__(self):
        self.budgets = {} # component_id -> balance

    def deposit_budget(self, component_id, amount):
        self.budgets[component_id] = self.budgets.get(component_id, 0) + amount
        logging.info(f"Economic Fabric: Deposited {amount} to {component_id}")

    def consume_budget(self, component_id, cost):
        current = self.budgets.get(component_id, 0)
        if current >= cost:
            self.budgets[component_id] -= cost
            logging.info(f"Economic Fabric: {component_id} consumed {cost}. Balance: {self.budgets[component_id]}")
            return True
        logging.error(f"Economic Fabric: Insufficient budget for {component_id}")
        return False

class FederatedCapacityMarket:
    def get_pricing_signal(self, region_load):
        """
        Dynamically calculates execution pricing based on regional load.
        """
        return 1.0 + (region_load * 0.5)
