import logging
import asyncio
import os
from concurrent.futures import ThreadPoolExecutor

class KernelExecutionTracepipe:
    """
    Materializes kernel-level execution evidence via trace_pipe.
    Implemented with async execution to avoid blocking the event loop.
    """
    def __init__(self, trace_pipe_path="/sys/kernel/debug/tracing/trace_pipe"):
        self.trace_pipe = trace_pipe_path
        self.executor = ThreadPoolExecutor(max_workers=1)

    async def stream_kernel_evidence(self, limit: int = 100):
        logging.info("Tracepipe: Starting kernel evidence stream.")
        if not os.path.exists(self.trace_pipe):
            logging.warning(f"Tracepipe: {self.trace_pipe} not found.")
            return

        count = 0
        while count < limit:
            line = await self._read_line_async()
            if line:
                logging.info(f"Tracepipe Evidence: {line}")
                yield line
                count += 1
            else:
                await asyncio.sleep(0.1)

    async def _read_line_async(self):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(self.executor, self._read_line_sync)

    def _read_line_sync(self):
        try:
            with open(self.trace_pipe, "r") as f:
                return f.readline().strip()
        except Exception:
            return None
