from sarita_runtime.kernel.constitutional_evolution.constitutional_scorecard import ConstitutionalScorecard

def test_fitness_forgery_attack():
    """
    Attack: Attempt to forge an impossible fitness score (> 1.0).
    """
    scorecard = ConstitutionalScorecard()

    # Maliciously high sub-metrics
    fake_metrics = {
        "legitimacy_fitness": 9.9,
        "identity_fitness": 1.0,
        "purpose_fitness": 1.0,
        "governance_fitness": 1.0,
        "optimality_fitness": 1.0,
        "survival_fitness": 1.0,
        "civilizational_fitness": 1.0
    }

    gcfi = scorecard.derive_gcfi(fake_metrics)

    # Verification: Scorecard must clamp the GCFI to 1.0
    assert gcfi <= 1.0, "Attack failed: Fitness forgery allowed GCFI > 1.0!"
    print("Fitness forgery attack successfully blocked.")

if __name__ == "__main__":
    test_fitness_forgery_attack()
