class CognitiveBudgetAllocator:
    def allocate_budget(self, domains, total_capacity=100):
        # Splits budget based on domain priority
        total_prio = sum(d["priority"] for d in domains)
        allocations = {}
        for d in domains:
            allocations[d["id"]] = (d["priority"] / total_prio) * total_capacity
        return allocations
