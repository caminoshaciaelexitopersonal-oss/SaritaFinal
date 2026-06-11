class PolicyQualityValidator:
    """
    Validates the quality of a universal policy.
    """
    def validate_quality(self, policy):
        """
        Ensures the policy meets quality targets for resilience and impact.
        """
        return policy.get("quality_score", 0.0) >= 0.90
