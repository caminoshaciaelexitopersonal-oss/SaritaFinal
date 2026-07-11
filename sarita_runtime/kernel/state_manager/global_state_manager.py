import json
import os
from .global_memory import GlobalMemory
from .global_execution_state import GlobalExecutionState
from .global_architecture_state import GlobalArchitectureState
from .global_governance_state import GlobalGovernanceState
from .global_runtime_state import GlobalRuntimeState
from .global_consistency_state import GlobalConsistencyState
from .global_certification_state import GlobalCertificationState
from .global_learning_state import GlobalLearningState
from .global_snapshot_manager import GlobalSnapshotManager

class GlobalStateManager:
    """
    Central Coordinator for the entire sovereign state space.
    Elimitanes fragmented local states and coordinates consistent state mutations.
    """
    def __init__(self):
        self.memory = GlobalMemory()
        self.execution = GlobalExecutionState()
        self.architecture = GlobalArchitectureState()
        self.governance = GlobalGovernanceState()
        self.runtime = GlobalRuntimeState()
        self.consistency = GlobalConsistencyState()
        self.certification = GlobalCertificationState()
        self.learning = GlobalLearningState()
        self.snapshots = GlobalSnapshotManager(self)

    def get_full_state(self) -> dict:
        """
        Gathers and returns the unified state dictionary.
        """
        return {
            "execution": self.execution.to_dict(),
            "architecture": self.architecture.to_dict(),
            "governance": self.governance.to_dict(),
            "runtime": self.runtime.to_dict(),
            "consistency": self.consistency.to_dict(),
            "certification": self.certification.to_dict(),
            "learning": self.learning.to_dict()
        }

    def persist_state_snapshot(self, path: str = "sarita_runtime/kernel/state_manager/global_state.json"):
        """
        Persists the entire unified system state to a secure uncontradictable JSON on disk.
        """
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(self.get_full_state(), f, indent=2)
