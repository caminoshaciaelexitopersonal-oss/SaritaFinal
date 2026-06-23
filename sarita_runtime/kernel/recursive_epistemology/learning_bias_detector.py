class LearningBiasDetector:
    def detect_bias(self, learning_logs):
        # Detects if learning is favoring a specific domain excessively
        domain_counts = {}
        for log in learning_logs:
            d = log.get("domain")
            domain_counts[d] = domain_counts.get(d, 0) + 1
        return domain_counts
