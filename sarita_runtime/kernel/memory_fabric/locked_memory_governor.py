import logging
import ctypes

class LockedMemoryGovernor:
    """
    Governs mlock/munlock to prevent page faults in sovereign execution.
    Material enforcement of physical memory locking.
    """
    def __init__(self):
        self.libc = ctypes.CDLL('libc.so.6', use_errno=True)

    def lock_all_process_memory(self):
        """
        Calls mlockall(MCL_CURRENT | MCL_FUTURE) to ensure no swapping.
        """
        logging.info("Memory Governor: Materializing absolute memory lock.")
        # MCL_CURRENT = 1, MCL_FUTURE = 2
        res = self.libc.mlockall(3)
        if res != 0:
            logging.error(f"Memory Governor: mlockall failed (errno {ctypes.get_errno()})")
            return False
        return True

    def unlock_all_memory(self):
        return self.libc.munlockall() == 0
