class DominantCivilizationSelector:
    """
    Final selection of the dominant civilization.
    """
    def select_dominant(self, pool):
        if not pool: return None
        # In a pool of 1, the survivor is the winner.
        return pool[0]
