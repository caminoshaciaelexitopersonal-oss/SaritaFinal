class CivilizationalTournamentEngine:
    """
    Orchestrates direct competition between Meta-Constitutions, Civilizations, and Universes.
    """
    def __init__(self, ranking_system, elimination_engine, selector):
        self.ranking_system = ranking_system
        self.elimination_engine = elimination_engine
        self.selector = selector

    def run_tournament(self, civilizations):
        """
        Runs an elimination tournament to find the dominant civilization.
        """
        current_pool = civilizations
        round_index = 1

        all_round_records = []

        while len(current_pool) > 1:
            # 1. Rank current pool
            rankings = self.ranking_system.rank_civilizations(current_pool)

            # 2. Record round data
            round_record = {
                "round": round_index,
                "pool_size": len(current_pool),
                "rankings": rankings
            }
            all_round_records.append(round_record)

            # 3. Eliminate bottom performers
            current_pool = self.elimination_engine.eliminate(rankings)
            round_index += 1

        winner = self.selector.select_dominant(current_pool)
        return winner, all_round_records
