class ReasoningFailureAnalyzer:
    def analyze_failure(self, reasoning_path, actual_outcome):
        # Detects where reasoning deviated from reality
        divergence = 0.0
        for step in reasoning_path:
            if step.get("prediction") != actual_outcome.get(step["id"]):
                divergence += 1.0
        return {"divergence": divergence, "failure_node": "REASONING_STEP_X"}
