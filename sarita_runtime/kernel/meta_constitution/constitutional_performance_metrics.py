class ConstitutionalPerformanceMetrics:
    """
    Collects and tracks performance metrics for the constitution.
    """
    def __init__(self, score_engine):
        self.score_engine = score_engine
        self.history = []

    def collect_metrics(self, raw_data: dict):
        score_report = self.score_engine.generate_score(raw_data)
        metrics = {
            "timestamp": raw_data["timestamp"],
            "reform_quality": raw_data["reform_quality"],
            "prediction_accuracy": raw_data["prediction_accuracy"],
            "governance_efficiency": score_report["governance_efficiency"],
            "adaptive_maturity": score_report["adaptive_maturity"],
            "evolution_score": score_report["evolution_score"]
        }
        self.history.append(metrics)
        return metrics
