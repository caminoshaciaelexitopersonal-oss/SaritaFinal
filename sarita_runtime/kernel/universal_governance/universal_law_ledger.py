import time

class UniversalLawLedger:
    """
    Ledger for recording universal laws and scientific discoveries.
    """
    def __init__(self, name="UniversalScienceLedger"):
        self.name = name
        self.entries = []

    def record(self, event_type, data):
        entry = {
            "timestamp": time.time(),
            "event_type": event_type,
            "data": data
        }
        self.entries.append(entry)
        return entry

    def record_law_discovery(self, law):
        self.record("LAW_DISCOVERED", law)

    def record_law_registration(self, law):
        self.record("LAW_REGISTERED", law)

    def record_rejection(self, attack_name, reason):
        self.record("REJECTION", {"attack": attack_name, "reason": reason})

class InvariantLedger(UniversalLawLedger):
    def record_invariant(self, invariant):
        self.record("INVARIANT_CERTIFIED", invariant)

class CausalityLedger(UniversalLawLedger):
    def record_causal_path(self, path):
        self.record("CAUSAL_PATH_VERIFIED", path)

class UniversalTheoremLedger(UniversalLawLedger):
    def record_theorem(self, theorem):
        self.record("THEOREM_CERTIFIED", theorem)
