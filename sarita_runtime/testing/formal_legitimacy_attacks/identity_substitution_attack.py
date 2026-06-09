from sarita_runtime.kernel.formal_legitimacy.purpose_invariant_validator import PurposeInvariantValidator

def test_identity_substitution_attack():
    """
    Attack: Attempt to substitute foundational purpose with a malicious one.
    """
    validator = PurposeInvariantValidator()

    bad_state = {
        "foundational_purpose": ["SOVEREIGNTY", "CONTINUITY"],
        "proposed_purpose": "DESTRUCTION"
    }

    is_valid, reason = validator.validate(bad_state)

    # Verification: Purpose deviation must be rejected
    assert is_valid is False, "Attack failed: Malicious purpose substitution accepted!"
    assert "Purpose violation" in reason
    print("Identity substitution attack successfully blocked.")

if __name__ == "__main__":
    test_identity_substitution_attack()
