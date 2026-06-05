import hashlib
import time

class HierarchicalCertificate:
    """
    Base class for certificates in the Sovereign Trust Chain (Phase 83.3).
    """
    def __init__(self, subject_id: str, issuer_id: str, issuer_signature: str, level: int):
        self.subject_id = subject_id
        self.issuer_id = issuer_id
        self.issuer_signature = issuer_signature
        self.level = level # 0: Root, 1: Authority, 2: Component
        self.issued_at = time.time()
        self.expiry_date = self.issued_at + (365 * 24 * 60 * 60) # 1 year default
        self.cert_hash = self._generate_hash()

    def _generate_hash(self):
        raw = f"{self.subject_id}:{self.issuer_id}:{self.issuer_signature}:{self.level}:{self.issued_at}"
        return hashlib.sha256(raw.encode()).hexdigest()
