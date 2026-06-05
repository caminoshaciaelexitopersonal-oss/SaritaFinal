class IdentityRevocationEngine:
    """Active engine to process trust revocation events (Phase 83.4)."""
    def __init__(self, registry):
        self.registry = registry

    def process_compromise(self, subject_id: str):
        # Automated response logic
        self.registry.revoke(subject_id, "Compromise detected by Sovereign Defense.")
