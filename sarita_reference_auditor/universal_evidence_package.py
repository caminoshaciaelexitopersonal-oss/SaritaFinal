import json
import hashlib
import time

class UniversalEvidencePackage:
    """
    Standardized, language-agnostic format for SARITA evidence (SUEP).
    Designed for consumption by third-party reference auditors.
    """
    def __init__(self, state: dict, events: list):
        self.package = {
            "suep_version": "2.0",
            "metadata": {
                "timestamp": time.time(),
                "producer": "SARITA_CORE",
                "schema_hash": self._calculate_schema_hash()
            },
            "payload": {
                "initial_state": state,
                "event_log": events
            }
        }

    def _calculate_schema_hash(self):
        # Hash of the expected SUEP schema to detect protocol drift
        return hashlib.sha256(b"SUEP_SCHEMA_V2").hexdigest()

    def serialize(self):
        return json.dumps(self.package, sort_keys=True)
