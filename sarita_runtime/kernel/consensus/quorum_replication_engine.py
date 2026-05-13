import logging

class QuorumReplicationEngine:
    def __init__(self, state_machine):
        self.state_machine = state_machine
        self.replicated_log = []

    def replicate_entry(self, entry, quorum_ack_count):
        logging.info(f"Replicating log entry: {entry.get('id')}")
        if quorum_ack_count >= 2: # Mock quorum for 3 nodes
            self.state_machine.apply_command(entry)
            self.replicated_log.append(entry)
            return True
        return False
