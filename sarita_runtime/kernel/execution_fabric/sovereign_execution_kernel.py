import logging
import asyncio
import uuid
import concurrent.futures
from sarita_runtime.kernel.microkernel_fabric.sovereign_microkernel import SovereignMicrokernel

class SovereignExecutionKernel:
    """
    Sovereign Execution Fabric Kernel (Phase 68).
    Eliminates asyncio polling. Uses ThreadPoolExecutor for blocking wait.
    """
    def __init__(self, node_id, fabric_router):
        self.node_id = node_id
        self.router = fabric_router
        self.microkernel = SovereignMicrokernel()
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)

    async def boot(self):
        await self.microkernel.boot()

    async def execute_federated_op(self, operation):
        task_id = operation.get('id', str(uuid.uuid4()))
        operation["callback"] = self.router.route_operation

        logging.info(f"Execution Kernel: Submitting {task_id} to material path.")

        # Physical submission
        self.microkernel.dispatcher.enqueue_task(task_id, operation, operation.get('priority', 2))

        # Efficient async wait for physical thread completion via executor
        loop = asyncio.get_event_loop()
        success = await loop.run_in_executor(
            self.executor,
            self.microkernel.dispatcher.wait_for_task,
            task_id
        )

        if success:
            return operation.get("result")
        return False
