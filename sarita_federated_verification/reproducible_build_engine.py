import hashlib
import os
import json

class ReproducibleBuildEngine:
    """
    Ensures that the running binary is deterministically derived from source code.
    """
    def __init__(self, source_root: str):
        self.source_root = source_root

    def generate_source_manifest(self):
        manifest = {}
        for root, dirs, files in os.walk(self.source_root):
            if ".git" in dirs:
                dirs.remove(".git")
            if "__pycache__" in dirs:
                dirs.remove("__pycache__")

            for file in files:
                if file.endswith(".py") or file.endswith(".json"):
                    path = os.path.join(root, file)
                    relative_path = os.path.relpath(path, self.source_root)
                    with open(path, "rb") as f:
                        manifest[relative_path] = hashlib.sha256(f.read()).hexdigest()
        return manifest

    def calculate_canonical_hash(self, manifest: dict):
        # Sort keys to ensure determinism
        sorted_keys = sorted(manifest.keys())
        combined = "".join(f"{k}:{manifest[k]}" for k in sorted_keys)
        return hashlib.sha256(combined.encode()).hexdigest()
