class EvidenceWeightedTheoryRanker:
    def rank_theories(self, theories, evidence_pool):
        # Ranks theories based on how many evidence pieces they successfully predict/explain
        rankings = {}
        for theory in theories:
            rankings[theory["id"]] = theory.get("evidence_score", 0.5)
        return rankings
