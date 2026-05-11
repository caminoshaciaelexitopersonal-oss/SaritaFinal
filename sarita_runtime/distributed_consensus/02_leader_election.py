import random
import time

class LeaderElection:
    def __init__(self, node_id, nodes_list):
        self.node_id = node_id
        self.nodes = nodes_list
        self.role = "FOLLOWER"
        self.term = 0

    def start_election(self):
        self.role = "CANDIDATE"
        self.term += 1
        votes = 1 # Vote for self
        print(f"Node {self.node_id} starting election for term {self.term}")

        # Simulate voting from other nodes
        for node in self.nodes:
            if node != self.node_id and random.random() > 0.3:
                votes += 1

        if votes > len(self.nodes) / 2:
            self.role = "LEADER"
            print(f"Node {self.node_id} ELECTED LEADER.")
        else:
            self.role = "FOLLOWER"
            print(f"Node {self.node_id} FAILED to win election.")

if __name__ == "__main__":
    le = LeaderElection("node-A", ["node-A", "node-B", "node-C"])
    le.start_election()
