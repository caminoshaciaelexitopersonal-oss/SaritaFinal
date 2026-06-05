import os
import json
import hashlib

class ArchitectureDriftDetector:
    """
    Detects structural changes in the Sovereign Kernel (Phase 80.3).
    """
    SOVEREIGN_COMPONENTS = {
        "sarita_runtime/kernel/runtime_graph/",
        "sarita_runtime/kernel/runtime_ledger/",
        "sarita_runtime/kernel/hardware_authority/",
        "sarita_runtime/kernel/scheduling_fabric/",
        "sarita_runtime/kernel/evidence_fabric/"
    }

    @staticmethod
    def generate_fingerprint(root_dir="sarita_runtime/kernel/"):
        fingerprint = {}
        for root, dirs, files in os.walk(root_dir):
            # Skip caches
            if "__pycache__" in root: continue

            for f in files:
                if f.endswith(".py"):
                    path = os.path.join(root, f)
                    with open(path, "rb") as bf:
                        content = bf.read()
                        f_hash = hashlib.sha256(content).hexdigest()
                        fingerprint[path] = f_hash
        return fingerprint

    @staticmethod
    def detect_drift(baseline_file, current_fingerprint):
        if not os.path.exists(baseline_file):
            return True, "No baseline found."

        with open(baseline_file, "r") as f:
            baseline = json.load(f)

        added = set(current_fingerprint.keys()) - set(baseline.keys())
        removed = set(baseline.keys()) - set(current_fingerprint.keys())
        modified = [p for p in baseline if p in current_fingerprint and baseline[p] != current_fingerprint[p]]

        drift = {
            "added": list(added),
            "removed": list(removed),
            "modified": modified
        }

        has_drift = any(drift.values())
        return has_drift, drift
