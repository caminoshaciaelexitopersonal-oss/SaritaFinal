import logging
from sarita_runtime.kernel.clock_fabric.runtime_clock_authority import RuntimeClockAuthority

class DeterministicEpochController:
    """
    Materializes execution epochs governed by constitutional runtime authority.
    """
    def __init__(self):
        self.clock = RuntimeClockAuthority()
        self.current_epoch = 0
        self.epoch_start_time = 0

    async def advance_epoch(self):
        self.current_epoch += 1
        self.epoch_start_time = self.clock.get_time_ns()
        logging.info(f"Epoch Controller: Advanced to Epoch {self.current_epoch} (TS: {self.epoch_start_time})")
        return self.current_epoch

    async def get_current_epoch_info(self):
        return {
            "id": self.current_epoch,
            "start_ns": self.epoch_start_time,
            "current_ns": self.clock.get_time_ns()
        }
