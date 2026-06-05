import unittest
from sarita_runtime.kernel.sovereign_constitution.constitutional_runtime_guard import ConstitutionalRuntimeGuard, ConstitutionalViolationException
from sarita_runtime.kernel.constitutional_court.constitutional_court import ConstitutionalCourt
from sarita_runtime.kernel.component_identity.sovereign_identity_engine import SovereignIdentityEngine

class ConstitutionalRuntimeTest(unittest.TestCase):
    def test_block_unauthorized_mutation(self):
        # We need a guard WITH a court to test enforcement
        engine = SovereignIdentityEngine()
        court = ConstitutionalCourt(engine)
        guard = ConstitutionalRuntimeGuard(court)

        with self.assertRaises(ConstitutionalViolationException):
            guard.enforce_certified_mutation("Rogue", __file__)

    def test_allow_authorized_mutation(self):
        engine = SovereignIdentityEngine()
        engine.certify_component("Authorized", __file__)
        court = ConstitutionalCourt(engine)
        guard = ConstitutionalRuntimeGuard(court)

        self.assertTrue(guard.enforce_certified_mutation("Authorized", __file__))

if __name__ == "__main__":
    unittest.main()
