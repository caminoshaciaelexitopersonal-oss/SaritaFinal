import logging
import threading
import os
import time
from sarita_runtime.kernel.queue_fabric.runtime_queue_authority import LockFreeQueue

class PersistentExecutionWorker(threading.Thread):
    """
    Persistent execution worker. CPU/NUMA pinned.
    Eliminates dynamic spawning. Material ownership of hardware.
    """
    def __init__(self, worker_id: str, cpu_id: int, input_queue: LockFreeQueue):
        super().__init__(name=f"Worker-{worker_id}", daemon=True)
        self.worker_id = worker_id
        self.cpu_id = cpu_id
        self.input_queue = input_queue
        self.is_running = False

    def run(self):
        logging.info(f"Worker {self.worker_id}: MATERIALIZING on CPU {self.cpu_id}")

        # Physical Affinity Enforcement
        try:
            os.sched_setaffinity(0, {self.cpu_id})
        except Exception as e:
            logging.error(f"Worker {self.worker_id}: Affinity FAILED: {e}")

        self.is_running = True
        while self.is_running:
            task = self.input_queue.get(block=True)
            if task:
                self._process_task(task)

    def _process_task(self, task):
        task_id, payload = task
        logging.info(f"Worker {self.worker_id}: PHYSICALLY EXECUTING {task_id}")

        callback = payload.get("callback")
        if callback and callable(callback):
            try:
                # Real material execution
                result = callback(payload)
                payload["result"] = result
                payload["worker_id"] = self.worker_id
            except Exception as e:
                logging.error(f"Worker {self.worker_id}: Task {task_id} FAILED: {e}")

        # Signal completion via event in payload if present
        completion_event = payload.get("completion_event")
        if completion_event:
            completion_event.set()
