class KernelMetadataManager:
    """
    Coordinates and persists schema metadata describing kernel namespaces.
    """
    def __init__(self):
        self.metadata = {}

    def set_metadata(self, key: str, value: dict):
        self.metadata[key] = value

    def get_metadata(self, key: str) -> dict:
        return self.metadata.get(key, {})
