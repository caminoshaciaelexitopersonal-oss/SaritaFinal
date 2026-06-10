class CivilizationRankingSystem:
    """
    Ranks civilizations based on multi-dimensional performance.
    """
    def rank_civilizations(self, civilizations):
        scored = []
        for civ in civilizations:
            score = self._calculate_tournament_score(civ)
            scored.append({
                "civilization": civ,
                "score": score,
                "fitness": civ.current_state["evolutionary_capacity"],
                "survival": civ.current_state["survival"],
                "dominance": self._calculate_dominance(civ)
            })

        # Sort by score descending
        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored

    def _calculate_tournament_score(self, civ):
        state = civ.current_state
        return (
            state["survival"] * 1000 +
            state["stability"] * 500 +
            state["legitimacy"] * 500 +
            state["prosperity"] * 500 +
            state["complexity"] * 200
        )

    def _calculate_dominance(self, civ):
        # Dominance is the relative superiority over average
        return civ.current_state["survival"] * 1.5
