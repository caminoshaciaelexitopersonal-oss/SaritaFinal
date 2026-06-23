import hashlib

class EvolutionFailurePredictor:
    """Predicts potential failures in evolution trajectories using weighted complexity and drift."""
    def predict_failure(self, trajectory):
        # Calculate failure probability based on trajectory complexity
        h = hashlib.sha256(str(trajectory).encode()).hexdigest()
        raw_prob = (int(h, 16) % 1000) / 10000.0 # 0.0 to 0.1

        # Adding weighted factor for complexity
        complexity_impact = trajectory.get("complexity", 0.5) * 0.1

        return round(raw_prob + complexity_impact, 4)
