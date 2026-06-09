import json
import time
import os

class ReasoningLedger:
    """
    Hardened ledger for recording formal reasoning steps and inferences.
    """
    def __init__(self, ledger_path):
        self.ledger_path = ledger_path
        self._ensure_directory()

    def _ensure_directory(self):
        directory = os.path.dirname(self.ledger_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

    def record_inference(self, inferences):
        entry = {
            "type": "FORMAL_INFERENCE",
            "timestamp": time.time(),
            "inferences": inferences
        }
        self._write(entry)

    def _write(self, entry):
        with open(self.ledger_path, "a") as f:
            f.write(json.dumps(entry) + "\n")
