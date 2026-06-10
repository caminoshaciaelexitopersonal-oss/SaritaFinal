class ExplorationDepthValidator:
    """
    Validates the depth of exploration in the discovery space.
    """
    def validate_depth(self, current_depth, target_depth=1000):
        return current_depth >= target_depth
