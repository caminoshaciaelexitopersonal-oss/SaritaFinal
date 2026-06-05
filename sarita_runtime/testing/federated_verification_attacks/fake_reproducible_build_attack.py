import hashlib
import json

class FakeReproducibleBuildAttack:
    """
    Simulates a build process that generates a binary which doesn't match the source code
    but tries to fake the build proof.
    """
    def run_attack(self, proof_engine, mal_hash):
        # A proof should only be valid if the source_hash in it matches the
        # actual source hash of the current source tree.
        actual_manifest = proof_engine.generate_source_manifest()
        actual_source_hash = proof_engine.calculate_canonical_hash(actual_manifest)

        if mal_hash != actual_source_hash:
            return True, "Attack blocked: Fake build hash does not match source reconstruction."
        return False, "Attack succeeded: Fake build hash accepted."
