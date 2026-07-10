class RuntimeResourceManager:
    """
    Manages limits and resource caps (CPU, RAM) allocated to system capabilities.
    """
    def __init__(self):
        self.limits = {
            "max_memory_mb": 512.0,
            "max_cpu_pct": 80.0
        }
        self.allocations = {}

    def allocate_resource(self, component: str, ram_mb: float) -> bool:
        current_total = sum(self.allocations.values())
        if current_total + ram_mb <= self.limits["max_memory_mb"]:
            self.allocations[component] = ram_mb
            return True
        return False

    def free_resource(self, component: str):
        if component in self.allocations:
            del self.allocations[component]
