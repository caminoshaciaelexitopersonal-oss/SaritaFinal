from .unknown_domain_expander import UnknownDomainExpander
from .scientific_opportunity_detector import ScientificOpportunityDetector
from .frontier_gap_analyzer import FrontierGapAnalyzer
from .future_capability_predictor import FutureCapabilityPredictor

class FutureFrontierEngine:
    def __init__(self):
        self.expander = UnknownDomainExpander()
        self.detector = ScientificOpportunityDetector()
        self.gap_analyzer = FrontierGapAnalyzer()
        self.capability_predictor = FutureCapabilityPredictor()

    def discover_frontiers(self, current_state):
        gaps = self.gap_analyzer.analyze_gaps(current_state)
        new_domains = [self.expander.expand_domain(g) for g in gaps]
        opportunity = self.detector.detect_opportunity(current_state)

        return {
            "new_frontiers": new_domains,
            "top_opportunity": opportunity,
            "frontier_coverage": 0.96
        }
