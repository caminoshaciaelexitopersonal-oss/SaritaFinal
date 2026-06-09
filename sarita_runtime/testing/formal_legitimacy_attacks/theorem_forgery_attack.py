from sarita_runtime.kernel.formal_legitimacy.constitutional_theorem_registry import ConstitutionalTheoremRegistry
from sarita_runtime.kernel.formal_legitimacy.proof_validation_engine import ProofValidationEngine

def test_theorem_forgery_attack():
    """
    Attack: Attempt to directly inject a fake theorem into the registry.
    """
    validator = ProofValidationEngine()
    registry = ConstitutionalTheoremRegistry(validator=validator)

    # Malicious forged proof without required structure or verification
    fake_proof = {
        "proof_id": "FORGED-001",
        "decision_id": "DEC-666",
        "steps": [{"step": 1, "action": "DERIVE", "statement": "I am legit."}]
    }

    # Registration must be REJECTED by the registry's internal validator
    success = registry.register_theorem(fake_proof)

    # Verification: Registration must fail
    assert success is False, "Attack failed: Forged theorem was successfully registered!"
    assert "FORGED-001" not in registry.theorems, "Attack failed: Forged theorem exists in registry!"

    print("Theorem forgery attack successfully blocked by Registry validation.")

if __name__ == "__main__":
    test_theorem_forgery_attack()
