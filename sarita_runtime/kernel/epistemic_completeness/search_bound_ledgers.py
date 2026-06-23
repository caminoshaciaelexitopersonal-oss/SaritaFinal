import hashlib
import time

class EpistemicLedgerBase:
    """Base scientific ledger with SHA-256 causal chaining for epistemic proofs."""
    def __init__(self, ledger_type):
        self.ledger_type = ledger_type
        self.entries = []
        self.last_hash = "0" * 64

    def record_bound(self, data):
        timestamp = time.time()
        payload = {
            "bound_type": self.ledger_type,
            "data": data,
            "timestamp": timestamp,
            "parent_hash": self.last_hash
        }
        h = hashlib.sha256(str(payload).encode()).hexdigest()
        payload["hash"] = h
        self.entries.append(payload)
        self.last_hash = h
        return h

class SearchBoundLedger(EpistemicLedgerBase):
    def __init__(self):
        super().__init__("SEARCH_BOUND")

class EpistemicLimitLedger(EpistemicLedgerBase):
    def __init__(self):
        super().__init__("EPISTEMIC_LIMIT")

class ExplorationCoverageLedger(EpistemicLedgerBase):
    def __init__(self):
        super().__init__("EXPLORATION_COVERAGE")
