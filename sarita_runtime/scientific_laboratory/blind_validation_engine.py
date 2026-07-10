class BlindValidationEngine:
    """
    Conducts single-blind experimental evaluations.
    Conceals group labels (e.g. experimental vs control) from evaluators to eliminate bias.
    """
    def __init__(self):
        pass

    def evaluate_blindly(self, labeled_groups: dict, evaluation_callable) -> dict:
        blinded = {}
        mapping = {}
        for idx, (label, data) in enumerate(labeled_groups.items()):
            blind_key = f"MASKED-GROUP-{idx+1:03d}"
            blinded[blind_key] = data
            mapping[blind_key] = label

        # Run evaluation on masked arrays
        results = {}
        for blind_key, data in blinded.items():
            results[blind_key] = evaluation_callable(data)

        # Map back to unmasked labels
        unmasked_results = {mapping[k]: v for k, v in results.items()}

        return {
            "masked_evaluation": results,
            "unmasked_evaluation": unmasked_results
        }
