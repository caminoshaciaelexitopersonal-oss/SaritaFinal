from sarita_runtime.kernel.formal_legitimacy.causal_proof_validator import CausalProofValidator

def test_causal_chain_attack():
    """
    Attack: Inject a non-monotonic causal step in a proof.
    """
    validator = CausalProofValidator()

    broken_proof = {
        "steps": [
            {"step": 1, "action": "ASSUME", "statement": "A"},
            {"step": 3, "action": "ENFORCE", "statement": "B"},
            {"step": 2, "action": "DERIVE", "statement": "C"} # Time travel step
        ]
    }

    is_valid = validator.validate_proof(broken_proof)

    # Verification: Non-monotonic steps must be rejected
    assert is_valid is False, "Attack failed: Broken causal chain was accepted!"
    print("Causal chain attack successfully blocked.")

if __name__ == "__main__":
    test_causal_chain_attack()
