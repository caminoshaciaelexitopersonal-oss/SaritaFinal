import os
import json

class ScientificRepository:
    """
    Handles local disk persistence of raw scientific experimental records.
    """
    def __init__(self):
        self.repo_dir = "sarita_runtime/scientific_laboratory/repository/"
        os.makedirs(self.repo_dir, exist_ok=True)

    def store_result(self, filename: str, results: dict):
        filepath = os.path.join(self.repo_dir, filename)
        with open(filepath, "w") as f:
            json.dump(results, f, indent=2)

    def load_result(self, filename: str) -> dict:
        filepath = os.path.join(self.repo_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                return json.load(f)
        return {}
