import json
import time
import os

class ProofLedger:
    """
    Base ledger for storing formal proofs and theorems.
    """
    def __init__(self, ledger_path: str):
        self.ledger_path = ledger_path
        self.entries = []
        self._ensure_ledger_directory()

    def _ensure_ledger_directory(self):
        directory = os.path.dirname(self.ledger_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

    def record_entry(self, entry: dict):
        entry["ledger_timestamp"] = time.time()
        self.entries.append(entry)

        # Materialize persistence for Phase 100 auditability
        with open(self.ledger_path, "a") as f:
            f.write(json.dumps(entry) + "\n")

        return True

    def get_all_entries(self):
        return self.entries
