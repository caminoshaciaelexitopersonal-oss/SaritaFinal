import hashlib
import time

class AttestationCertificate:
    def __init__(self, component_id: str, component_hash: str, hardware_sig: str):
        self.component_id = component_id
        self.component_hash = component_hash
        self.hardware_sig = hardware_sig
        self.timestamp = time.time()

class RuntimeAttestationEngine:
    """
    Certifies that active code matches its cryptographically certified baseline (Phase 85.3).
    """
    def __init__(self, hardware_rot, identity_engine):
        self.hardware_rot = hardware_rot
        self.identity_engine = identity_engine
        self.attestations = {}

    def attest_component(self, component_id: str, file_path: str):
        # 1. Verify Software Identity
        is_legit = self.identity_engine.validate_identity(component_id, file_path)
        if not is_legit:
            return False, "Software identity validation failed."

        # 2. Add Hardware Attestation
        with open(file_path, "rb") as f:
            f_hash = hashlib.sha256(f.read()).hexdigest()

        hw_sig = self.hardware_rot.get_hardware_signature(f_hash)
        cert = AttestationCertificate(component_id, f_hash, hw_sig)
        self.attestations[component_id] = cert
        return True, cert
