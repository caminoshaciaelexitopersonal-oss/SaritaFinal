import unittest
from sarita_runtime.kernel.key_governance.quorum_authorization_engine import QuorumAuthorizationEngine

class CompromisedAuthorityAttack(unittest.TestCase):
    def test_single_authority_insufficient(self):
        # Critical decisions require a quorum of 2
        quorum_engine = QuorumAuthorizationEngine(required_quorum=2)

        proposal_id = "root_replacement_84"

        # 1. Compromised Authority A approves rogue proposal
        quorum_engine.register_approval(proposal_id, "Compromised_Auth_A")

        # 2. Check if authorized (should be False)
        self.assertFalse(quorum_engine.is_authorized(proposal_id))

        # 3. Valid Authority B approves
        quorum_engine.register_approval(proposal_id, "Valid_Auth_B")

        # 4. Check if authorized (should be True)
        self.assertTrue(quorum_engine.is_authorized(proposal_id))

if __name__ == "__main__":
    unittest.main()
