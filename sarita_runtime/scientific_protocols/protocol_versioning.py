class ProtocolVersioning:
    """
    Manages semantic version mapping and historical mutation entries for protocols.
    """
    def __init__(self):
        self.versions = {}

    def tag_version(self, name: str, version: str, protocol_dict: dict):
        self.versions[f"{name}@{version}"] = protocol_dict

    def get_version(self, name: str, version: str) -> dict:
        return self.versions.get(f"{name}@{version}", {})
