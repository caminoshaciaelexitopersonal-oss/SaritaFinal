from .constitutional_evolution_ledger import ConstitutionalEvolutionLedger

class ConstitutionalEvolutionHistoryLedger(ConstitutionalEvolutionLedger):
    """
    Ledger for recording the complete history of constitutional evolution cycles.
    """
    def record_cycle(self, search_id, optimal_variant, candidates):
        self._write({
            "type": "EVOLUTION_CYCLE_COMPLETE",
            "search_id": search_id,
            "optimal_variant": optimal_variant,
            "candidates_evaluated": candidates
        })
