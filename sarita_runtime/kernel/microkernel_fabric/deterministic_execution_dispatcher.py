import logging
import threading
from typing import Dict, Any, List
from sarita_runtime.kernel.queue_fabric.runtime_queue_authority import LockFreeQueue

class DeterministicExecutionDispatcher:
    """
    Governs CPU affinity and execution ordering.
    PROHIBIDO: time.sleep, asyncio.sleep.
    Uses threading.Condition for efficient waiting.
    """
    def __init__(self):
        self.queues = {
            0: LockFreeQueue(100),
            1: LockFreeQueue(200),
            2: LockFreeQueue(500),
            3: LockFreeQueue(1000)
        }
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
        logging.info(f"Dispatcher: Enqueued material task {task_id}")

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
                    self.condition.wait() # Efficient kernel-level wait

            if task:
                self._execute_material_task(task)

    def _execute_material_task(self, task):
        task_id, payload = task
        logging.info(f"Dispatcher: Executing physical task {task_id}")

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
