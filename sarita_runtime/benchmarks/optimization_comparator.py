class OptimizationComparator:
    def compare_optimizations(self, v_old: dict, v_new: dict) -> dict:
        return {
            "yield_increase": round(v_new.get("yield", 0.95) - v_old.get("yield", 0.82), 4),
            "inefficiencies_removed_delta": round(v_new.get("removed", 5) - v_old.get("removed", 2), 4)
        }
