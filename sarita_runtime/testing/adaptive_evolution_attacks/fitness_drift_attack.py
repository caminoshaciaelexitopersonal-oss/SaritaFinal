from sarita_runtime.kernel.adaptive_evolution.lineage_evaluator import LineageEvaluator

def test_fitness_drift_attack():
    """
    Attack: Claim high fitness for a genome that has experienced rapid mutation decay.
    """
    # This attack verifies that the lineage evaluator correctly calculates
    # dominance and survival based on actual fitness, not claimed state.

    class FakeFitnessEngine:
        def evaluate_fitness(self, genome):
            # Reality: Fitness is very low due to drift
            return {"gcfi": 0.2}

    evaluator = LineageEvaluator(FakeFitnessEngine())

    class MockGenome:
        genome_id = "DRIFTED-001"
        mutation_history = ["M1", "M2", "M3"]

    data = evaluator.evaluate_generation(500, MockGenome())

    # Verification: Survival probability must be low for low fitness
    assert data["survival_evolution"] < 0.5, "Attack failed: Fitness drift not detected!"
    print("Fitness drift attack successfully blocked.")

if __name__ == "__main__":
    test_fitness_drift_attack()
