import hashlib
import json
import time

class CausalRevisionLedger:
    def __init__(self):
        self.ledger = []
        self.current_hash = "0" * 64

    def record_revision(self, model_id, previous_path, revised_path, improvement_score, parent_hash=None):
        timestamp = time.time()
        entry = {
            "timestamp": timestamp,
            "model_id": model_id,
            "previous_path": previous_path,
            "revised_path": revised_path,
            "improvement_score": improvement_score,
            "parent_hash": parent_hash or self.current_hash
        }

        entry_json = json.dumps(entry, sort_keys=True).encode()
        entry_hash = hashlib.sha256(entry_json).hexdigest()

        entry["hash"] = entry_hash
        self.ledger.append(entry)
        self.current_hash = entry_hash
        return entry_hash
