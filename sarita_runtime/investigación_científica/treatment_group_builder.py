class TreatmentGroupBuilder:
    """
    Builds treatment groups with specified independent variables perturbed or adjusted.
    """
    def __init__(self):
        pass

    def build_group(self, group_id: str, name: str, variables_to_perturb: dict) -> dict:
        treatment_specs = {}
        for var_name, pert_val in variables_to_perturb.items():
            treatment_specs[var_name] = {
                "role": "TREATMENT",
                "target_value": pert_val,
                "is_treatment": True
            }
        return {
            "group_id": group_id,
            "name": name,
            "specifications": treatment_specs
        }
