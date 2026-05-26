import logging

class RuntimePressureGraph:
    """
    Correlates CPU, memory, IO, and IRQ pressure into a single organism.
    """
    def __init__(self):
        self.pressure_matrix = {}

    def update_pressure_signal(self, subsystem: str, level: float):
        logging.debug(f"Pressure Graph: {subsystem} signal: {level}")
        self.pressure_matrix[subsystem] = level

    def get_collapsed_pressure(self):
        if not self.pressure_matrix: return 0.0
        return sum(self.pressure_matrix.values()) / len(self.pressure_matrix)
