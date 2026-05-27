import logging
import threading
from typing import Dict, Any, List
from sarita_runtime.kernel.queue_fabric.runtime_queue_authority import HighPerformanceQueue
from sarita_runtime.kernel.io_uring_fabric.io_uring_execution_engine import IoUringExecutionEngine

class DeterministicExecutionDispatcher:
    def __init__(self):
        self.queues = {
            0: HighPerformanceQueue(100),
            1: HighPerformanceQueue(200),
            2: HighPerformanceQueue(500),
            3: HighPerformanceQueue(1000)
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
                        if item: task = item; break
                    if task: break
                    self.condition.wait(timeout=0.1)
            if task: self._execute_material_task(task)

    def _execute_material_task(self, task):
        task_id, payload = task
        if payload.get('type') == 'IO_URING_OP':
            res = self.io_engine.submit_and_wait(1)
            payload['result'] = {'status': 'SUCCESS', 'res': res}
        else:
            callback = payload.get('callback')
            if callback: payload['result'] = callback(payload)
        if task_id in self.task_events: self.task_events[task_id].set()

    def wait_for_completion(self, task_id: str):
        event = self.task_events.get(task_id)
        return event.wait(timeout=30.0) if event else False
