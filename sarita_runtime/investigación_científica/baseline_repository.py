class BaselineRepository:
    """
    Acts as a repository database storing historical and simplified project baseline configurations.
    """
    def __init__(self):
        self.baselines = {
            "gci": 0.8500,
            "gsai": 0.8200,
            "ggci": 0.8800,
            "gsei": 0.8000,
            "consistency": 0.8600,
            "product_health": 0.8900
        }

    def get_reference_value(self, key: str) -> float:
        return self.baselines.get(key)

    def register_baseline_metric(self, key: str, val: float):
        self.baselines[key] = val
