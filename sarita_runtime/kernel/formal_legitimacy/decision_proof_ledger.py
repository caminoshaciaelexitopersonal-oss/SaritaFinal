from .proof_ledger import ProofLedger

class DecisionProofLedger(ProofLedger):
    """
    Hardened ledger specifically for decision proofs.
    """
    def record_proof(self, decision_id: str, proof: dict):
        self.record_entry({
            "type": "DECISION_PROOF",
            "decision_id": decision_id,
            "proof": proof
        })
