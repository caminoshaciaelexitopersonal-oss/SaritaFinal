import hashlib

class RuntimeLedger:
    """
    Append-only ledger for recording meta-evolutionary events with causal chaining.
    """
    def __init__(self):
        self.events = []
        self.last_hash = "0" * 64

    def record_event(self, event_type, data):
        timestamp = data.get("timestamp", 0)
        payload = str(data).encode()
        current_hash = hashlib.sha256(self.last_hash.encode() + payload).hexdigest()

        event_record = {
            "type": event_type,
            "data": data,
            "parent_hash": self.last_hash,
            "hash": current_hash
        }

        self.events.append(event_record)
        self.last_hash = current_hash
        return current_hash

    def get_last_event(self):
        if not self.events:
            return None
        return self.events[-1]
