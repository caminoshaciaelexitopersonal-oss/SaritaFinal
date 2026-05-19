import random
import logging

class LeaderElection:
    def __init__(self, state_manager):
        self.raft = state_manager

    def tick(self):
        if self.raft.state == "FOLLOWER":
             logging.info("Heartbeat timeout. Starting election...")
             self.raft.state = "CANDIDATE"
             return True
        return False
