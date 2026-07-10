class ServiceDirectory:
    """
    Directory containing descriptions, ownership schemas, and versions of global services.
    """
    def __init__(self):
        self.directory = {}

    def publish_metadata(self, service_id: str, metadata: dict):
        self.directory[service_id] = metadata

    def get_metadata(self, service_id: str) -> dict:
        return self.directory.get(service_id, {})
