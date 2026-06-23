from .cognitive_budget_allocator import CognitiveBudgetAllocator
from .exploration_exploitation_balancer import ExplorationExploitationBalancer
from .research_efficiency_optimizer import ResearchEfficiencyOptimizer
from .scientific_roi_calculator import ScientificROICalculator

class ResearchResourceEngine:
    def __init__(self):
        self.budget_allocator = CognitiveBudgetAllocator()
        self.balancer = ExplorationExploitationBalancer()
        self.optimizer = ResearchEfficiencyOptimizer()
        self.roi_calculator = ScientificROICalculator()

    def manage_resources(self, domains, global_uncertainty):
        allocations = self.budget_allocator.allocate_budget(domains)
        balance = self.balancer.balance(global_uncertainty)
        return {"allocations": allocations, "balance": balance}
