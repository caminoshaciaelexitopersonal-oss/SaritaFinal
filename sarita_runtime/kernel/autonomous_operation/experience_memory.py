import json
import os

class ExperienceMemory:
    """
    Epistemic storage of experience tuples (State, Action, Reward, Next State).
    Maintains a persistent audit ledger of all autonomous successes and failures.
    """
    def __init__(self):
        self.memory_filepath = "sarita_runtime/kernel/autonomous_operation/experience_memory.json"
        self.experiences = []
        self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_filepath):
            try:
                with open(self.memory_filepath, "r") as f:
                    self.experiences = json.load(f)
            except Exception:
                self.experiences = []
        else:
            self.experiences = []

    def record_experience(self, action_id, state_before, state_after, reward, metadata):
        """
        Records a new learning experience.
        """
        experience = {
            "experience_id": f"EXP-{len(self.experiences)+1:04d}",
            "action_id": action_id,
            "state_before": state_before,
            "state_after": state_after,
            "reward": float(reward),
            "metadata": metadata
        }
        self.experiences.append(experience)
        self.save_memory()

    def save_memory(self):
        os.makedirs(os.path.dirname(self.memory_filepath), exist_ok=True)
        with open(self.memory_filepath, "w") as f:
            json.dump(self.experiences, f, indent=2)

    def retrieve_by_reward(self, threshold=0.5):
        return [exp for exp in self.experiences if exp["reward"] >= threshold]
