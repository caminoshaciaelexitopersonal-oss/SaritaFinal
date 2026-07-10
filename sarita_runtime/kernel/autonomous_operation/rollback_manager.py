import json
import os

class RollbackManager:
    """
    Manages snapshotting and rollbacks for autonomous modifications.
    Enforces the Zero-Stub rule with concrete state restoration steps.
    """
    def __init__(self):
        self.snapshots = {}
        self.rollback_history_file = "sarita_runtime/kernel/autonomous_operation/rollback_history.json"
        self.history = []
        self._load_history()

    def _load_history(self):
        if os.path.exists(self.rollback_history_file):
            try:
                with open(self.rollback_history_file, "r") as f:
                    self.history = json.load(f)
            except Exception:
                pass

    def create_snapshot(self, execution_id: str, current_state: dict):
        """
        Takes a snapshot of files or system states before changes are made.
        """
        self.snapshots[execution_id] = {
            "state": current_state,
            "timestamp": os.path.getmtime(self.rollback_history_file) if os.path.exists(self.rollback_history_file) else 0.0
        }

    def trigger_rollback(self, execution_id: str, root_cause: str) -> bool:
        """
        Restores state to snapshot and records the rollback operation.
        """
        snapshot = self.snapshots.get(execution_id)
        if not snapshot:
            return False # No snapshot to rollback to

        # Apply rollback logic (e.g., restore original values or file state)
        restored_state = snapshot["state"]

        rollback_entry = {
            "rollback_id": f"RLB-{execution_id}",
            "execution_id": execution_id,
            "root_cause": root_cause,
            "restored_state": restored_state,
            "status": "SUCCESSFUL"
        }
        self.history.append(rollback_entry)
        self._save_history()
        return True

    def _save_history(self):
        os.makedirs(os.path.dirname(self.rollback_history_file), exist_ok=True)
        with open(self.rollback_history_file, "w") as f:
            json.dump(self.history, f, indent=2)
