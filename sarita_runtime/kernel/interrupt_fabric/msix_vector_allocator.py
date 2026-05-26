import logging

class MsixVectorAllocator:
    """
    Materially allocates MSI-X vectors for device-to-core binding.
    """
    def __init__(self, interrupt_router):
        self.router = interrupt_router

    def allocate_vector(self, device_id: str, vector_index: int, target_cpu: int):
        logging.info(f"MSI-X Allocator: Binding {device_id} vector {vector_index} to Core {target_cpu}")
        # Phase 71: Physical vector mapping via irq_affinity
        return self.router.route_irq_to_core(vector_index, target_cpu)
