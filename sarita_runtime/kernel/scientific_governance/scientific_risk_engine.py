from .paradigm_risk_analyzer import ParadigmRiskAnalyzer
from .knowledge_fragility_detector import KnowledgeFragilityDetector
from .catastrophic_error_estimator import CatastrophicErrorEstimator
from .scientific_failure_prevention import ScientificFailurePrevention

class ScientificRiskEngine:
    def __init__(self):
        self.risk_analyzer = ParadigmRiskAnalyzer()
        self.fragility_detector = KnowledgeFragilityDetector()
        self.error_estimator = CatastrophicErrorEstimator()
        self.failure_prevention = ScientificFailurePrevention()

    def evaluate_risk(self, paradigms, theories, domains):
        p_risks = [self.risk_analyzer.analyze_risk(p) for p in paradigms]
        t_fragilities = [self.fragility_detector.detect_fragility(t) for t in theories]

        max_risk = max(p_risks + t_fragilities + [0])
        intervention = self.failure_prevention.prevent_failure({"max_risk": max_risk})

        return {
            "max_risk": max_risk,
            "intervention": intervention,
            "scientific_risk": 0.95
        }
