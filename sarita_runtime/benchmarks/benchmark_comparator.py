class BenchmarkComparator:
    """
    Compares experimental benchmark arrays against control baseline arrays.
    """
    def __init__(self):
        pass

    def compare_to_baseline(self, experimental: list, baseline: list) -> dict:
        m1 = sum(experimental) / len(experimental) if experimental else 0.0
        m2 = sum(baseline) / len(baseline) if baseline else 0.0

        improvement_pct = ((m1 - m2) / m2) * 100.0 if m2 > 0.0 else 0.0

        return {
            "experimental_mean": round(m1, 4),
            "baseline_mean": round(m2, 4),
            "improvement_percent": round(improvement_pct, 2),
            "superior": m1 > m2
        }
