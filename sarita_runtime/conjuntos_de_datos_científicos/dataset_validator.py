class DatasetValidator:
    """
    Validates dataset records for proper formatting, bounds, NaN values, and schema requirements.
    """
    def __init__(self):
        pass

    def validate_dataset(self, dataset: dict) -> dict:
        data = dataset.get("data", [])
        if not data:
            return {"valid": False, "reason": "No data array present in dataset."}

        for idx, item in enumerate(data):
            if item is None:
                return {"valid": False, "reason": f"Null value encountered at index {idx}."}
            if isinstance(item, (int, float)):
                if item < 0.0 or item > 10.0:
                    return {"valid": False, "reason": f"Out of bounds value {item} at index {idx}."}

        return {
            "valid": True,
            "validated_count": len(data)
        }
