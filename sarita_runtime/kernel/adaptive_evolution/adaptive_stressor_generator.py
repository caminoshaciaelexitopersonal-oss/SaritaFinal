import uuid
import random

class AdaptiveStressorGenerator:
    """
    Generates dynamic stressors based on epoch and probability.
    """
    def generate_stressors(self, epoch_id):
        stressors = []

        # Possible environmental shifts
        variable_targets = ["users", "operational_volume", "threat_level", "resource_availability", "regulatory_complexity"]

        # Generate random stressors for the epoch
        for target in variable_targets:
            if random.random() < 0.2: # 20% chance of shift per variable
                stressors.append({
                    "state_id": f"STR-{uuid.uuid4()}",
                    "target_variable": target,
                    "type": "THREAT" if target == "threat_level" else "SHIFT",
                    "severity": random.uniform(0.1, 0.8),
                    "probability": random.random(),
                    "impact": random.uniform(0.2, 0.5),
                    "duration": random.randint(1, 10)
                })

        return stressors
