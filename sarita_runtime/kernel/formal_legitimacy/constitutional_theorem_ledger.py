from .proof_ledger import ProofLedger

class ConstitutionalTheoremLedger(ProofLedger):
    """
    Ledger for storing all globally proven constitutional theorems.
    """
    def record_theorem(self, theorem: dict):
        self.record_entry({
            "type": "CONSTITUTIONAL_THEOREM",
            "theorem": theorem
        })
