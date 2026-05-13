import logging

class NodeGossipSync:
    def sync_topology(self, node_id, topology):
        logging.info(f"Gossip Syncing topology from node: {node_id}")
        return True

class ClusterTopologyState:
    def __init__(self):
        self.version = 1
        self.nodes = []
