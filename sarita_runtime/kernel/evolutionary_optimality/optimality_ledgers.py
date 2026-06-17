import hashlib
import time

class OptimalityLedgerBase:
    """Base scientific ledger with SHA-256 causal chaining for optimality proofs."""
    def __init__(self, ledger_type):
        self.ledger_type = ledger_type
        self.entries = []
        self.last_hash = "0" * 64

    def record_proof(self, data):
        timestamp = time.time()
        payload = {
            "proof_type": self.ledger_type,
            "data": data,
            "timestamp": timestamp,
            "parent_hash": self.last_hash
        }
        h = hashlib.sha256(str(payload).encode()).hexdigest()
        payload["hash"] = h
        self.entries.append(payload)
        self.last_hash = h
        return h

class EvolutionOptimalityLedger(OptimalityLedgerBase):
    def __init__(self):
        super().__init__("EVOLUTION_OPTIMALITY")

class ParetoFrontierLedger(OptimalityLedgerBase):
    def __init__(self):
        super().__init__("PARETO_FRONTIER")

class CounterfactualLedger(OptimalityLedgerBase):
    def __init__(self):
        super().__init__("COUNTERFACTUAL_SIMULATION")

class EvolutionRegretLedger(OptimalityLedgerBase):
    def __init__(self):
        super().__init__("EVOLUTION_REGRET")
