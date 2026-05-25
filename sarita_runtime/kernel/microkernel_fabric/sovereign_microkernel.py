import logging
import asyncio
from typing import Dict, Any, List
from sarita_runtime.kernel.microkernel_fabric.deterministic_execution_dispatcher import DeterministicExecutionDispatcher
from sarita_runtime.kernel.microkernel_fabric.kernel_execution_orchestrator import KernelExecutionOrchestrator
from sarita_runtime.kernel.runtime_determinism.deterministic_latency_controller import DeterministicLatencyController
from sarita_runtime.kernel.clock_fabric.runtime_clock_authority import RuntimeClockAuthority
from sarita_runtime.kernel.microkernel_fabric.execution_epoch_orchestrator import ExecutionEpochOrchestrator
from sarita_runtime.kernel.queue_fabric.runtime_queue_authority import RuntimeQueueAuthority

class SovereignMicrokernel:
    """
    Sovereign Microkernel Execution Fabric.
    Abstracts task execution, queues, and priority routing.
    """
    def __init__(self):
        self.dispatcher = DeterministicExecutionDispatcher()
        self.orchestrator = KernelExecutionOrchestrator()
        self.clock = RuntimeClockAuthority()
        self.epoch_orchestrator = ExecutionEpochOrchestrator()
        self.queue_authority = RuntimeQueueAuthority()
        self.latency_controller = DeterministicLatencyController()
        self.active_tasks = {}

    async def boot(self):
        logging.info("BOOTING Sovereign Microkernel...")
        await self.orchestrator.initialize_execution_planes()
        await self.dispatcher.start_dispatch_loop()
        logging.info("Sovereign Microkernel ONLINE.")

    async def submit_task(self, task_id: str, payload: Dict[str, Any], priority: int = 1):
        logging.info(f"Microkernel: Accepting task {task_id} with priority {priority}")
        # Validate provenance and measure latency during submission
        if await self.orchestrator.validate_task_legitimacy(task_id, payload):
            await self.latency_controller.measure_execution_latency(
                self.dispatcher.enqueue_task, task_id, payload, priority
            )
            return True
        else:
            logging.error(f"Microkernel: Task {task_id} REJECTED - Legitimacy check failed.")
            return False

    async def get_execution_status(self, task_id: str):
        return await self.dispatcher.get_task_status(task_id)
