import logging
from sarita_runtime.kernel.io_uring_fabric.io_uring_execution_engine import IoUringExecutionEngine

class IoUringCqeReclaimer:
    """
    Reclaims completed CQEs from the completion ring.
    Materializes completion harvesting.
    """
    def __init__(self, engine: IoUringExecutionEngine):
        self.engine = engine

    def reap_completions(self):
        logging.info("CQE Reclaimer: Materially reaping CQEs via engine.")
        completions = []
        while True:
            index = self.engine.reap_cqe()
            if index is None:
                break
            completions.append({"index": index, "status": "COMPLETED"})
        return completions
