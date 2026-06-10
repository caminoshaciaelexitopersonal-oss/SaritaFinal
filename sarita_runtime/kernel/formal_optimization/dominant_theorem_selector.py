class DominantTheoremSelector:
    """
    Selects the dominant theorem from tournament results.
    """
    def select_dominant(self, tournament_results):
        if not tournament_results:
            return None
        # The first theorem in tournament results is the winner (highest score)
        return tournament_results[0]
