import hashlib
import time

class MetaGovernanceLedger:
    """Base scientific ledger with SHA-256 causal chaining for meta-governance."""
    def __init__(self, ledger_type):
        self.ledger_type = ledger_type
        self.entries = []
        self.last_hash = "0" * 64

    def record(self, data):
        timestamp = time.time()
        payload = {
            "type": self.ledger_type,
            "data": data,
            "timestamp": timestamp,
            "parent_hash": self.last_hash
        }
        h = hashlib.sha256(str(payload).encode()).hexdigest()
        payload["hash"] = h
        self.entries.append(payload)
        self.last_hash = h
        return h

class MetaConstitutionLedger(MetaGovernanceLedger):
    def __init__(self):
        super().__init__("META_CONSTITUTION")

class AxiomLedger(MetaGovernanceLedger):
    def __init__(self):
        super().__init__("AXIOM_GOVERNANCE")

class ConstitutionalLegitimacyLedger(MetaGovernanceLedger):
    def __init__(self):
        super().__init__("CONSTITUTIONAL_LEGITIMACY")

class PrincipleTraceabilityLedger(MetaGovernanceLedger):
    def __init__(self):
        super().__init__("PRINCIPLE_TRACEABILITY")

class MetaSovereigntyLedger(MetaGovernanceLedger):
    def __init__(self):
        super().__init__("META_SOVEREIGNTY")
