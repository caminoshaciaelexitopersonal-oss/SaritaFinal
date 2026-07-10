class ArchitectureComparator:
    def compare_architectures(self, v_old: dict, v_new: dict) -> dict:
        return {
            "gsai_increase": round(v_new.get("gsai", 0.95) - v_old.get("gsai", 0.92), 4),
            "coupling_reduction": round(v_old.get("coupling", 0.35) - v_new.get("coupling", 0.12), 4)
        }
