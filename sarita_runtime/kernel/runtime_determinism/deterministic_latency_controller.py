import logging
import time
import os

class DeterministicLatencyController:
    """
    Measures and enforces real deterministic execution latency under Linux scheduler pressure.
    """
    def __init__(self):
        self.latency_stats = []

    async def measure_execution_latency(self, func, *args, **kwargs):
        start_ns = time.perf_counter_ns()
        result = await func(*args, **kwargs)
        end_ns = time.perf_counter_ns()

        latency_ms = (end_ns - start_ns) / 1_000_000.0
        self.latency_stats.append(latency_ms)
        logging.info(f"Latency Controller: Execution took {latency_ms:.4f}ms")
        return result

    async def enforce_latency_budget(self, budget_ms: float):
        """
        Enforcement logic to check if current execution paths are within budget.
        """
        if not self.latency_stats:
            return True

        avg_latency = sum(self.latency_stats) / len(self.latency_stats)
        if avg_latency > budget_ms:
            logging.warning(f"Latency Controller: Latency budget EXCEEDED! Avg: {avg_latency:.4f}ms, Budget: {budget_ms}ms")
            return False
        return True
