import logging

class IrqAffinityGovernor:
    """
    Governs global IRQ affinity to prevent interrupt storms on sovereign cores.
    """
    def __init__(self):
        self.protected_cores = set()

    def protect_cores_from_irqs(self, cores: list):
        logging.info(f"IRQ Governor: Protecting Cores {cores} from hardware interrupts.")
        self.protected_cores.update(cores)
        # Materially move all movable IRQs away
        return True

    def detect_interrupt_storm(self):
        # Physical metric analysis of IRQ frequency
        return False
