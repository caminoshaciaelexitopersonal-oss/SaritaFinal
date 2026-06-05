import hashlib

class CrossDomainConsensusAttack:
    """
    Simulates the injection of a fake consensus proof.
    """
    def run_attack(self, consensus_util, domain_keys):
        fake_proof = {
            "evidence_hash": "evil_state_hash",
            "domains": ["domain_alpha"],
            "signatures": {
                "domain_alpha": "FAKE_SIG_123"
            }
        }

        success, msg = consensus_util.verify_consensus_proof(fake_proof, domain_keys)

        if not success:
            return True, "Attack blocked: Fake consensus proof rejected due to invalid signature."
        return False, "Attack succeeded: Fake consensus proof was accepted."
