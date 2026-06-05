import hashlib
import time

class KeyLifecycleManager:
    """
    Manages the formal lifecycle of sovereign cryptographic keys (Phase 84.2).
    """
    def __init__(self):
        self.keys = {} # key_id -> details

    def create_key(self, key_type: str, owner: str):
        key_id = hashlib.sha256(f"{key_type}:{owner}:{time.time()}".encode()).hexdigest()[:16]
        self.keys[key_id] = {
            "type": key_type,
            "owner": owner,
            "status": "CREATED",
            "created_at": time.time(),
            "activated_at": None,
            "rotated_at": None,
            "retired_at": None
        }
        return key_id

    def activate_key(self, key_id: str):
        if key_id in self.keys:
            self.keys[key_id]["status"] = "ACTIVE"
            self.keys[key_id]["activated_at"] = time.time()
            return True
        return False

    def get_key_status(self, key_id: str):
        return self.keys.get(key_id, {}).get("status", "UNKNOWN")
