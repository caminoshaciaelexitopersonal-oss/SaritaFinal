import hashlib

class DetachedStateValidator:
    """
    Validates state transformations using exported JSON snapshots (Phase 87.2).
    """
    @staticmethod
    def calculate_state_hash(state_data: dict):
        import json
        serialized = json.dumps(state_data, sort_keys=True)
        return hashlib.sha256(serialized.encode()).hexdigest()

    @staticmethod
    def verify_transition(state_n_hash: str, transition_msg: str, state_n1_hash: str, proof: str):
        raw = f"{state_n_hash}:{transition_msg}:{state_n1_hash}"
        calc_proof = hashlib.sha256(raw.encode()).hexdigest()
        return calc_proof == proof
