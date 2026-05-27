import logging
import threading
from typing import Dict, Any, List
from sarita_runtime.kernel.microkernel_fabric.deterministic_execution_dispatcher import DeterministicExecutionDispatcher
from sarita_runtime.kernel.microkernel_fabric.kernel_execution_orchestrator import KernelExecutionOrchestrator
from sarita_runtime.kernel.runtime_determinism.deterministic_latency_controller import DeterministicLatencyController
from sarita_runtime.kernel.clock_fabric.runtime_clock_authority import RuntimeClockAuthority
from sarita_runtime.kernel.microkernel_fabric.execution_epoch_orchestrator import ExecutionEpochOrchestrator
from sarita_runtime.kernel.unified_authority.unified_kernel_authority import UnifiedKernelAuthority
from sarita_runtime.kernel.runtime_state_machine.execution_state_controller import ExecutionStateController, ExecutionState

class SovereignMicrokernel:
    """
    Sovereign Microkernel Execution Fabric.
    Refactored to ELIMINATE asyncio dependency on critical path.
    Uses physical threads and synchronous authorization.
    """
    def __init__(self):
        self.unified_authority = UnifiedKernelAuthority()
        self.dispatcher = DeterministicExecutionDispatcher()
        self.orchestrator = KernelExecutionOrchestrator()
        self.clock = RuntimeClockAuthority()
        self.epoch_orchestrator = ExecutionEpochOrchestrator()
        self.latency_controller = DeterministicLatencyController()
        self.state_machine = ExecutionStateController()

    def boot(self):
        """Material boot process. Sync/Threaded."""
        logging.info("BOOTING Sovereign Microkernel (Material Path)...")
        # Initialize state synchronously
        self.state_machine.transition_to_sync(ExecutionState.INIT)

        # Dispatcher starts its own physical thread
        self.dispatcher.start_dispatch_loop()

        self.state_machine.transition_to_sync(ExecutionState.VERIFIED)
        logging.info("Sovereign Microkernel ONLINE.")
        return True

    def submit_task(self, task_id: str, payload: Dict[str, Any], priority: int = 1):
        """Material task submission. No async overhead."""
        logging.info(f"Microkernel: Offloading {task_id} to physical substrate.")

        # Synchronous authorization via Unified Authority
        if self.unified_authority.authorize_physical_action("DISPATCH", "SUBMIT_TASK", payload):
            self.dispatcher.enqueue_task(task_id, payload, priority)
            return True

        logging.error(f"Microkernel: {task_id} REJECTED by Unified Authority.")
        return False
