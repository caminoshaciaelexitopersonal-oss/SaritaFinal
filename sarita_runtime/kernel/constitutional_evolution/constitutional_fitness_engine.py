class ConstitutionalFitnessEngine:
    """
    Orchestrates the evaluation of constitutional variant fitness.
    """
    def __init__(self, evaluator, scorecard):
        self.evaluator = evaluator
        self.scorecard = scorecard

    def evaluate_fitness(self, genome):
        metrics = self.evaluator.calculate_sub_fitness(genome)
        gcfi = self.scorecard.derive_gcfi(metrics)

        return {
            "genome_id": genome.genome_id,
            "metrics": metrics,
            "gcfi": gcfi
        }
