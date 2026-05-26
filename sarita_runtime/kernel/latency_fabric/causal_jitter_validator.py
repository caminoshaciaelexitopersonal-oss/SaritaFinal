import logging

class CausalJitterValidator:
    """
    Detects physical noise and validates tail latency compliance.
    """
    def __init__(self):
        pass

    def validate_tail_latency(self, p99_latency_ns: int, budget_ns: int):
        logging.info(f"Jitter Validator: Validating p99 {p99_latency_ns}ns against budget {budget_ns}ns")
        return p99_latency_ns <= budget_ns
