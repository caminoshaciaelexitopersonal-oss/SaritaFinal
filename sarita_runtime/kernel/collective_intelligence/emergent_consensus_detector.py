class EmergentConsensusDetector:
    def detect_consensus(self, universe_decisions):
        if not universe_decisions:
            return None

        counts = {}
        for d in universe_decisions:
            counts[d] = counts.get(d, 0) + 1

        top_decision, count = max(counts.items(), key=lambda x: x[1])
        if count > len(universe_decisions) * 0.6:
            return top_decision
        return None
