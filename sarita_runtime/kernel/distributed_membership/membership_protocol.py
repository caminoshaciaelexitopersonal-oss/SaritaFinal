import uuid
import time
import logging

class MembershipProtocol:
    def __init__(self, node_id):
        self.node_id = node_id
        self.peers = {} # node_id -> status

    def process_gossip(self, incoming_gossip):
        # 51.2 - Gossip synchronization real
        for node, data in incoming_gossip.items():
            if node not in self.peers or data['version'] > self.peers[node]['version']:
                self.peers[node] = data
                logging.info(f"NODE_TOPOLOGY_UPDATED: {node} version {data['version']}")

    def generate_heartbeat(self):
        return {
            "node_id": self.node_id,
            "status": "ALIVE",
            "timestamp": time.time(),
            "version": int(time.time())
        }

    def detect_dead_nodes(self, timeout=30):
        now = time.time()
        dead = [k for k, v in self.peers.items() if now - v["timestamp"] > timeout]
        return dead

if __name__ == "__main__":
    mp = MembershipProtocol("node-A")
    hb = mp.generate_heartbeat()
    mp.process_gossip({"node-B": {"status": "ALIVE", "timestamp": time.time(), "version": 1}})
