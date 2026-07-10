class GovernanceComparator:
    def compare_governance(self, v_old: dict, v_new: dict) -> dict:
        return {
            "compliance_delta": round(v_new.get("compliance", 1.0) - v_old.get("compliance", 0.9), 4),
            "conflict_reduction": round(v_old.get("conflicts", 2) - v_new.get("conflicts", 0), 4)
        }
