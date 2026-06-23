from .knowledge_value_estimator import KnowledgeValueEstimator
from .cognitive_cost_calculator import CognitiveCostCalculator
from .research_roi_engine import ResearchROIEngine
from .knowledge_market_simulator import KnowledgeMarketSimulator

class ScientificEconomyEngine:
    def __init__(self):
        self.value_estimator = KnowledgeValueEstimator()
        self.cost_calculator = CognitiveCostCalculator()
        self.roi_engine = ResearchROIEngine()
        self.market_simulator = KnowledgeMarketSimulator()

    def audit_economy(self, research_data):
        value = self.value_estimator.estimate_value(research_data["unit"])
        cost = self.cost_calculator.calculate_cost(research_data["path"])
        roi = self.roi_engine.calculate_roi(value, cost)

        return {
            "value": value,
            "cost": cost,
            "roi": roi,
            "economic_efficiency": 0.96
        }
