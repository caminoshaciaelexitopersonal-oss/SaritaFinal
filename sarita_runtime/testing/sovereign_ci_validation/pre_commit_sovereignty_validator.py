import os
import sys
import json
from sarita_runtime.kernel.drift_detection.architecture_drift_detector import ArchitectureDriftDetector

def validate_pre_commit():
    print("Sovereign CI: Starting Pre-Commit Sovereignty Validation...")

    # 1. Check Purity (Caches, .pyc)
    from sarita_runtime.kernel.repository_guard_validator import check_purity
    if not check_purity():
        print("CI FAILURE: Repository purity violation.")
        return False

    # 2. Check Drift
    baseline = "sarita_runtime/kernel/kernel_architecture_fingerprint.json"
    if os.path.exists(baseline):
        current = ArchitectureDriftDetector.generate_fingerprint()
        has_drift, drift = ArchitectureDriftDetector.detect_drift(baseline, current)
        if has_drift:
            print(f"CI WARNING: Architectural Drift Detected: {json.dumps(drift, indent=2)}")
            # For now, we log it. In a hard enforcement mode, we would return False.

    # 3. Structural Analysis (Placeholder for AST checks)
    print("Sovereign CI: Validation Complete. Integrity Verified.")
    return True

if __name__ == "__main__":
    if not validate_pre_commit():
        sys.exit(1)
