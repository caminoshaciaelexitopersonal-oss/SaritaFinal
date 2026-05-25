import logging
import asyncio
from typing import Dict, Any, List
from sarita_runtime.kernel.unified_authority.unified_kernel_authority import UnifiedKernelAuthority
from sarita_runtime.kernel.microkernel_fabric.deterministic_execution_dispatcher import DeterministicExecutionDispatcher
from sarita_runtime.kernel.microkernel_fabric.kernel_execution_orchestrator import KernelExecutionOrchestrator
from sarita_runtime.kernel.runtime_state_machine.execution_state_controller import ExecutionStateController, ExecutionState

class SovereignMicrokernel:
    """
    Sovereign Microkernel Execution Fabric.
    Refactored for Phase 67: Unified Sovereign Material Kernel Collapse.
    Centralized authority through UnifiedKernelAuthority.
    """
    def __init__(self):
        self.unified_authority = UnifiedKernelAuthority()
        self.dispatcher = DeterministicExecutionDispatcher()
        self.orchestrator = KernelExecutionOrchestrator()
        self.state_machine = ExecutionStateController()
        self.active_tasks = {}

    async def boot(self):
        logging.info("BOOTING Sovereign Microkernel (Unified Authority)...")
        await self.state_machine.transition_to(ExecutionState.INIT)

        await self.orchestrator.initialize_execution_planes()
        self.dispatcher.start_dispatch_loop()

        await self.state_machine.transition_to(ExecutionState.VERIFIED)
        logging.info("Sovereign Microkernel ONLINE.")

    async def submit_task(self, task_id: str, payload: Dict[str, Any], priority: int = 1):
        logging.info(f"Microkernel: Submitting task {task_id} via Unified Authority.")

        # Centralized authorization for ALL decisions (Refactored to synchronous)
        if self.unified_authority.authorize_physical_action("DISPATCH", "SUBMIT_TASK", payload):
            self.dispatcher.enqueue_task(task_id, payload, priority)
            return True

        return False

    async def get_execution_status(self, task_id: str):
        return self.dispatcher.get_task_status(task_id)
