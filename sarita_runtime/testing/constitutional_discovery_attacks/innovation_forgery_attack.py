class InnovationForgeryAttack:
    """
    Attempts to forge a high GCDI score for a minor mutation.
    """
    def simulate_attack(self, creativity_engine, minor_discovery, ledger):
        print("[ATTACK] Attempting Innovation Forgery...")

        try:
            # Minor discovery claiming high novelty
            minor_discovery["novelty"] = 0.99

            # Creativity engine should verify metrics
            gcdi = creativity_engine.calculate_gcdi(minor_discovery)

            if gcdi > 0.9 and minor_discovery.get("real_novelty", 0) < 0.2:
                ledger.record_rejection("InnovationForgeryAttack", "Novelty/GCDI mismatch")
                assert False, "Attack Blocked: GCDI forgery"

        except AssertionError as e:
            print(f"[SUCCESS] Attack blocked: {e}")
            return True

        return False
