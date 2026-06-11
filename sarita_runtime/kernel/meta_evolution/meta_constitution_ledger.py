import time
import json

class MetaEvolutionLedger:
    """
    Base ledger for meta-evolutionary events.
    """
    def __init__(self, name="MetaEvolutionLedger"):
        self.name = name
        self.entries = []

    def record(self, event_type, data):
        entry = {
            "timestamp": time.time(),
            "event_type": event_type,
            "data": data
        }
        self.entries.append(entry)
        # In real implementation, this would persist to SQLite with SHA-256 chaining
        return entry

    def record_rejection(self, attack_name, reason):
        self.record("REJECTION", {"attack": attack_name, "reason": reason})

class MetaConstitutionLedger(MetaEvolutionLedger):
    def record_meta_constitution(self, meta):
        self.record("META_CONSTITUTION_CREATED", meta.to_dict())
