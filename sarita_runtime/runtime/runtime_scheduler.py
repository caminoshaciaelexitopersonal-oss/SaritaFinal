import collections

class RuntimeScheduler:
    """
    Sovereign Task Scheduler. Coordinates priority-weighted task executions.
    """
    def __init__(self):
        self.queue = collections.deque()

    def schedule_task(self, name: str, task_callable, priority: int = 1):
        self.queue.append({
            "name": name,
            "callable": task_callable,
            "priority": priority
        })
        # Keep queue sorted by priority descending
        sorted_queue = sorted(self.queue, key=lambda x: x["priority"], reverse=True)
        self.queue = collections.deque(sorted_queue)

    def pop_next_task(self):
        if self.queue:
            return self.queue.popleft()
        return None
