class KeyCustodyRegistry:
    """Registry for key custody and ownership (Phase 84.2)."""
    def __init__(self):
        self.custody_map = {} # key_id -> authorized_custodian

    def assign_custody(self, key_id: str, custodian: str):
        self.custody_map[key_id] = custodian

    def verify_custody(self, key_id: str, custodian: str):
        return self.custody_map.get(key_id) == custodian
