class ConstitutionalLawRegistry:
    """Registry for constitutional laws (Phase 81.1)."""
    @staticmethod
    def list_laws():
        from sarita_runtime.kernel.sovereign_constitution.sovereign_constitution import SovereignConstitution
        return SovereignConstitution.LAWS
