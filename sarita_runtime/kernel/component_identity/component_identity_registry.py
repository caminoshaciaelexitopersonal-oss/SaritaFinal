import hashlib
import time
import json

class ComponentCertificate:
    """
    Sovereign Identity Certificate for Kernel Components (Phase 82.2).
    """
    def __init__(self, component_id: str, component_hash: str, authorized_by: str = "SARITA_CONSTITUTIONAL_COURT"):
        self.component_id = component_id
        self.component_hash = component_hash
        self.authorized_by = authorized_by
        self.issued_at = time.time()
        self.signature = self._generate_signature()

    def _generate_signature(self):
        raw = f"{self.component_id}:{self.component_hash}:{self.authorized_by}:{self.issued_at}"
        return hashlib.sha256(raw.encode()).hexdigest()

    def to_dict(self):
        return {
            "component_id": self.component_id,
            "component_hash": self.component_hash,
            "authorized_by": self.authorized_by,
            "issued_at": self.issued_at,
            "signature": self.signature
        }

class ComponentIdentityRegistry:
    """Registry for all certified sovereign components."""
    def __init__(self):
        self.certificates = {}

    def register_component(self, cert: ComponentCertificate):
        self.certificates[cert.component_id] = cert

    def is_authorized(self, component_id: str, current_hash: str):
        cert = self.certificates.get(component_id)
        if not cert: return False
        return cert.component_hash == current_hash
