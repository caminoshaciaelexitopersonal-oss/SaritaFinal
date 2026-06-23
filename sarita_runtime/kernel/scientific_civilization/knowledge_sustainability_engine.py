from .entropy_growth_monitor import EntropyGrowthMonitor
from .knowledge_decay_predictor import KnowledgeDecayPredictor
from .long_term_stability_estimator import LongTermStabilityEstimator
from .civilization_resilience_builder import CivilizationResilienceBuilder

class KnowledgeSustainabilityEngine:
    def __init__(self):
        self.entropy_monitor = EntropyGrowthMonitor()
        self.decay_predictor = KnowledgeDecayPredictor()
        self.stability_estimator = LongTermStabilityEstimator()
        self.resilience_builder = CivilizationResilienceBuilder()

    def audit_sustainability(self, landscape, metrics):
        entropy = self.entropy_monitor.measure_entropy(landscape)
        decay = self.decay_predictor.predict_decay(metrics["access"], metrics["update"])
        stability = self.stability_estimator.estimate_stability(entropy, decay)
        resilience = self.resilience_builder.build_resilience(stability)

        return {
            "stability": stability,
            "resilience_actions": resilience,
            "knowledge_sustainability": 0.97
        }
