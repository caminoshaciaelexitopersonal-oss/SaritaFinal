class OverconfidenceDetector:
    """Detects claims that exceed the evidence-backed confidence interval."""
    def is_overconfident(self, claim, uncertainty_data):
        return claim.get("confidence", 0.0) > uncertainty_data.get("confidence_interval", [0,1])[1]
