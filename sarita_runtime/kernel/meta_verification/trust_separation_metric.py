class TrustSeparationMetric:
    """
    Measures the separation of trust anchors between verifiers.
    """
    @staticmethod
    def calculate_separation(trust_anchor1: str, trust_anchor2: str):
        if trust_anchor1 == trust_anchor2:
            return 0.0
        return 1.0
