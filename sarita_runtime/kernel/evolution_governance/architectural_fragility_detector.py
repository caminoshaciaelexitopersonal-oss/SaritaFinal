class ArchitecturalFragilityDetector:
    """Detects architectural fragility in evolution proposals."""
    def detect_fragility(self, proposal):
        # Complexity over a certain threshold increases fragility
        complexity = proposal.get("complexity", 0.5)
        return complexity > 0.8
