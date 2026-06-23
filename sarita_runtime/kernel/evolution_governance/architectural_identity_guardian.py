class ArchitecturalIdentityGuardian:
    """Ensures ontological continuity during structural changes using target path analysis."""
    def verify_identity(self, evolution_plan):
        # Identity is compromised if core identity files are modified
        targets = evolution_plan.get("targets", [])
        if "identity_core" in targets:
            return 0.0

        # Identity persistence factor based on non-core target volume
        persistence = 1.0 - (len(targets) * 0.02)
        return round(max(0.0, persistence), 4)
