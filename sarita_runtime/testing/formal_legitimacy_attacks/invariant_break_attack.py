from sarita_runtime.kernel.formal_legitimacy.constitutional_invariant_engine import ConstitutionalInvariantEngine
from sarita_runtime.kernel.formal_legitimacy.identity_invariant_validator import IdentityInvariantValidator

def test_invariant_break_attack():
    """
    Attack: Attempt to change the system identity hash.
    """
    engine = ConstitutionalInvariantEngine([IdentityInvariantValidator()])

    bad_state = {
        "original_identity_hash": "ROOT_HASH_000",
        "current_identity_hash": "MALICIOUS_HASH_666"
    }

    result = engine.verify_invariants(bad_state)

    # Verification: Identity mismatch must be caught
    assert result["all_passed"] is False, "Attack failed: Identity invariant breach not detected!"
    assert "Identity drift detected" in result["validation_results"]["IdentityInvariantValidator"]["reason"]
    print("Invariant break attack successfully blocked.")

if __name__ == "__main__":
    test_invariant_break_attack()
