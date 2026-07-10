from sarita_runtime.statistics.variance_engine import VarianceEngine

class BenchmarkStatistics:
    """
    Computes standard deviation and variances of benchmark iterations.
    """
    def __init__(self):
        self.variance_eng = VarianceEngine()

    def aggregate_benchmark_stats(self, scores: list) -> dict:
        return {
            "mean": round(self.variance_eng.calculate_mean(scores), 4),
            "std_dev": round(self.variance_eng.calculate_std_dev(scores), 4)
        }
