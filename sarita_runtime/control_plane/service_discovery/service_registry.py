import time
import logging

class ServiceRegistry:
    def __init__(self):
        self.services = {} # service_name -> {node_id, status, last_heartbeat}

    def register_service(self, name, node_id, metadata=None):
        self.services[name] = {
            "node_id": node_id,
            "status": "ALIVE",
            "last_heartbeat": time.time(),
            "metadata": metadata or {}
        }
        logging.info(f"Service Registered: {name} on Node {node_id}")

    def get_service(self, name):
        return self.services.get(name)

    def prune_dead_services(self, timeout=30):
        now = time.time()
        dead = [k for k, v in self.services.items() if now - v["last_heartbeat"] > timeout]
        for k in dead:
            logging.warning(f"Service {k} marked as DEAD.")
            self.services[k]["status"] = "DEAD"

if __name__ == "__main__":
    registry = ServiceRegistry()
    registry.register_service("FinanceWorker", "node-01")
    print(registry.get_service("FinanceWorker"))
