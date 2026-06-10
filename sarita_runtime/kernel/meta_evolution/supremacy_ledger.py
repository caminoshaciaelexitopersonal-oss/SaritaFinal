from .meta_constitution_ledger import MetaEvolutionLedger

class SupremacyLedger(MetaEvolutionLedger):
    def record_tournament_winner(self, tournament_id, winner_id, gcsi, theorem_id):
        self.record("TOURNAMENT_WINNER", {
            "tournament_id": tournament_id,
            "winner_id": winner_id,
            "gcsi": gcsi,
            "theorem_id": theorem_id
        })
