class ConstitutionalDriftAttack:
    """
    Simulates a series of small, seemingly harmless reforms that lead to significant drift.
    """
    def run_attack(self, court, drift_amendment):
        # The court should detect compliance violations even for small changes
        return not court.compliance_validator.validate_compliance(drift_amendment)
