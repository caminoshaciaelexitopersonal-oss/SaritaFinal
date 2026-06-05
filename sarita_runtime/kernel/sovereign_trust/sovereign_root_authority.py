from sarita_runtime.kernel.sovereign_trust.root_certificate import RootCertificate

class SovereignRootAuthority:
    """
    Single authorized entity to issue the initial root of trust (Phase 83.2).
    """
    def __init__(self):
        self.root_cert = RootCertificate()

    def get_root_signature(self):
        return self.root_cert.signature
