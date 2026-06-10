from sarita_runtime.kernel.formal_optimization.dominance_validator import DominanceValidator

def test_pareto_corruption_attack():
    """
    Attack: Attempt to claim dominance for a solution that is actually dominated.
    """
    validator = DominanceValidator()
    objectives = ["legitimacy", "survival"]

    # Sol A is strictly worse than Sol B
    sol_a = {"legitimacy": 0.5, "survival": 0.5}
    sol_b = {"legitimacy": 0.8, "survival": 0.9}

    # Claim: A dominates B
    a_dominates_b = validator.validate_dominance(sol_a, sol_b, objectives)

    # Verification: Dominance claim must be false
    assert a_dominates_b is False, "Attack failed: Dominated solution claimed dominance!"
    print("Pareto corruption attack successfully blocked.")

if __name__ == "__main__":
    test_pareto_corruption_attack()
