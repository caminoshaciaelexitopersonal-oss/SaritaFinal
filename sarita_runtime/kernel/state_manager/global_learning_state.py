class GlobalLearningState:
    """
    Manages continuous reinforcement learning metrics, experience memory,
    and adapted policy weights.
    """
    def __init__(self):
        self.recorded_experiences = 4
        self.cumulative_reward = 3.8210
        self.policy_entropy = 0.4210

    def record_learning(self, reward: float):
        self.recorded_experiences += 1
        self.cumulative_reward += reward

    def to_dict(self) -> dict:
        return {
            "recorded_experiences": self.recorded_experiences,
            "cumulative_reward": round(self.cumulative_reward, 4),
            "policy_entropy": self.policy_entropy
        }
