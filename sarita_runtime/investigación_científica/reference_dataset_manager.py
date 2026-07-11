class ReferenceDatasetManager:
    """
    Manages reference datasets defined for comparative and baseline testing protocols.
    """
    def __init__(self):
        self.datasets = {}

    def register_reference_dataset(self, dataset_name: str, values: list):
        self.datasets[dataset_name] = values

    def get_reference_dataset(self, dataset_name: str) -> list:
        return self.datasets.get(dataset_name, [])
