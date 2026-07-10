from .kernel_registry import KernelRegistry
from .kernel_directory import KernelDirectory
from .kernel_capability_registry import KernelCapabilityRegistry
from .kernel_metadata_manager import KernelMetadataManager
from .kernel_boot_engine import KernelBootEngine
from .kernel_state_engine import KernelStateEngine
from .kernel_context_manager import KernelContextManager
from .kernel_health_manager import KernelHealthManager

# Service Registry Imports
from .service_registry import ServiceRegistry
from .service_directory import ServiceDirectory
from .service_locator import ServiceLocator
from .service_health_checker import ServiceHealthChecker
from .service_dependency_manager import ServiceDependencyManager

class UnifiedKernel:
    """
    Sovereign Unified Kernel Facade (Phase 132).
    The sole governing process registry of SARITA's operational ecosystem.
    Registers and tracks all historical phases and engines as active services.
    """
    def __init__(self, state_manager=None):
        self.registry = KernelRegistry()
        self.directory = KernelDirectory()
        self.capabilities = KernelCapabilityRegistry()
        self.metadata = KernelMetadataManager()
        self.boot_engine = KernelBootEngine(self)
        self.state_engine = KernelStateEngine(state_manager) if state_manager else None
        self.context_manager = KernelContextManager()
        self.health_manager = KernelHealthManager(self)

        # Service Registry infrastructure
        self.service_registry = ServiceRegistry()
        self.service_directory = ServiceDirectory()
        self.service_health = ServiceHealthChecker(self.service_registry)
        self.service_dependencies = ServiceDependencyManager()

        # Wire ServiceLocator static reference
        ServiceLocator.set_registry(self.service_registry)

        # Boot defaults
        self._register_bootstrap_capabilities()

    def _register_bootstrap_capabilities(self):
        # Automated capability discovery logic: scans directories to discover active modules
        import os
        kernel_dir = "sarita_runtime/kernel/"
        if os.path.exists(kernel_dir):
            subdirs = [d for d in os.listdir(kernel_dir) if os.path.isdir(os.path.join(kernel_dir, d))]
            for s in subdirs:
                if s not in ["__pycache__", "unified_kernel"]:
                    # Synthesize capability name and version from directory name
                    cap_name = s.replace("_", " ")
                    self.capabilities.register_capability(s, f"Auto-Discovered-Phase", active=True)

        # Ensure our core phases are actively mapped
        self.capabilities.register_capability("meta_evolution", "Phase-126", active=True)
        self.capabilities.register_capability("cosmogenesis", "Phase-127", active=True)
        self.capabilities.register_capability("auto_architecture", "Phase-128", active=True)
        self.capabilities.register_capability("global_certification", "Phase-129", active=True)
        self.capabilities.register_capability("formal_consistency", "Phase-130", active=True)
        self.capabilities.register_capability("autonomous_operation", "Phase-131", active=True)
        self.capabilities.register_capability("unified_product", "Phase-132", active=True)

    def boot(self) -> bool:
        """
        Launches the core kernel.
        """
        return self.boot_engine.execute_boot_sequence()
