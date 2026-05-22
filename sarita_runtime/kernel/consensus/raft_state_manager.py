import time
import logging

class RaftStateManager:
    def __init__(self, node_id, quorum_size):
        self.node_id = node_id
        self.quorum_size = quorum_size
        self.current_term = 0
        self.voted_for = None
        self.log = []
        self.commit_index = 0
        self.state = "FOLLOWER"

    def receive_heartbeat(self, leader_id, term):
        if term >= self.current_term:
            self.state = "FOLLOWER"
            self.current_term = term
            return True
        return False

    def request_vote(self, term, candidate_id):
        if term > self.current_term:
            self.current_term = term
            self.voted_for = candidate_id
            return True
        return False

class DurableConsensus:
    def persist_quorum(self, term, leader_id):
        print(f"Persisting Term {term} Leader {leader_id} to SQL/Redis...")
        # Lógica real de persistencia en infrastructure.global_system_state
        return True

if __name__ == "__main__":
    raft = RaftStateManager("node-1", 2)
    print(f"Node Status: {raft.state}")
