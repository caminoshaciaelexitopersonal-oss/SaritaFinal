from sarita_runtime.kernel.sovereign_trust.component_certificate_chain import HierarchicalCertificate

class AuthorityCertificate(HierarchicalCertificate):
    """Level 2 Certificate for Sovereign Authorities (Phase 83.3)."""
    def __init__(self, auth_id: str, court_id: str, court_sig: str):
        super().__init__(auth_id, court_id, court_sig, level=2)
