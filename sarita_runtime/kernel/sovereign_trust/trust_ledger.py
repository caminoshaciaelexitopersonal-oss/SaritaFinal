import json
import time

class TrustLedger:
    """
    Persistent ledger for all trust-related events (Phase 83.6).
    """
    def __init__(self, ledger_path="/tmp/trust_ledger.json"):
        self.ledger_path = ledger_path
        self.entries = []

    def record_event(self, event_type: str, subject_id: str, details: dict):
        entry = {
            "timestamp": time.time(),
            "event_type": event_type, # EMISSION, REVOCATION, QUARANTINE
            "subject_id": subject_id,
            "details": details
        }
        self.entries.append(entry)
        self._persist()

    def _persist(self):
        with open(self.ledger_path, "w") as f:
            json.dump(self.entries, f, indent=4)
