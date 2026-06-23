import hashlib
import time

class CertificationLedgerBase:
    """Base scientific ledger with SHA-256 causal chaining for independent certification."""
    def __init__(self, ledger_type):
        self.ledger_type = ledger_type
        self.entries = []
        self.last_hash = "0" * 64

    def record_certification(self, data):
        timestamp = time.time()
        payload = {
            "cert_type": self.ledger_type,
            "data": data,
            "timestamp": timestamp,
            "parent_hash": self.last_hash
        }
        h = hashlib.sha256(str(payload).encode()).hexdigest()
        payload["hash"] = h
        self.entries.append(payload)
        self.last_hash = h
        return h

class GlobalCertificationLedger(CertificationLedgerBase):
    def __init__(self):
        super().__init__("GLOBAL_SOVEREIGN_CERTIFICATION")

class EvolutionAuthenticityLedger(CertificationLedgerBase):
    def __init__(self):
        super().__init__("EVOLUTION_AUTHENTICITY")

class MathematicalValidationLedger(CertificationLedgerBase):
    def __init__(self):
        super().__init__("MATHEMATICAL_VALIDATION")

class ScientificEvidenceLedger(CertificationLedgerBase):
    def __init__(self):
        super().__init__("SCIENTIFIC_EVIDENCE")

class ReproducibilityLedger(CertificationLedgerBase):
    def __init__(self):
        super().__init__("SCIENTIFIC_REPRODUCIBILITY")
