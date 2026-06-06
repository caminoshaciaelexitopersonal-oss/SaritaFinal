import time

class PolicyEvolutionRegistry:
    """
    Tracks the autonomous evolution of system policies.
    """
    def __init__(self):
        self.policies = {} # policy_id -> history

    def update_policy(self, policy_id: str, new_value: any, reason: str):
        if policy_id not in self.policies:
            self.policies[policy_id] = []

        self.policies[policy_id].append({
            "value": new_value,
            "reason": reason,
            "timestamp": time.time()
        })
