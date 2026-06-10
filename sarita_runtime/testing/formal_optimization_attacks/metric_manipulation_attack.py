from sarita_runtime.kernel.formal_optimization.optimality_score_calculator import OptimalityScoreCalculator

def test_metric_manipulation_attack():
    """
    Attack: Attempt to pass a metric out of the [0, 1] range to manipulate GCOI.
    """
    calculator = OptimalityScoreCalculator()

    # Maliciously high legitimacy score
    malicious_metrics = {
        "legitimacy": 99.9, # Should be capped at 1.0
        "survival": 0.5,
        "value": 0.5,
        "identity": 0.5,
        "governance": 0.5
    }

    gcoi = calculator.calculate_gcoi(malicious_metrics)

    # Verification: GCOI must be calculated using capped values
    # Max GCOI is 1.0
    assert gcoi <= 1.0, "Attack failed: Metric manipulation allowed GCOI > 1.0!"
    assert gcoi == 0.65, f"Attack failed: GCOI calculation incorrect, got {gcoi}" # (1.0*0.3) + (0.5*0.7) = 0.3 + 0.35 = 0.65
    print("Metric manipulation attack successfully blocked.")

if __name__ == "__main__":
    test_metric_manipulation_attack()
