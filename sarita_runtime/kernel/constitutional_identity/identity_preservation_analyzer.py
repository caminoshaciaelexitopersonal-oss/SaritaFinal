class IdentityPreservationAnalyzer:
    """
    Analyzes how much of SARITA's identity is preserved across a transition.
    """
    def analyze_preservation(self, state_before: dict, state_after: dict):
        # Preservation = Intersection of Core Principles / Total Core Principles
        core_before = set(state_before.get("core_principles", []))
        core_after = set(state_after.get("core_principles", []))

        if not core_before:
            return 1.0

        preservation_score = len(core_before.intersection(core_after)) / len(core_before)
        return preservation_score
