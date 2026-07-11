import time
from .runtime_context import RuntimeContext
from .runtime_session_manager import RuntimeSessionManager
from .runtime_resource_manager import RuntimeResourceManager
from .runtime_executor import RuntimeExecutor
from .runtime_supervisor import RuntimeSupervisor
from .runtime_monitor import RuntimeMonitor
from .runtime_scheduler import RuntimeScheduler
from .runtime_orchestrator import RuntimeOrchestrator

from sarita_runtime.kernel.unified_kernel.unified_kernel import UnifiedKernel
from sarita_runtime.kernel.state_manager.global_state_manager import GlobalStateManager
from sarita_runtime.kernel.event_bus.event_bus import UnifiedEventBus

class RuntimeMaster:
    """
    Sovereign Runtime Master Process (Phase 132).
    The sole master execution engine controlling boot, shutdown, task planning,
    session boundaries, and error recovery across the entire SARITA Operating System.
    """
    def __init__(self):
        # 1. State, Event Bus & Unified Kernel
        self.state_manager = GlobalStateManager()
        self.event_bus = UnifiedEventBus()
        self.kernel = UnifiedKernel(self.state_manager)

        # Register Event Bus and State Manager as system services
        self.kernel.service_registry.register("service.event_bus", self.event_bus)
        self.kernel.service_registry.register("service.state_manager", self.state_manager)

        # 2. Runtime Sub-Components
        self.context = RuntimeContext()
        self.session_manager = RuntimeSessionManager()
        self.resource_manager = RuntimeResourceManager()
        self.executor = RuntimeExecutor()
        self.supervisor = RuntimeSupervisor(self)
        self.monitor = RuntimeMonitor()
        self.scheduler = RuntimeScheduler()
        self.orchestrator = RuntimeOrchestrator(self)

    def startup(self) -> bool:
        """
        Launches the master runtime process and boots the unified kernel.
        """
        print("RuntimeMaster: Starting master execution loop...")
        self.state_manager.runtime.set_status("ONLINE")

        # Publish System Boot Event
        self.event_bus.publish("system.boot", {"timestamp": time.time()}, sender="runtime_master")

        # Boot Unified Kernel
        boot_success = self.kernel.boot()
        if boot_success:
            self.event_bus.publish("state.changed", {"new_state": "OPERATIONAL"}, sender="runtime_master")

        return boot_success

    def shutdown(self):
        """
        Safely shuts down the master runtime process and persists final state blocks.
        """
        print("RuntimeMaster: Shutting down master execution loop...")
        self.event_bus.publish("system.shutdown", {"timestamp": time.time()}, sender="runtime_master")
        self.state_manager.runtime.set_status("OFFLINE")
        self.state_manager.persist_state_snapshot()
