class DeterministicReproductionValidator:
    """
    Compares build results from multiple environments to ensure bit-by-bit identity.
    """
    @staticmethod
    def validate_reproduction(hashes: list):
        if not hashes:
            return False, "No build hashes provided."

        first = hashes[0]
        if all(h == first for h in hashes):
            return True, f"Reproduction successful across {len(hashes)} environments."
        return False, "Non-deterministic build detected! Hashes diverge."
