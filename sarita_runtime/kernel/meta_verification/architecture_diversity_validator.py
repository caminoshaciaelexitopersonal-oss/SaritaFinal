class ArchitectureDiversityValidator:
    """
    Verifies that the verifiers use distinct architectural approaches.
    """
    @staticmethod
    def validate_architecture(provenances: list):
        architectures = set(p.get("architecture_type", "standard") for p in provenances)
        # Architecture types could be: 'imperative', 'functional', 'spec-driven', 'replay-based'
        return len(architectures) >= 2
