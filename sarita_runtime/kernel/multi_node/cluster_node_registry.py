import uuid
import logging

class ClusterNodeRegistry:
    def __init__(self):
        self.nodes = {} # node_id -> metadata

    def register_node(self, node_name, region, capabilities):
        node_id = str(uuid.uuid4())
        self.nodes[node_id] = {
            "name": node_name,
            "region": region,
            "capabilities": capabilities,
            "status": "ALIVE",
            "last_heartbeat": 0
        }
        logging.info(f"NODE_REGISTERED: {node_name} in {region}")
        return node_id

    def update_heartbeat(self, node_id, timestamp):
        if node_id in self.nodes:
            self.nodes[node_id]["last_heartbeat"] = timestamp
            return True
        return False

class RuntimeMembershipManager:
    def check_quorum(self, total_expected):
        alive = sum(1 for n in self.nodes.values() if n["status"] == "ALIVE")
        return alive >= (total_expected // 2) + 1
