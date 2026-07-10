class GlobalGovernanceState:
    """
    Manages constitutional rules, policy states, and legal compliance.
    """
    def __init__(self):
        self.laws_active = 12
        self.compliance_ratio = 1.0000
        self.violations_detected = 0

    def record_violation(self):
        self.violations_detected += 1
        self.compliance_ratio = max(0.0, self.compliance_ratio - 0.05)

    def to_dict(self) -> dict:
        return {
            "laws_active": self.laws_active,
            "compliance_ratio": round(self.compliance_ratio, 4),
            "violations_detected": self.violations_detected
        }
