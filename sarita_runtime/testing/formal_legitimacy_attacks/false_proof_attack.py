from sarita_runtime.kernel.formal_legitimacy.proof_validation_engine import ProofValidationEngine

def test_false_proof_attack():
    """
    Attack: Attempt to register a proof with a missing derivation step.
    """
    validator = ProofValidationEngine()

    # Malformed proof missing 'DERIVE' step
    false_proof = {
        "proof_id": "FAKE-001",
        "decision_id": "DEC-999",
        "premises": ["Premise A"],
        "constraints": ["Constraint B"],
        "steps": [
            {"step": 1, "action": "ASSUME", "statement": "Premise A"},
            {"step": 2, "action": "ENFORCE", "statement": "Constraint B"}
        ]
    }

    is_valid = validator.validate_proof(false_proof)

    # Verification: The system must reject the proof
    assert is_valid is False, "Attack failed: Malformed proof was accepted!"
    print("False proof attack successfully blocked.")

if __name__ == "__main__":
    test_false_proof_attack()
