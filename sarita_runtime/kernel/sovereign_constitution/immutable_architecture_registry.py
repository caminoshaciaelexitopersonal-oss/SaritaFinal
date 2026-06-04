import json
import os
from sarita_runtime.kernel.drift_detection.architecture_drift_detector import ArchitectureDriftDetector

class ImmutableArchitectureRegistry:
    """
    Registry for the immutable topological state of the SARITA Kernel (Phase 81.3).
    """
    REGISTRY_PATH = "sarita_runtime/kernel/sovereign_constitution/kernel_constitutional_topology.json"

    @staticmethod
    def freeze_topology():
        topology = ArchitectureDriftDetector.generate_fingerprint()
        with open(ImmutableArchitectureRegistry.REGISTRY_PATH, "w") as f:
            json.dump(topology, f, indent=4, sort_keys=True)
        print(f"Constitutional Topology frozen at: {ImmutableArchitectureRegistry.REGISTRY_PATH}")

    @staticmethod
    def verify_integrity():
        if not os.path.exists(ImmutableArchitectureRegistry.REGISTRY_PATH):
            return False, "Topology registry missing."

        current_topology = ArchitectureDriftDetector.generate_fingerprint()
        has_drift, drift = ArchitectureDriftDetector.detect_drift(ImmutableArchitectureRegistry.REGISTRY_PATH, current_topology)
        return not has_drift, drift

if __name__ == "__main__":
    ImmutableArchitectureRegistry.freeze_topology()
