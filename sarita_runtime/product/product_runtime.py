class ProductRuntime:
    """
    Coordinates product-level execution loops and links with RuntimeMaster.
    """
    def __init__(self, master_runtime):
        self.master_runtime = master_runtime

    def is_running(self) -> bool:
        return self.master_runtime.state_manager.runtime.status == "ONLINE"
