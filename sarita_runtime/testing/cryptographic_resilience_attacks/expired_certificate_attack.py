import unittest
import time
from sarita_runtime.kernel.sovereign_trust.component_certificate_chain import SovereignComponentCertificate
from sarita_runtime.kernel.sovereign_trust.trust_chain_validator import TrustChainValidator
from sarita_runtime.kernel.sovereign_trust.sovereign_root_authority import TrustAnchor

class ExpiredCertificateAttack(unittest.TestCase):
    def test_expired_certificate_rejection(self):
        # 1. Create a certificate that is already expired
        cert = SovereignComponentCertificate("Comp1", "Auth1", "sig1", "hash1")
        cert.expiry_date = time.time() - 3600 # Expired 1 hour ago

        anchor = TrustAnchor("root_sig")

        # 2. Validate
        is_valid, msg = TrustChainValidator.validate_chain(cert, anchor)

        self.assertFalse(is_valid)
        self.assertEqual(msg, "Certificate expired.")

if __name__ == "__main__":
    unittest.main()
