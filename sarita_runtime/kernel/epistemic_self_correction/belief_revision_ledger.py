import hashlib
import json
import time

class BeliefRevisionLedger:
    def __init__(self):
        self.ledger = []
        self.current_hash = "0" * 64

    def record_revision(self, belief_id, old_state, new_state, causal_evidence, parent_hash=None):
        timestamp = time.time()
        entry = {
            "timestamp": timestamp,
            "belief_id": belief_id,
            "old_state": old_state,
            "new_state": new_state,
            "causal_evidence": causal_evidence,
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

    def verify_integrity(self):
        for i in range(1, len(self.ledger)):
            prev_hash = self.ledger[i-1]["hash"]
            if self.ledger[i]["parent_hash"] != prev_hash:
                return False
        return True
