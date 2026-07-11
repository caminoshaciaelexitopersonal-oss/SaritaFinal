class KernelStateEngine:
    """
    Direct interface connecting internal kernel execution loops to the Global State Manager.
    """
    def __init__(self, state_manager):
        self.state_mgr = state_manager

    def sync_kernel_state(self, updates: dict):
        """
        Pushes kernel states to the global state manager.
        """
        for k, v in updates.items():
            self.state_mgr.memory.set(f"kernel.{k}", v)
