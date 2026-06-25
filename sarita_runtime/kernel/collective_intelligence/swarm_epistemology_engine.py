class SwarmEpistemologyEngine:
    def __init__(self):
        pass

    def evaluate_swarm_coherence(self, universe_insights):
        # Insights are lists of concept_ids
        if not universe_insights:
            return 0.0

        # Swarm coherence is the density of overlapping insights
        all_insights = []
        for insights in universe_insights:
            all_insights.extend(insights)

        unique = set(all_insights)
        if not unique:
            return 0.0

        coherence = (len(all_insights) - len(unique)) / len(all_insights)
        return round(coherence, 4)
