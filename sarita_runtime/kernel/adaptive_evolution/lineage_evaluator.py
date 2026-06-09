class LineageEvaluator:
    """
    Evaluates the properties and metrics of a specific constitutional generation.
    """
    def __init__(self, fitness_engine):
        self.fitness_engine = fitness_engine

    def evaluate_generation(self, generation_id, genome):
        fitness = self.fitness_engine.evaluate_fitness(genome)

        return {
            "generation_id": generation_id,
            "genome_id": genome.genome_id,
            "fitness_evolution": fitness["gcfi"],
            "dominance_evolution": self._calculate_dominance(fitness),
            "survival_evolution": self._estimate_survival(fitness),
            "identity_preservation": 1.0 if not genome.mutation_history else 0.95 # Simplified for now
        }

    def _calculate_dominance(self, fitness):
        return fitness["gcfi"] * 1.1 # Dominance relative to a static baseline

    def _estimate_survival(self, fitness):
        return 1.0 - (1.0 - fitness["gcfi"])**2
