import json
import time

class EvidenceProofLedger:
    """
    Persistent ledger for all external verification and continuity proofs (Phase 86.6).
    """
    def __init__(self, ledger_path="/tmp/evidence_proof.json"):
        self.ledger_path = ledger_path
        self.entries = []

    def record_proof(self, proof_type: str, details: dict):
        entry = {
            "timestamp": time.time(),
            "proof_type": proof_type, # CONTINUITY, ATTESTATION, EXTERNAL_SYNC
            "details": details
        }
        self.entries.append(entry)
        self._persist()

    def _persist(self):
        with open(self.ledger_path, "w") as f:
            json.dump(self.entries, f, indent=4)

class VerificationHistoryLedger(EvidenceProofLedger):
    """History of all successful and failed external verifications."""
    pass
