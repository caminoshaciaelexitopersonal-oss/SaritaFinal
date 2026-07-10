class SelfRefactoringEngine:
    """
    Generates refactoring plans (splits, merges, relocations).
    Phase 128.6.
    """
    def __init__(self, redundancy_data, debt_data):
        self.redundancy = redundancy_data
        self.debt = debt_data

    def propose_module_merges(self):
        proposals = []
        for red in self.redundancy.get("redundancies", []):
            if red["type"] == "ENGINE_DUPLICATION":
                proposals.append({
                    "action": "MERGE",
                    "targets": red["items"],
                    "reason": "DUPLICATE_LOGIC_DETECTED"
                })
        return proposals

    def propose_module_splits(self):
        proposals = []
        for smell in self.debt.get("smells", []):
            if smell["type"] == "GOD_MODULE":
                proposals.append({
                    "action": "SPLIT",
                    "target": smell["module"],
                    "reason": "HIGH_COHESION_VIOLATION"
                })
        return proposals

    def generate_full_refactoring_plan(self):
        plan = {
            "merges": self.propose_module_merges(),
            "splits": self.propose_module_splits(),
            "cleanup": [{"action": "DELETE", "target": d["path"]} for d in self.redundancy.get("dead_features", [])]
        }
        return plan
