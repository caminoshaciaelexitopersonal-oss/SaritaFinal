class FutureCivilizationBuilder:
    """
    Constructs potential civilizational states for future projections.
    """
    def build_future_civilization(self, current_params, generational_delta):
        """
        Projects parameters forward by N generations.
        """
        projected_params = {
            "legitimacy": max(0.0, current_params.get("legitimacy", 1.0) - 0.001 * generational_delta),
            "adaptation": min(1.0, current_params.get("adaptation", 0.5) + 0.0005 * generational_delta),
            "stability": max(0.0, current_params.get("stability", 1.0) - 0.0008 * generational_delta)
        }
        return projected_params
