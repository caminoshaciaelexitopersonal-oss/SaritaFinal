from .learning_policy_validator import LearningPolicyValidator
from .adaptation_strategy_evaluator import AdaptationStrategyEvaluator
from .learning_bias_detector import LearningBiasDetector

class MetaLearningGovernanceEngine:
    def __init__(self):
        self.policy_validator = LearningPolicyValidator()
        self.strategy_evaluator = AdaptationStrategyEvaluator()
        self.bias_detector = LearningBiasDetector()

    def audit_learning(self, policy, strategy, logs):
        valid_policy = self.policy_validator.validate_policy(policy)
        bias = self.bias_detector.detect_bias(logs)
        return {"policy_compliant": valid_policy, "bias_profile": bias}
