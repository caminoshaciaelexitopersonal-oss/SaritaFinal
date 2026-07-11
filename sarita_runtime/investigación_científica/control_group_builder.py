class ControlGroupBuilder:
    """
    Builds the baseline control group specifications with unperturbed/default configurations.
    """
    def __init__(self):
        pass

    def build_group(self, variables: dict) -> dict:
        control_specs = {}
        for var_name, info in variables.items():
            control_specs[var_name] = {
                "role": "CONTROL",
                "target_value": info.get("baseline", 0.0),
                "is_treatment": False
            }
        return {
            "group_id": "GROUP-CONTROL",
            "name": "Control Group (Baseline)",
            "specifications": control_specs
        }
