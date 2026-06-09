class OriginIntegrityVerifier:
    """
    Verifies that all reforms can be traced back to the Foundational Principle Registry.
    """
    def verify_origin(self, principle_id: str, registry):
        return principle_id in registry.get_foundational_set()
