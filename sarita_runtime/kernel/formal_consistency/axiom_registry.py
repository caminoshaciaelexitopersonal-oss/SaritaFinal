import json

class AxiomRegistry:
    """
    Registry for formal axioms and postulates.
    Phase 130.3.
    """
    def __init__(self):
        self.axioms = {}
        self.postulates = {}

    def register_axiom(self, aid, definition):
        self.axioms[aid] = {
            "id": aid,
            "definition": definition,
            "status": "REGISTERED"
        }

    def register_postulate(self, pid, definition):
        self.postulates[pid] = {
            "id": pid,
            "definition": definition
        }

    def get_all_axioms(self):
        return self.axioms

    def export_registry(self, filepath="sarita_runtime/kernel/formal_consistency/axiom_registry.json"):
        with open(filepath, "w") as f:
            json.dump({"axioms": self.axioms, "postulates": self.postulates}, f, indent=2)
