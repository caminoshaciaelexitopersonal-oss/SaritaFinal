import random

class CausalityArchitectureBuilder:
    """
    Builds different causality models for a cosmos.
    Models can range from strictly linear to branching, retrocausal, or probabilistic.
    """
    def __init__(self):
        self.causality_modes = ["LINEAR", "BRANCHING", "PROBABILISTIC", "RETROCAUSAL", "CIRCULAR"]

    def build_causality_model(self, genome_seed):
        # Use genome to bias the selection
        mode_idx = int(genome_seed * len(self.causality_modes)) % len(self.causality_modes)
        mode = self.causality_modes[mode_idx]

        return {
            "mode": mode,
            "consistency_threshold": round(random.uniform(0.7, 0.99), 4),
            "propagation_speed": round(random.uniform(0.1, 1.0), 4),
            "reversibility": 0.1 if mode == "LINEAR" else round(random.uniform(0.2, 0.8), 4)
        }
