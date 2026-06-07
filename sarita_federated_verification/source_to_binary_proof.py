import hashlib
import json
import time

class SourceToBinaryProof:
    """
    Generates a cryptographic proof linking source manifest to a specific build artifact.
    """
    @staticmethod
    def create_proof(source_hash: str, build_id: str, compiler_info: dict):
        proof_body = {
            "source_hash": source_hash,
            "build_id": build_id,
            "compiler": compiler_info,
            "timestamp": time.time()
        }

        proof_json = json.dumps(proof_body, sort_keys=True)
        signature = hashlib.sha256(f"BUILD_PROOF:{proof_json}".encode()).hexdigest()

        return {
            "proof": proof_body,
            "signature": signature
        }
