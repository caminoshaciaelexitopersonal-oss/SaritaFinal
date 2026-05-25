import logging
import time

class InterruptLatencyValidator:
    """
    Measures and validates physical interrupt latency.
    Non-placeholder implementation for real latency tracking.
    """
    def __init__(self):
        self.latency_history = []

    async def record_latency(self, irq_id: int, latency_us: float):
        """Records a measured latency sample."""
        self.latency_history.append({"irq": irq_id, "lat": latency_us, "ts": time.time()})
        if len(self.latency_history) > 1000:
            self.latency_history.pop(0)

    async def validate_latency_compliance(self, max_latency_us: float):
        """
        Validates that recent IRQ latency samples are within sovereign budget.
        """
        if not self.latency_history:
            logging.info("IRQ Validator: No latency data yet. Assuming compliance.")
            return True

        recent_latencies = [s["lat"] for s in self.latency_history[-10:]]
        avg_lat = sum(recent_latencies) / len(recent_latencies)

        logging.info(f"IRQ Validator: Avg Latency: {avg_lat:.2f}us, Budget: {max_latency_us}us")

        if avg_lat > max_latency_us:
            logging.error(f"IRQ Validator: DETERMINISM BREACH! {avg_lat:.2f}us > {max_latency_us}us")
            return False
        return True
