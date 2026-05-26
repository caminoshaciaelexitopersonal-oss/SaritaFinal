import logging
import ctypes
import os

# io_uring material constants
SYS_IO_URING_SETUP = 425
SYS_IO_URING_ENTER = 426
IORING_OFF_SQ_RING = 0
IORING_OFF_CQ_RING = 0x8000000
IORING_OFF_SQES    = 0x10000000

class io_sqring_offsets(ctypes.Structure):
    _fields_ = [("head", ctypes.c_uint), ("tail", ctypes.c_uint), ("ring_mask", ctypes.c_uint), ("ring_entries", ctypes.c_uint), ("flags", ctypes.c_uint), ("dropped", ctypes.c_uint), ("array", ctypes.c_uint), ("resv1", ctypes.c_uint), ("resv2", ctypes.c_uint64)]

class io_cqring_offsets(ctypes.Structure):
    _fields_ = [("head", ctypes.c_uint), ("tail", ctypes.c_uint), ("ring_mask", ctypes.c_uint), ("ring_entries", ctypes.c_uint), ("overflow", ctypes.c_uint), ("cqes", ctypes.c_uint), ("flags", ctypes.c_uint), ("resv1", ctypes.c_uint), ("resv2", ctypes.c_uint64)]

class io_uring_params(ctypes.Structure):
    _fields_ = [("sq_entries", ctypes.c_uint), ("cq_entries", ctypes.c_uint), ("flags", ctypes.c_uint), ("sq_thread_cpu", ctypes.c_uint), ("sq_thread_idle", ctypes.c_uint), ("features", ctypes.c_uint), ("wq_fd", ctypes.c_uint), ("resv", ctypes.c_uint * 3), ("sq_off", io_sqring_offsets), ("cq_off", io_cqring_offsets)]

class IoUringExecutionEngine:
    """
    Material io_uring engine.
    Uses real mmap and shared memory for ring interaction.
    """
    def __init__(self, entries: int = 128):
        self.entries = entries
        self.ring_fd = -1
        self.libc = ctypes.CDLL('libc.so.6', use_errno=True)
        self.sq_ptr = None
        self.cq_ptr = None
        self.sqe_ptr = None

    def initialize_material_rings(self):
        logging.info("io_uring Engine: Initializing material rings.")
        params = io_uring_params()
        res = self.libc.syscall(SYS_IO_URING_SETUP, self.entries, ctypes.byref(params))
        if res < 0:
            logging.error(f"io_uring Engine: Setup failed (errno {ctypes.get_errno()})")
            return False

        self.ring_fd = res

        # Calculate material mmap sizes
        sq_size = params.sq_off.array + params.sq_entries * 4
        cq_size = params.cq_off.cqes + params.cq_entries * 16 # cqe is 16 bytes
        sqe_size = params.sq_entries * 64 # sqe is 64 bytes

        self.sq_ptr = self._mmap(sq_size, IORING_OFF_SQ_RING)
        self.cq_ptr = self._mmap(cq_size, IORING_OFF_CQ_RING)
        self.sqe_ptr = self._mmap(sqe_size, IORING_OFF_SQES)

        if not all([self.sq_ptr, self.cq_ptr, self.sqe_ptr]):
            logging.error("io_uring Engine: mmap failed.")
            return False

        logging.info(f"io_uring Engine: Physical substrate mapped (FD {self.ring_fd})")
        return True

    def _mmap(self, size: int, offset: int):
        mmap = self.libc.mmap
        mmap.restype = ctypes.c_void_p
        mmap.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_long]
        # PROT_READ|PROT_WRITE=3, MAP_SHARED=1
        ptr = mmap(None, size, 3, 1, self.ring_fd, offset)
        return None if ptr == -1 else ptr

    def submit_and_wait(self, to_submit: int):
        if self.ring_fd < 0: return -1
        # Real-time kernel entry
        return self.libc.syscall(SYS_IO_URING_ENTER, self.ring_fd, to_submit, 0, 0, None)

    def __del__(self):
        if self.ring_fd >= 0:
            os.close(self.ring_fd)
