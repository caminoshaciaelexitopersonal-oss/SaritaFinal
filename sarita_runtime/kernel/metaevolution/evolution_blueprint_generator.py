class EvolutionBlueprintGenerator:
    """
    Generates evolutionary blueprints from specifications and justifications.
    """
    def generate_blueprint(self, cap_spec, justification):
        return {
            "specification": cap_spec,
            "justification": justification,
            "deployment_path": f"metaevolution/blueprints/{cap_spec['id']}.json",
            "status": "APPROVED" if justification["is_valid"] else "REJECTED"
        }
