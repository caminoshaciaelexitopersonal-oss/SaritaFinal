class EvolutionaryBranchTracker:
    """Tracks the status and history of all evolutionary branches."""
    def get_active_branches(self, search_tree):
        return search_tree.get("branches", [])
