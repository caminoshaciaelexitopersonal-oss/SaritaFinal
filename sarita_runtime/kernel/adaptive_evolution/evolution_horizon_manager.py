class EvolutionHorizonManager:
    """
    Manages the planning and boundaries of long-term evolution horizons.
    """
    def __init__(self, max_horizon=500):
        self.max_horizon = max_horizon

    def is_within_horizon(self, current_gen):
        return current_gen <= self.max_horizon
