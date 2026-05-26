import logging

class DeterministicRestartAuthority:
    """
    Absolute authority over sovereign restart.
    Ensures replay determinism during re-initialization.
    """
    def __init__(self, reconstructor):
        self.reconstructor = reconstructor

    def authorize_restart(self):
        logging.info("Restart Authority: Authorizing material deterministic restart.")
        if self.reconstructor.reconstruct_from_last_stable_epoch():
            return "READY_FOR_EXECUTION"
        return "RECOVERY_FAILED"
