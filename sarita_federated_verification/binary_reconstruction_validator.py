import os
import hashlib

class BinaryReconstructionValidator:
    """
    Validates that a given binary matches a source-reconstructed hash.
    """
    @staticmethod
    def validate_binary(binary_path: str, expected_hash: str):
        if not os.path.exists(binary_path):
            return False, "Binary not found."

        with open(binary_path, "rb") as f:
            actual_hash = hashlib.sha256(f.read()).hexdigest()

        if actual_hash == expected_hash:
            return True, "Binary integrity verified."
        return False, f"Hash mismatch. Actual: {actual_hash[:8]}, Expected: {expected_hash[:8]}"
