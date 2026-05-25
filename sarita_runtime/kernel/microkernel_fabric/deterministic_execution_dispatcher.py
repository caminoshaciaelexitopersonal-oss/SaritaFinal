import asyncio
import logging
from typing import Dict, Any, List
import time
import subprocess

class DeterministicExecutionDispatcher:
    """
    Governs CPU affinity, execution ordering, and scheduling lineage.
    Utilizes Condition variables for efficient, non-polling task dispatch.
    """
    def __init__(self):
        self.queues = {
            0: [],  # CRITICAL (using lists for use with Condition)
            1: [],  # HIGH
            2: [],  # NORMAL
            3: []   # LOW
        }
        self.condition = asyncio.Condition()
        self.execution_log = []
        self.task_states = {}
        self.task_completions = {} # task_id -> asyncio.Event
        self.current_epoch = 0
        self.is_running = False

    async def enqueue_task(self, task_id: str, payload: Dict[str, Any], priority: int):
        priority = max(0, min(priority, 3))
        async with self.condition:
            self.queues[priority].append((task_id, payload, time.time()))
            self.task_states[task_id] = "ENQUEUED"
            self.task_completions[task_id] = asyncio.Event()
            self.condition.notify_all()
        logging.info(f"Dispatcher: Task {task_id} enqueued at priority {priority}")

    async def start_dispatch_loop(self):
        if not self.is_running:
            self.is_running = True
            asyncio.create_task(self._dispatch_loop())

    async def _dispatch_loop(self):
        logging.info("Dispatcher: Execution loop started.")
        while self.is_running:
            task = None
            priority = None

            async with self.condition:
                while self.is_running:
                    # Strict priority selection
                    for p in range(4):
                        if self.queues[p]:
                            task = self.queues[p].pop(0)
                            priority = p
                            break
                    if task:
                        break
                    await self.condition.wait()

            if task:
                task_id, payload, ts = task
                await self._execute_task(task_id, payload, priority)

    async def _execute_task(self, task_id: str, payload: Dict[str, Any], priority: int):
        self.task_states[task_id] = "EXECUTING"
        logging.info(f"Dispatcher: EXECUTING task {task_id} (Priority: {priority}, Epoch: {self.current_epoch})")

        start_time = time.time()

        callback = payload.get("callback")
        if callback and callable(callback):
            try:
                if asyncio.iscoroutinefunction(callback):
                    result = await callback(payload)
                else:
                    result = callback(payload)
                payload["result"] = result
            except Exception as e:
                logging.error(f"Dispatcher: Task {task_id} callback failed: {e}")
        elif payload.get("command"):
            try:
                proc = await asyncio.create_subprocess_shell(
                    payload["command"],
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE
                )
                stdout, stderr = await proc.communicate()
                payload["result"] = {"stdout": stdout.decode(), "stderr": stderr.decode(), "code": proc.returncode}
            except Exception as e:
                logging.error(f"Dispatcher: Task {task_id} command failed: {e}")

        end_time = time.time()
        self.task_states[task_id] = "COMPLETED"

        # Notify completion
        if task_id in self.task_completions:
            self.task_completions[task_id].set()

        self.execution_log.append({
            "task_id": task_id,
            "priority": priority,
            "epoch": self.current_epoch,
            "duration": end_time - start_time,
            "timestamp": end_time
        })
        self.current_epoch += 1

    async def wait_for_completion(self, task_id: str):
        if task_id in self.task_completions:
            await self.task_completions[task_id].wait()
            return True
        return False

    async def get_task_status(self, task_id: str):
        return self.task_states.get(task_id, "UNKNOWN")
