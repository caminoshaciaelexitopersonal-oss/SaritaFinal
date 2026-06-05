import hashlib
import time

class RootCertificate:
    """
    Ultimate Root of Trust for the Sovereign Kernel (Phase 83.2).
    """
    def __init__(self, owner: str = "SARITA_SOVEREIGN_SYSTEM"):
        self.owner = owner
        self.issued_at = time.time()
        self.root_id = hashlib.sha256(f"{owner}:{self.issued_at}".encode()).hexdigest()
        self.signature = self._self_sign()

    def _self_sign(self):
        raw = f"{self.owner}:{self.root_id}:{self.issued_at}"
        return hashlib.sha256(raw.encode()).hexdigest()
