class StructuralTransformationGenerator:
    """
    Generates specific transformation instructions from a plan.
    """
    def generate_transformations(self, plan):
        transformations = []
        for step in plan["steps"]:
            transformations.append({
                "name": f"TRANSFORM_{step['action']}_{step['target']}",
                "expected_delta": 0.05
            })
        return transformations
