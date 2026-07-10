from .benchmark_catalog import BenchmarkCatalog
from .baseline_generator import BaselineGenerator
from .benchmark_runner import BenchmarkRunner
from .benchmark_comparator import BenchmarkComparator
from .benchmark_statistics import BenchmarkStatistics
from .benchmark_ranker import BenchmarkRanker
from .benchmark_visualizer import BenchmarkVisualizer

class UnifiedBenchmarkEngine:
    """
    Sovereign Benchmark Engine (Phase 133).
    Evaluates and compares active SARITA product configurations against baselines.
    """
    def __init__(self):
        self.catalog = BenchmarkCatalog()
        self.baseline = BaselineGenerator()
        self.runner = BenchmarkRunner()
        self.comparator = BenchmarkComparator()
        self.statistics = BenchmarkStatistics()
        self.ranker = BenchmarkRanker()
        self.visualizer = BenchmarkVisualizer()

    def run_benchmark_trial(self, test_key: str, action_callable) -> dict:
        """
        Executes a benchmark, compares against dynamically generated baseline,
        and aggregates statistics.
        """
        test_info = self.catalog.get_test(test_key)

        # 1. Generate baseline
        base_data = self.baseline.generate_baseline(size=10)

        # 2. Run experimental trials
        exp_data = self.runner.run_benchmark(action_callable, iterations=10)

        # 3. Compare and gather statistics
        comp_res = self.comparator.compare_to_baseline(exp_data, base_data)
        stats = self.statistics.aggregate_benchmark_stats(exp_data)

        # 4. Format report
        return {
            "test_key": test_key,
            "test_name": test_info.get("name", "Benchmark Test"),
            "baseline_mean": comp_res["baseline_mean"],
            "experimental_mean": comp_res["experimental_mean"],
            "improvement_pct": comp_res["improvement_percent"],
            "superior": comp_res["superior"],
            "stats": stats
        }
