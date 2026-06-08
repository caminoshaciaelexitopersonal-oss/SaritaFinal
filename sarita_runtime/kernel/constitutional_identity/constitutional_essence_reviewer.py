class ConstitutionalEssenceReviewer:
    """
    Reviews constitutional reforms from an ontic perspective.
    """
    def review_essence(self, reform: dict):
        # Does the reform touch the "Soul" of SARITA?
        if reform.get("type") == "ONTOLOGICAL":
            return False, "Essence Violation: Core Identity cannot be reformed."
        return True, "Peripheral Reform: Essence untouched."
