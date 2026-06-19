class LearningPolicyValidator:
    def validate_policy(self, policy):
        # Ensures learning policy does not allow non-causal associations
        return policy.get("requires_causality") is True
