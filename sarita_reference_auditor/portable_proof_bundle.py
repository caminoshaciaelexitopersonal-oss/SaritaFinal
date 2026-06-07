import hashlib

class PortableProofBundle:
    """
    A self-contained bundle containing evidence, signatures, and build proofs.
    Everything needed to independently verify SARITA without the repository.
    """
    @staticmethod
    def create_bundle(suep_json: str, consensus_proof: dict, build_proof: dict):
        bundle = {
            "evidence": suep_json,
            "consensus": consensus_proof,
            "build": build_proof,
            "bundle_hash": hashlib.sha256(suep_json.encode()).hexdigest()
        }
        return bundle
