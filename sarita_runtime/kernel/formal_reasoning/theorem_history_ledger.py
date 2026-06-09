from .reasoning_ledger import ReasoningLedger

class TheoremHistoryLedger(ReasoningLedger):
    """
    Ledger for storing the lifecycle and derivation history of theorems.
    """
    def record_theorem(self, theorem_data):
        entry = {
            "type": "THEOREM_DEFINITION",
            "theorem_id": theorem_data["theorem_id"],
            "conclusion": theorem_data["derived_conclusion"],
            "chain_length": theorem_data["proof_length"],
            "timestamp": theorem_data["timestamp"]
        }
        self._write(entry)
