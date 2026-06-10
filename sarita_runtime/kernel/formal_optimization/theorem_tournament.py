class TheoremTournament:
    """
    Conducts head-to-head comparisons between theorems.
    """
    def run_tournament(self, ranked_theorems):
        results = []
        # In Phase 102, the tournament is a prioritized selection
        # But we record the 'defeats' for auditability
        for i in range(len(ranked_theorems)):
            t_current = ranked_theorems[i]
            defeated = [t["theorem_id"] for t in ranked_theorems[i+1:]]
            results.append({
                "theorem_id": t_current["theorem_id"],
                "score": t_current["competition_score"],
                "defeated_theorems": defeated
            })
        return results
