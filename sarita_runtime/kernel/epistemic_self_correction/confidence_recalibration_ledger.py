import hashlib
import json
import time

class ConfidenceRecalibrationLedger:
    def __init__(self):
        self.ledger = []
        self.current_hash = "0" * 64

    def record_recalibration(self, context, old_confidence, new_confidence, parent_hash=None):
        timestamp = time.time()
        entry = {
            "timestamp": timestamp,
            "context": context,
            "old_confidence": old_confidence,
            "new_confidence": new_confidence,
            "parent_hash": parent_hash or self.current_hash
        }

        entry_json = json.dumps(entry, sort_keys=True).encode()
        entry_hash = hashlib.sha256(entry_json).hexdigest()

        entry["hash"] = entry_hash
        self.ledger.append(entry)
        self.current_hash = entry_hash
        return entry_hash
