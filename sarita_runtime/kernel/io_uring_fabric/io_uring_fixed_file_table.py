import logging
from sarita_runtime.kernel.io_uring_fabric.io_uring_execution_engine import IoUringExecutionEngine

class IoUringFixedFileTable:
    """
    Manages the registered file table for io_uring.
    Eliminates file open/close overhead in the physical path.
    """
    def __init__(self, engine: IoUringExecutionEngine):
        self.engine = engine
        self.file_table = {}

    def register_file(self, fd: int):
        logging.info(f"File Table: Registering FD {fd} in material ring.")
        self.file_table[fd] = True
        self.engine.register_files([fd])
        return True
