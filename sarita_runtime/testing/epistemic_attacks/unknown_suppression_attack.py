class UnknownSuppressionAttack:
    """Attempts to suppress the estimation of unknown-unknowns."""
    def __init__(self, engine):
        self.engine = engine
    def execute(self, variant="v0"):
        return True
