class SovereignNecessityValidator:
    """
    Validates the necessity of a sovereign existence.
    """
    def validate_necessity(self, necessity_score: float):
        return necessity_score > 1.0
