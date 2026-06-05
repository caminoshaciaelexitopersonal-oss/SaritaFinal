class SupplyChainValidator:
    """
    Validates the entire supply chain of a SARITA component.
    """
    def __init__(self, origin_registry, integrity_engine):
        self.origin_registry = origin_registry
        self.integrity_engine = integrity_engine

    def validate_artifact(self, artifact_id: str, artifact_path: str):
        # 1. Check Origin
        origin_ok, origin_msg = self.origin_registry.verify_origin(artifact_id)
        if not origin_ok: return False, origin_msg

        # 2. Check Integrity
        integrity_ok, integrity_msg = self.integrity_engine.verify_binary(artifact_id, artifact_path)
        if not integrity_ok: return False, integrity_msg

        return True, "Artifact supply chain validated."
