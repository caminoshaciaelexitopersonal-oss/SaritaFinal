class FalseOptimalityAttack:
    """Attempts to forge evidence of optimality for a suboptimal path."""
    def __init__(self, engine):
        self.engine = engine
    def execute(self, variant="v0"):
        return True
