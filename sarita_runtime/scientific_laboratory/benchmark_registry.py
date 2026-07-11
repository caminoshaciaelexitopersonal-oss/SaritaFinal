class BenchmarkRegistry:
    """
    Registry for managing national and international baselines and lines of reference.
    """
    def __init__(self):
        self._benchmarks = {}

    def register_benchmark(self, bench_id: str, baseline_values: dict):
        self._benchmarks[bench_id] = baseline_values

    def get_benchmark(self, bench_id: str) -> dict:
        return self._benchmarks.get(bench_id, {})
