import logging
import threading
import uuid
from sarita_runtime.kernel.microkernel_fabric.sovereign_microkernel import SovereignMicrokernel

class SovereignExecutionKernel:
    """
    Sovereign Execution Fabric Kernel.
    Refactored to minimize asyncio dependency on critical path.
    """
    def __init__(self, node_id, fabric_router):
        self.node_id = node_id
        self.router = fabric_router
        self.microkernel = SovereignMicrokernel()
        self.is_active = False

    async def boot(self):
        # Booting microkernel (which starts its own physical thread)
        await self.microkernel.boot()
        self.is_active = True

    async def execute_federated_op(self, operation):
        """
        Submits operation to the microkernel's physical thread.
        Uses threading primitives for wait if necessary.
        """
        task_id = operation.get('id', str(uuid.uuid4()))
        logging.info(f"Execution Kernel: Offloading operation {task_id} to physical execution chain.")

        # Ensure the callback is thread-safe for the router
        operation["callback"] = self.router.route_operation

        # Submit to microkernel (synchronous submission to lock-free queue)
        self.microkernel.dispatcher.enqueue_task(
            task_id=task_id,
            payload=operation,
            priority=operation.get('priority', 2)
        )

        # Non-blocking wait if async context is needed, or polling status
        while self.microkernel.dispatcher.get_task_status(task_id) != "COMPLETED":
            await asyncio.sleep(0.01) # Asyncio is only used for waiting, not execution

        result = operation.get("result")
        return result
