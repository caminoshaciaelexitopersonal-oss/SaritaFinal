class ExternalPressureModel:
    """
    Calculates the impact of external stressors on environmental variables.
    """
    def apply_pressures(self, base_state, stressors):
        new_state = base_state.copy()
        for s in stressors:
            # Impact = Severity * Duration factor
            impact_val = s["severity"] * s["impact"]
            target = s["target_variable"]
            if target in new_state:
                if s["type"] == "THREAT":
                    new_state[target] += impact_val
                else:
                    new_state[target] -= impact_val

            # Clamp values to logical boundaries
            new_state[target] = max(0.0, min(10.0 if "volume" in target or "users" in target else 1.0, new_state[target]))

        return new_state
