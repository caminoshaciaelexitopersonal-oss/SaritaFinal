class DatasetRegistry:
    """
    Registry for managing testing corpora, data frames, and input files.
    """
    def __init__(self):
        self._datasets = {
            "synthetic_telemetry_v1": {"records": 5000, "features": ["risk", "priority", "cohesion"]}
        }

    def register_dataset(self, key: str, details: dict):
        self._datasets[key] = details

    def get_dataset(self, key: str) -> dict:
        return self._datasets.get(key, {})
