import logging

class SubmissionCompletionSynchronizer:
    """
    Manages SQ head/tail and CQ deterministic completion tracking.
    """
    def __init__(self):
        self.sq_tail = 0
        self.cq_head = 0

    def advance_sq(self):
        self.sq_tail += 1
        return self.sq_tail

    def reap_cq(self, count: int):
        self.cq_head += count
        logging.debug(f"CQ Synchronizer: Reaped {count} completions. Head: {self.cq_head}")
