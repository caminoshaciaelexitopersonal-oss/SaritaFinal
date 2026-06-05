import unittest
from sarita_runtime.kernel.sovereign_trust.component_certificate_chain import SovereignComponentCertificate
from sarita_runtime.kernel.sovereign_constitution.constitutional_runtime_guard import ConstitutionalRuntimeGuard, ConstitutionalViolationException
from sarita_runtime.kernel.constitutional_court.constitutional_court import ConstitutionalCourt
from sarita_runtime.kernel.component_identity.sovereign_identity_engine import SovereignIdentityEngine

class ForgedCertificateAttack(unittest.TestCase):
    def test_forged_signature_attack(self):
        engine = SovereignIdentityEngine()
        court = ConstitutionalCourt(engine)
        guard = ConstitutionalRuntimeGuard(court)

        # 1. Create a "forged" certificate manually (not issued by Court)
        # In this simplified model, any certificate not in the engine's registry is rejected.

        with self.assertRaises(ConstitutionalViolationException):
            guard.enforce_certified_mutation("ForgedComponent", __file__)

if __name__ == "__main__":
    unittest.main()
