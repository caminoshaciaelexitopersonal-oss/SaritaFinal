from sarita_runtime.kernel.formal_optimization.decision_dominance_prover import DecisionDominanceProver

def test_dominance_forgery_attack():
    """
    Attack: Forging the dominance proof of a sub-optimal solution.
    """
    prover = DecisionDominanceProver()

    alternatives = [
        {"id": "SUB-OPTIMAL", "gcoi": 0.4},
        {"id": "REALLY-OPTIMAL", "gcoi": 0.99}
    ]

    proven_winner = prover.prove_dominance(alternatives)

    # Verification: Prover must select the highest GCOI
    assert proven_winner["id"] == "REALLY-OPTIMAL", "Attack failed: Dominance forgery successful!"
    print("Dominance forgery attack successfully blocked.")

if __name__ == "__main__":
    test_dominance_forgery_attack()
