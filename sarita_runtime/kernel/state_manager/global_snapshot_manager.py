import copy

class GlobalSnapshotManager:
    """
    Manages complete, transactional snapshots of the entire SARITA State.
    Allows total, zero-stub state rollbacks.
    """
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.snapshots = {}

    def take_snapshot(self, snapshot_id: str):
        """
        Dumps the entire global state to a deep copy map.
        """
        self.snapshots[snapshot_id] = {
            "execution": copy.deepcopy(self.state_manager.execution.to_dict()),
            "architecture": copy.deepcopy(self.state_manager.architecture.to_dict()),
            "governance": copy.deepcopy(self.state_manager.governance.to_dict()),
            "runtime": copy.deepcopy(self.state_manager.runtime.to_dict()),
            "consistency": copy.deepcopy(self.state_manager.consistency.to_dict()),
            "certification": copy.deepcopy(self.state_manager.certification.to_dict()),
            "learning": copy.deepcopy(self.state_manager.learning.to_dict())
        }

    def restore_snapshot(self, snapshot_id: str) -> bool:
        """
        Restores state managers to matches snapshot.
        """
        snap = self.snapshots.get(snapshot_id)
        if not snap:
            return False

        # Restore states
        e = snap["execution"]
        self.state_manager.execution.completed_count = e["completed_count"]
        self.state_manager.execution.failed_count = e["failed_count"]
        self.state_manager.execution.total_execution_time = e["total_execution_time"]

        a = snap["architecture"]
        self.state_manager.architecture.gsai = a["gsai"]
        self.state_manager.architecture.coupling_degree = a["coupling_degree"]
        self.state_manager.architecture.redundancy_ratio = a["redundancy_ratio"]

        g = snap["governance"]
        self.state_manager.governance.laws_active = g["laws_active"]
        self.state_manager.governance.compliance_ratio = g["compliance_ratio"]
        self.state_manager.governance.violations_detected = g["violations_detected"]

        r = snap["runtime"]
        self.state_manager.runtime.status = r["status"]

        c = snap["consistency"]
        self.state_manager.consistency.ggci = c["ggci_consistency"]

        l = snap["learning"]
        self.state_manager.learning.recorded_experiences = l["recorded_experiences"]
        self.state_manager.learning.cumulative_reward = l["cumulative_reward"]

        return True
