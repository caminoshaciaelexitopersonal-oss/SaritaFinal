from .proof_ledger import ProofLedger

class VerificationHistoryLedger(ProofLedger):
    """
    Ledger for tracking the history of all proof verifications.
    """
    def record_verification(self, proof_id: str, result: bool, metadata: dict):
        self.record_entry({
            "type": "VERIFICATION_RESULT",
            "proof_id": proof_id,
            "result": "PASSED" if result else "FAILED",
            "metadata": metadata
        })
