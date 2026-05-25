import logging

class MonotonicConsensusClock:
    """
    Ensures monotonic time across the distributed runtime via consensus.
    """
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.logical_clock = 0

    async def synchronize(self, external_time_ns: int):
        """
        Adjusts logical clock while maintaining monotonicity.
        """
        if external_time_ns > self.logical_clock:
            self.logical_clock = external_time_ns
        else:
            self.logical_clock += 1

        logging.debug(f"Consensus Clock: Synchronized to {self.logical_clock}")
        return self.logical_clock

    async def get_sovereign_tick(self):
        self.logical_clock += 1
        return self.logical_clock
