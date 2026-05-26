import logging

class RuntimePressureOracle:
    """
    Unifies all physical pressure signals.
    Gobernar saturación física global.
    """
    def __init__(self):
        self.subsystem_signals = {}

    def update_oracle(self, subsystem: str, score: float):
        logging.debug(f"Pressure Oracle: {subsystem} -> {score:.2f}")
        self.subsystem_signals[subsystem] = score

    def predict_global_saturation(self):
        if not self.subsystem_signals: return 0.0
        return sum(self.subsystem_signals.values()) / len(self.subsystem_signals)
