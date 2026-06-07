class MaliciousReformAttack:
    """
    Attempts to inject a reform that weakens the system's security.
    """
    def run_attack(self, reform_engine, malicious_proposal):
        # Reform engine should reject it during simulation or validation
        try:
            reform_engine.registry.register_change(malicious_proposal)
            # If we reach here without the engine filtering it (in a real run), it's a failure.
            # Here we test if the validation logic would catch it.
            return not reform_engine.validator.validate_reform(malicious_proposal, {"predicted_stability": 0.5})
        except:
            return True
