import queue
import time

class ExperimentalScheduler:
    """
    Schedules experiments based on priority or temporal rules, execution queues, or pipeline requirements.
    """
    def __init__(self, exp_manager):
        self.exp_manager = exp_manager
        self.queue = []

    def schedule(self, experiment_id: str, runner_func, priority: int = 1):
        self.queue.append({
            "experiment_id": experiment_id,
            "runner": runner_func,
            "priority": priority,
            "scheduled_at": time.time()
        })
        self.queue.sort(key=lambda x: (-x["priority"], x["scheduled_at"]))

    def run_next(self) -> dict:
        if not self.queue:
            return {"status": "EMPTY_QUEUE"}
        task = self.queue.pop(0)
        res = self.exp_manager.run_experiment(task["experiment_id"], task["runner"])
        return {
            "experiment_id": task["experiment_id"],
            "result": res
        }

    def run_all(self) -> list:
        results = []
        while self.queue:
            results.append(self.run_next())
        return results
