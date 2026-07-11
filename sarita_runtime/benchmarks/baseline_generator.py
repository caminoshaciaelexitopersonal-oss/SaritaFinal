import math

class BaselineGenerator:
    """
    Synthesizes and generates realistic control baselines and historical lines of reference.
    """
    def __init__(self):
        pass

    def generate_baseline(self, size: int = 10) -> list:
        # Generates a standard control baseline of performance indices (centered around 0.85)
        # using a deterministic sine wave to ensure absolute repeatability.
        return [round(0.85 + 0.05 * math.sin(i * 0.5), 4) for i in range(size)]
