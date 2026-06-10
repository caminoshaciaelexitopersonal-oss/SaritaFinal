from .constitutional_evolution_ledger import ConstitutionalEvolutionLedger

class ConstitutionalFitnessLedger(ConstitutionalEvolutionLedger):
    """
    Ledger for recording fitness evaluation results for genomes.
    """
    def record_fitness(self, genome_id, fitness_data):
        self._write({
            "type": "FITNESS_EVALUATION",
            "genome_id": genome_id,
            "gcfi": fitness_data["gcfi"],
            "sub_metrics": fitness_data["metrics"]
        })
