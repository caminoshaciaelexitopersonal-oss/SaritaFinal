import time

class ConstitutionalJustificationRegistry:
    """
    Registry for SARITA's formal justifications of existence.
    """
    def __init__(self):
        self.justifications = {
            "SOVEREIGN_AUTONOMY": {"weight": 0.4, "status": "VALIDATED"},
            "CAUSAL_INTEGRITY": {"weight": 0.4, "status": "VALIDATED"},
            "GOVERNANCE_EFFICIENCY": {"weight": 0.2, "status": "VALIDATED"}
        }

    def get_validated_justifications(self):
        return {k: v for k, v in self.justifications.items() if v["status"] == "VALIDATED"}
