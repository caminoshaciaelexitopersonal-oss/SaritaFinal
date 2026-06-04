import hashlib
import os
from sarita_runtime.kernel.component_identity.component_identity_registry import ComponentCertificate, ComponentIdentityRegistry

class SovereignIdentityEngine:
    """
    Engine for generating and validating component identities (Phase 82.2).
    """
    def __init__(self):
        self.registry = ComponentIdentityRegistry()

    def certify_component(self, component_id: str, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Cannot certify missing component at {file_path}")

        with open(file_path, "rb") as f:
            content = f.read()
            f_hash = hashlib.sha256(content).hexdigest()

        cert = ComponentCertificate(component_id, f_hash)
        self.registry.register_component(cert)
        return cert

    def validate_identity(self, component_id: str, file_path: str):
        with open(file_path, "rb") as f:
            current_hash = hashlib.sha256(f.read()).hexdigest()
        return self.registry.is_authorized(component_id, current_hash)
