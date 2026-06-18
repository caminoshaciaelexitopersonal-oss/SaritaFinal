import hashlib
import json
import time

class EpistemicFailureLedger:
    def __init__(self):
        self.ledger = []
        self.current_hash = "0" * 64

    def record_failure(self, failure_id, failure_type, analysis, lesson_learned, parent_hash=None):
        timestamp = time.time()
        entry = {
            "timestamp": timestamp,
            "failure_id": failure_id,
            "failure_type": failure_type,
            "analysis": analysis,
            "lesson_learned": lesson_learned,
            "parent_hash": parent_hash or self.current_hash
        }

        entry_json = json.dumps(entry, sort_keys=True).encode()
        entry_hash = hashlib.sha256(entry_json).hexdigest()

        entry["hash"] = entry_hash
        self.ledger.append(entry)
        self.current_hash = entry_hash
        return entry_hash
