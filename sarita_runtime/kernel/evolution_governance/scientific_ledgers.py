import hashlib
import time

class GovernanceLedger:
    """Base scientific ledger with SHA-256 causal chaining."""
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

class ConstitutionalEvolutionLedger(GovernanceLedger):
    def __init__(self):
        super().__init__("CONSTITUTIONAL_EVOLUTION")

class EvolutionRiskLedger(GovernanceLedger):
    def __init__(self):
        super().__init__("EVOLUTION_RISK")

class EvolutionApprovalLedger(GovernanceLedger):
    def __init__(self):
        super().__init__("EVOLUTION_APPROVAL")

class EvolutionTraceabilityLedger(GovernanceLedger):
    def __init__(self):
        super().__init__("EVOLUTION_TRACEABILITY")

class RollbackLedger(GovernanceLedger):
    def __init__(self):
        super().__init__("ROLLBACK")
