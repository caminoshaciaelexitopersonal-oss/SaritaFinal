from .product_manifest import ProductManifest
from .product_version_manager import ProductVersionManager
from .product_configuration import ProductConfiguration
from .product_registry import ProductRegistry
from .product_lifecycle import ProductLifecycle
from .product_bootstrap import ProductBootstrap
from .product_shutdown_manager import ProductShutdownManager
from .product_health_index import ProductHealthIndex

from .capability_registry import ProductCapabilityRegistry
from .capability_mapper import CapabilityMapper
from .capability_graph import CapabilityGraph
from .capability_dependencies import CapabilityDependencies
from .capability_health import CapabilityHealth

from sarita_runtime.runtime.runtime_master import RuntimeMaster

class SaritaProduct:
    """
    SARITA Sovereign Cognitive Operating System (MVSL Phase 132).
    The consolidated product class representing the entire cognitive organism.
    """
    def __init__(self):
        # 1. Product Metadata & Configuration
        self.manifest = ProductManifest()
        self.version = ProductVersionManager()
        self.configuration = ProductConfiguration()
        self.registry = ProductRegistry()

        # 2. Capabilities Infrastructure
        self.capability_registry = ProductCapabilityRegistry()
        self.capability_mapper = CapabilityMapper(self.capability_registry)
        self.capability_graph = CapabilityGraph()
        self.capability_dependencies = CapabilityDependencies(self.capability_graph)
        self.capability_health = CapabilityHealth(self.capability_registry)

        # Map capabilities immediately
        self.capability_mapper.run_auto_mapping()

        # 3. Health & Indexing
        self.health_index = ProductHealthIndex()

        # 4. Master Process Runtime
        self.runtime_master = RuntimeMaster()

        # 5. Bootstrap, Lifecycle, and Shutdown
        self.bootstrap = ProductBootstrap(self)
        self.lifecycle = ProductLifecycle(self)
        self.shutdown_manager = ProductShutdownManager(self)

    def start(self) -> bool:
        """
        Launches the complete SARITA Product.
        """
        print("SaritaProduct: Initializing startup loop...")
        self.lifecycle.transition_to("RUNNING")

        # Ingest nodes into Knowledge Graph to establish Principle 4 and Principle 5
        kg = self.runtime_master.kernel.service_registry.get_service("service.knowledge_graph")
        if kg:
            kg.add_node("product.sarita", "engine", {"version": self.version.get_version_string()})
            kg.add_node("product.runtime", "engine", {"status": "ONLINE"})
            kg.add_relationship("product.sarita", "product.runtime", "controls")

        boot_ok = self.bootstrap.initiate_bootstrap()
        if boot_ok:
            self.lifecycle.transition_to("ACTIVE")

        return boot_ok

    def stop(self):
        """
        Closes the complete SARITA Product.
        """
        print("SaritaProduct: Initializing closure loop...")
        self.lifecycle.transition_to("TERMINATING")
        self.shutdown_manager.execute_shutdown()
