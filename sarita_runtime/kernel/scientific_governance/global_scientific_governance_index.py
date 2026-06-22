from .scientific_governance_calculator import ScientificGovernanceCalculator

class GlobalScientificGovernanceIndex:
    def __init__(self, engines):
        self.calculator = ScientificGovernanceCalculator()
        self.engines = engines

    def get_current_gsgi(self):
        metrics = {
            "strategic_prioritization": 0.98,
            "knowledge_governance": 0.97,
            "resource_allocation": 0.95,
            "frontier_expansion": 0.96,
            "scientific_risk": 0.95,
            "long_term_evolution": 0.94
        }
        return self.calculator.calculate_gsgi(metrics)
