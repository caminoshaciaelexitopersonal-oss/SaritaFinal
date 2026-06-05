class TrustQuarantineEngine:
    """Engine for automated trust quarantine (Phase 83.4)."""
    def __init__(self, registry):
        self.registry = registry

    def apply_quarantine(self, subject_id: str, duration: int):
        self.registry.quarantine(subject_id, duration)
