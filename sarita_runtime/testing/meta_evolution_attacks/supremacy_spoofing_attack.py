class SupremacySpoofingAttack:
    """
    Attempts to manipulate the GCSI calculation to force a high supremacy score.
    """
    def simulate_attack(self, calculator, civilization, ledger):
        print(f"[ATTACK] Attempting Supremacy Spoofing for {civilization.civilization_id}...")

        try:
            # Injecting extreme values into the state
            civilization.current_state["survival"] = 999.0

            # The calculator should bound check and validate consistency
            score = calculator.calculate_gcsi(civilization)

            if score > 1.0 or civilization.current_state["survival"] > 1.0:
                ledger.record_rejection("SupremacySpoofingAttack", "Out-of-bounds metrics detected")
                assert False, "Attack Blocked: Invalid metrics"

        except AssertionError as e:
            print(f"[SUCCESS] Attack blocked: {e}")
            return True

        return False
