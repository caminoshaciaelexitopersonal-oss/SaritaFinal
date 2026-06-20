class IndexConflictResolver:
    def resolve_conflict(self, index_a, index_b, priority_map):
        # Resolves conflicts between indices based on pre-defined sovereignty priority
        prio_a = priority_map.get(index_a["name"], 0)
        prio_b = priority_map.get(index_b["name"], 0)
        return index_a if prio_a > prio_b else index_b
