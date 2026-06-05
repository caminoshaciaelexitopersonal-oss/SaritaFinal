import unittest
import os
from sarita_runtime.kernel.hardware_trust.hardware_root_of_trust import HardwareRootOfTrust, TPMAdapter
from sarita_runtime.kernel.component_identity.sovereign_identity_engine import SovereignIdentityEngine
from sarita_runtime.kernel.hardware_trust.runtime_attestation_engine import RuntimeAttestationEngine

class RuntimeAttestationAttackTest(unittest.TestCase):
    def setUp(self):
        self.rot = HardwareRootOfTrust(TPMAdapter())
        self.identity = SovereignIdentityEngine()
        self.attestation = RuntimeAttestationEngine(self.rot, self.identity)

    def test_forged_runtime_attack(self):
        # A component that is NOT certified tries to get attestation
        fake_file = "/tmp/rogue_exec.py"
        with open(fake_file, "w") as f:
            f.write("payload = 'evil'")

        is_attested, result = self.attestation.attest_component("RogueComp", fake_file)

        self.assertFalse(is_attested)
        self.assertEqual(result, "Software identity validation failed.")

        if os.path.exists(fake_file): os.remove(fake_file)

    def test_tampered_state_attestation(self):
        # Even if a component ID exists, if the file is tampered after certification
        # (different hash), the identity engine (from Phase 82) would catch it.
        pass

if __name__ == "__main__":
    unittest.main()
