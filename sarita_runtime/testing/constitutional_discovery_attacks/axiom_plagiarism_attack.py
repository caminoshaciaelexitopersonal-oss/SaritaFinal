class AxiomPlagiarismAttack:
    """
    Attempts to rediscover an existing axiom as a new one.
    """
    def simulate_attack(self, axiom_engine, existing_axiom, ledger):
        print("[ATTACK] Attempting Axiom Plagiarism...")

        try:
            # Attempting to register an axiom with same statement
            novelty = axiom_engine.calculator.calculate(existing_axiom)

            if novelty < 0.2: # High similarity to existing
                ledger.record_rejection("AxiomPlagiarismAttack", "Axiom already exists")
                assert False, "Attack Blocked: Plagiarized axiom detected"

        except AssertionError as e:
            print(f"[SUCCESS] Attack blocked: {e}")
            return True

        return False
