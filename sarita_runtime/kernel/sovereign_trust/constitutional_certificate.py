from sarita_runtime.kernel.sovereign_trust.component_certificate_chain import HierarchicalCertificate

class ConstitutionalCertificate(HierarchicalCertificate):
    """Level 1 Certificate for the Constitutional Court (Phase 83.3)."""
    def __init__(self, court_id: str, root_id: str, root_sig: str):
        super().__init__(court_id, root_id, root_sig, level=1)
