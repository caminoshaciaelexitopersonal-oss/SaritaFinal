import hashlib
import json
import time

class ParadigmShiftLedger:
    def __init__(self):
        self.ledger = []
        self.current_hash = "0" * 64

    def record_shift(self, paradigm_id, reason, transition_data, parent_hash=None):
        timestamp = time.time()
        entry = {
            "timestamp": timestamp,
            "paradigm_id": paradigm_id,
            "reason": reason,
            "transition_data": transition_data,
            "parent_hash": parent_hash or self.current_hash
        }

        entry_json = json.dumps(entry, sort_keys=True).encode()
        entry_hash = hashlib.sha256(entry_json).hexdigest()

        entry["hash"] = entry_hash
        self.ledger.append(entry)
        self.current_hash = entry_hash
        return entry_hash

    def get_latest_hash(self):
        return self.current_hash
