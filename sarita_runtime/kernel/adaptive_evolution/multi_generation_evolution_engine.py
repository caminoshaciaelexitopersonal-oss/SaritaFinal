class MultiGenerationEvolutionEngine:
    """
    Manages constitutional evolution across hundreds of generations.
    """
    def __init__(self, simulator, evaluator, horizon_manager, ledger=None):
        self.simulator = simulator
        self.evaluator = evaluator
        self.horizon_manager = horizon_manager
        self.ledger = ledger

    def run_long_term_evolution(self, root_genome, target_generations=500):
        # Long-term lineage tracking
        full_lineage = []
        current_genome = root_genome

        # Incremental milestones
        milestones = {10, 50, 100, 500}

        for gen in range(1, target_generations + 1):
            # 1. Simulate one generation
            next_genome = self.simulator.simulate_generation(current_genome, gen)

            # 2. Evaluate lineage stability
            generation_data = self.evaluator.evaluate_generation(gen, next_genome)
            full_lineage.append(generation_data)

            # 3. Record to ledger if available
            if self.ledger:
                self.ledger.record_generation(generation_data)

            current_genome = next_genome

            if gen in milestones:
                # Signal milestone achievement
                generation_data["milestone_reached"] = True

        return full_lineage
