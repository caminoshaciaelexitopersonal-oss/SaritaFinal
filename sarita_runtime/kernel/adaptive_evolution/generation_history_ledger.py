from .adaptive_evolution_ledger import AdaptiveEvolutionLedger

class GenerationHistoryLedger(AdaptiveEvolutionLedger):
    """
    Ledger for recording the full history of simulated generations.
    """
    def record_generation(self, generation_data):
        self._write({
            "type": "GENERATION_RECORD",
            "generation_id": generation_data["generation_id"],
            "genome_id": generation_data["genome_id"],
            "fitness": generation_data["fitness_evolution"]
        })
