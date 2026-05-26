import logging
import os
from sarita_runtime.kernel.interrupt_fabric.physical_interrupt_router import PhysicalInterruptRouter

class PhysicalDmaPressureRouter:
    """
    Governs DMA pressure and locality materially.
    """
    def __init__(self, interrupt_router: PhysicalInterruptRouter):
        self.pci_path = "/sys/bus/pci/devices"
        self.router = interrupt_router

    def align_device_with_core(self, device_id: str, cpu_id: int):
        logging.info(f"DMA Router: Materializing locality for {device_id} -> Core {cpu_id}")

        # Real hardware locality: Find MSIs for the device and route them
        msi_path = os.path.join(self.pci_path, device_id, "msi_irqs")
        if not os.path.exists(msi_path):
            return False

        try:
            for irq in os.listdir(msi_path):
                if irq.isdigit():
                    self.router.route_irq_to_core(int(irq), cpu_id)
            return True
        except Exception as e:
            logging.error(f"DMA Router: Alignment failure: {e}")
            return False
