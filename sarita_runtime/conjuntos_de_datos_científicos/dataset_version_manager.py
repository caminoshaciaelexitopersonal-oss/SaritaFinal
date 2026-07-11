class DatasetVersionManager:
    """
    Manages semantic versioning (e.g. v1.0.0, v1.1.0) and transitions for scientific datasets.
    """
    def __init__(self):
        self.versions = {}

    def register_version(self, semantic_name: str, dataset_id: str):
        self.versions[semantic_name] = dataset_id

    def get_dataset_id_for_version(self, semantic_name: str) -> str:
        return self.versions.get(semantic_name)
