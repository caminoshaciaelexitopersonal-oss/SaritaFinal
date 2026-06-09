class ConstitutionalExplorer:
    """
    Explores the constitutional landscape to detect local and global optima.
    """
    def __init__(self, fitness_engine, mutation_engine):
        self.fitness_engine = fitness_engine
        self.mutation_engine = mutation_engine

    def explore_landscape(self, seed_genome, radius=5):
        """
        Samples the neighborhood around a seed genome to map the fitness landscape.
        """
        neighborhood = []
        for i in range(radius):
            neighbor = self.mutation_engine.mutate(seed_genome)
            fitness = self.fitness_engine.evaluate_fitness(neighbor)
            neighborhood.append({
                "id": neighbor.genome_id,
                "fitness": fitness["gcfi"]
            })
        return neighborhood
