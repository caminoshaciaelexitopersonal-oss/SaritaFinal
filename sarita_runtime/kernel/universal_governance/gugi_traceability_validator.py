class GUGITraceabilityValidator:
    """
    Validates that every component of the GUGI has a verifiable scientific origin.
    """
    def __init__(self, tracker):
        self.tracker = tracker

    def validate_gugi_components(self, gugi_data):
        for component_id in gugi_data.get("components", []):
            if not self.tracker.verify_lineage_completeness(component_id):
                return False
        return True
