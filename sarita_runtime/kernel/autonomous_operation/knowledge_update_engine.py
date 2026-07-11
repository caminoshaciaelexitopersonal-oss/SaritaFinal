import json
import os

class KnowledgeUpdateEngine:
    """
    Coordinates and persists modifications to SARITA's operational ontology,
    learned rules, and action heuristics.
    """
    def __init__(self):
        self.knowledge_filepath = "sarita_runtime/kernel/autonomous_operation/knowledge_base.json"
        self.knowledge = {
            "best_performing_paths": [],
            "critical_risk_zones": [],
            "last_updated_epoch": 0
        }
        self.load_knowledge()

    def load_knowledge(self):
        if os.path.exists(self.knowledge_filepath):
            try:
                with open(self.knowledge_filepath, "r") as f:
                    self.knowledge = json.load(f)
            except Exception:
                pass

    def integrate_knowledge(self, execution_id: str, success: bool, risk_level: float, improvements: list):
        """
        Integrates fresh execution results into the long-term knowledge repository.
        """
        if success:
            self.knowledge["best_performing_paths"].append({
                "execution_id": execution_id,
                "improvements": improvements,
                "risk_level": risk_level
            })
            # Limit list size to preserve clean state
            self.knowledge["best_performing_paths"] = self.knowledge["best_performing_paths"][-50:]
        else:
            self.knowledge["critical_risk_zones"].append({
                "execution_id": execution_id,
                "risk_level": risk_level,
                "failure_signature": "ROLLBACK_OR_INCONSISTENCY"
            })
            self.knowledge["critical_risk_zones"] = self.knowledge["critical_risk_zones"][-50:]

        import time
        self.knowledge["last_updated_epoch"] = int(time.time())
        self.save_knowledge()

    def save_knowledge(self):
        os.makedirs(os.path.dirname(self.knowledge_filepath), exist_ok=True)
        with open(self.knowledge_filepath, "w") as f:
            json.dump(self.knowledge, f, indent=2)
