import logging

class RuntimeMemoryAllocator:
    """
    Federated Runtime Memory Allocator.
    Manages deterministic memory ownership and lineage.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.allocations = {} # component_id -> allocation_meta

    def allocate_memory(self, component_id, size, epoch):
        if self._can_allocate(size):
            self.allocations[component_id] = {
                "size": size,
                "epoch": epoch,
                "lineage": f"MEM-{epoch}-{component_id}"
            }
            logging.info(f"Memory Plane: Allocated {size} units to {component_id} at epoch {epoch}")
            return True
        return False

    def _can_allocate(self, size):
        current_load = sum(a['size'] for a in self.allocations.values())
        return (current_load + size) <= self.capacity

class FederatedMemoryGuard:
    def detect_orphans(self, active_components):
