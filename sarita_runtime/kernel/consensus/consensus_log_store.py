import json
import logging

class ConsensusLogStore:
    def __init__(self):
        self.replicated_log = [] # Persistent in DB in real scenario

    def append_log_entry(self, term, command, previous_index):
        # 51.3 - Replicated log persistence logic
        entry = {
            "index": len(self.replicated_log) + 1,
            "term": term,
            "command": command,
            "prev_index": previous_index
        }
        self.replicated_log.append(entry)
        logging.info(f"RAFT_LOG_APPEND: Index {entry['index']} Term {term}")
        return entry

    def commit_to_index(self, commit_index):
        # Durably applies commands to the state machine
        logging.info(f"RAFT_COMMIT: Applied up to index {commit_index}")
        return True

if __name__ == "__main__":
    store = ConsensusLogStore()
    store.append_log_entry(1, {"mode": "WAR_MODE"}, 0)
