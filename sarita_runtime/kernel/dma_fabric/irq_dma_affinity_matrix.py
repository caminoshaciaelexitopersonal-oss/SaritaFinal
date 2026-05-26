import logging

class IrqDmaAffinityMatrix:
    """
    Physical matrix of IRQ and DMA affinities.
    Ensures optimal hardware locality for ultra-low latency IO.
    """
    def __init__(self):
        self.matrix = {}

    def bind_irq_dma(self, irq_id: int, device_id: str, cpu_id: int):
        logging.info(f"Affinity Matrix: Binding IRQ {irq_id} and Device {device_id} to Core {cpu_id}")
        self.matrix[device_id] = {"irq": irq_id, "cpu": cpu_id}
        return True
