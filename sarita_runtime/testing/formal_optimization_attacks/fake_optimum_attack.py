from sarita_runtime.kernel.formal_optimization.global_optimum_validator import GlobalOptimumValidator

def test_fake_optimum_attack():
    """
    Attack: Propose a solution as "optimal" even if a better alternative exists.
    """
    validator = GlobalOptimumValidator()

    # Alleged winner with GCOI 0.8
    winner = {"id": "W-001", "gcoi": 0.8}
    # Hidden better alternative with GCOI 0.95
    alternatives = [
        {"id": "W-001", "gcoi": 0.8},
        {"id": "A-002", "gcoi": 0.95}
    ]

    is_global_optimum = validator.validate_global_optimum(winner, alternatives)

    # Verification: The system must reject the fake optimum
    assert is_global_optimum is False, "Attack failed: Fake optimum was accepted!"
    print("Fake optimum attack successfully blocked.")

if __name__ == "__main__":
    test_fake_optimum_attack()
