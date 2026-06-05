import json
import os
from sarita_runtime.kernel.drift_detection.architecture_drift_detector import ArchitectureDriftDetector

def generate_and_save_fingerprint():
    fingerprint = ArchitectureDriftDetector.generate_fingerprint()
    output_path = "sarita_runtime/kernel/kernel_architecture_fingerprint.json"
    with open(output_path, "w") as f:
        json.dump(fingerprint, f, indent=4, sort_keys=True)
    print(f"Sovereign Architecture Fingerprint generated at: {output_path}")
    return output_path

if __name__ == "__main__":
    generate_and_save_fingerprint()
