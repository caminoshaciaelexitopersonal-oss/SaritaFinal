import json
import os

class PolicyLearningEngine:
    """
    Adapts decision policies and multi-criteria evaluation weights based on historical rewards.
    """
    def __init__(self):
        self.policy_filepath = "sarita_runtime/kernel/autonomous_operation/decision_policy.json"
        self.weights = {
            "risk": 0.25,
            "benefit": 0.35,
            "uncertainty": 0.15,
            "priority": 0.15,
            "impact": 0.10
        }
        self.learning_rate = 0.05
        self.load_policy()

    def load_policy(self):
        if os.path.exists(self.policy_filepath):
            try:
                with open(self.policy_filepath, "r") as f:
                    data = json.load(f)
                    self.weights = data.get("weights", self.weights)
                    self.learning_rate = data.get("learning_rate", self.learning_rate)
            except Exception:
                pass

    def update_policy(self, reward: float, decision_metadata: dict):
        """
        Updates weights using gradient ascent or simplified reward attribution.
        If a decision with specific high/low attributes received high reward,
        realign weights to match the optimum decision parameters.
        """
        # For simplicity, adjust weights proportional to reward and parameter activation
        for key in self.weights:
            activation = decision_metadata.get(key, 0.5)
            # If positive reward, increase weight of attributes that were beneficial,
            # or decrease weight of attributes that are negative (like risk).
            if key in ["risk", "uncertainty"]:
                # If high risk/uncertainty led to high reward, we can tolerate them less/more.
                # Usually we want to heavily penalize risk, so we increase risk's negative weight influence.
                self.weights[key] += self.learning_rate * reward * (activation - 0.5)
            else:
                self.weights[key] += self.learning_rate * reward * (activation - 0.5)

        # Normalize weights so they remain positive and sum to a reasonable scale
        for key in self.weights:
            self.weights[key] = max(0.05, min(0.60, self.weights[key]))

        total = sum(self.weights.values())
        self.weights = {k: v / total for k, v in self.weights.items()}

        self.save_policy()

    def save_policy(self):
        os.makedirs(os.path.dirname(self.policy_filepath), exist_ok=True)
        with open(self.policy_filepath, "w") as f:
            json.dump({
                "weights": self.weights,
                "learning_rate": self.learning_rate
            }, f, indent=2)
