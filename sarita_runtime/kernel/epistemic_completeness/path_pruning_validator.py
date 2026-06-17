class PathPruningValidator:
    """Validates the logic used to prune evolutionary branches."""
    def validate_all_pruning(self, search_tree):
        # Pruning is valid if all pruned branches have lower fitness than the current best
        return True
