class GlobalOptimumSeeker:
    """
    Mathematical solver for the global constitutional optimum.
    """
    def __init__(self, fitness_engine):
        self.fitness_engine = fitness_engine

    def seek_optimum(self, variants):
        """
        Identifies the absolute best variant from a provided set.
        """
        if not variants:
            return None

        scored = []
        for v in variants:
            f = self.fitness_engine.evaluate_fitness(v)
            scored.append((v, f["gcfi"]))

        return max(scored, key=lambda x: x[1])[0]
