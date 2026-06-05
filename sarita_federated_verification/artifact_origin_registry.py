class ArtifactOriginRegistry:
    """
    Maintains a record of legitimate sources for SARITA artifacts.
    """
    def __init__(self):
        self.origins = {} # artifact_id -> {repository, maintainer_key, build_server}

    def register_origin(self, artifact_id: str, info: dict):
        self.origins[artifact_id] = info

    def verify_origin(self, artifact_id: str):
        if artifact_id in self.origins:
            return True, "Origin known and registered."
        return False, "Unknown artifact origin!"
