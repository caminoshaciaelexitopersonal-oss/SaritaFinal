import hashlib
import json

class CrossDomainConsensus:
    """
    Facilitates the exchange of consensus proofs between distinct domains.
    """
    @staticmethod
    def generate_consensus_proof(evidence_hash: str, domain_signatures: dict):
        # domain_signatures: {domain_id: signature}
        payload = {
            "evidence_hash": evidence_hash,
            "domains": list(domain_signatures.keys()),
            "signatures": domain_signatures
        }

        return payload

    @staticmethod
    def verify_consensus_proof(proof: dict, domain_keys: dict):
        """
        Verifies that each signature in the proof is valid for the corresponding domain.
        """
        evidence_hash = proof["evidence_hash"]
        for domain_id in proof["domains"]:
            if domain_id not in domain_keys:
                return False, f"Missing public key for domain: {domain_id}"

            signature = proof["signatures"][domain_id]
            public_key = domain_keys[domain_id]

            # Reconstruct signed payload simulation
            # Payload for consensus is the evidence_hash
            expected_sig_content = f"{evidence_hash}:{public_key}"
            expected_signature = f"SIG_{hashlib.sha256(expected_sig_content.encode()).hexdigest()}"

            if signature != expected_signature:
                return False, f"Invalid signature for domain: {domain_id}"

        return True, "All domain signatures verified."
