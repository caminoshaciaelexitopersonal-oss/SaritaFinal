class LongTermStabilityEstimator:
    def estimate_stability(self, entropy, decay):
        # Long-term stability is inversely proportional to entropy and decay
        return 1.0 / (1.0 + entropy + decay)
