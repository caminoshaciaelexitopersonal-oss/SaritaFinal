import logging
import uuid
import threading
from sarita_runtime.kernel.microkernel_fabric.sovereign_microkernel import SovereignMicrokernel

class SovereignExecutionKernel:
    """
    Sovereign Execution Fabric Kernel (Phase 72).
    Absolute delegation to the Sovereign Microkernel material path.
    ELIMINATES asyncio on the critical execution path.
    """
    def __init__(self, node_id, fabric_router):
        self.node_id = node_id
        self.router = fabric_router
        self.microkernel = SovereignMicrokernel()
        self.is_active = False

    def boot(self):
        """Material boot."""
        self.microkernel.boot()
        self.is_active = True
        return True

    def execute_material_op(self, operation):
        """
        Executes an operation via the microkernel material path.
        Synchronous and deterministic.
        """
        task_id = operation.get('id', str(uuid.uuid4()))
        logging.info(f"Execution Kernel: Offloading {task_id} to material substrate.")

        # Assign thread-safe router callback
        operation["callback"] = self.router.route_operation

        # Submit to microkernel (sync submission to LockFreeQueue)
        success = self.microkernel.submit_task(task_id, operation, operation.get('priority', 2))

        if success:
            # Physical wait for completion (no polling, uses threading.Event inside)
            self.microkernel.dispatcher.wait_for_completion(task_id)
            return operation.get("result")

        return False

class DistributedExecutionRouter:
    def route_operation(self, operation):
        logging.info(f"Execution Router: Material routing for {operation['type']}")
        return {"status": "SUCCESS", "op_id": operation.get("id")}
