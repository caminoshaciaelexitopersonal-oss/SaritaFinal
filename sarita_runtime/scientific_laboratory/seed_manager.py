class SeedManager:
    """
    Enforces deterministic seed assignments across execution threads and loops.
    """
    def __init__(self, master_seed: int = 42):
        self.master_seed = master_seed
        self.assigned_seeds = {}

    def get_seed_for_thread(self, thread_name: str) -> int:
        if thread_name not in self.assigned_seeds:
            # Shift master seed deterministically
            self.assigned_seeds[thread_name] = self.master_seed + len(self.assigned_seeds) * 17
        return self.assigned_seeds[thread_name]
