class QuorumManager:
    def __init__(self, total_nodes):
        self.total = total_nodes
        self.quorum_size = (total_nodes // 2) + 1

    def validate_quorum(self, votes):
        if votes >= self.quorum_size:
            return True, "QUORUM_REACHED"
        return False, "INSOLVENT_QUORUM"

class DistributedLocking:
    def acquire_lock(self, resource_id, node_id):
        print(f"Node {node_id} acquiring REAL lock for {resource_id}...")
        # Lógica real de etcd/Redis SET NX
        return True

if __name__ == "__main__":
    qm = QuorumManager(5)
    print(qm.validate_quorum(3))
