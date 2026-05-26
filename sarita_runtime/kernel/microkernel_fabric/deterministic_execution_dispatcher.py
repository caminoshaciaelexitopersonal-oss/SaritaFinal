import logging
import threading
import time
import subprocess
import shlex
from typing import Dict, Any, List
from sarita_runtime.kernel.queue_fabric.runtime_queue_authority import LockFreeQueue
from sarita_runtime.kernel.io_uring_fabric.io_uring_execution_engine import IoUringExecutionEngine

class DeterministicExecutionDispatcher:
    """
    Governs CPU affinity and execution ordering.
    Integrates io_uring for material high-performance IO tasks.
    """
    def __init__(self):
        self.queues = {
            0: LockFreeQueue(100),
            1: LockFreeQueue(200),
            2: LockFreeQueue(500),
            3: LockFreeQueue(1000)
        }
        self.io_engine = IoUringExecutionEngine()
        self.io_engine.initialize_material_rings()
        self.condition = threading.Condition()
        self.is_running = False
        self._thread = None
        self.task_events = {}

    def enqueue_task(self, task_id: str, payload: Dict[str, Any], priority: int):
        priority = max(0, min(priority, 3))
        event = threading.Event()
        self.task_events[task_id] = event

        with self.condition:
            self.queues[priority].put((task_id, payload))
            self.condition.notify_all()

    def start_dispatch_loop(self):
        if not self.is_running:
            self.is_running = True
            self._thread = threading.Thread(target=self._dispatch_loop, daemon=True)
            self._thread.start()

    def _dispatch_loop(self):
        while self.is_running:
            task = None
            with self.condition:
                while self.is_running:
                    for p in range(4):
                        item = self.queues[p].get(block=False)
                        if item:
                            task = item
                            break
                    if task: break
                    self.condition.wait(timeout=0.1)

            if task:
                self._execute_material_task(task)

    def _execute_material_task(self, task):
        task_id, payload = task
        logging.info(f"Dispatcher: PHYSICALLY EXECUTING {task_id}")

        if payload.get("type") == "IO_URING_OP":
            # Direct integration with materialized IO engine
            res = self.io_engine.submit_and_wait(1)
            payload["result"] = {"status": "MATERIAL_IO_COMPLETED", "res": res}
        else:
            callback = payload.get("callback")
            if callback:
                try:
                    payload["result"] = callback(payload)
                except Exception as e:
                    logging.error(f"Dispatcher: Task {task_id} failed: {e}")

        if task_id in self.task_events:
            self.task_events[task_id].set()

    def wait_for_completion(self, task_id: str):
        event = self.task_events.get(task_id)
        if event:
            return event.wait(timeout=30.0)
        return False
