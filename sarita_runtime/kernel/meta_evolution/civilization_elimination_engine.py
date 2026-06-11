class CivilizationEliminationEngine:
    """
    Handles the elimination logic for tournaments.
    """
    def eliminate(self, rankings, elimination_rate=0.5):
        # Keep top performers
        keep_count = max(1, int(len(rankings) * elimination_rate))
        survivors = [r["civilization"] for r in rankings[:keep_count]]
        return survivors
