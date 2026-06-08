import time

class IdentityCoreRegistry:
    """
    Registry for SARITA's essential identity components.
    """
    def __init__(self):
        self.core_elements = {
            "AUTHORITY_UNICITY": {"type": "PRINCIPLE", "status": "INVARIANT"},
            "MATERIAL_EVIDENCE": {"type": "PRINCIPLE", "status": "INVARIANT"},
            "SOVEREIGN_CLOSURE": {"type": "PRINCIPLE", "status": "INVARIANT"},
            "CONSTITUTIONAL_SUPREMACY": {"type": "PRINCIPLE", "status": "INVARIANT"}
        }

    def get_invariants(self):
        return [k for k, v in self.core_elements.items() if v["status"] == "INVARIANT"]
