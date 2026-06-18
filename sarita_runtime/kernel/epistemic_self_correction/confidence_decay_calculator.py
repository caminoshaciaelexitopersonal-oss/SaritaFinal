import time

class ConfidenceDecayCalculator:
    def calculate_decay(self, initial_confidence, timestamp):
        # Confidence decays over time if not refreshed with new evidence
        age = time.time() - timestamp
        decay_factor = 0.999 ** (age / 3600) # Decay per hour
        return initial_confidence * decay_factor
