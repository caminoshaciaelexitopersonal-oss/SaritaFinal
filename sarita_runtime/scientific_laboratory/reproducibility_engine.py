from .deterministic_runner import DeterministicRunner
from .seed_manager import SeedManager
from .environment_capture import EnvironmentCapture
from .execution_snapshot import ExecutionSnapshot
from .replay_engine import SandboxReplayEngine

class ScientificReproducibilityEngine:
    """
    Sovereign Reproducibility Engine (Phase 133).
    Ensures that every experimental trial can be replicated under matching environments.
    """
    def __init__(self):
        self.runner = DeterministicRunner()
        self.seeds = SeedManager()
        self.env = EnvironmentCapture()
        self.snapshot = ExecutionSnapshot()
        self.replay = SandboxReplayEngine()

    def certify_reproducibility(self, trial_callable, expected_outputs: list) -> dict:
        """
        Runs environment capturing, seeds deterministic runs, and executes comparative replays.
        """
        env_meta = self.env.capture_environment_metadata()
        is_reproducible = self.replay.replay_and_compare(trial_callable, expected_outputs)

        return {
            "reproducible": is_reproducible,
            "environment": env_meta,
            "reproducibility_ratio": 1.0000 if is_reproducible else 0.0000,
            "confidence_threshold": 1.0000
        }
