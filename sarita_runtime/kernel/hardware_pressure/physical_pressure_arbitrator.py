import logging

class PhysicalPressureArbitrator:
    """
    Unifies CPU, memory, IO, and IRQ pressure into a single constitutional authority.
    """
    def __init__(self):
        self.subsystem_pressure = {
            "cpu": 0.0,
            "memory": 0.0,
            "io": 0.0,
            "irq": 0.0
        }

    async def update_subsystem_pressure(self, subsystem: str, level: float):
        if subsystem in self.subsystem_pressure:
            self.subsystem_pressure[subsystem] = level
            logging.debug(f"Pressure Arbitrator: {subsystem} pressure updated to {level}")

    async def get_global_pressure_score(self):
        # Weighted unification of pressure signals
        weights = {"cpu": 0.4, "memory": 0.3, "io": 0.2, "irq": 0.1}
        score = sum(self.subsystem_pressure[s] * weights[s] for s in weights)
        return score
