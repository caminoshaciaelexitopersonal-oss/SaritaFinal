from .multi_paradigm_manager import MultiParadigmManager
from .paradigm_survival_selector import ParadigmSurvivalSelector
from .evidence_weighted_competition import EvidenceWeightedCompetition

class ParadigmCompetitionEngine:
    def __init__(self):
        self.manager = MultiParadigmManager()
        self.selector = ParadigmSurvivalSelector()
        self.competitor = EvidenceWeightedCompetition()

    def run_tournament(self, evidence_set):
        paradigms = self.manager.get_all()
        results = self.competitor.run_competition(paradigms, evidence_set)
        survivors = self.selector.select_survivors(results)
        return {"results": results, "survivors": survivors}

    def simulate_mass_competition(self, count=1000):
        # Simulates 1000 simultaneous paradigms
        for i in range(count):
            self.manager.add_paradigm({"id": f"P-{i}", "explains": lambda e: True})
        return len(self.manager.get_all())
