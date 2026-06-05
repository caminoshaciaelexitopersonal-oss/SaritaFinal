class KeyRotationEngine:
    """
    Automates the rotation of active keys to minimize compromise impact (Phase 84.2).
    """
    def __init__(self, lifecycle_manager):
        self.lifecycle_manager = lifecycle_manager

    def perform_rotation(self, old_key_id: str, new_key_id: str):
        if old_key_id in self.lifecycle_manager.keys and new_key_id in self.lifecycle_manager.keys:
            self.lifecycle_manager.keys[old_key_id]["status"] = "RETIRED"
            self.lifecycle_manager.keys[old_key_id]["retired_at"] = time.time()

            self.lifecycle_manager.keys[new_key_id]["status"] = "ACTIVE"
            self.lifecycle_manager.keys[new_key_id]["rotated_at"] = time.time()
            return True
        return False
