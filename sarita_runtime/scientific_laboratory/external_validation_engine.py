class ExternalValidationEngine:
    """
    Validates evidence packages without using any internal SARITA modules or imports.
    Saves validation logs under external boundaries.
    """
    def __init__(self):
        pass

    def validate_external_evidence(self, raw_evidence_data: dict) -> dict:
        # Independently check that indices are on a 0.0000 - 1.0000 scale
        valid = True
        issues = []
        for key, val in raw_evidence_data.items():
            if isinstance(val, (int, float)):
                if val < 0.0 or val > 1.0:
                    valid = False
                    issues.append(f"Value '{key}' is out of bounds [0, 1]!")

        return {
            "valid": valid,
            "issues": issues,
            "validation_authority": "EXTERNAL-REFEREE-001"
        }
