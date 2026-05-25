import logging
import os

class RuntimeEntropyGovernor:
    """
    Governs entropy consumption physically.
    """
    def __init__(self):
        self.entropy_avail = "/proc/sys/kernel/random/entropy_avail"

    async def ensure_entropy_threshold(self, min_entropy: int = 1024):
        """
        Ensures that physical entropy is above threshold for deterministic seeding.
        """
        try:
            with open(self.entropy_avail, "r") as f:
                avail = int(f.read().strip())

            logging.info(f"Entropy Governor: Available physical entropy: {avail}")
            if avail < min_entropy:
                logging.warning(f"Entropy Governor: Entropy STARVATION ({avail} < {min_entropy}).")
                return False
            return True
        except Exception as e:
            logging.error(f"Entropy Governor: Failed to read entropy: {e}")
            return False
