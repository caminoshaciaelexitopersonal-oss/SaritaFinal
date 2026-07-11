class PerformanceRanker:
    """
    Ranks multiple execution architectures, configurations, or historical runs against one another.
    """
    def __init__(self):
        pass

    def rank_configurations(self, configs_dict: dict, evaluation_metric: str) -> list:
        items = []
        for name, metrics in configs_dict.items():
            val = metrics.get(evaluation_metric, 0.0)
            items.append((name, val))

        items.sort(key=lambda x: x[1], reverse=True)

        ranked = []
        for rank, (name, val) in enumerate(items, 1):
            ranked.append({
                "rank": rank,
                "configuration_name": name,
                "metric_value": val
            })
        return ranked
