import hashlib

class DependencyIntegrityEngine:
    """
    Ensures that third-party dependencies haven't been poisoned.
    """
    def __init__(self):
        self.known_hashes = {} # dep_name -> hash

    def register_dependency(self, name: str, expected_hash: str):
        self.known_hashes[name] = expected_hash

    def verify_binary(self, name: str, file_path: str):
        if name not in self.known_hashes:
            return False, f"No integrity baseline for {name}"

        with open(file_path, "rb") as f:
            actual_hash = hashlib.sha256(f.read()).hexdigest()

        if actual_hash == self.known_hashes[name]:
            return True, "Dependency integrity verified."
        return False, "Dependency integrity violation!"
