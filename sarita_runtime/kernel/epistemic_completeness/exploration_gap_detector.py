class ExplorationGapDetector:
    """Detects missing regions in the search space exploration."""
    def detect_exploration_gaps(self, search_space, coverage):
        if coverage < 1.0:
            return ["LATENT_REGION_A"]
        return []
