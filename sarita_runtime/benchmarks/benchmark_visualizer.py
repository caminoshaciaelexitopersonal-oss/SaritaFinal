class BenchmarkVisualizer:
    """
    Renders comparative performance bar-charts in text/ASCII format.
    """
    def __init__(self):
        pass

    def render_ascii_bars(self, results: dict) -> str:
        lines = []
        lines.append("=== BENCHMARK COMPARATIVE RESULTS ===")
        for name, mean_score in results.items():
            # Multiply by 20 to represent as a scale out of 20 bars
            bar_len = int(mean_score * 20.0)
            bar_len = max(0, min(20, bar_len))
            bar_str = "█" * bar_len + "░" * (20 - bar_len)
            lines.append(f"{name:<18} | {bar_str} | Mean: {mean_score:.4f}")
        lines.append("=====================================")
        return "\n".join(lines)
