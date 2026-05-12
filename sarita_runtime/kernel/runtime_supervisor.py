import asyncio
import logging
import signal
import subprocess

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("RuntimeSupervisor")

class RuntimeSupervisor:
    def __init__(self):
        self.workers = {} # name -> process
        self.running = True

    async def spawn_worker(self, name, command):
        logger.info(f"Spawning worker: {name} with cmd: {command}")
        process = await asyncio.create_subprocess_exec(
            *command.split(),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        self.workers[name] = process
        asyncio.create_task(self.monitor_process(name, process))

    async def monitor_process(self, name, process):
        stdout, stderr = await process.communicate()
        if process.returncode != 0:
            logger.error(f"Worker {name} crashed with exit code {process.returncode}")
            if self.running:
                logger.info(f"Restarting worker {name}...")
                # await self.spawn_worker(name, command) # Logic for restart
        else:
            logger.info(f"Worker {name} finished gracefully.")

    async def shutdown(self):
        logger.info("Initiating graceful shutdown of all workers...")
        self.running = False
        for name, process in self.workers.items():
            process.terminate()
        logger.info("Shutdown complete.")

if __name__ == "__main__":
    supervisor = RuntimeSupervisor()
    # Usage: asyncio.run(supervisor.spawn_worker("FinanceWorker", "python -m sarita_runtime.kernel.workers.financial_worker"))
