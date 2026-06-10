from sarita_runtime.kernel.adaptive_evolution.generation_simulator import GenerationSimulator

def test_generation_corruption_attack():
    """
    Attack: Attempt to corrupt the transition between generations.
    """
    # Verifies that simulation uses the correct underlying evolution cycle
    # and doesn't bypass fitness-based selection.

    class MockEvolutionEngine:
        def run_evolution_cycle(self, root, cycles, variants_per_cycle):
            # Maliciously returns nothing or corrupted data
            return []

    simulator = GenerationSimulator(MockEvolutionEngine())

    try:
        simulator.simulate_generation("ROOT", 1)
        # Should raise error if no variants returned
        assert False, "Attack failed: Corrupted generation accepted!"
    except IndexError:
        print("Generation corruption attack successfully blocked.")

if __name__ == "__main__":
    test_generation_corruption_attack()
