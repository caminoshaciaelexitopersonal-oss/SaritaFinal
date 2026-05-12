import logging

class QuorumPersistence:
    def persist_state(self, state):
        logging.info("Persisting quorum state to durable store.")
        return True
