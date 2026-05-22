import asyncio
import logging
import uuid
import json
import time

class FederatedNodeRegistry:
    def __init__(self, cluster_id, region):
        self.cluster_id = cluster_id
        self.region = region
        self.federation_id = str(uuid.uuid4())
        self.nodes = {} # node_id -> metadata
        self.topology_hash = ""
        self.sync_epoch = 0

    def register_node(self, node_id, metadata):
        metadata['last_seen'] = time.time()
        self.nodes[node_id] = metadata
        self._update_topology()
        logging.info(f"Node {node_id} registered in federation {self.federation_id}")

    def _update_topology(self):
        # Deterministic topology hash for convergence check
        topology_str = json.dumps(sorted(self.nodes.keys()))
        import hashlib
        self.topology_hash = hashlib.sha256(topology_str.encode()).hexdigest()
        self.sync_epoch += 1

    def get_topology(self):
        return {
            "federation_id": self.federation_id,
            "cluster_id": self.cluster_id,
            "region": self.region,
            "topology_hash": self.topology_hash,
            "sync_epoch": self.sync_epoch,
            "nodes": list(self.nodes.keys())
        }
