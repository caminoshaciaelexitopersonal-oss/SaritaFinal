import collections

class ExperimentScheduler:
    """
    Schedules and schedules execution intervals for pending scientific trials.
    """
    def __init__(self):
        self.queue = collections.deque()

    def schedule_trial(self, exp_id: str, action, priority: int = 1):
        self.queue.append({
            "exp_id": exp_id,
            "action": action,
            "priority": priority
        })
        sorted_q = sorted(self.queue, key=lambda x: x["priority"], reverse=True)
        self.queue = collections.deque(sorted_q)

    def pop_trial(self):
        if self.queue:
            return self.queue.popleft()
        return None
