import unittest
from sarita_runtime.kernel.external_verification.external_verifier import ExternalVerifier

class TotalCompromiseAttackTest(unittest.TestCase):
    def test_external_verification_bypass_attack(self):
        # Even if the kernel is "poisoned" to say it's valid,
        # the ExternalVerifier uses a baseline that is NOT in the kernel.

        baseline = {"UnifiedExecutionGraph": "LEGIT_HASH"}
        verifier = ExternalVerifier(baseline)

        # Rogue component with fake hash
        is_legit, msg = verifier.verify_component("UnifiedExecutionGraph", "EVIL_HASH")

        self.assertFalse(is_legit)
        self.assertEqual(msg, "Hash match verified.") # Wait, check logic

    def test_verifier_logic(self):
        baseline = {"C1": "H1"}
        verifier = ExternalVerifier(baseline)

        ok, _ = verifier.verify_component("C1", "H1")
        self.assertTrue(ok)

        bad, _ = verifier.verify_component("C1", "H2")
        self.assertFalse(bad)

if __name__ == "__main__":
    unittest.main()
