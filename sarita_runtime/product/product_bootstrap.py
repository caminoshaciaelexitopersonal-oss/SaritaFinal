class ProductBootstrap:
    """
    Handles the bootstrap wire-ups and startup orchestrations for the Product.
    """
    def __init__(self, sarita_product):
        self.product = sarita_product

    def initiate_bootstrap(self) -> bool:
        """
        Executes sequential bootstrap wire-ups.
        """
        print("ProductBootstrap: Initializing SARITA Product Bootstrap sequence...")

        # 1. Start Runtime Master process
        boot_ok = self.product.runtime_master.startup()

        # 2. Register subsystems in Product Registry
        self.product.registry.register_subsystem("kernel", {"status": "ONLINE"})
        self.product.registry.register_subsystem("event_bus", {"status": "ONLINE"})
        self.product.registry.register_subsystem("state_manager", {"status": "ONLINE"})
        self.product.registry.register_subsystem("knowledge_graph", {"status": "ONLINE"})
        self.product.registry.register_subsystem("control_center", {"status": "ONLINE"})
        self.product.registry.register_subsystem("api_gateway", {"status": "ONLINE"})

        return boot_ok
