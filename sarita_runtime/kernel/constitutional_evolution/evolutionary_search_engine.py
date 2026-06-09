class EvolutionarySearchEngine:
    """
    Algorithm implementing genetic search over constitutional genomes.
    """
    def __init__(self, evolutionary_engine, fitness_engine):
        self.evolutionary_engine = evolutionary_engine
        self.fitness_engine = fitness_engine

    def perform_search(self, start_genome, target_fitness=0.95, max_generations=5):
        """
        Iteratively evolves the population until target fitness is met or limit reached.
        """
        current_population = [start_genome]
        search_history = []

        for gen in range(max_generations):
            # Evolve one step
            current_population = self.evolutionary_engine.run_evolution_cycle(
                current_population[0], cycles=1, variants_per_cycle=20
            )

            # Check best fitness
            best_genome = current_population[0]
            fitness = self.fitness_engine.evaluate_fitness(best_genome)
            search_history.append(fitness["gcfi"])

            if fitness["gcfi"] >= target_fitness:
                break

        return search_history
