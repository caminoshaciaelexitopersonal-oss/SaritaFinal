class ErrorPatternDetector:
    def detect_patterns(self, failure_history):
        # Identifies recurring logical fallacies or biases
        patterns = {}
        for failure in failure_history:
            ftype = failure.get("type")
            patterns[ftype] = patterns.get(ftype, 0) + 1
        return patterns
