import json
import time

class RuntimeIntegrityLedger:
    """
    Persistent ledger for all execution and state attestation events (Phase 85.6).
    """
    def __init__(self, ledger_path="/tmp/runtime_integrity.json"):
        self.ledger_path = ledger_path
        self.entries = []

    def record_attestation(self, attestation):
        entry = {
            "type": "ATTESTATION",
            "component": attestation.component_id,
            "hw_sig": attestation.hardware_sig,
            "timestamp": attestation.timestamp
        }
        self.entries.append(entry)
        self._persist()

    def record_state_certification(self, certificate):
        entry = {
            "type": "STATE_CERT",
            "state_domain": certificate.state_type,
            "hash": certificate.state_hash,
            "hw_sig": certificate.hardware_sig,
            "timestamp": certificate.certified_at
        }
        self.entries.append(entry)
        self._persist()

    def _persist(self):
        with open(self.ledger_path, "w") as f:
            json.dump(self.entries, f, indent=4)
