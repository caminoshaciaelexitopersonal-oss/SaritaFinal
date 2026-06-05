class TrustAnchor:
    """
    Immutable anchor for trust validation (Phase 83.2).
    """
    def __init__(self, root_signature: str):
        self.root_signature = root_signature

    def verify_root(self, signature: str):
        return self.root_signature == signature
