from .validator_challenger import ValidatorChallenger
from .metric_refutation_engine import MetricRefutationEngine
from .index_attack_validator import IndexAttackValidator
from .self_critique_engine import SelfCritiqueEngine

class MetaFalsifiabilityEngine:
    def __init__(self):
        self.challenger = ValidatorChallenger()
        self.refuter = MetricRefutationEngine()
        self.attack_validator = IndexAttackValidator()
        self.critique_engine = SelfCritiqueEngine()

    def stress_test_indices(self, indices):
        results = {}
        for name, value in indices.items():
            counter_evidence = {"strength": 0.95} # Simulated strong attack
            is_refuted = self.refuter.attempt_refutation(value, counter_evidence)
            results[name] = {"refuted": is_refuted, "survival_score": 1.0 - value if is_refuted else value}
        return results
