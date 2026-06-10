from sarita_runtime.kernel.formal_legitimacy.decision_replay_validator import DecisionReplayValidator

def test_decision_replay_attack():
    """
    Attack: Attempt to submit a non-deterministic decision.
    """
    validator = DecisionReplayValidator()

    non_det_decision = {
        "id": "DEC-X",
        "is_deterministic": False # Maliciously non-deterministic
    }

    is_valid = validator.validate_replay(non_det_decision)

    # Verification: Non-deterministic decisions must fail replay validation
    assert is_valid is False, "Attack failed: Non-deterministic decision accepted!"
    print("Decision replay attack successfully blocked.")

if __name__ == "__main__":
    test_decision_replay_attack()
