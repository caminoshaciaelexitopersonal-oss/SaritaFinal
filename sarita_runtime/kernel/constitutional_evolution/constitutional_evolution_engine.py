import uuid
from .constitutional_genome import ConstitutionalGenome

class ConstitutionalEvolutionEngine:
    """
    Manages the lifecycle of constitutional variant generation and selection.
    """
    def __init__(self, mutation_engine, crossover_engine, selection_engine, fitness_engine):
        self.mutation_engine = mutation_engine
        self.crossover_engine = crossover_engine
        self.selection_engine = selection_engine
        self.fitness_engine = fitness_engine

    def run_evolution_cycle(self, root_genome, cycles=1, variants_per_cycle=100):
        population = [root_genome]

        for _ in range(cycles):
            # 1. Generate variants
            variants = []
            for i in range(variants_per_cycle):
                # Apply mutation or crossover
                if i % 2 == 0:
                    child = self.mutation_engine.mutate(root_genome)
                else:
                    # In a real cycle we'd cross over random parents
                    child = self.crossover_engine.crossover(root_genome, root_genome)
                variants.append(child)

            # 2. Evaluate fitness
            scored_variants = []
            for v in variants:
                fitness = self.fitness_engine.evaluate_fitness(v)
                scored_variants.append((v, fitness))

            # 3. Selection
            population = self.selection_engine.select_next_generation(scored_variants)

        return population
