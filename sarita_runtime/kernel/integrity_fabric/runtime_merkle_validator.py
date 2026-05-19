import hashlib
import logging
import json

class RuntimeMerkleValidator:
    """
    Maintains a Merkle tree of the entire federated runtime state.
    Provides mathematically verifiable proof of operational integrity.
    """
    def __init__(self):
        self.leaves = []
        self.root_hash = ""

    def update_leaf(self, component_id, state):
        leaf_data = f"{component_id}:{json.dumps(state, sort_keys=True)}"
        leaf_hash = hashlib.sha256(leaf_data.encode()).hexdigest()
        self.leaves.append(leaf_hash)
        self._recalculate_root()

    def _recalculate_root(self):
        # Deterministic Merkle Root calculation
        if not self.leaves:
            self.root_hash = ""
            return

        current_layer = sorted(self.leaves)
        while len(current_layer) > 1:
            next_layer = []
            for i in range(0, len(current_layer), 2):
                l1 = current_layer[i]
                l2 = current_layer[i+1] if i+1 < len(current_layer) else l1
                next_layer.append(hashlib.sha256((l1 + l2).encode()).hexdigest())
            current_layer = next_layer
        self.root_hash = current_layer[0]
        logging.info(f"Integrity Fabric: New Merkle Root established: {self.root_hash[:8]}")

class FederatedHashChain:
    def append_transition(self, prev_hash, state_delta):
        """
        Creates an immutable hash chain of all runtime transitions.
        """
        new_hash = hashlib.sha256(f"{prev_hash}:{state_delta}".encode()).hexdigest()
        return new_hash
