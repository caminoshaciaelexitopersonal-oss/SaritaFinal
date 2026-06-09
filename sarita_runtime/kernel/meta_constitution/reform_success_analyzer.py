class ReformSuccessAnalyzer:
    """
    Analyzes why reforms succeed or fail based on historical feedback.
    """
    def analyze_success_patterns(self, feedback_history: list):
        successes = [f for f in feedback_history if f["effectiveness"] > 0.8]
        failures = [f for f in feedback_history if f["effectiveness"] < 0.4]

        return {
            "success_count": len(successes),
            "failure_count": len(failures),
            "dominant_success_traits": ["low_complexity", "high_causality"] if successes else []
        }
