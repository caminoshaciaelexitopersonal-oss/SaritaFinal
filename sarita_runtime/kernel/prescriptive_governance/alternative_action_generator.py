class AlternativeActionGenerator:
    """
    Generates alternative actions to a given recommendation.
    """
    def generate_alternatives(self, prescription):
        """
        Creates a set of alternate governance moves.
        """
        return [{"id": "ALT-001", "action": "DO_NOTHING"}, {"id": "ALT-002", "action": "PARTIAL_REFORM"}]
