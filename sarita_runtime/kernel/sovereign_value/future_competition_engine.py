class FutureCompetitionEngine:
    """
    Orchestrates the competition between projected constitutional futures.
    """
    def __init__(self, ranker, tournament, selector):
        self.ranker = ranker
        self.tournament = tournament
        self.selector = selector

    def compete_futures(self, projections: list):
        # 1. Rank initial projections
        ranked = self.ranker.rank_futures(projections)

        # 2. Run Tournament
        winners = self.tournament.run_tournament(ranked)

        # 3. Select Dominant Future
        dominant = self.selector.select_dominant(winners)

        return {
            "dominant_future": dominant,
            "competition_summary": f"Reduced {len(projections)} futures to 1 dominant path."
        }
