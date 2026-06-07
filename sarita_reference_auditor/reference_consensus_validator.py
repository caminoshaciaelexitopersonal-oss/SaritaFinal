import hashlib
import json

class ReferenceConsensusValidator:
    """
    Independent validator for multi-domain consensus.
    """
    @staticmethod
    def verify_consensus_proof(proof: dict, domain_keys: dict):
        evidence_hash = proof["evidence_hash"]
        for domain_id in proof["domains"]:
            if domain_id not in domain_keys:
                return False, f"Unknown domain: {domain_id}"

            signature = proof["signatures"][domain_id]
            pub_key = domain_keys[domain_id]

            # Independent reconstruction of signature simulation
            expected = f"SIG_{hashlib.sha256(f'{evidence_hash}:{pub_key}'.encode()).hexdigest()}"
            if signature != expected:
                return False, f"Invalid signature for domain {domain_id}"

        return True, "Consensus verified by reference auditor."
