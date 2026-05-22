import asyncio
import logging
from temporalio.client import Client
from temporalio.worker import Worker

class DistributedSagaRuntime:
    def __init__(self, temporal_host="localhost:7233"):
        self.host = temporal_host
        self.client = None

    async def connect(self):
        self.client = await Client.connect(self.host)
        logging.info(f"Connected to Temporal Cluster at {self.host}")

    async def run_worker(self, task_queue, workflows, activities):
        # 50.4 - Real Worker execution
        worker = Worker(
            self.client,
            task_queue=task_queue,
            workflows=workflows,
            activities=activities
        )
        logging.info(f"Temporal Worker active on queue: {task_queue}")
        await worker.run()

if __name__ == "__main__":
    runtime = DistributedSagaRuntime()
    # asyncio.run(runtime.connect())
