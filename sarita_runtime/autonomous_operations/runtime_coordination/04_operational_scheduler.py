import asyncio
import logging

class OperationalScheduler:
    def schedule_task(self, task_name, cron):
        logging.info(f"Autonomous Scheduler: task {task_name} scheduled at {cron}")
        return True
