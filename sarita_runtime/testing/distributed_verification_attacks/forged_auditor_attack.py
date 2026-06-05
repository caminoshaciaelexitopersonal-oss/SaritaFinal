import unittest
from sarita_runtime.kernel.distributed_verification.auditor_consensus_engine import AuditorConsensusEngine

class DistributedVerificationAttackTest(unittest.TestCase):
    def test_insufficient_quorum_rejection(self):
        # 1. Consensus requires 3 auditors
        engine = AuditorConsensusEngine(required_quorum=3)
        evidence_hash = "EVIDENCE_A"

        # 2. Only 2 auditors submit positive verdicts
        engine.submit_verdict("Auditor_1", evidence_hash, True, "sig1")
        engine.submit_verdict("Auditor_2", evidence_hash, True, "sig2")

        # 3. Check consensus (should be False)
        is_consensus, msg = engine.get_consensus(evidence_hash)
        self.assertFalse(is_consensus)
        self.assertIn("Quorum not met (2/3)", msg)

        # 4. 3rd auditor submits
        engine.submit_verdict("Auditor_3", evidence_hash, True, "sig3")
        is_consensus, _ = engine.get_consensus(evidence_hash)
        self.assertTrue(is_consensus)

    def test_negative_verdict_exclusion(self):
        engine = AuditorConsensusEngine(required_quorum=2)
        evidence_hash = "EVIDENCE_B"

        engine.submit_verdict("Auditor_1", evidence_hash, True, "sig1")
        engine.submit_verdict("Auditor_2", evidence_hash, False, "sig2") # Negative

        is_consensus, _ = engine.get_consensus(evidence_hash)
        self.assertFalse(is_consensus, "Negative verdict should not count toward quorum.")

if __name__ == "__main__":
    unittest.main()
