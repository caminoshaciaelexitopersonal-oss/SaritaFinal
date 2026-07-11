from .deterministic_runner import DeterministicRunner

class SandboxReplayEngine:
    """
    Executes replay trials to verify output reproducibility.
    """
    def __init__(self):
        self.runner = DeterministicRunner()

    def replay_and_compare(self, action_callable, expected_outputs: list) -> bool:
        """
        Replays the action and asserts matching result outputs.
        """
        replayed_out = []
        for i in range(len(expected_outputs)):
            res = self.runner.run_seeded(action_callable, i)
            replayed_out.append(res)

        return replayed_out == expected_outputs
