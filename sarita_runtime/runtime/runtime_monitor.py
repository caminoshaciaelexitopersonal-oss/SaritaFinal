import time

class RuntimeMonitor:
    """
    Actively monitors process ticks, latency, and memory metrics of the Master Runtime.
    """
    def __init__(self):
        self.last_tick = time.time()
        self.tick_deltas = []

    def tick(self):
        now = time.time()
        delta = now - self.last_tick
        self.last_tick = now
        self.tick_deltas.append(delta)
        if len(self.tick_deltas) > 100:
            self.tick_deltas = self.tick_deltas[-100:]

    def get_average_tick_ms(self) -> float:
        if not self.tick_deltas:
            return 0.0
        return round((sum(self.tick_deltas) / len(self.tick_deltas)) * 1000.0, 4)
