import logging
from sarita_runtime.kernel.io_uring_fabric.io_uring_execution_engine import IoUringExecutionEngine

class IoUringBufferRegistry:
    """
    Manages fixed, pre-registered buffers for zero-copy io_uring.
    """
    def __init__(self, engine: IoUringExecutionEngine):
        self.engine = engine
        self.registered_buffers = {}

    def register_buffer(self, buffer_id: str, buffer_ptr: int, size: int):
        logging.info(f"Buffer Registry: Materializing buffer {buffer_id} ({size} bytes)")
        # Real-world: self.engine.register_buffers(...)
        self.registered_buffers[buffer_id] = {"ptr": buffer_ptr, "size": size}
        self.engine.register_buffers([{"ptr": buffer_ptr, "len": size}])
        return True
