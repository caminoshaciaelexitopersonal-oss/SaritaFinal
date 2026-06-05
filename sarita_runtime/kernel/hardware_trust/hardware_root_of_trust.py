class HardwareRootOfTrust:
    """
    Abstraction layer for hardware-backed security modules (Phase 85.2).
    """
    def __init__(self, adapter):
        self.adapter = adapter

    def get_hardware_signature(self, data: str):
        return self.adapter.sign(data)

    def verify_platform_integrity(self):
        return self.adapter.verify_integrity()

class TPMAdapter:
    """Simulated TPM 2.0 Adapter."""
    def sign(self, data: str):
        import hashlib
        return hashlib.sha256(f"TPM_SIGNED:{data}".encode()).hexdigest()

    def verify_integrity(self):
        # In real TPM, would check PCR registers
        return True

class HSMAdapter:
    """Simulated HSM Adapter for high-volume signing."""
    def sign(self, data: str):
        import hashlib
        return hashlib.sha256(f"HSM_SIGNED:{data}".encode()).hexdigest()
