import unittest
import os
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.constitutional_court.constitutional_court import ConstitutionalCourt
from sarita_runtime.kernel.component_identity.sovereign_identity_engine import SovereignIdentityEngine
from sarita_runtime.kernel.sovereign_constitution.constitutional_runtime_guard import ConstitutionalRuntimeGuard, ConstitutionalViolationException

class IdentityAttackValidation(unittest.TestCase):
    def setUp(self):
        self.engine = SovereignIdentityEngine()
        self.court = ConstitutionalCourt(self.engine)
        # Certify the real one
        self.engine.certify_component("UnifiedExecutionGraph", "sarita_runtime/kernel/runtime_graph/unified_execution_graph.py")

    def test_identity_spoofing_attack(self):
        fake_file = "/tmp/fake_graph.py"
        with open(fake_file, "w") as f:
            f.write("print('I am the real graph')")

        guard = ConstitutionalRuntimeGuard(self.court)

        with self.assertRaises(ConstitutionalViolationException):
            guard.enforce_certified_mutation("UnifiedExecutionGraph", fake_file)

        if os.path.exists(fake_file): os.remove(fake_file)

    def test_fake_component_id_attack(self):
        guard = ConstitutionalRuntimeGuard(self.court)
        with self.assertRaises(ConstitutionalViolationException):
            guard.enforce_certified_mutation("RogueSubsystem", __file__)

if __name__ == "__main__":
    unittest.main()
