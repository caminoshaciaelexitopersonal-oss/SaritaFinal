import logging
import ctypes
import os

class IoUringRingMapper:
    """
    Materializes memory mapping for io_uring rings.
    Enables shared memory communication between SARITA and the Linux kernel.
    """
    def __init__(self, ring_fd: int):
        self.ring_fd = ring_fd
        self.libc = ctypes.CDLL('libc.so.6', use_errno=True)

    def mmap_sq_ring(self, size: int):
        logging.info(f"io_uring Mapper: mmap SQ ring for FD {self.ring_fd}")
        # Offset 0 is IORING_OFF_SQ_RING
        return self._mmap(size, 0)

    def mmap_cq_ring(self, size: int):
        logging.info(f"io_uring Mapper: mmap CQ ring for FD {self.ring_fd}")
        # Offset 0x8000000 is IORING_OFF_CQ_RING
        return self._mmap(size, 0x8000000)

    def _mmap(self, size: int, offset: int):
        # mmap(void *addr, size_t length, int prot, int flags, int fd, off_t offset);
        mmap = self.libc.mmap
        mmap.restype = ctypes.c_void_p
        mmap.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_long]

        # PROT_READ|PROT_WRITE = 3, MAP_SHARED = 1
        res = mmap(None, size, 3, 1, self.ring_fd, offset)
        if res == -1:
            errno = ctypes.get_errno()
            logging.error(f"io_uring Mapper: mmap FAILED (errno {errno})")
            return None
        return res
