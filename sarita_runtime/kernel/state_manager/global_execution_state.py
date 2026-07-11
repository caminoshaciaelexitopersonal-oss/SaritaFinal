class GlobalExecutionState:
    """
    Tracks state of autonomous task execution flows, queues, and latency metrics.
    """
    def __init__(self):
        self.active_tasks = {}
        self.completed_count = 0
        self.failed_count = 0
        self.total_execution_time = 0.0

    def start_task(self, task_id: str, metadata: dict):
        self.active_tasks[task_id] = metadata

    def end_task(self, task_id: str, success: bool, run_time: float):
        if task_id in self.active_tasks:
            del self.active_tasks[task_id]
        if success:
            self.completed_count += 1
        else:
            self.failed_count += 1
        self.total_execution_time += run_time

    def to_dict(self) -> dict:
        return {
            "active_tasks_count": len(self.active_tasks),
            "completed_count": self.completed_count,
            "failed_count": self.failed_count,
            "total_execution_time": round(self.total_execution_time, 4)
        }
