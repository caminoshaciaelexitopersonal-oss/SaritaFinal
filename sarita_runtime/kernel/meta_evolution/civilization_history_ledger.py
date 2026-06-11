from .meta_constitution_ledger import MetaEvolutionLedger

class CivilizationHistoryLedger(MetaEvolutionLedger):
    def record_civilization_evolution(self, civ_id, generation, metrics):
        self.record("CIVILIZATION_EVOLUTION", {
            "civ_id": civ_id,
            "generation": generation,
            "metrics": metrics
        })
