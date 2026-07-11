class ProductShutdownManager:
    """
    Shuts down and unregisters all active processes and services in sequential reverse order.
    """
    def __init__(self, product):
        self.product = product

    def execute_shutdown(self):
        print("ProductShutdownManager: Closing services...")
        self.product.runtime_master.shutdown()
        self.product.lifecycle.transition_to("OFFLINE")
        print("ProductShutdownManager: Safe closure complete.")
