import json
import time

class CryptographicGovernanceLedger:
    """
    Persistent ledger for all key and certificate management events (Phase 84.6).
    """
    def __init__(self, ledger_path="/tmp/crypto_gov_ledger.json"):
        self.ledger_path = ledger_path
        self.entries = []

    def record_event(self, event_type: str, actor: str, details: dict):
        entry = {
            "timestamp": time.time(),
            "event_type": event_type, # KEY_CREATION, KEY_ROTATION, KEY_RETIREMENT, QUORUM_REFORM
            "actor": actor,
            "details": details
        }
        self.entries.append(entry)
        self._persist()

    def _persist(self):
        with open(self.ledger_path, "w") as f:
            json.dump(self.entries, f, indent=4)

class KeyHistoryLedger(CryptographicGovernanceLedger):
    """Specific history of key transitions."""
    pass
