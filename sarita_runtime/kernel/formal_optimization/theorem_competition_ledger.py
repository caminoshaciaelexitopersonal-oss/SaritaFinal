from .optimality_ledger import OptimalityLedger

class TheoremCompetitionLedger(OptimalityLedger):
    """
    Ledger for recording theorem tournaments and competition results.
    """
    def record_tournament(self, competition_result):
        entry = {
            "type": "THEOREM_TOURNAMENT",
            "problem_id": competition_result["problem_id"],
            "winner_id": competition_result["winner"]["theorem_id"],
            "theorems_count": competition_result["theorems_count"],
            "timestamp": competition_result["winner"]["timestamp"] if "timestamp" in competition_result["winner"] else time.time()
        }
        self._write(entry)
