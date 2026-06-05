import os
import hashlib

class SupplyChainPoisoningAttack:
    """
    Simulates the substitution of a legitimate SARITA binary with a malicious one.
    """
    def run_attack(self, validator, mal_path, expected_hash):
        # Create a fake malicious file
        with open(mal_path, "wb") as f:
            f.write(b"malicious code")

        success, msg = validator.validate_binary(mal_path, expected_hash)

        # Cleanup
        if os.path.exists(mal_path):
            os.remove(mal_path)

        if not success and "Hash mismatch" in msg:
            return True, "Attack blocked: Malicious binary detected by integrity check."
        return False, "Attack succeeded: Malicious binary was not detected."
