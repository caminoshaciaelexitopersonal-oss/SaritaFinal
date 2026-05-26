import logging

class PhysicalSaturationController:
    """
    Governs global physical saturation.
    Reactions as a single sovereign physical organism.
    """
    def __init__(self, graph):
        self.graph = graph

    def resolve_saturation(self):
        pressure = self.graph.get_collapsed_pressure()
        if pressure > 0.85:
            logging.critical(f"Saturation Controller: GLOBAL SATURATION detected ({pressure:.2f}). Triggering collapse prevention.")
            return "COLLAPSE_PREVENTION_ACTIVE"
        return "STABLE"
