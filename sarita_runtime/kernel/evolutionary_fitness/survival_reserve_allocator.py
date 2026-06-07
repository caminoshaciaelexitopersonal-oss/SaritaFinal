class SurvivalReserveAllocator:
    """
    Allocates and protects a "Survival Reserve" of resources.
    """
    def __init__(self, reserve_pct: float = 0.2):
        self.reserve_pct = reserve_pct

    def protect_reserve(self, total_budget: float):
        reserve = total_budget * self.reserve_pct
        return reserve
