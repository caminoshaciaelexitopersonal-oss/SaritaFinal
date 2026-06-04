import uuid
import time
import hashlib
import json

class PhysicalExecutionVertex:
    """
    Sovereign Execution Vertex (Phase 76/77).
    Each vertex possesses absolute material evidence.
    """
    def __init__(self, task_id: str, payload: dict, vertex_id: str = None):
        self.vertex_id = vertex_id if vertex_id else str(uuid.uuid4())
        self.task_id = task_id
        self.payload = payload

        self.timestamp = time.time()
        self.execution_epoch = 0

        # Causal Integrity
        self.previous_hash = payload.get('previous_hash', '0' * 64)
        self.vertex_hash = self._calculate_material_hash()

        self.edges = []

    def _calculate_material_hash(self):
        """Generates a material hash for the entire decision evidence."""
        evidence_body = {
            "v_id": self.vertex_id,
            "t_id": self.task_id,
            "payload": self.payload,
            "epoch": self.execution_epoch,
            "prev": self.previous_hash
        }
        evidence_str = json.dumps(evidence_body, sort_keys=True)
        return hashlib.sha256(evidence_str.encode()).hexdigest()

    def to_dict(self):
        return {
            "vertex_id": self.vertex_id,
            "task_id": self.task_id,
            "payload": self.payload,
            "timestamp": self.timestamp,
            "epoch": self.execution_epoch,
            "hash": self.vertex_hash,
            "prev_hash": self.previous_hash
        }
