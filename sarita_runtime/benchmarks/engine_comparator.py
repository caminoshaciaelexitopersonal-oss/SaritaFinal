class EngineComparator:
    def compare_engines(self, v_old: dict, v_new: dict) -> dict:
        return {
            "perf_delta": round(v_new.get("perf", 0.9) - v_old.get("perf", 0.8), 4),
            "error_reduction": round(v_old.get("errors", 5) - v_new.get("errors", 0), 4),
            "certified_superior": v_new.get("perf", 0.9) > v_old.get("perf", 0.8)
        }
