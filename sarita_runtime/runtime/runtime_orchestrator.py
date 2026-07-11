class RuntimeOrchestrator:
    """
    Coordinates master execution sequences and manages state sync loops.
    """
    def __init__(self, master):
        self.master = master

    def orchestrate_sync_loop(self):
        """
        Synchronizes runtime states into Global State Manager.
        """
        full_state = self.master.state_manager.get_full_state()
        self.master.kernel.state_engine.sync_kernel_state({
            "uptime": full_state["runtime"]["uptime_sec"],
            "status": full_state["runtime"]["status"]
        })
