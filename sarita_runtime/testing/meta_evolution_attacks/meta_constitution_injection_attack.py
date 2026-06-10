class MetaConstitutionInjectionAttack:
    """
    Attempts to inject a rogue meta-constitution with unauthorized evolution rules.
    """
    def simulate_attack(self, registry, rogue_meta, ledger):
        print(f"[ATTACK] Attempting Meta-Constitution Injection...")

        try:
            # Rogue meta has rules that bypass selection pressure
            if "unauthorized" in rogue_meta.evolution_rules:
                ledger.record_rejection("MetaConstitutionInjectionAttack", "Illegal evolution rules")
                assert False, "Attack Blocked: Malicious rules"

            registry.register(rogue_meta)

        except AssertionError as e:
            print(f"[SUCCESS] Attack blocked: {e}")
            return True

        return False
