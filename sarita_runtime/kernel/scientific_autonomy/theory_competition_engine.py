from .theory_survival_selector import TheorySurvivalSelector
from .evidence_weighted_theory_ranker import EvidenceWeightedTheoryRanker
from .scientific_revolution_detector import ScientificRevolutionDetector

class TheoryCompetitionEngine:
    def __init__(self):
        self.selector = TheorySurvivalSelector()
        self.ranker = EvidenceWeightedTheoryRanker()
        self.detector = ScientificRevolutionDetector()

    def run_competition(self, theories, evidence_pool):
        rankings = self.ranker.rank_theories(theories, evidence_pool)
        survivors = self.selector.select_survivors(rankings)

        dominant = max(theories, key=lambda t: t.get("evidence_score", 0))
        # Simple simulation: assume a challenger theory exists
        challenger = {"id": "T-CHALLENGER", "evidence_score": dominant.get("evidence_score", 0) + 0.01}
        revolution = self.detector.detect_revolution(dominant, challenger)

        return {
            "rankings": rankings,
            "survivors": survivors,
            "revolution_detected": revolution
        }
