import logging
import ctypes

class KernelPollingSubmissionEngine:
    """
    Materializes kernel submission through ring entry and SQ management.
    """
    def __init__(self, ring_fd: int):
        self.ring_fd = ring_fd
        self.libc = ctypes.CDLL('libc.so.6', use_errno=True)

    def submit_and_wait(self, to_submit: int, min_complete: int):
        """
        Calls io_uring_enter to submit events and wait for completions.
        """
        logging.debug(f"io_uring Engine: Submitting {to_submit} requests.")
        # SYS_IO_URING_ENTER = 426
        res = self.libc.syscall(426, self.ring_fd, to_submit, min_complete, 1, None)
        if res < 0:
            logging.error(f"io_uring Engine: io_uring_enter FAILED (errno {ctypes.get_errno()})")
            return False
        return True
