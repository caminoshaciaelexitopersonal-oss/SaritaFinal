class AlgorithmComparator:
    def compare_algorithms(self, v_old: dict, v_new: dict) -> dict:
        return {
            "speed_multiplier": round(v_old.get("latency_ms", 10.0) / max(0.001, v_new.get("latency_ms", 5.0)), 2),
            "memory_saved_mb": round(v_old.get("memory_mb", 50.0) - v_new.get("memory_mb", 35.0), 2)
        }
