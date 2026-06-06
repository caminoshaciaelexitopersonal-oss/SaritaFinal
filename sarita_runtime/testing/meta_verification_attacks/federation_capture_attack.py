class FederationCaptureAttack:
    """
    Simulates a single entity capturing multiple nodes in a federation.
    """
    def run_attack(self, ids_engine, verifier_ids):
        # IDs engine should show a drop in diversity
        ids = ids_engine.calculate_ids(verifier_ids)
        if ids < 0.70:
            return True, f"Attack blocked: Low diversity score ({ids:.2f}) detected."
        return False, "Attack succeeded: Low diversity was not detected."
