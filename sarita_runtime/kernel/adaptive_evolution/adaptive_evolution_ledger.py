import json
import time
import os

class AdaptiveEvolutionLedger:
    """
    Base ledger for recording multi-generational and adaptive evolution data.
    """
    def __init__(self, ledger_path):
        self.ledger_path = ledger_path
        self._ensure_directory()

    def _ensure_directory(self):
        directory = os.path.dirname(self.ledger_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

    def _write(self, entry):
        entry["ledger_timestamp"] = time.time()
        with open(self.ledger_path, "a") as f:
            f.write(json.dumps(entry) + "\n")
