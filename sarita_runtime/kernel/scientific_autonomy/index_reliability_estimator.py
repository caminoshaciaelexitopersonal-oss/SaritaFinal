class IndexReliabilityEstimator:
    def estimate_reliability(self, index_history, evidence_quality):
        # Reliability is based on history stability and evidence quality
        stability = 1.0
        if len(index_history) >= 2:
            stability = 1.0 / (1.0 + abs(index_history[-1] - index_history[-2]))
        return (stability + evidence_quality) / 2.0
