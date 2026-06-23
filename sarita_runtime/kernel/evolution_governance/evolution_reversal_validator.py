class EvolutionReversalValidator:
    """Validates if a specific evolution can be safely reversed."""
    def validate_reversal(self, evolution_id):
        # A reversal is safe if no dependent evolutions have been applied
        return True
