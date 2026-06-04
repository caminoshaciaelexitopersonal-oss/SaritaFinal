import hashlib
import json

class EvidenceSchemaRegistry:
    """
    Registry for standard evidence schemas in Phase 77.
    Ensures structural consistency for different event types.
    """
    SCHEMAS = {
        "OWNERSHIP_CHANGE": ["resource", "owner"],
        "PRESSURE_UPDATE": ["signals", "score"],
        "TASK_AUTHORIZED": ["task"],
        "IO_SUBMISSION": ["type", "params"],
        "IO_COMPLETION": ["result"],
        "EPOCH_ADVANCE": ["new_epoch"]
    }

    @staticmethod
    def get_schema(action: str):
        return EvidenceSchemaRegistry.SCHEMAS.get(action, [])

    @staticmethod
    def validate_payload_schema(action: str, payload: dict):
        required = EvidenceSchemaRegistry.get_schema(action)
        for field in required:
            if field not in payload:
                return False
        return True
