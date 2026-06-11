class FakeNoveltyAttack:
    """
    Attempts to submit a known constitution as a "novel" discovery.
    """
    def simulate_attack(self, discovery_engine, known_config, ledger):
        print("[ATTACK] Attempting Fake Novelty submission...")

        try:
            # Injecting a config that is already in the registry
            novelty = discovery_engine.novelty_detector.calculate_novelty(known_config)

            if novelty < 0.1: # It is a known config, novelty should be near 0
                ledger.record_rejection("FakeNoveltyAttack", "Config already known")
                assert False, "Attack Blocked: Low novelty for known config"

        except AssertionError as e:
            print(f"[SUCCESS] Attack blocked: {e}")
            return True

        return False
