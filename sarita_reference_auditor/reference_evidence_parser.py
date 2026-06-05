import json

class ReferenceEvidenceParser:
    """
    Parses SARITA evidence packages without using any SARITA internal code.
    Uses only standard Python libraries.
    """
    @staticmethod
    def parse_bundle(raw_json: str):
        try:
            data = json.loads(raw_json)
            # Validate basic structure according to the public spec
            if "version" not in data or "data" not in data:
                raise ValueError("Invalid bundle format")
            return data
        except Exception as e:
            return {"error": str(e)}
