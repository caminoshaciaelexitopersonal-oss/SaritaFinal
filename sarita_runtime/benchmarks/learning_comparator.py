class LearningComparator:
    def compare_learning(self, v_old: dict, v_new: dict) -> dict:
        return {
            "reward_gain": round(v_new.get("reward", 1.5) - v_old.get("reward", 0.5), 4),
            "convergence_speedup": round(v_old.get("epochs_to_converge", 100) - v_new.get("epochs_to_converge", 40), 2)
        }
