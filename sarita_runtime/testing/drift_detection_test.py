import unittest
import os
import json
from sarita_runtime.kernel.drift_detection.architecture_drift_detector import ArchitectureDriftDetector

class DriftDetectionTest(unittest.TestCase):
    def test_fingerprint_generation(self):
        fingerprint = ArchitectureDriftDetector.generate_fingerprint()
        self.assertIn("sarita_runtime/kernel/runtime_graph/unified_execution_graph.py", fingerprint)

    def test_drift_detection(self):
        baseline_path = "/tmp/arch_baseline.json"
        fingerprint = ArchitectureDriftDetector.generate_fingerprint()

        with open(baseline_path, "w") as f:
            json.dump(fingerprint, f)

        has_drift, drift = ArchitectureDriftDetector.detect_drift(baseline_path, fingerprint)
        self.assertFalse(has_drift)

        # Simulate modification
        fingerprint["new_file.py"] = "abc"
        has_drift, drift = ArchitectureDriftDetector.detect_drift(baseline_path, fingerprint)
        self.assertTrue(has_drift)
        self.assertIn("new_file.py", drift["added"])

        if os.path.exists(baseline_path): os.remove(baseline_path)

if __name__ == "__main__":
    unittest.main()
