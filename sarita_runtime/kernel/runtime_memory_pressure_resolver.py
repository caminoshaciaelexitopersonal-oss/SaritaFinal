import logging

class RuntimeMemoryPressureResolver:
    """
    Resolves memory pressure materially within the SARITA substrate.
    """
    def __init__(self, governor):
        self.governor = governor

    def resolve_pressure(self, current_usage: int, limit: int):
        if current_usage > limit * 0.9:
            logging.critical("Memory Resolver: CRITICAL PRESSURE. Triggering sovereign reclaim.")
            return self.governor.trigger_sovereign_reclaim("sovereign_cores", 1024 * 1024 * 100) # 100MB
        return False
