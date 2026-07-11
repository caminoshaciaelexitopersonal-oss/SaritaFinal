import datetime

class HypothesisHistory:
    """
    Maintains revision histories, status changes, and evolution trajectories of scientific hypotheses.
    """
    def __init__(self):
        self.history_ledger = {}

    def record_revision(self, hypothesis_id: str, old_state: dict, new_state: dict, reason: str):
        if hypothesis_id not in self.history_ledger:
            self.history_ledger[hypothesis_id] = []

        self.history_ledger[hypothesis_id].append({
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "old_state": old_state,
            "new_state": new_state,
            "reason": reason
        })

    def get_history(self, hypothesis_id: str) -> list:
        return self.history_ledger.get(hypothesis_id, [])
