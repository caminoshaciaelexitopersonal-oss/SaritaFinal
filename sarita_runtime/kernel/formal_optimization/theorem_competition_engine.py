class TheoremCompetitionEngine:
    """
    Manages competition between multiple valid theorems to select the dominant solution.
    """
    def __init__(self, ranker, tournament, selector):
        self.ranker = ranker
        self.tournament = tournament
        self.selector = selector

    def resolve_competition(self, problem_id, theorems):
        """
        Runs a tournament between theorems and selects the winner.
        """
        if not theorems:
            return None

        ranked_theorems = self.ranker.rank_theorems(theorems)
        tournament_results = self.tournament.run_tournament(ranked_theorems)
        winner = self.selector.select_dominant(tournament_results)

        return {
            "problem_id": problem_id,
            "theorems_count": len(theorems),
            "winner": winner,
            "tournament_results": tournament_results
        }
