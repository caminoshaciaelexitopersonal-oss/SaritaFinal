import logging

class DurableConsensusEngine:
    def __init__(self, node_id, total_nodes):
        self.node_id = node_id
        self.total_nodes = total_nodes
        self.leadership_term = 0
        self.is_leader = False

    def propose_state_change(self, target_mode, quorum_votes):
        logging.info(f"Node {self.node_id} proposing state change to {target_mode}...")
        if quorum_votes >= (self.total_nodes // 2) + 1:
            logging.info("Quorum reached. Persisting state change to DB...")
            # Lógica real: UPDATE infrastructure.global_system_state
            return True
        logging.warning("Failed to reach quorum. Aborting.")
        return False

    def prevent_split_brain(self, detected_leaders):
        if len(detected_leaders) > 1:
            logging.critical("SPLIT-BRAIN DETECTED. Initiating fencing protocols...")
            # Lógica real: Shutdown self or fence node
            return True
        return False

if __name__ == "__main__":
    engine = DurableConsensusEngine("node-alpha", 3)
    engine.propose_state_change("WAR_MODE", 2)
