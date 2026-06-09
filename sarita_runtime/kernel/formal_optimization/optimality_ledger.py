import json
import time
import os

class OptimalityLedger:
    """
    Hardened ledger for recording optimality proofs and metrics.
    """
    def __init__(self, ledger_path):
        self.ledger_path = ledger_path
        self._ensure_directory()

    def _ensure_directory(self):
        directory = os.path.dirname(self.ledger_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

    def record_optimality_proof(self, proof):
        entry = {
            "type": "OPTIMALITY_PROOF",
            "proof_id": proof["proof_id"],
            "decision_id": proof["decision_id"],
            "winner_id": proof["winner_selection"],
            "timestamp": time.time()
        }
        self._write(entry)

    def _write(self, entry):
        with open(self.ledger_path, "a") as f:
            f.write(json.dumps(entry) + "\n")
