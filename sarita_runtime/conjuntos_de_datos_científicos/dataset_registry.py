class DatasetRegistry:
    """
    Maintains a global record registry of generated and validated datasets.
    """
    def __init__(self):
        self.registry = {}

    def register_dataset(self, dataset: dict):
        d_id = dataset["dataset_id"]
        self.registry[d_id] = dataset

    def get_dataset(self, dataset_id: str) -> dict:
        return self.registry.get(dataset_id)

    def list_all_datasets(self) -> list:
        return list(self.registry.values())
